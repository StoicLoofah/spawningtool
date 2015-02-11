#!/usr/bin/env python
import argparse
import math
from collections import Counter

from spawningtool.parser import parse_replay


def map_replays(filenames, map_fn, results, update_fn, cache_dir=None, **kwargs):
    for filename in filenames:
        filename = filename.rstrip('\n')
        replay = parse_replay(filename, cache_dir=cache_dir)
        map_fn(replay, results, update_fn, **kwargs)


def check_supplies(replay, results, update_fn, condition=None, min_time=None, max_time=None):
    if len(replay['players']) != 2:
        return
    players = list(replay['players'].values())
    player_1 = players[0]
    player_2 = players[1]
    if player_1['is_winner'] == player_2['is_winner']:
        return

    is_counting_player_1 = not condition or condition(replay, player_1, player_2)
    is_counting_player_2 = not condition or condition(replay, player_2, player_1)

    if is_counting_player_1 or is_counting_player_2:
        if min_time is None:
            min_time = 0
        min_time = int(min_time) * 16

        if max_time is None:
            max_time = 10000
        max_time = int(max_time) * 16

        player_2_supply = player_2['supply']
        supply_len = len(player_2_supply)
        for i, data in enumerate(player_1['supply']):
            if i >= supply_len or min_time > data[0]:
                continue
            if max_time < data[0]:  # we're not going down at this point
                return
            diff = data[1] - player_2_supply[i][1]

            if is_counting_player_1:
                update_fn(results, player_1, player_2, data[1], player_2_supply[i][1], data[0])
            if is_counting_player_2:
                update_fn(results, player_2, player_1, player_2_supply[i][1], data[1], data[0])


def count_win_rate_by_supply_difference(filenames, condition=None, cache_dir=None,
        min_time=None, max_time=None):
    results = {
            'num_games_counter': Counter(),
            'num_wins_counter': Counter(),
            }

    def update_fn(results, player_1, player_2, supply_1, supply_2, frames):
        diff = supply_1 - supply_2

        results['num_games_counter'][diff] += 1
        if player_1['is_winner']:
            results['num_wins_counter'][diff] += 1


    map_replays(filenames, check_supplies, results, update_fn, cache_dir, condition=condition,
            min_time=min_time, max_time=max_time)

    return [ [str(i),
        str(results['num_wins_counter'][i]),
        str(results['num_games_counter'][i])]
            for i in range(-100, 100)]


def count_win_rate_by_supply_ratio(filenames, condition=None, cache_dir=None,
        min_time=None, max_time=None):
    results = {
            'num_games_counter': Counter(),
            'num_wins_counter': Counter(),
            }

    def update_fn(results, player_1, player_2, supply_1, supply_2, frames):
        if supply_1 == 0 or supply_2 == 0:
            return

        result = int(round(math.log(1.0 * supply_1 / supply_2) * 50))

        results['num_games_counter'][result] += 1
        if player_1['is_winner']:
            results['num_wins_counter'][result] += 1

    map_replays(filenames, check_supplies, results, update_fn, cache_dir, condition=condition,
            min_time=min_time, max_time=max_time)

    return [ [str(i),
        str(results['num_wins_counter'][i]),
        str(results['num_games_counter'][i])]
            for i in range(-100, 100)]


def count_win_rate_by_time_supply_difference(filenames, condition=None, cache_dir=None,
        min_time=None, max_time=None):
    results = {
            'num_games_counter': Counter(),
            'num_wins_counter': Counter(),
            }

    def update_fn(results, player_1, player_2, supply_1, supply_2, frames):
        diff = supply_1 - supply_2
        minute = frames / (16 * 60)
        index = (diff, minute)

        results['num_games_counter'][index] += 1
        if player_1['is_winner']:
            results['num_wins_counter'][index] += 1


    map_replays(filenames, check_supplies, results, update_fn, cache_dir, condition=condition,
            min_time=min_time, max_time=max_time)

    return [ [str(index[0]), str(index[1]),
        str(results['num_wins_counter'][index]),
        str(results['num_games_counter'][index])]
        for index in list(results['num_wins_counter'].keys())
        if results['num_games_counter'][index] > 30]


RACE_BY_LETTER = {'z': 'Zerg', 't': 'Terran', 'p': 'Protoss'}

OBJECTIVES = {
        'supply_difference': count_win_rate_by_supply_difference,
        'supply_ratio': count_win_rate_by_supply_ratio,
        'supply_time_difference': count_win_rate_by_time_supply_difference,
        }


def main():
    """
    Execute spawningtool
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', help='text file with a list of SC2Replay paths')
    parser.add_argument('--cache-dir', help='Directory to cache results in')
    parser.add_argument('--matchup', help='Which matchup to check')
    parser.add_argument('--objective', help='What is being calculated')
    parser.add_argument('--min-time', help='lower bound to count')
    parser.add_argument('--max-time', help='upper bound to count')

    args = parser.parse_args()

    condition = None
    if args.matchup and len(args.matchup) == 3:
        player_1_race = RACE_BY_LETTER[args.matchup[0].lower()]
        player_2_race = RACE_BY_LETTER[args.matchup[2].lower()]

        condition = lambda replay, player_1, player_2: \
                player_1['race'] == player_1_race and player_2['race'] == player_2_race

    objective_fn = OBJECTIVES.get(args.objective, count_win_rate_by_supply_difference)

    with open(args.filenames, 'r') as fin:
        result = objective_fn(fin, condition=condition, cache_dir=args.cache_dir,
                min_time=args.min_time, max_time=args.max_time)
        for row in result:
            print(','.join([str(val) for val in row]))

if __name__ == '__main__':
    main()
