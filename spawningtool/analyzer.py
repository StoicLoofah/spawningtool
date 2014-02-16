#!/usr/bin/env python
import argparse
from collections import Counter

from spawningtool.parser import parse_replay


def map_replays(filenames, map_fn, cache_dir=None):
    for filename in filenames:
        filename = filename.rstrip('\n')
        replay = parse_replay(filename, cache_dir=cache_dir)
        map_fn(replay)


def count_win_percentage_by_supply_difference(filenames, condition=None, cache_dir=None):
    num_games_counter = Counter()
    num_wins_counter = Counter()

    def update_counters(replay):
        if len(replay['players']) != 2:
            return
        players = replay['players'].values()
        player_1 = players[0]
        player_2 = players[1]
        if player_1['is_winner'] == player_2['is_winner']:
            return

        is_counting_player_1 = not condition or condition(replay, player_1, player_2)
        is_counting_player_2 = not condition or condition(replay, player_1, player_2)

        if is_counting_player_1 or is_counting_player_2:
            player_2_supply = player_2['supply']
            supply_len = len(player_2_supply)
            for i, data in enumerate(player_1['supply']):
                if i >= supply_len:
                    continue
                diff = data[1] - player_2_supply[i][1]

                if is_counting_player_1:
                    num_games_counter[diff] += 1
                    if player_1['is_winner']:
                        num_wins_counter[diff] += 1

                if is_counting_player_2:
                    num_games_counter[-diff] += 1
                    if player_2['is_winner']:
                        num_wins_counter[-diff] += 1

    map_replays(filenames, update_counters, cache_dir)

    return [ [unicode(i), unicode(num_wins_counter[i]), unicode(num_games_counter[i])]
            for i in range(-100, 100)]


RACE_BY_LETTER = {'z': 'Zerg', 't': 'Terran', 'p': 'Protoss'}


def main():
    """
    Execute spawningtool
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', help='text file with a list of SC2Replay paths')
    parser.add_argument('--cache-dir', help='Directory to cache results in')
    parser.add_argument('--matchup', help='Which matchup to check')

    args = parser.parse_args()

    condition = None
    if args.matchup and len(args.matchup) == 3:
        player_1_race = RACE_BY_LETTER[args.matchup[0].lower()]
        player_2_race = RACE_BY_LETTER[args.matchup[2].lower()]

        condition = lambda replay, player_1, player_2: \
                player_1['race'] == player_1_race and player_2['race'] == player_2_race

    with open(args.filenames, 'r') as fin:
        result = count_win_percentage_by_supply_difference(
                fin, condition=condition, cache_dir=args.cache_dir)
        for row in result:
            print ','.join([unicode(val) for val in row])

if __name__ == '__main__':
    main()
