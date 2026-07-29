import json
import unittest

import spawningtool.parser
import spawningtool.exception
from spawningtool import lotv_constants


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
            # json.dump(results, expected_results_file, indent=4)
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

    def test_patch_380_terran(self):
        """
        Test 3.8.0 patch (played 2016-11-26): pre-2019 Terran build times, in
        particular Hyperflight Rotors at 121s (79s today) and Weapon Refit at
        43s (100s today)
        """
        self._test_replay('patch_380_terran.SC2Replay',
                          'patch_380_terran.json')

    def test_patch_380_zerg(self):
        """
        Test 3.8.0 patch (played 2016-11-26): pre-5.0.12 Hydralisk Den upgrades,
        Grooved Spines and Muscular Augments both at 71s (50s and 64s today)
        """
        self._test_replay('patch_380_zerg.SC2Replay',
                          'patch_380_zerg.json')

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

    def test_patch_4_6_0_pvt(self):
        """
        PvT played 2018-09-08, before 4.7.1 and 4.8.2: Adept at 27s, Warp Gate
        Research at 114s, Stimpack at 121s and Forge upgrades at 114/136
        """
        self._test_replay('patch_4_6_0_pvt.SC2Replay',
                          'patch_4_6_0_pvt.json')

    def test_patch_4_9_2_zvt(self):
        """
        ZvT played 2019-06-27, between the March and August 2019 balance
        updates: Stimpack still at 121s and Centrifugal Hooks at 79s
        """
        self._test_replay('patch_4_9_2_zvt.SC2Replay',
                          'patch_4_9_2_zvt.json')

    def test_patch_5_0_4_pvt(self):
        """
        PvT played 2020-11-05, between 5.0.2 and 5.0.9, when the Void Ray was
        briefly reduced to 37s (43s both before and after)
        """
        self._test_replay('patch_5_0_4_pvt.SC2Replay',
                          'patch_5_0_4_pvt.json')

    def test_patch_5_0_10_pvz(self):
        """
        PvZ played 2022-11-19, after 5.0.9 put the Void Ray back to 43s and
        before 5.0.11/5.0.12: Sentry 26s, Hydralisk Den upgrades 71s
        """
        self._test_replay('patch_5_0_10_pvz.SC2Replay',
                          'patch_5_0_10_pvz.json')

    def test_patch_5_0_11(self):
        """
        Test 5.0.11 patch
        """
        self._test_replay('patch_5_0_11.SC2Replay',
                          'patch_5_0_11.json')

    def test_patch_5_0_13_tvp(self):
        """
        TvP played 2024-09-06, after 5.0.13 and before 5.0.14: Stalker still at
        30s and Hyperflight Rotors at 100s
        """
        self._test_replay('patch_5_0_13_tvp.SC2Replay',
                          'patch_5_0_13_tvp.json')

    def test_patch_5_0_14_tvp(self):
        """
        TvP played 2025-04-29, after 5.0.14 reduced the Stalker to 27s and
        before 5.0.15 reduced Hyperflight Rotors to 79s
        """
        self._test_replay('patch_5_0_14_tvp.SC2Replay',
                          'patch_5_0_14_tvp.json')

    def test_patch_5_0_16(self):
        """
        Test 5.0.16 patch (Warpgate Research build time adjustment)
        """
        self._test_replay('patch_5_0_16.SC2Replay',
                          'patch_5_0_16.json')

    def test_patch_5_0_16_hotfix(self):
        """
        Test 5.0.16 hotfix (played 2026-07-05): hotfix build times apply
        (Reaper, Adept, High/Dark Templar) with the 40% Warpgate reduction
        still in effect (5.0.16b's 50% is not yet active)
        """
        self._test_replay('patch_5_0_16_hotfix.SC2Replay',
                          'patch_5_0_16_hotfix.json')

    def test_patch_5_0_16b(self):
        """
        Test 5.0.16b hotfix (played 2026-07-19): 50% Warpgate Research
        Gateway unit build time reduction
        """
        self._test_replay('patch_5_0_16b.SC2Replay',
                          'patch_5_0_16b.json')


