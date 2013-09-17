"""
spawningtool.parser
~~~~~~~~~~~~~~~~~~~
"""
import sc2reader

from spawningtool.constants import (BO_EXCLUDED, BO_CHANGED_EXCLUDED, BUILD_TIMES,
        TRACKED_ABILITIES, )
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


def _frame_to_time(frame):
    seconds = frame / 16
    return '{0}:{1:02d}'.format(seconds / 60, seconds % 60)


class TrackerEvent(object):
    """
    not necesarily a trackerevent, but event was too generic
    """
    def __init__(self, frame, supply=None):
        self.frame = frame
        self.supply = supply

    def to_dict(self):
        raise NotImplementedError

    def __unicode__(self):
        if self.supply:
            return '{} {} Event'.format(self.supply, self.frame)
        return '{} Event'.format(self.frame)


class BuildEvent(TrackerEvent):
    def __init__(self, name, frame, supply):
        self.name = name
        super(BuildEvent, self).__init__(frame, supply)

    def is_worker(self):
        return self.name in ['SCV', 'Drone', 'Probe']

    def to_dict(self):
        return {
            'frame': self.frame,
            'time': _frame_to_time(self.frame),
            'name': self.name,
            'supply': self.supply,
            'is_worker': self.is_worker()
        }

    def __unicode__(self):
        return '{} {} {}'.format(
            self.supply,
            _frame_to_time(self.frame),
            self.name
        )


class DiedEvent(TrackerEvent):
    def __init__(self, name, frame, killer):
        self.name = name
        super(DiedEvent, self).__init__(frame, None)
        self.killer = killer  # player id

    def to_dict(self):
        return {
            'frame': self.frame,
            'time': _frame_to_time(self.frame),
            'name': self.name,
            'killer': self.killer,
        }

    def __unicode__(self):
        return '{} {} killed by {}'.format(
            _frame_to_time(self.frame),
            self.name,
            self.killer,
            )


