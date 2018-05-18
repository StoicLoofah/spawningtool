import json
import unittest

import spawningtool.parser
import spawningtool.exception


class SpawningToolTestCase(unittest.TestCase):
    def assertDictsEqual(self, results, expected_results):
        self.assertObjectsEqual(results, expected_results, '')

    def assertObjectsEqual(self, results, expected_results, path):
        if type(results) == dict:
            expected_keys = set(expected_results.keys())
            for key, value in results.items():
                key = str(key)
                if not key in expected_results:
                    self.assertFalse('{0} {1}'.format(path, key))
                self.assertObjectsEqual(value, expected_results[key],
                        '{0} {1}'.format(path, key))
                expected_keys.remove(key)
            if expected_keys:
                self.assertFalse(path)
        elif type(results) == list:
            if len(results) != len(expected_results):
                print(len(results))
                print(len(expected_results))
                self.assertFalse(path)
            for i, value in enumerate(results):
                self.assertObjectsEqual(value, expected_results[i],
                        '{0} {1}'.format(path, i))
        else:
            if results != expected_results:
                self.assertFalse(path)

    def _test_replay(self, filename, expected_results_filename):
        results = spawningtool.parser.parse_replay("replays/{}".format(filename))
        with open('tests/{}'.format(expected_results_filename), 'r') as expected_results_file:
            expected_results = json.load(expected_results_file)

        self.assertDictsEqual(results, expected_results)


class ParseReplayTest(SpawningToolTestCase):

    def test_hots_replay(self):
        """
        testing a valid replay
        """
        self._test_replay('LiquidTLO vs Thorzain.SC2Replay',
                          'tlo_v_thorzain.json')

    def test_gameheart_replay(self):
        """
        testing a gameheart replay
        """
        self._test_replay('gameheart.SC2Replay',
                          'gameheart.json')

    def test_old_replay(self):
        """
        parsing a file that doesn't have tracker events
        """
        self.assertRaises(spawningtool.exception.ReplayFormatError,
                spawningtool.parser.parse_replay, "replays/oldreplay.SC2Replay")

    def test_read_error(self):
        """
        parsing a file that isn't a replay
        """
        self.assertRaises(spawningtool.exception.ReadError,
                spawningtool.parser.parse_replay, "tests/tlo_v_thorzain.json")

    def test_patch_380(self):
        """
        Test 3.8.0 patch
        """
        self._test_replay('patch_380_protoss.SC2Replay',
                          'patch_380_protoss.json')

    def test_patch_400(self):
        """
        Test 4.0.0 patch
        """
        self._test_replay('patch_400.SC2Replay',
                          'patch_400.json')

    def test_coop(self):
        """
        Test Kerrigan Co-op game
        """
        self._test_replay('kerrigan.SC2Replay',
                          'kerrigan.json')


if __name__ == '__main__':
    unittest.main()