class LotVBuildDataHistoryTest(unittest.TestCase):
    """
    The build times picked for a replay's date, independent of any replay file.
    """

    def seconds(self, timestamp, unit_name):
        build_data = lotv_constants.build_data_for_timestamp(timestamp)
        return round(build_data[unit_name]['build_time'] / lotv_constants.FRAMES_PER_SECOND, 1)

    def timestamp(self, date):
        return lotv_constants._patch_timestamp(date)

    def test_current_build_times_end_the_history(self):
        """
        the last recorded change for each unit lands on its BUILD_DATA value.
        lotv_constants asserts this at import while build times are still in
        seconds; this re-checks it against the converted frame values.
        """
        latest = {}
        for _, _, units in lotv_constants.BUILD_TIME_CHANGES:
            for unit_name, (_, new) in units.items():
                latest[unit_name] = new

        for unit_name, new in latest.items():
            self.assertEqual(
                round(lotv_constants.BUILD_DATA[unit_name]['build_time'] /
                      lotv_constants.FRAMES_PER_SECOND, 1),
                new, unit_name)

    def test_history_is_chronological(self):
        for unit_name, history in lotv_constants.BUILD_DATA_HISTORY.items():
            timestamps = [timestamp for timestamp, _ in history]
            self.assertEqual(timestamps, sorted(timestamps), unit_name)

    def test_build_time_before_any_change(self):
        """
        a replay older than every recorded change gets the oldest known value
        """
        before = self.timestamp('2016-01-01')
        self.assertEqual(self.seconds(before, 'Adept'), 27)  # 27 -> 30 in 4.8.2
        self.assertEqual(self.seconds(before, 'Oracle'), 43)  # 43 -> 37 in 2017
        self.assertEqual(self.seconds(before, 'Carrier'), 86)  # 86 -> 64 in 4.7.1

    def test_build_time_between_changes(self):
        """
        a value that changed twice resolves to whichever was live at the time
        """
        # Void Ray was reduced in 5.0.2 and put back in 5.0.9
        self.assertEqual(self.seconds(self.timestamp('2020-01-01'), 'VoidRay'), 43)
        self.assertEqual(self.seconds(self.timestamp('2021-06-01'), 'VoidRay'), 37)
        self.assertEqual(self.seconds(self.timestamp('2026-01-01'), 'VoidRay'), 43)

    def test_air_and_ground_upgrades_diverge(self):
        """
        the 2019 balance update raised Forge AND Cybernetics Core upgrade times;
        only the Forge ones came back down in 5.0.11, so air and ground differ
        """
        before = self.timestamp('2019-01-01')
        between = self.timestamp('2020-01-01')
        now = self.timestamp('2026-01-01')

        self.assertEqual(self.seconds(before, 'ProtossGroundWeaponsLevel1'), 114)
        self.assertEqual(self.seconds(before, 'ProtossAirWeaponsLevel1'), 114)
        self.assertEqual(self.seconds(between, 'ProtossGroundWeaponsLevel1'), 129)
        self.assertEqual(self.seconds(between, 'ProtossAirWeaponsLevel1'), 129)
        self.assertEqual(self.seconds(now, 'ProtossGroundWeaponsLevel1'), 122)
        self.assertEqual(self.seconds(now, 'ProtossAirWeaponsLevel1'), 129)

    def test_stalker_5_0_14(self):
        self.assertEqual(self.seconds(self.timestamp('2024-11-01'), 'Stalker'), 30)
        self.assertEqual(self.seconds(self.timestamp('2024-12-01'), 'Stalker'), 27)

    def test_hyperflight_rotors_three_steps(self):
        """
        raised in 3.8.0, then cut in 5.0.11 and again in 5.0.15
        """
        self.assertEqual(self.seconds(self.timestamp('2016-01-01'), 'BansheeSpeed'), 93)
        self.assertEqual(self.seconds(self.timestamp('2020-01-01'), 'BansheeSpeed'), 121)
        self.assertEqual(self.seconds(self.timestamp('2024-01-01'), 'BansheeSpeed'), 100)
        self.assertEqual(self.seconds(self.timestamp('2026-01-01'), 'BansheeSpeed'), 79)

    def test_5_0_16_before_hotfix(self):
        """
        5.0.16 raised High/Dark Templar to 43s; the hotfix a week later cut them
        to 40s without changing the build number, so only the date tells them
        apart
        """
        during = self.timestamp('2026-06-25')
        after = self.timestamp('2026-07-05')
        self.assertEqual(self.seconds(during, 'HighTemplar'), 43)
        self.assertEqual(self.seconds(during, 'DarkTemplar'), 43)
        self.assertEqual(self.seconds(during, 'Adept'), 30)
        self.assertEqual(self.seconds(during, 'Reaper'), 32)
        self.assertEqual(self.seconds(after, 'HighTemplar'), 40)
        self.assertEqual(self.seconds(after, 'DarkTemplar'), 40)
        self.assertEqual(self.seconds(after, 'Adept'), 33)
        self.assertEqual(self.seconds(after, 'Reaper'), 34)

    def test_undated_replay_uses_current_build_times(self):
        build_data = lotv_constants.build_data_for_timestamp(None)
        self.assertIs(build_data, lotv_constants.BUILD_DATA)

    def test_warpgate_modifier_by_date(self):
        modifier = lotv_constants.warpgate_build_time_modifier
        # Before 5.0.16 there was no percentage modifier, only separate warp-in
        # build times, so this doesn't apply rather than defaulting to 40%
        self.assertIsNone(modifier(self.timestamp('2016-01-01')))
        self.assertIsNone(modifier(self.timestamp('2026-06-21')))
        self.assertEqual(modifier(self.timestamp('2026-06-25')), 0.6)  # 5.0.16, 40%
        self.assertEqual(modifier(self.timestamp('2026-07-15')), 0.6)
        self.assertEqual(modifier(self.timestamp('2026-07-16')), 0.5)  # 5.0.16b, 50%
        self.assertEqual(modifier(self.timestamp('2026-08-01')), 0.5)
        self.assertEqual(modifier(None), 0.5)


if __name__ == '__main__':
    unittest.main()
