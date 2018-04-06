"""
spawningtool.__main__
~~~~~~~~~~~~~~~~~
"""
#!/usr/bin/env python
import argparse

from spawningtool.exception import CutoffTimeError, ReplayFormatError
from spawningtool.parser import parse_replay


def print_player_header(player):
    if player['commander']:
        print('{} ({} - {})'.format(player['name'], player['race'], player['commander']))
    else:
        print('{} ({})'.format(player['name'], player['race']))

def print_builds(result, show_workers):
    for player in result['players'].values():
        if result['cooperative'] and not player['is_human']:
            continue
        print_player_header(player)
        if player['clock_position'] is not None:
            print('Start Position: {}:00'.format(player['clock_position']))
        for event in player['buildOrder']:
            if not event['is_worker'] or show_workers:
                print('{} {} {}{}'.format(
                    event['supply'],
                    event['time'],
                    event['name'],
                    ' (Chronoboosted)' if event['is_chronoboosted'] else ''
                ))
        print('')


def print_units_lost(result):
    for player in result['players'].values():
        if result['cooperative'] and not player['is_human']:
            continue
        print_player_header(player)
        for event in player['unitsLost']:
                print('{} {} killed by {}'.format(
                    event['time'],
                    event['name'],
                    event['killer']
                ))
        print('')


def print_abilities(result):
    for player in result['players'].values():
        if result['cooperative'] and not player['is_human']:
            continue
        print_player_header(player)
        for event in player['abilities']:
                print('{} {}'.format(
                    event['time'],
                    event['name'],
                ))
        print('')


def print_results(result, args):
    """
    Print the results of the build order
    """
    print_all = not args.build and not args.units_lost and not args.abilities
    print(result['map'])
    print(result['build'])
    if print_all or args.build:
        print_builds(result, args.workers)
    if print_all or args.units_lost:
        print_units_lost(result)
    if print_all or args.abilities:
        print_abilities(result)


def main():
    """
    Execute spawningtool
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('replay_file', help='.SC2Replay file to load')
    parser.add_argument(
        '--cutoff-time', help='Game time at which to stop displaying events'
    )
    parser.add_argument(
        '--cache-dir', help='Directory to cache results in'
    )
    parser.add_argument(
        '--map-details', help='Include map details and positions', action="store_true"
    )
    # print arguments
    parser.add_argument(
        '--build', help='Print out the build orders', action="store_true"
    )
    parser.add_argument(
        '--units-lost', help='Print out the units lost', action="store_true"
    )
    parser.add_argument(
        '--abilities', help='Print out the abilities', action="store_true"
    )
    parser.add_argument(
        '--workers', help='Print out the workers in the build', action="store_true"
    )

    args = parser.parse_args()
    try:
        result = parse_replay(
                args.replay_file,
                cutoff_time=args.cutoff_time,
                cache_dir=args.cache_dir,
                include_map_details=bool(args.map_details))
    except CutoffTimeError as error:
        print(error.message)
    except ReplayFormatError as error:
        print(error.message)
        print(error.parsed_data)
    else:
        print_results(result, args)


if __name__ == '__main__':
    main()
