"""
spawningtool.__main__
~~~~~~~~~~~~~~~~~
"""
#!/usr/bin/env python
import argparse

from spawningtool.exception import CutoffTimeError, ReplayFormatError
from spawningtool.parser import parse_replay


def print_results(result):
    """
    Print the results of the build order
    """
    print result['map']
    print result['build']
    for player in result['players'].itervalues():
        print '{} ({})'.format(player['name'], player['race'])
        for event in player['buildOrder']:
            if not event['is_worker']:
                print '{} {} {}'.format(
                    event['supply'],
                    event['time'],
                    event['name']
                )
        print ''


def main():
    """
    Execute spawningtool
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('replay_file', help='.SC2Replay file to load')
    parser.add_argument(
        '--cutoff-time', help='Game time at which to stop displaying events'
    )
    args = parser.parse_args()
    try:
        result = parse_replay(args.replay_file, cutoff_time=args.cutoff_time)
    except CutoffTimeError as error:
        print error.message
    except ReplayFormatError as error:
        print error.message
        print error.parsed_data
    else:
        print_results(result)


if __name__ == '__main__':
    main()
