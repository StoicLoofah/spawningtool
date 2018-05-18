import json

import spawningtool.parser

def create_expected_results(filename):
    with open('temp.json', 'w') as fout:
        results = spawningtool.parser.parse_replay(filename)
        json.dump(results, fout, indent=4)
