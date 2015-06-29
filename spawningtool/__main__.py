"""
spawningtool.__main__
~~~~~~~~~~~~~~~~~
"""
#!/usr/bin/env python
import argparse

from spawningtool.exception import CutoffTimeError, ReplayFormatError
from spawningtool.parser import parse_replay


def print_builds(result):
    for player in result['players'].values():
        print('{} ({})'.format(player['name'], player['race']))
        if player['clock_position'] is not None:
            print('Start Position: {}:00'.format(player['clock_position']))
        for event in player['buildOrder']:
            if not event['is_worker']:
                print('{} {} {}{}'.format(
                    event['supply'],
                    event['time'],
                    event['name'],
                    ' (Chronoboosted)' if event['is_chronoboosted'] else ''
                ))
        print('')


def print_units_lost(result):
    for player in result['players'].values():
        print('{} ({})'.format(player['name'], player['race']))
        for event in player['unitsLost']:
                print('{} {} killed by {}'.format(
                    event['time'],
                    event['name'],
                    event['killer']
                ))
        print('')


def print_abilities(result):
    for player in result['players'].values():
        print('{} ({})'.format(player['name'], player['race']))
        for event in player['abilities']:
                print('{} {}'.format(
                    event['time'],
                    event['name'],
                ))
        print('')


def print_results(result):
    """
    Print the results of the build order
    """
    print(result['map'])
    print(result['build'])
    print_builds(result)
    print_units_lost(result)
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
        print_results(result)


if __name__ == '__main__':
    main()
