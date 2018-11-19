"""
spawningtool.parser
~~~~~~~~~~~~~~~~~~~
"""


import hashlib
import json
import os
import sc2reader

from spawningtool import coop_constants, hots_constants, lotv_constants
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


def get_protocol(base_build):
    try:
        protocol_name = 'protocol{}'.format(base_build)
        _temp = __import__('s2protocol', globals(), locals(), [protocol_name])
    except:
        return None
    else:
        return getattr(_temp, protocol_name)


class TrackerEvent(object):
    """
    not necesarily a trackerevent, but event was too generic
    """

    def __init__(self, frame, frames_per_second, supply=None, clock_position=None):
        self.frame = frame
        self.supply = supply
        self.clock_position = clock_position
        self.frames_per_second = frames_per_second

    def to_dict(self):
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
        super(BuildEvent, self).__init__(frame, frames_per_second, supply,
                                         clock_position=clock_position)

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
        super(DiedEvent, self).__init__(frame, frames_per_second, None,
                                        clock_position=clock_position)
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


class GameParser(object):
    """
    Wrapper around the parser. This stores data into attributes to avoid long lists of
    parameters
    """

    replay_file = None  # file path or file-like object
    cache_path = None
    replay = None  # sc2reader parsed version
    parsed_data = None

    unit_build_time_modifier = None  # special case for various commanders
    upgrade_build_time_modifier = None  # special case for various commanders
    building_morph_build_time_modifier = None  # special case for Abathur

    builds = None
    units_lost = None
    abilities = None
    chronoboosts = None
    chronoboost_multiplier = None

    constants = None
    frames_per_second = None
    bo_excluded = None
    bo_changed_excluded = None
    bo_upgrades_excluded = None
    tracked_abilities = None

    def __init__(self, replay_file):
        self.replay_file = replay_file

    def get_parsed_data(self, cutoff_time=None, cache_dir=None, include_map_details=False):
        """
        primary entry point to get a JSON-like representation fo the replay data
        """

        cached_data = self.get_cached_data(cache_dir)
        if cached_data:
            return cached_data

        self.load_replay()

        self.parsed_data = {
            'buildOrderExtracted': False,
            'message': '',
            'build': self.replay.build,
            'baseBuild': self.replay.versions[5],
            'category': self.replay.category,
            'expansion': self.replay.expansion,
            'unix_timestamp': self.replay.unix_timestamp,  # time completed
            'frames': self.replay.frames,
            'game_type': self.replay.real_type,
            'region': self.replay.region,
            'map': self.replay.map_name,
            'map_hash': self.replay.map_hash,
            # as of 4/6/18, co-op replays are not marked as co-op
            'cooperative': (self.replay.cooperative or
                            any(player.commander for player in self.replay.players)),
        }

        self.check_replay_version()

        self.parsed_data['players'] = dict(
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
                 'commander': player.commander,
             }) for key, player in self.replay.player.items()
        )

        self.parse_map_details(include_map_details)

        self.parse_events(cutoff_time, include_map_details)

        if self.cache_path:
            with open(self.cache_path, 'w') as fout:
                json.dump(self.parsed_data, fout)

        return self.parsed_data

    def get_cached_data(self, cache_dir):
        """
        retrieves cached result if possible. If not, then it will set the cache path if
        provided
        """
        self.cache_path = None
        if cache_dir:
            replay_hash = None
            if isinstance(self.replay_file, str):
                with open(self.replay_file, 'r') as fin:
                    replay_hash = hashlib.md5(fin.read()).hexdigest()
            else:
                replay_hash = hashlib.md5(self.replay_file.read()).hexdigest()
            cache_path = os.path.join(cache_dir, replay_hash)
            if os.path.exists(cache_path):
                with open(cache_path, 'r') as cache_file:
                    result = json.load(cache_file)
                    return result
        return None

    def load_replay(self):
        try:
            self.replay = sc2reader.load_replay(self.replay_file)
        except (sc2reader.exceptions.ReadError, sc2reader.exceptions.MPQError) as error:
            raise ReadError(str(error))

    def check_replay_version(self):
        if not getattr(self.replay, 'tracker_events', None):
            if self.replay.build < 25604:  # this is 2.0.8
                raise ReplayFormatError(DATA_NOT_SUPPORTED, self.parsed_data)
            else:
                raise ReplayFormatError((
                    'No tracker data could be found, despite this being the'
                    ' right version ({}). Sorry.'.format(self.parsed_data['build'])
                ), self.parsed_data)

        if self.replay.expansion == 'WoL':
            # primarily because the build times are off, but I don't want to deal with it
            raise ReplayFormatError(('spawningtool does not support WoL.'), self.parsed_data)

    def parse_map_details(self, include_map_details):
        """
        Retrieves map details primarily for map dimensions to determine clock positions of
        various events
        """
        try:
            if include_map_details:
                self.replay.load_map()
        except:
            include_map_details = False

        # reset if something goes wrong
        self.parsed_data['include_map_details'] = include_map_details

        if include_map_details:
            self.parsed_data['map_details'] = {
                'height': self.replay.map.map_info.height,
                'width': self.replay.map.map_info.width,
            }

    def parse_events(self, cutoff_time, include_map_details=False):
        """
        Parse all events within the replay
        """
        self.set_constants()
        self.parsed_data['frames_per_second'] = self.frames_per_second

        self.add_ability_events()
        self.make_event_timeline(self.abilities, cutoff_time, 'abilities')

        self.set_chronoboost_data()

        self.set_commander_talents()

        self.add_tracker_events(include_map_details)
        self.make_event_timeline(self.builds, cutoff_time, 'buildOrder')
        self.make_event_timeline(self.units_lost, cutoff_time, 'unitsLost')

        self.parsed_data['buildOrderExtracted'] = True  # legacy code

    def set_constants(self):
        """
        Determine what set of game data constants to use. HotS, LotV, and Co-op all have
        different sets of units with their own build times. They even vary in the game speed
        """

        if self.parsed_data['cooperative']:
            self.constants = coop_constants

        else:
            if self.replay.expansion == 'LotV':
                self.constants = lotv_constants
            else:
                self.constants = hots_constants

            for event in self.replay.tracker_events:
                if event.frame > 1:
                    break
                # TODO this is a hack for early LotV replays done in HotS
                # and also correctly sets early supply
                if (event.name == 'PlayerStatsEvent' and
                        event.pid in self.parsed_data['players'] and
                        event.frame == 1 and int(event.food_used) == 12):
                    self.parsed_data['players'][event.pid]['supply'][0][1] = 12
                    self.parsed_data['expansion'] = 'LotV'
                    self.constants = lotv_constants

        self.frames_per_second = self.constants.FRAMES_PER_SECOND
        self.bo_excluded = self.constants.BO_EXCLUDED
        self.bo_changed_excluded = self.constants.BO_CHANGED_EXCLUDED
        self.bo_upgrades_excluded = self.constants.BO_UPGRADES_EXCLUDED
        self.tracked_abilities = self.constants.TRACKED_ABILITIES

    def set_commander_talents(self):
        """
        https://us.battle.net/forums/en/sc2/topic/20752557371

        some co-op commanders have special talents that affects build times.

        Swann Power Set 2, power 1 "Immortality Protocol Cost and Build Time" TODO
        """
        self.unit_build_time_modifier = {}
        self.upgrade_build_time_modifier = {}
        self.building_morph_build_time_modifier = {}

        for key, player in self.replay.player.items():
            # Expeditious Evolutions
            # (Power Set 3, power 1)
            # reduces evolution times by 2% for each point
            if player.commander == 'Kerrigan':
                self.upgrade_build_time_modifier[key] = 1 - (player.commander_mastery_talents[4] * .02)

            # Structure Morph and Evolution Rate
            # reduces evolution times by 2% for each point
            if player.commander == 'Abathur':
                self.upgrade_build_time_modifier[key] = 1 - (player.commander_mastery_talents[5] * .02)
                self.building_morph_build_time_modifier[key] = 1 - (player.commander_mastery_talents[5] * .02)

            # Chrono Boost Efficiency
            # (Power Set 3, power 1)
            # increases chronoboost effectiveness by 1% for each point
            if player.commander in ['Artanis', 'Vorazun', 'Karax', 'Fenix']:
                self.chronoboost_multiplier += player.commander_mastery_talents[4] * .01

            # Chrono Boost Efficiency
            # (Power Set 3, power 2)
            # increases chronoboost effectiveness by 1% for each point
            if player.commander in ['Alarak']:
                self.chronoboost_multiplier += player.commander_mastery_talents[5] * .01

            # Research and Development
            # Upgrade research time and resource costs are halved
            # Does not affect weapon and armor upgrades.
            if player.commander == 'Nova' and player.commander_level >= 11:
                self.upgrade_build_time_modifier[key] = .5

            # Impatience
            # Mira's Unit Build and Research times are reduced by 30%
            if player.commander == 'Horner' and player.commander_level >= 6:
                self.unit_build_time_modifier[key] = .7
                self.upgrade_build_time_modifier[key] = .7

            # Chronometry
            # Zeratul's Gateway and Robo units build 50% faster
            if player.commander == 'Zeratul' and player.commander_level >= 10:
                self.unit_build_time_modifier[key] = .5

    def add_ability_events(self):
        """
        Create events around abilities being casted e.g. ChronoBoost, Snipe
        """

        self.abilities = dict((key, GameTimeline()) for key in self.replay.player.keys())
        legit_ability_event_types = set([
            'TargetPointCommandEvent',
            'TargetUnitCommandEvent',
            'DataCommandEvent',
            'BasicCommandEvent',
            ])
        for event in self.replay.game_events:
            if event.name in legit_ability_event_types:
                self.add_ability_event(event)

    def add_ability_event(self, event):
        player = event.player.pid
        ability_name = event.ability_name

        if ability_name not in self.tracked_abilities or not player:
            return

        self.abilities[player].add_event(AbilityEvent(ability_name, event.frame,
                                                      self.frames_per_second))

    def set_chronoboost_data(self):
        CHRONOBOOST_HOTS = 1  # 20 second boost by 50%
        CHRONOBOOST_LOTV = 2  # persistent boost on a building
        CHRONOBOOST_40 = 3  # 10 second boost by 100%

        self.chronoboosts = {}

        if self.replay.expansion == 'LotV' and 1513641600 > self.replay.unix_timestamp > 1510617600:
            # 100% for 10 seconds
            chronoboost_version = CHRONOBOOST_40
            # {pid_1: {'Building': [frame_1, frame_2, ..], ..}, ..}
            raw_chronoboosts = {key: {} for key in self.replay.player.keys()}
            self.chronoboost_multiplier = 1

        elif self.replay.expansion == 'LotV' and \
            1510617600 > self.replay.unix_timestamp > 1441238400 or \
            self.parsed_data['cooperative']:
            # Continuous
            chronoboost_version = CHRONOBOOST_LOTV
            # {pid_1: [[building_1, frame_1], [building_2, frame_2], ..], ..}
            raw_chronoboosts = {key: [] for key in self.replay.player.keys()}
            self.chronoboost_multiplier = .15

        else:
            # 50% for 20 seconds
            chronoboost_version = CHRONOBOOST_HOTS
            # {pid_1: {'Building': [frame_1, frame_2, ..], ..}, ..}
            raw_chronoboosts = {key: {} for key in self.replay.player.keys()}
            self.chronoboost_multiplier = .5

        for event in self.replay.game_events:
            if (event.name == 'TargetUnitCommandEvent' and
                    event.ability_name in ('ChronoBoost', 'ChronoBoostEnergyCost') and
                    event.target):
                player = event.player.pid
                if chronoboost_version == CHRONOBOOST_LOTV:
                    raw_chronoboosts[player].append([event.target.name, event.frame])
                elif chronoboost_version in (CHRONOBOOST_HOTS, CHRONOBOOST_40):
                    if not event.target.name in raw_chronoboosts[player]:
                        raw_chronoboosts[player][event.target.name] = []
                    raw_chronoboosts[player][event.target.name].append(event.frame)

        if chronoboost_version == CHRONOBOOST_LOTV:
            self.process_lotv_chronoboosts(raw_chronoboosts)
        elif chronoboost_version == CHRONOBOOST_HOTS:
            self.process_hots_chronoboosts(raw_chronoboosts, 16 * 20)
        elif chronoboost_version == CHRONOBOOST_40:
            self.process_hots_chronoboosts(raw_chronoboosts, 22.4 * 10)

    def process_lotv_chronoboosts(self, raw_chronoboosts):
        """
        potentially inaccurate if they never move their chronoboost
        """

        for player, all_boosts in raw_chronoboosts.items():
            last_building = 'Nexus'
            last_start_frame = 0

            self.chronoboosts[player] = {}
            all_boosts.append(['', self.replay.frames])
            for building, frame in all_boosts:
                if not last_building in self.chronoboosts[player]:
                    self.chronoboosts[player][last_building] = []
                self.chronoboosts[player][last_building].append([last_start_frame, frame])
                last_building = building
                last_start_frame = frame

            for boosts in self.chronoboosts[player].values():
                boosts.reverse()

    def process_hots_chronoboosts(self, raw_chronoboosts, chronoboost_duration):
        """
        convert raw chronoboosts to a set of frame ranges over which the chronoboost is applied
        to that building. This should be easier to backtrack build times

        This, to some degree, avoids double-counting if a chronoboosted building is
        chronoboosted again or if all of the buildings of the same type are chronoboosted
        """
        self.chronoboosts = {}

        for player, all_boosts in raw_chronoboosts.items():
            self.chronoboosts[player] = {}
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

                self.chronoboosts[player][building] = frame_ranges

    def add_tracker_events(self, include_map_details):
        self.builds = dict((key, GameTimeline()) for key in self.replay.player.keys())
        self.units_lost = dict((key, GameTimeline()) for key in self.replay.player.keys())

        for event in self.replay.tracker_events:
            if event.frame == 0:
                # set player start position
                if include_map_details and event.name == 'UnitBornEvent' and \
                        event.unit_type_name in ['Nexus', 'CommandCenter', 'Hatchery'] and \
                        event.control_pid in self.parsed_data['players']:
                    self.parsed_data['players'][event.control_pid]['clock_position'] = \
                            self.get_clock_position(event)
                continue

            event.frame = int(event.frame)

            if event.name == 'PlayerStatsEvent' and event.pid in self.parsed_data['players']:
                self.parsed_data['players'][event.pid]['supply'].append(
                    [event.frame, int(event.food_used)])
            elif event.name == 'UnitBornEvent':
                self.add_unit_born_event(event)
            elif event.name == 'UnitInitEvent':
                self.add_unit_init_event(event)
            elif event.name == 'UpgradeCompleteEvent':
                self.add_upgrade_event(event)
            elif event.name == 'UnitTypeChangeEvent':
                self.add_change_event(event)
            elif event.name == 'UnitDiedEvent':
                self.add_died_event(event)

    def add_unit_born_event(self, event):
        """
        unit_born is when the unit is actually created, so we subtract the unit build time
        to get when it was started.
        If the unit morphs, it's preferable to use the unit_type_name since it's what it was
        actually born as. sc2reader does, however, provide some nice normalization, so
        swap the display name as necessary
        """
        player = event.control_pid
        unit_name = event.unit_type_name
        if unit_name in self.bo_excluded or player == 0 or event.unit.hallucinated:
            return

        if not unit_name in self.get_build_data(player):
            unit_name = event.unit.name
            if unit_name in self.bo_excluded:
                return

        if unit_name is None:
            unit_name = event.unit_type_name + ' (unit_born data missing)'
            frame = event.frame
            is_chronoboosted = False
        else:
            modifier = self.unit_build_time_modifier.get(player, 1)
            if unit_name in ['SCV', 'Probe']:
                # for Horner, do not apply modifier for SCVs
                # for Zeratul, do not apply modifier for Probes
                modifier = 1
            frame, unit_name, is_chronoboosted = \
                self.adjust_build_time(event.frame, player, unit_name, modifier)

        # for safety to ignore observer units from GH and such
        if not player in self.parsed_data['players']:
            return

        unit_name = self.get_display_name(unit_name, player)

        supply = self.get_supply(player, frame)
        self.builds[player].add_event(
            BuildEvent(unit_name, frame, self.frames_per_second, supply,
                       self.get_clock_position(event), is_chronoboosted))

    def add_unit_init_event(self, event):
        """
        these are mostly buildings, but it may be warped-in units
        """
        player = event.control_pid
        unit_name = event.unit_type_name
        if unit_name in self.bo_excluded or player == 0 or event.unit.hallucinated:
            return
        frame = event.frame

        # for safety to ignore observer units from GH and such
        if not player in self.parsed_data['players']:
            return

        unit_name = self.get_display_name(unit_name, player)

        supply = self.parsed_data['players'][player]['supply'][-1][1]
        self.builds[player].add_event(BuildEvent(unit_name, frame, self.frames_per_second,
                                                 supply, self.get_clock_position(event)))

    def add_upgrade_event(self, event):
        """
        need to reverse the time
        """
        player = event.pid
        if player == 0:
            return
        unit_name = event.upgrade_type_name

        if unit_name in self.bo_upgrades_excluded:
            return

        if unit_name in self.get_build_data(player):
            modifier = self.upgrade_build_time_modifier.get(player, 1)
            if unit_name.startswith('Terran') and \
                    ('ArmorsLevel' in unit_name or 'WeaponsLevel' in unit_name):
                # For Nova and Mira, do not apply modifier to standard upgrades
                modifier = 1
            frame, unit_name, is_chronoboosted = \
                self.adjust_build_time(event.frame, player, unit_name, modifier)
        else:
            unit_name += ' (upgrade missing)'
            frame = event.frame
            is_chronoboosted = False

        unit_name = self.get_display_name(unit_name, player)

        supply = self.get_supply(player, frame)
        self.builds[player].add_event(BuildEvent(
            unit_name, frame, self.frames_per_second, supply, is_chronoboosted=is_chronoboosted))

    def add_change_event(self, event):
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
        if player == 0 or unit_name in self.bo_changed_excluded:
            return

        try:
            data = self.get_build_data(player)[unit_name]
            if data.get('type') == 'Building' and data.get('is_morph'):
                modifier = self.building_morph_build_time_modifier.get(player, 1)
            else:
                modifier = 1
            build_time = data['build_time'] * modifier
            frame = event.frame - build_time
        except KeyError:
            return

        unit_name = self.get_display_name(unit_name, player)
        supply = self.get_supply(player, frame)
        self.builds[player].add_event(BuildEvent(unit_name, frame, self.frames_per_second, supply))

    def add_died_event(self, event):
        """
        for born events, the name needed to be corrected for evolutions
        but if it dies, then it should die in its final form
        """
        if not event.unit or not event.unit.owner:
            return
        player = event.unit.owner.pid
        unit_name = event.unit.name

        if unit_name in self.bo_excluded or player == 0:
            return

        killer = event.killer_pid

        unit_name = self.get_display_name(unit_name, player)
        self.units_lost[player].add_event(
            DiedEvent(unit_name, event.frame, self.frames_per_second, killer,
                      self.get_clock_position(event)))

    def get_build_data(self, player):
        if self.parsed_data['cooperative'] and player in self.replay.player:
            commander = self.replay.player[player].commander
            if commander:
                return self.constants.COMMANDER_BUILD_DATA[commander]
        return self.constants.BUILD_DATA

    def adjust_build_time(self, frame, player, unit_name, build_time_modifier=1):
        """
        chronoboosts is arranged in reverse order.

        This is only an approximation. The edge case behavior isn't perfect (particularly
        around chronoboosts starting before the the guessed start time). We also cannot
        distinguish which building exactly gets boosted. Even so, this is better than no
        tracking at all
        """
        build_data = self.get_build_data(player)
        if not unit_name in build_data:
            unit_name += ' (Error on build time)'
            return frame, unit_name, False

        cur_build_data = build_data[unit_name]

        projected_start = frame - build_data[unit_name]['build_time'] * build_time_modifier
        chronoboosted = False

        if self.chronoboosts.get(player):
            for building in cur_build_data['built_from']:
                if building in self.chronoboosts[player]:
                    for cur_frame_start, cur_frame_end in self.chronoboosts[player][building]:
                        if cur_frame_end > projected_start and cur_frame_start < frame:
                            overlap = min(cur_frame_end, frame) - \
                                max(cur_frame_start, projected_start)
                            reduction = int(overlap * self.chronoboost_multiplier)
                            projected_start += reduction
                            chronoboosted = True

        if projected_start < 0:
            projected_start = 1  # can happen with some weird rounding

        return projected_start, unit_name, chronoboosted

    # 0, 0 is bottom left
    CLOCK_POSITIONS = {
        2: {0: 11, 1: 12, 2: 1},
        1: {0: 9, 1: 0, 2: 3},
        0: {0: 7, 1: 6, 2: 5},
    }

    def get_clock_position(self, event):
        if not self.parsed_data['include_map_details']:
            return None
        x_section = min(event.x // (self.parsed_data['map_details']['width'] // 3), 2)
        y_section = min(event.y // (self.parsed_data['map_details']['height'] // 3), 2)
        return self.CLOCK_POSITIONS[y_section][x_section]

    def get_supply(self, player, frame):
        """
        supply is a list of [FRAME, SUPPLY] lists.
        use binary search to find the supply at or just before the frame provided
        """
        supply = self.parsed_data['players'][player]['supply']
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

    def get_display_name(self, unit_name, player):
        build_data = self.get_build_data(player).get(unit_name)
        if build_data and 'display_name' in build_data:
            return build_data.get('display_name')
        return unit_name

    def make_event_timeline(self, timelines, cutoff_time, field):
        """
        Converts the GameTimeline into a JSON-like format
        """
        for i, timeline in timelines.items():
            timeline.sort()

            self.parsed_data['players'][i][field] = []
            for event in timeline.timeline:

                # If desired, stop parsing for events after a given time
                current_gametime = _frame_to_time(event.frame, self.frames_per_second)
                if (cutoff_time and
                        convert_gametime_to_float(current_gametime) >
                        convert_gametime_to_float(cutoff_time)):
                    break

                self.parsed_data['players'][i][field].append(event.to_dict())


def parse_replay(replay_file, cutoff_time=None, cache_dir=None, include_map_details=False):
    """
    Parse replay for build order related events.

    :param replay_file: either be a path to a file or a file-like object.
    :param cutoff_time: the time at which we stop processing the replay.
    :cache_dir: path to a folder where cached results are saved to and retrieved from
    """

    parser = GameParser(replay_file)

    return parser.get_parsed_data(cutoff_time, cache_dir, include_map_details)
