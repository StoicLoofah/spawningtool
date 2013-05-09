import argparse

from s2protocol import protocol15405
from s2protocol.mpyq import mpyq

from constants import *


def _gameloop_to_time(gameloop):
    seconds = gameloop / 16
    return '{0}:{1:02d}'.format(seconds / 60, seconds % 60)


class TrackerEvent(object):
    def __init__(self, gameloop, supply=None):
        self.gameloop = gameloop
        self.supply = supply

    def __unicode__(self):
        if self.supply:
            return '{0} {1} Event'.format(self.supply, self.gameloop)
        return '{0} Event'.format(self.gameloop)


class BuildEvent(TrackerEvent):
    def __init__(self, name, gameloop, supply):
        self.name = name
        super(BuildEvent, self).__init__(gameloop, supply)

    def is_worker(self):
        return self.name in ['SCV', 'Drone', 'Probe']

    def __unicode__(self):
        return '{0} {1} {2}'.format(self.supply, _gameloop_to_time(self.gameloop), self.name)


class GameTimeline(object):
    def __init__(self):
        self.timeline = []

    def add_event(self, event):
        self.timeline.append(event)

    def sort(self):
        self.timeline.sort(key=lambda a: a.gameloop)

    def __unicode__(self):
        return '\n'.join([unicode(event) for event in self.timeline])


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


def parse_replay(file_name):
    parsed_data = {'buildOrderExtracted': False, 'message': ''}

    archive = mpyq.MPQArchive(file_name)

    contents = archive.header['user_data_header']['content']
    header = protocol15405.decode_replay_header(contents)

    baseBuild = header['m_version']['m_baseBuild']
    parsed_data['build'] = baseBuild
    try:
        protocol_name = 'protocol%s' % (baseBuild,)
        _temp = __import__('s2protocol', globals(), locals(), [protocol_name])
        protocol = getattr(_temp, protocol_name)
    except:
        parsed_data['message'] = 'Could locate the replay version'
        return parsed_data

    contents = archive.read_file('replay.details')
    details = protocol.decode_replay_details(contents)
    parsed_data['map'] = details['m_title']
    num_players = len(details['m_playerList'])
    parsed_data['numPlayers'] = num_players
    parsed_data['players'] = [{
        'name': raw_data['m_name'],
        'race': raw_data['m_race'],
        'is_winner': raw_data['m_result'] == 1,
        'supply': [[0, 6]]
        } for raw_data in details['m_playerList']]

    builds = [GameTimeline() for i in range(parsed_data['numPlayers'])]

    if hasattr(protocol, 'decode_replay_tracker_events'):
        contents = archive.read_file('replay.tracker.events')
        has_events = False
        for event in protocol.decode_replay_tracker_events(contents):
            has_events = True
            event_type = event['_event']
            if event['_gameloop'] == 0:
                continue
            if event_type == 'NNet.Replay.Tracker.SPlayerStatsEvent':
                parsed_data['players'][event['m_playerId'] - 1]['supply'].append(
                        [event['_gameloop'], event['m_stats']['m_scoreValueFoodUsed'] / 4096])
            elif event_type == 'NNet.Replay.Tracker.SUnitBornEvent':  # need to reverse this
                player = event['m_controlPlayerId']
                unit_name = event['m_unitTypeName']
                if unit_name in BO_EXCLUDED or player == 0:
                    continue
                try:
                    gameloop = event['_gameloop'] - BUILD_TIMES[unit_name]
                except KeyError:
                    gameloop = event['_gameloop']
                    unit_name += ' (Error on time)'
                supply = get_supply(parsed_data['players'][player - 1]['supply'], gameloop)
                builds[player - 1].add_event(BuildEvent(unit_name, gameloop, supply))
            elif event_type == 'NNet.Replay.Tracker.SUnitInitEvent':
                player = event['m_controlPlayerId']
                unit_name = event['m_unitTypeName']
                if unit_name in BO_EXCLUDED or player == 0:
                    continue
                gameloop = event['_gameloop']
                supply = parsed_data['players'][player - 1]['supply'][-1][1]
                builds[player - 1].add_event(BuildEvent(unit_name, gameloop, supply))
            elif event_type == 'NNet.Replay.Tracker.SUpgradeEvent':  # need to reverse this
                player = event['m_playerId']
                if player == 0:
                    continue
                unit_name = event['m_upgradeTypeName']
                try:
                    gameloop = event['_gameloop'] - BUILD_TIMES[unit_name]
                except KeyError:
                    gameloop = event['_gameloop']
                    unit_name += ' (Error on time)'
                supply = get_supply(parsed_data['players'][player - 1]['supply'], gameloop)
                builds[player - 1].add_event(BuildEvent(unit_name, gameloop, supply))

        if not  has_events:
            parsed_data['message'] = 'No tracker data could be found, despite this being the right version ({0}). Sorry.'.format(parsed_data['build'])
            return parsed_data

        for build in builds:
            build.sort()

        parsed_data['buildOrderExtracted'] = True
        for i in range(num_players):
            parsed_data['players'][i]['buildOrder'] = [
                    {
                        'gameloop': event.gameloop,
                        'time': _gameloop_to_time(event.gameloop),
                        'name': event.name,
                        'supply': event.supply,
                        'is_worker': event.is_worker()
                        } for event in builds[i].timeline]
        return parsed_data

    parsed_data['message'] = 'This replay version does not support the data needed for the build order'
    return parsed_data


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('replay_file', help='.SC2Replay file to load')
    args = parser.parse_args()
    result = parse_replay(args.replay_file)

    if result['buildOrderExtracted']:
        print result['map']
        print result['build']
        for player in result['players']:
            print '{0} ({1})'.format(player['name'], player['race'])
            for event in player['buildOrder']:
                if not event['is_worker']:
                    print '{0} {1} {2}'.format(event['supply'], event['time'], event['name'])
            print ''
    else:
        print result['message']


