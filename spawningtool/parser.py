"""
spawningtool.parser
~~~~~~~~~~~~~~~~~~~
"""


import hashlib
import json
import os
import sc2reader

from spawningtool import hots_constants, lotv_constants
from spawningtool.exception import CutoffTimeError, ReplayFormatError, ReadError


DATA_NOT_SUPPORTED = (
    'This replay version does not support the data needed for the build order'
)


def convert_gametime_to_float(gametime):
    """
    Converts a gametime (5:47) to a float (5.45)
    """
    try:
        return float(gametime.replace(":", "."))
    except ValueError:
        raise CutoffTimeError()


def _frame_to_time(frame, frames_per_second):
    seconds = int(frame // frames_per_second)
    return '{0}:{1:02d}'.format(seconds // 60, seconds % 60)


# 0, 0 is bottom left
CLOCK_POSITIONS = {
        2: {0: 11, 1: 12, 2: 1},
        1: {0: 9, 1: 0, 2: 3},
        0: {0: 7, 1: 6, 2: 5},
        }

def _get_clock_position(parsed_data, event):
    if not parsed_data['include_map_details']:
        return None
    x_section = event.x // (parsed_data['map_details']['width'] // 3)
    y_section = event.y // (parsed_data['map_details']['height'] // 3)
    return CLOCK_POSITIONS[y_section][x_section]


class TrackerEvent(object):
    """
    not necesarily a trackerevent, but event was too generic
    """
    def __init__(self, frame, frames_per_second, supply=None, clock_position=None):
        self.frame = frame
        self.supply = supply
        self.clock_position = clock_position
        self.frames_per_second = frames_per_second

    def to_dict(self, frames):
        raise NotImplementedError

    def __unicode__(self):
        if self.supply:
            return '{} {} Event'.format(self.supply, self.frame)
        return '{} Event'.format(self.frame)


class BuildEvent(TrackerEvent):
    def __init__(self, name, frame, frames_per_second, supply, clock_position=None,
            is_chronoboosted=False):
        self.name = name
        self.is_chronoboosted = is_chronoboosted
        super(BuildEvent, self).__init__(frame, frames_per_second, supply, clock_position=clock_position)

    def is_worker(self):
        return self.name in ['SCV', 'Drone', 'Probe']

    def to_dict(self):
        return {
            'frame': self.frame,
            'time': _frame_to_time(self.frame, self.frames_per_second),
            'name': self.name,
            'supply': self.supply,
            'is_worker': self.is_worker(),
            'clock_position': self.clock_position,
            'is_chronoboosted': self.is_chronoboosted,
        }

    def __unicode__(self):
        return '{} {} {}{}'.format(
            self.supply,
            _frame_to_time(self.frame, self.frames_per_second),
            self.name,
            ' (Chronoboosted)' if self.is_chronoboosted else '',
        )


class DiedEvent(TrackerEvent):
    def __init__(self, name, frame, frames_per_second, killer, clock_position=None):
        self.name = name
        super(DiedEvent, self).__init__(frame, frames_per_second, None, clock_position=clock_position)
        self.killer = killer  # player id

    def to_dict(self):
        return {
            'frame': self.frame,
            'time': _frame_to_time(self.frame, self.frames_per_second),
            'name': self.name,
            'killer': self.killer,
            'clock_position': self.clock_position,
        }

    def __unicode__(self):
        return '{} {} killed by {}'.format(
            _frame_to_time(self.frame, self.frames_per_second),
            self.name,
            self.killer,
            )


class AbilityEvent(TrackerEvent):
    def __init__(self, name, frame, frames_per_second):
        self.name = name
        super(AbilityEvent, self).__init__(frame, frames_per_second, None)

    def to_dict(self):
        return {
            'frame': self.frame,
            'time': _frame_to_time(self.frame, self.frames_per_second),
            'name': self.name,
        }

    def __unicode__(self):
        return '{} {}'.format(
            _frame_to_time(self.frame, self.frames_per_second),
            self.name,
            )


class GameTimeline(object):
    def __init__(self):
        self.timeline = []

    def add_event(self, event):
        self.timeline.append(event)

    def sort(self):
        self.timeline.sort(key=lambda a: a.frame)

    def __unicode__(self):
        return '\n'.join([str(event) for event in self.timeline])


def get_protocol(base_build):
    try:
        protocol_name = 'protocol{}'.format(base_build)
        _temp = __import__('s2protocol', globals(), locals(), [protocol_name])
    except:
        return
    else:
        return getattr(_temp, protocol_name)


def get_supply(supply, frame):
    """
    supply is a list of [FRAME, SUPPLY] lists
    use binary search to find the supply at or just before the frame provided
    """
    start = 0
    end = len(supply) - 1

    while start < end:
        mid = (start + end) // 2
        val = supply[mid][0]
        if val == frame:
            return mid
        if frame < val:
            end = mid - 1
        else:
            start = mid + 1

    if start != 0 and supply[start][0] > frame:
        start -= 1

    return supply[start][1]


def unit_born_event(builds, event, parsed_data, constants, chronoboosts):
    """
    need to reverse the time
    if the unit morphs, it's preferable to use the unit_type_name since it's what it was
    actually born as. sc2reader does, however, provide some nice normalization, so
    swap the display name as necessary
    """
    player = event.control_pid
    unit_name = event.unit_type_name
    if unit_name in constants.BO_EXCLUDED or player == 0 or event.unit.hallucinated:
        return

    if not unit_name in constants.BUILD_DATA:
        unit_name = event.unit.name
        if unit_name in constants.BO_EXCLUDED:
            return
    if unit_name is None:
        unit_name = '(None)'

    frame, unit_name, is_chronoboosted = adjust_build_time(
            event, player, unit_name, constants, chronoboosts)

    # for safety to ignore observer units from GH and such
    if not player in parsed_data['players']:
        return

    supply = get_supply(parsed_data['players'][player]['supply'], frame)
    builds[player].add_event(BuildEvent(unit_name, frame, constants.FRAMES_PER_SECOND, supply,
        _get_clock_position(parsed_data, event), is_chronoboosted))


def unit_init_event(builds, event, parsed_data, constants):
    """
    these are mostly buildings, but I believe it may also include warped units
    """
    player = event.control_pid
    unit_name = event.unit_type_name
    if unit_name in constants.BO_EXCLUDED or player == 0 or event.unit.hallucinated:
        return
    frame = event.frame

    # for safety to ignore observer units from GH and such
    if not player in parsed_data['players']:
        return

    supply = parsed_data['players'][player]['supply'][-1][1]
    builds[player].add_event(BuildEvent(unit_name, frame, constants.FRAMES_PER_SECOND, supply,
        _get_clock_position(parsed_data, event)))

def adjust_build_time(event, player, unit_name, constants, chronoboosts):
    """
    chronoboosts is arranged in reverse order.

    This is only an approximation. The edge case behavior isn't perfect (particularly around
    chronoboosts starting before the the guessed start time). We also cannot distinguish which
    building exactly gets boosted. Even so, this is better than no tracking at all
    """
    frame = event.frame
    if not unit_name in constants.BUILD_DATA:
        unit_name += ' (Error on upgrade time)'
        return frame, unit_name, False

    cur_build_data = constants.BUILD_DATA[unit_name]

    projected_start = frame - constants.BUILD_DATA[unit_name]['build_time']
    chronoboosted = False

    if chronoboosts.get(player):
        for building in cur_build_data['built_from']:
            if building in chronoboosts[player]:
                for cur_frame_start, cur_frame_end in chronoboosts[player][building]:
                    if cur_frame_end > projected_start and cur_frame_start < frame:
                        overlap = min(cur_frame_end, frame) - max(cur_frame_start, projected_start)
                        reduction = overlap // 2
                        projected_start += reduction
                        chronoboosted = True

    return projected_start, unit_name, chronoboosted

def upgrade_event(builds, event, parsed_data, constants, chronoboosts):
    """
    need to reverse the time
    """
    player = event.pid
    if player == 0:
        return
    unit_name = event.upgrade_type_name

    frame, unit_name, is_chronoboosted = adjust_build_time(
            event, player, unit_name, constants, chronoboosts)

    supply = get_supply(parsed_data['players'][player]['supply'], frame)
    builds[player].add_event(BuildEvent(
        unit_name, frame, constants.FRAMES_PER_SECOND, supply, is_chronoboosted=is_chronoboosted))


def change_event(builds, event, parsed_data, constants):
    """
    these are triggered when units morph or transform. We do need to track these
    because they tell us when certain units are morphed in
    However, we also need to exclude a lot from constants.BO_CHANGED_EXCLUDED because they
    can be misleading
    """
    if not event.unit.owner:  # happened when knocking down rocks
        return
    player = event.unit.owner.pid
    unit_name = event.unit_type_name
    if player == 0 or unit_name in constants.BO_CHANGED_EXCLUDED:
        return

    try:
        frame = event.frame - constants.BUILD_DATA[unit_name]['build_time']
    except KeyError:
        return

    supply = get_supply(parsed_data['players'][player]['supply'], frame)
    builds[player].add_event(BuildEvent(unit_name, frame, constants.FRAMES_PER_SECOND, supply))


def died_event(units_lost, event, parsed_data, constants):
    """
    for born events, the name needed to be corrected for evolutions
    but if it dies, then it should die in its final form
    """
    if not event.unit or not event.unit.owner:
        return
    player = event.unit.owner.pid
    unit_name = event.unit.name

    if unit_name in constants.BO_EXCLUDED or player == 0:
        return

    killer = event.killer_pid

    units_lost[player].add_event(DiedEvent(unit_name, event.frame, constants.FRAMES_PER_SECOND, killer,
        _get_clock_position(parsed_data, event)))


def ability_event(abilities, event, constants, raw_chronoboosts):
    """
    Create events around abilities being casted e.g. ChronoBoost, Snipe
    """
    player = event.player.pid
    ability_name = event.ability_name

    if ability_name not in constants.TRACKED_ABILITIES or not player:
        return

    # this is imprecise; we cannot distinguish WHICH of the units of the type it came from
    if ability_name == 'ChronoBoost' and event.target:
        if not event.target.name in raw_chronoboosts[player]:
            raw_chronoboosts[player][event.target.name] = []
        raw_chronoboosts[player][event.target.name].append(event.frame)

    abilities[player].add_event(AbilityEvent(ability_name, event.frame, constants.FRAMES_PER_SECOND))


def make_event_timeline(timelines, cutoff_time, parsed_data, field, constants):
    """
    Converts the GameTimeline into a readable structure
    """
    for i, timeline in timelines.items():
        timeline.sort()

        parsed_data['players'][i][field] = []
        for event in timeline.timeline:

            # If desired, stop parsing for events after a given time
            current_gametime = _frame_to_time(event.frame, constants.FRAMES_PER_SECOND)
            if (cutoff_time and
                    convert_gametime_to_float(current_gametime) >
                    convert_gametime_to_float(cutoff_time)):
                break

            parsed_data['players'][i][field].append(event.to_dict())


def process_chronoboosts(raw_chronoboosts):
    """
    convert raw chronoboosts to a set of frame ranges over which the chronoboost is applied
    to that building. This should be easier to backtrack build times

    This, to some degree, avoids double-counting if a chronoboosted building is chronoboosted
    again or if all of the buildings of the same type are chronoboosted
    """
    chronoboosts = {}
    chronoboost_duration = 16 * 20  # this is true in HotS and LotV

    for player, all_boosts in raw_chronoboosts.items():
        chronoboosts[player] = {}
        for building, frames in all_boosts.items():
            frame_ranges = []
            cur_frame_range = None

            for start_raw_frame in frames:
                if not cur_frame_range:
                    cur_frame_range = [start_raw_frame, start_raw_frame + chronoboost_duration]
                elif cur_frame_range[1] > start_raw_frame:
                    cur_frame_range[1] = start_raw_frame + chronoboost_duration
                else:
                    frame_ranges.append(cur_frame_range)
                    cur_frame_range = [start_raw_frame, start_raw_frame + chronoboost_duration]

            if cur_frame_range:
                frame_ranges.append(cur_frame_range)

            frame_ranges.reverse()  # because we need to step backwards when using this

            chronoboosts[player][building] = frame_ranges

    return chronoboosts


def parse_events(replay, cutoff_time, parsed_data, cache_path=None, include_map_details=False):
    """
    Parse all game related events
    """
    if not getattr(replay, 'tracker_events', None):
        if replay.build < 25604:  # this is 2.0.8
            raise ReplayFormatError(DATA_NOT_SUPPORTED, parsed_data)
        else:
            raise ReplayFormatError((
                'No tracker data could be found, despite this being the'
                ' right version ({}). Sorry.'.format(parsed_data['build'])
            ), parsed_data)

    if replay.expansion == 'WoL':
        # primarily because the build times are off, but I don't want to deal with it
        raise ReplayFormatError(('spawningtool currently only supports HotS.'), parsed_data)

    constants = hots_constants

    builds = dict((key, GameTimeline()) for key in replay.player.keys())
    units_lost = dict((key, GameTimeline()) for key in replay.player.keys())
    abilities = dict((key, GameTimeline()) for key in replay.player.keys())

    # {pid_1: {'Building': [frame_1, frame_2, ..], ..}, ..}
    raw_chronoboosts = {key: {} for key in replay.player.keys()}

    legit_ability_event_types = set([
        'TargetPointCommandEvent',
        'TargetUnitCommandEvent',
        'DataCommandEvent',
        'BasicCommandEvent',
        ])
    for event in replay.game_events:
        if event.name in legit_ability_event_types:
            ability_event(abilities, event, constants, raw_chronoboosts)

    chronoboosts = process_chronoboosts(raw_chronoboosts)

    for event in replay.tracker_events:
        if event.frame == 0:
            # set player start position
            if include_map_details and event.name == 'UnitBornEvent' and \
                    event.unit_type_name in ['Nexus', 'CommandCenter', 'Hatchery'] and \
                    event.control_pid in parsed_data['players']:
                parsed_data['players'][event.control_pid]['clock_position'] = \
                        _get_clock_position(parsed_data, event)
            continue

        event.frame = int(event.frame)

        if event.name == 'PlayerStatsEvent' and event.pid in parsed_data['players']:
            parsed_data['players'][event.pid]['supply'].append(
                [event.frame, int(event.food_used)])
            # TODO this is a hack for LotV; hopefully I have a better solution coming up
            if event.frame == 1 and int(event.food_used) == 12:
                parsed_data['players'][event.pid]['supply'][0][1] = 12
                parsed_data['expansion'] = 'LotV'
                constants = lotv_constants
        elif event.name == 'UnitBornEvent':
            unit_born_event(builds, event, parsed_data, constants, chronoboosts)
        elif event.name == 'UnitInitEvent':
            unit_init_event(builds, event, parsed_data, constants)
        elif event.name == 'UpgradeCompleteEvent':
            upgrade_event(builds, event, parsed_data, constants, chronoboosts)
        elif event.name == 'UnitTypeChangeEvent':
            change_event(builds, event, parsed_data, constants)
        elif event.name == 'UnitDiedEvent':
            died_event(units_lost, event, parsed_data,constants)

    parsed_data['buildOrderExtracted'] = True  # legacy code
    make_event_timeline(builds, cutoff_time, parsed_data, 'buildOrder', constants)
    make_event_timeline(units_lost, cutoff_time, parsed_data, 'unitsLost', constants)
    make_event_timeline(abilities, cutoff_time, parsed_data, 'abilities', constants)

    if cache_path:
        with open(cache_path, 'w') as fout:
            json.dump(parsed_data, fout)

    return parsed_data


def parse_map_details(replay, parsed_data):
    parsed_data['map_details'] = {
            'height': replay.map.map_info.height,
            'width': replay.map.map_info.width,
            }


def parse_replay(replay_file, cutoff_time=None, cache_dir=None, include_map_details=False):
    """
    replay_file can either be a path to a file or a file-like object
    Parse replay for build order related events
    cutoff_time determines a point at which we stop processing the replay
    cache_dir setups a folder where results are stored for the future
    """

    cache_path = None
    if cache_dir:
        replay_hash = None
        if isinstance(replay_file, str):
            with open(replay_file, 'r') as fin:
                replay_hash = hashlib.md5(fin.read()).hexdigest()
        else:
            replay_hash = hashlib.md5(replay_file.read()).hexdigest()
        cache_path = os.path.join(cache_dir, replay_hash)
        if os.path.exists(cache_path):
            with open(cache_path, 'r') as cache_file:
                result = json.load(cache_file)
                return result

    try:
        replay = sc2reader.load_replay(replay_file)
    except (sc2reader.exceptions.ReadError, sc2reader.exceptions.MPQError) as error:
        raise ReadError(str(error))

    parsed_data = {
        'buildOrderExtracted': False,
        'message': '',
        'build': replay.build,
        'baseBuild': replay.versions[5],
        'category': replay.category,
        'expansion': replay.expansion,
        'unix_timestamp': replay.unix_timestamp,  # time completed
        'frames': replay.frames,
        'game_type': replay.real_type,
        'region': replay.region,
        'map': replay.map_name,
        'map_hash': replay.map_hash,
    }

    parsed_data['players'] = dict(
        (key,
            {
                'name': player.name,
                'pick_race': player.pick_race,  # can be random
                'race': player.play_race,
                'league': player.highest_league if player.is_human else None,
                'level': player.combined_race_levels if player.is_human else None,
                'is_winner': player.team.result == 'Win',
                'result': player.team.result,
                'is_human': player.is_human,
                'handicap': player.handicap,
                'color': player.color.hex,
                'uid': player.toon_id,  # naming change from sc2reader
                'region': player.region,
                'supply': [[0, 6]],
                'team': player.team.number,
                'clock_position': None,
            }) for key, player in replay.player.items()
    )

    try:
        if include_map_details:
            replay.load_map()
    except:
        include_map_details = False
    parsed_data['include_map_details'] = include_map_details  # reset if something goes wrong
    if include_map_details:
        parse_map_details(replay, parsed_data)

    return parse_events(
        replay,
        cutoff_time,
        parsed_data,
        cache_path,
        include_map_details
    )
