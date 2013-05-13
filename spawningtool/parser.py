"""
spawningtool.parser
~~~~~~~~~~~~~~~~~~~
"""
import sc2reader

from spawningtool.constants import BO_EXCLUDED, BUILD_TIMES
from spawningtool.exception import CutoffTimeError, ReplayFormatError


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
    def __init__(self, frame, supply=None):
        self.frame = frame
        self.supply = supply

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

    def __unicode__(self):
        return '{} {} {}'.format(
            self.supply,
            _frame_to_time(self.frame),
            self.name
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
    player = event.control_pid
    unit_name = event.unit_type_name
    if unit_name in BO_EXCLUDED or player == 0:
        return
    try:
        frame = event.frame - BUILD_TIMES[unit_name]
    except KeyError:
        frame = event.frame
        unit_name += ' (Error on time)'
    supply = get_supply(parsed_data['players'][player]['supply'], frame)
    builds[player].add_event(BuildEvent(unit_name, frame, supply))


def unit_init_event(builds, event, parsed_data):
    player = event.control_pid
    unit_name = event.unit_type_name
    if unit_name in BO_EXCLUDED or player == 0:
        return
    frame = event.frame
    supply = parsed_data['players'][player]['supply'][-1][1]
    builds[player].add_event(BuildEvent(unit_name, frame, supply))


def upgrade_event(builds, event, parsed_data):
    player = event.pid
    if player == 0:
        return
    unit_name = event.upgrade_type_name
    try:
        frame = event.frame - BUILD_TIMES[unit_name]
    except KeyError:
        frame = event.frame
        unit_name += ' (Error on time)'
    supply = get_supply(parsed_data['players'][player]['supply'], frame)
    builds[player].add_event(BuildEvent(unit_name, frame, supply))


def make_event_timeline(builds, cutoff_time, parsed_data):
    """
    Converts the GameTimeline into a readable structure
    """
    for i, build in builds.iteritems():
        build.sort()

        parsed_data['players'][i]['buildOrder'] = []
        for event in build.timeline:

            # If desired, stop parsing for events after a given time
            current_gametime = _frame_to_time(event.frame)
            if (cutoff_time and
                    convert_gametime_to_float(current_gametime) >
                    convert_gametime_to_float(cutoff_time)):
                break

            parsed_data['players'][i]['buildOrder'].append(
                {
                    'frame': event.frame,
                    'time': _frame_to_time(event.frame),
                    'name': event.name,
                    'supply': event.supply,
                    'is_worker': event.is_worker()
                }
            )


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

    builds = dict((key, GameTimeline()) for key in replay.player.iterkeys())

    for event in replay.tracker_events:
        if event.frame == 0:
            continue

        if event.name == 'PlayerStatsEvent':
            parsed_data['players'][event.pid]['supply'].append(
                [event.frame, event.food_used / 4096])
        elif event.name == 'UnitBornEvent':  # need to reverse this
            unit_born_event(builds, event, parsed_data)
        elif event.name == 'UnitInitEvent':
            unit_init_event(builds, event, parsed_data)
        elif event.name == 'UpgradeCompleteEvent':  # need to reverse this
            upgrade_event(builds, event, parsed_data)

    parsed_data['buildOrderExtracted'] = True  # legacy code
    make_event_timeline(builds, cutoff_time, parsed_data)
    return parsed_data


def parse_replay(replay_file, cutoff_time=None):
    """
    Parse replay for build order related events
    """
    replay = sc2reader.load_replay(replay_file)

    parsed_data = {
        'buildOrderExtracted': False,
        'message': '',
        'build': replay.build,
        'baseBuild': replay.versions[5],
        'map': replay.map_name,
    }

    parsed_data['players'] = dict(
        (key,
            {
                'name': player.name,
                'race': player.play_race,
                'is_winner': player.team.result == 'Win',
                'is_human': player.is_human,
                'supply': [[0, 6]],
            }) for key, player in replay.player.iteritems()
    )

    return parse_events(
        replay,
        cutoff_time,
        parsed_data,
    )
