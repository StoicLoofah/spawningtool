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


archive = mpyq.MPQArchive('replays/myreplay.SC2Replay')

contents = archive.header['user_data_header']['content']
header = protocol15405.decode_replay_header(contents)

baseBuild = header['m_version']['m_baseBuild']
try:
    protocol_name = 'protocol%s' % (baseBuild,)
    _temp = __import__('s2protocol', globals(), locals(), [protocol_name])
    protocol = getattr(_temp, protocol_name)
except:
    print >> sys.stderr, 'Unsupported base build: %d' % baseBuild
    sys.exit(1)

builds = [GameTimeline() for i in range(2)]
supplies = [[[0, 6]] for i in range(2)]

def get_supply(supply, gameloop):
    start = 0
    end = len(supply)

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


if hasattr(protocol, 'decode_replay_tracker_events'):
    contents = archive.read_file('replay.tracker.events')

    for event in protocol.decode_replay_tracker_events(contents):
        event_type = event['_event']
        if event['_gameloop'] == 0:
            continue
        if event_type == 'NNet.Replay.Tracker.SPlayerStatsEvent':
            supplies[event['m_playerId'] - 1].append(
                    [event['_gameloop'], event['m_stats']['m_scoreValueFoodUsed'] / 4096])
        elif event_type == 'NNet.Replay.Tracker.SUnitBornEvent':  # need to reverse this
            player = event['m_controlPlayerId']
            unit_name = event['m_unitTypeName']
            if unit_name in BO_EXCLUDED or player == 0:
                continue
            gameloop = event['_gameloop'] - BUILD_TIMES[unit_name]
            supply = get_supply(supplies[player - 1], gameloop)
            builds[player - 1].add_event(BuildEvent(unit_name, gameloop, supply))
        elif event_type == 'NNet.Replay.Tracker.SUnitInitEvent':
            player = event['m_controlPlayerId']
            unit_name = event['m_unitTypeName']
            if unit_name in BO_EXCLUDED or player == 0:
                continue
            gameloop = event['_gameloop']
            supply = supplies[player - 1][-1][1]
            builds[player - 1].add_event(BuildEvent(unit_name, gameloop, supply))
        elif event_type == 'NNet.Replay.Tracker.SUpgradeEvent':  # need to reverse this
            player = event['m_playerId']
            if player == 0:
                continue
            unit_name = event['m_upgradeTypeName']
            gameloop = event['_gameloop'] - BUILD_TIMES[unit_name]
            supply = get_supply(supplies[player - 1], gameloop)
            builds[player - 1].add_event(BuildEvent(unit_name, gameloop, supply))

    print supplies
    for build in builds:
        build.sort()
        print unicode(build)
else:
    print 'cannot do anything with this'

