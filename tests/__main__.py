import json
import unittest

import spawningtool.parser


class SpawningToolTestCase(unittest.TestCase):
    def assertDictsEqual(self, results, expected_results):
        self.assertObjectsEqual(results, expected_results, '')

    def assertObjectsEqual(self, results, expected_results, path):
        if type(results) in [str, unicode] and type(expected_results) in [str, unicode]:
            pass
        else:
            """
            print path
            print results
            print expected_results
            """
            self.assertEqual(type(results), type(expected_results))

        if type(results) == dict:
            expected_keys = set(expected_results.keys())
            for key, value in results.iteritems():
                key = unicode(key)
                if not key in expected_results:
                    self.assertFalse('{0} {1}'.format(path, key))
                self.assertObjectsEqual(value, expected_results[key],
                        '{0} {1}'.format(path, key))
                expected_keys.remove(key)
            if expected_keys:
                self.assertFalse(path)
        elif type(results) == list:
            if len(results) != len(expected_results):
                self.assertFalse(path)
            for i, value in enumerate(results):
                self.assertObjectsEqual(value, expected_results[i],
                        '{0} {1}'.format(path, i))
        else:
            if results != expected_results:
                self.assertFalse(path)


class ParseReplayTest(SpawningToolTestCase):

    def test_result(self):
        self.results = spawningtool.parser.parse_replay("replays/LiquidTLO vs Thorzain.SC2Replay")
        with open('tests/tlo_v_thorzain.json', 'r') as expected_results_file:
            self.expected_results = json.load(expected_results_file)

        self.assertDictsEqual(self.results, self.expected_results)


if __name__ == '__main__':
    unittest.main()
