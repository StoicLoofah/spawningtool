#!/usr/bin/env python
import argparse
from collections import Counter

from spawningtool.parser import parse_replay


def map_replays(filenames, map_fn):
    for filename in filenames:
        filename = filename.rstrip('\n')
        replay = parse_replay(filename)
        map_fn(replay)


def count_win_percentage_by_supply_difference(filenames):
    num_games_counter = Counter()
    num_wins_counter = Counter()

    def update_counters(replay):
        if len(replay['players']) != 2:
            return
        winner = None
        loser = None
        for player in replay['players'].values():
            if player['is_winner']:
                winner = player
            else:
                loser = player
        if not winner or not loser:
            return
        loser_supply = loser['supply']
        for i, data in enumerate(winner['supply']):
            diff = data[1] - loser_supply[i][1]
            if diff > 0:
                num_wins_counter[diff] += 1
            num_games_counter[abs(diff)] += 1

    map_replays(filenames, update_counters)

    return [ [unicode(i), unicode(num_wins_counter[i]), unicode(num_games_counter[i])]
            for i in range(200)]


def main():
    """
    Execute spawningtool
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', help='text file with a list of SC2Replay paths')
    args = parser.parse_args()
    with open(args.filenames, 'r') as fin:
        result = count_win_percentage_by_supply_difference(fin)
        for row in result:
            print ','.join([unicode(val) for val in row])

if __name__ == '__main__':
    main()
