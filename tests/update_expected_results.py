#!/usr/bin/env python
import argparse
import json

import spawningtool.parser


def main():
    """
    Execute spawningtool
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('replay_file', help='.SC2Replay file to load')
    args = parser.parse_args()

    with open('tests/{}.json'.format(args.replay_file), 'w') as fout:
        results = spawningtool.parser.parse_replay('replays/{}.SC2Replay'.format(args.replay_file))
        json.dump(results, fout, indent=4)


if __name__ == '__main__':
    main()
