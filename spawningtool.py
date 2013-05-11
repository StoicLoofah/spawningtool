"""
spawningtool
~~~~~~~~~~~~
"""
from s2protocol import protocol15405
from s2protocol.mpyq import mpyq

from constants import BO_EXCLUDED, BUILD_TIMES
from exception import CutoffTimeError, ReplayFormatError


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


def _gameloop_to_time(gameloop):
    seconds = gameloop / 16
    return '{0}:{1:02d}'.format(seconds / 60, seconds % 60)


class TrackerEvent(object):
    def __init__(self, gameloop, supply=None):
        self.gameloop = gameloop
        self.supply = supply

    def __unicode__(self):
        if self.supply:
            return '{} {} Event'.format(self.supply, self.gameloop)
        return '{} Event'.format(self.gameloop)


class BuildEvent(TrackerEvent):
    def __init__(self, name, gameloop, supply):
        self.name = name
        super(BuildEvent, self).__init__(gameloop, supply)

    def is_worker(self):
        return self.name in ['SCV', 'Drone', 'Probe']

    def __unicode__(self):
        return '{} {} {}'.format(
            self.supply, 
            _gameloop_to_time(self.gameloop), 
            self.name
        )


class GameTimeline(object):
    def __init__(self):
        self.timeline = []

    def add_event(self, event):
        self.timeline.append(event)

    def sort(self):
        self.timeline.sort(key=lambda a: a.gameloop)

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


def get_supply(supply, gameloop):
    start = 0
    end = len(supply) - 1

    while start < end:
        mid = (start + end) / 2
        val = supply[mid][0]
        if val == gameloop:
            return mid
        if gameloop < val:
            end = mid - 1
        else:
            start = mid + 1

    if start != 0 and supply[start][0] > gameloop:
        start -= 1

    return supply[start][1]


def unit_born_event(builds, event, parsed_data):
    player = event['m_controlPlayerId']
    unit_name = event['m_unitTypeName']
    if unit_name in BO_EXCLUDED or player == 0:
        return
    try:
        gameloop = event['_gameloop'] - BUILD_TIMES[unit_name]
    except KeyError:
        gameloop = event['_gameloop']
        unit_name += ' (Error on time)'
    supply = get_supply(parsed_data['players'][player - 1]['supply'], gameloop)
    builds[player - 1].add_event(BuildEvent(unit_name, gameloop, supply))


def unit_init_event(builds, event, parsed_data):
    player = event['m_controlPlayerId']
    unit_name = event['m_unitTypeName']
    if unit_name in BO_EXCLUDED or player == 0:
        return
    gameloop = event['_gameloop']
    supply = parsed_data['players'][player - 1]['supply'][-1][1]
    builds[player - 1].add_event(BuildEvent(unit_name, gameloop, supply))


def upgrade_event(builds, event, parsed_data):
    player = event['m_playerId']
    if player == 0:
        return
    unit_name = event['m_upgradeTypeName']
    try:
        gameloop = event['_gameloop'] - BUILD_TIMES[unit_name]
    except KeyError:
        gameloop = event['_gameloop']
        unit_name += ' (Error on time)'
    supply = get_supply(parsed_data['players'][player - 1]['supply'], gameloop)
    builds[player - 1].add_event(BuildEvent(unit_name, gameloop, supply))


def make_event_timeline(builds, cutoff_time, parsed_data):
    """
    Make an event timeline
    """
    for i in xrange(parsed_data["numPlayers"]):

        parsed_data['players'][i]['buildOrder'] = []
        for event in builds[i].timeline:

            # If desired, stop parsing for events after a given time
            current_gametime = _gameloop_to_time(event.gameloop)
            if (cutoff_time and 
                    convert_gametime_to_float(current_gametime) > 
                    convert_gametime_to_float(cutoff_time)):
                break
            
            parsed_data['players'][i]['buildOrder'].append(
                {
                    'gameloop': event.gameloop,
                    'time': _gameloop_to_time(event.gameloop),
                    'name': event.name,
                    'supply': event.supply,
                    'is_worker': event.is_worker()
                }
            )


def parse_events(archive, cutoff_time, header, parsed_data, protocol):
    """
    Parse all game related events
    """
    builds = [GameTimeline() for _ in xrange(parsed_data['numPlayers'])]

    if hasattr(protocol, 'decode_replay_tracker_events'):
        contents = archive.read_file('replay.tracker.events')
        events = protocol.decode_replay_tracker_events(contents)

        has_events = False
        for event in events:
            has_events = True
            event_type = event['_event']
            if event['_gameloop'] == 0:
                continue
    
            if event_type == 'NNet.Replay.Tracker.SPlayerStatsEvent':
                parsed_data['players'][event['m_playerId'] - 1]['supply'].append(
                    [event['_gameloop'], event['m_stats']['m_scoreValueFoodUsed'] / 4096])
            elif event_type == 'NNet.Replay.Tracker.SUnitBornEvent':  # need to reverse this    
                unit_born_event(builds, event, parsed_data)
            elif event_type == 'NNet.Replay.Tracker.SUnitInitEvent':
                unit_init_event(builds, event, parsed_data)
            elif event_type == 'NNet.Replay.Tracker.SUpgradeEvent':  # need to reverse this 
                upgrade_event(builds, event, parsed_data)

        if not has_events:
            if header['m_version']['m_build'] < 25604:  # this is 2.0.8
                message = DATA_NOT_SUPPORTED
            else:
                message = (
                    'No tracker data could be found, despite this being the'
                    ' right version ({}). Sorry.'.format(parsed_data['build'])
                )
            raise ReplayFormatError(message)

        for build in builds:
            build.sort()
        
        make_event_timeline(builds, cutoff_time, parsed_data)
    
        return parsed_data
    else:
        raise ReplayFormatError(DATA_NOT_SUPPORTED)


def parse_replay(args):
    """
    Parse replay for build order related events
    """
    archive = mpyq.MPQArchive(args.replay_file)

    contents = archive.header['user_data_header']['content']
    header = protocol15405.decode_replay_header(contents)

    base_build = header['m_version']['m_baseBuild']
    parsed_data = {'build': base_build}

    protocol = get_protocol(base_build)
    if not protocol:
        raise ReplayFormatError('Could locate the replay version')

    contents = archive.read_file('replay.details')
    details = protocol.decode_replay_details(contents)
    parsed_data['numPlayers'] = len(details["m_playerList"])
    parsed_data['map'] = details['m_title']
    parsed_data['players'] = [
        {
            'name': raw_data['m_name'],
            'race': raw_data['m_race'],
            'is_winner': raw_data['m_result'] == 1,
            'supply': [[0, 6]]
        } for raw_data in details['m_playerList']
    ]

    return parse_events(
        archive, 
        args.cutoff_time, 
        header, 
        parsed_data, 
        protocol
    )