class AbilityEvent(TrackerEvent):
    def __init__(self, name, frame):
        self.name = name
        super(AbilityEvent, self).__init__(frame, None)

    def to_dict(self):
        return {
            'frame': self.frame,
            'time': _frame_to_time(self.frame),
            'name': self.name,
        }

    def __unicode__(self):
        return '{} {}'.format(
            _frame_to_time(self.frame),
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
        return '\n'.join([unicode(event) for event in self.timeline])


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
        mid = (start + end) / 2
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


def unit_born_event(builds, event, parsed_data):
    """
    need to reverse the time
    if the unit morphs, it's preferable to use the unit_type_name since it's what it was
    actually born as. sc2reader does, however, provide some nice normalization, so
    swap the display name as necessary
    """
    player = event.control_pid
    unit_name = event.unit_type_name
    if unit_name in BO_EXCLUDED or player == 0 or event.unit.hallucinated:
        return

    if not unit_name in BUILD_TIMES:
        unit_name = event.unit.name
        if unit_name in BO_EXCLUDED:
            return
    if unit_name is None:
        unit_name = '(None)'

    try:
        frame = event.frame - BUILD_TIMES[unit_name]
    except KeyError:
        frame = event.frame
        unit_name += ' (Error on born time)'
    supply = get_supply(parsed_data['players'][player]['supply'], frame)
    builds[player].add_event(BuildEvent(unit_name, frame, supply))


def unit_init_event(builds, event, parsed_data):
    player = event.control_pid
    unit_name = event.unit_type_name
    if unit_name in BO_EXCLUDED or player == 0 or event.unit.hallucinated:
        return
    frame = event.frame
    supply = parsed_data['players'][player]['supply'][-1][1]
    builds[player].add_event(BuildEvent(unit_name, frame, supply))


def upgrade_event(builds, event, parsed_data):
    """
    need to reverse the time
    """
    player = event.pid
    if player == 0:
        return
    unit_name = event.upgrade_type_name
    try:
        frame = event.frame - BUILD_TIMES[unit_name]
    except KeyError:
        frame = event.frame
        unit_name += ' (Error on upgrade time)'
    supply = get_supply(parsed_data['players'][player]['supply'], frame)
    builds[player].add_event(BuildEvent(unit_name, frame, supply))


def change_event(builds, event, parsed_data):
    if not event.unit.owner:  # happened when knocking down rocks
        return
    player = event.unit.owner.pid
    unit_name = event.unit_type_name
    if player == 0 or unit_name in BO_CHANGED_EXCLUDED:
        return

    try:
        frame = event.frame - BUILD_TIMES[unit_name]
    except KeyError:
        return

    supply = get_supply(parsed_data['players'][player]['supply'], frame)
    builds[player].add_event(BuildEvent(unit_name, frame, supply))


def died_event(units_lost, event):
    """
    for born events, the name needed to be corrected for evolutions
    but if it dies, then it should die in its final form
    """
    if not event.unit or not event.unit.owner:
        return
    player = event.unit.owner.pid
    unit_name = event.unit.name

    if unit_name in BO_EXCLUDED or player == 0:
        return

    killer = event.killer_pid

    units_lost[player].add_event(DiedEvent(unit_name, event.frame, killer))


def ability_event(abilities, event):
    player = event.player.pid
    ability_name = event.ability_name

    if ability_name not in TRACKED_ABILITIES or not player:
        return

    abilities[player].add_event(AbilityEvent(ability_name, event.frame))


def make_event_timeline(timelines, cutoff_time, parsed_data, field):
    """
    Converts the GameTimeline into a readable structure
    """
    for i, timeline in timelines.iteritems():
        timeline.sort()

        parsed_data['players'][i][field] = []
        for event in timeline.timeline:

            # If desired, stop parsing for events after a given time
            current_gametime = _frame_to_time(event.frame)
            if (cutoff_time and
                    convert_gametime_to_float(current_gametime) >
                    convert_gametime_to_float(cutoff_time)):
                break

            parsed_data['players'][i][field].append(event.to_dict())


def parse_events(replay, cutoff_time, parsed_data):
    """
    Parse all game related events
    """
    if not hasattr(replay, 'tracker_events'):
        if replay.build < 25604:  # this is 2.0.8
            raise ReplayFormatError(DATA_NOT_SUPPORTED, parsed_data)
        else:
            raise ReplayFormatError((
                'No tracker data could be found, despite this being the'
                ' right version ({}). Sorry.'.format(parsed_data['build'])
            ), parsed_data)

    if replay.expansion != 'HotS':
        # primarily because the build times are off, but I don't want to deal with it
        raise ReplayFormatError(('spawningtool currently only supports HotS.'), parsed_data)

    builds = dict((key, GameTimeline()) for key in replay.player.iterkeys())
    units_lost = dict((key, GameTimeline()) for key in replay.player.iterkeys())
    abilities = dict((key, GameTimeline()) for key in replay.player.iterkeys())

    for event in replay.tracker_events:
        if event.frame == 0:
            continue
        if event.name == 'PlayerStatsEvent' and event.pid in parsed_data['players']:
            parsed_data['players'][event.pid]['supply'].append(
                [event.frame, int(event.food_used)])
        elif event.name == 'UnitBornEvent':
            unit_born_event(builds, event, parsed_data)
        elif event.name == 'UnitInitEvent':
            unit_init_event(builds, event, parsed_data)
        elif event.name == 'UpgradeCompleteEvent':
            upgrade_event(builds, event, parsed_data)
        elif event.name == 'UnitTypeChangeEvent':
            change_event(builds, event, parsed_data)
        elif event.name == 'UnitDiedEvent':
            died_event(units_lost, event)

    legit_ability_event_types = set([
        'LocationAbilityEvent',
        'TargetAbilityEvent',
        'SelfAbilityEvent',
        'AbilityEvent',
        ])
    for event in replay.game_events:
        if event.name in legit_ability_event_types:
            ability_event(abilities, event)

    parsed_data['buildOrderExtracted'] = True  # legacy code
    make_event_timeline(builds, cutoff_time, parsed_data, 'buildOrder')
    make_event_timeline(units_lost, cutoff_time, parsed_data, 'unitsLost')
    make_event_timeline(abilities, cutoff_time, parsed_data, 'abilities')
    return parsed_data


def parse_replay(replay_file, cutoff_time=None):
    """
    Parse replay for build order related events
    """
    try:
        replay = sc2reader.load_replay(replay_file)
    except sc2reader.exceptions.ReadError as error:
        raise ReadError(error.message)
    except Exception as error:  # Maybe a MPQError
        raise ReadError(error.message)

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
        'gateway': replay.gateway,
        'map': replay.map_name,
        'map_hash': replay.map_hash,
    }

    parsed_data['players'] = dict(
        (key,
            {
                'name': player.name,
                'pick_race': player.pick_race,  # can be random
                'race': player.play_race,
                'is_winner': player.team.result == 'Win',
                'result': player.team.result,
                'is_human': player.is_human,
                'handicap': player.handicap,
                'color': player.color.hex,
                'uid': player.toon_id,  # naming change from sc2reader
                'region': player.region,
                'supply': [[0, 6]],
                'team': player.team.number,
            }) for key, player in replay.player.iteritems()
    )

    return parse_events(
        replay,
        cutoff_time,
        parsed_data,
    )
