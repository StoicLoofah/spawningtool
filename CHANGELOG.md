Changes
=======

* v2.13.0, July 29, 2026 -- select build times by replay date so balance hotfixes that reuse a build number are handled without breaking older replays; add 5.0.16 hotfix (Reaper 32->34, Adept 30->33, High/Dark Templar 43->40) and 5.0.16b (Warpgate Research Gateway reduction 40%->50%, effective 2026-07-16). Record the full history of LotV build time changes back to 3.8.0 in `BUILD_TIME_CHANGES`, so replays are scored with the build times that were live on the day they were played, and verify at import that each unit's recorded changes chain into its current value. That check surfaced several errors: High/Dark Templar were raised 39->43 in 5.0.16 before the hotfix cut them to 40; the Void Ray was reduced 43->37 in 5.0.2 and put back to 43 in 5.0.9, which had been applied in reverse; Hyperflight Rotors had been left at 121s through the 5.0.11 reduction to 100s and the 5.0.15 reduction to 79s; the Stalker's 5.0.14 reduction from 30s to 27s was missing; and the March 25, 2019 balance update raised the Cybernetics Core air upgrades along with the Forge ground ones (to 129/154/179), which 5.0.11 then reduced for the Forge only, so air and ground upgrade times now differ. Adds ladder data for 5.0.14 and 5.0.15, which had never been tracked (also noting the 5.0.14 revert to the 5.0.11 Cyclone, which brought Mag-Field Accelerator back and dropped Hurricane Engines), and adds eight new test replays spanning 4.6.0, 4.9.2, 5.0.4, 5.0.10, 5.0.13 and 5.0.14 plus the 3.8.0 Terran and Zerg replays that were already in `replays/` but unused, all of which fail if the date-based lookup is bypassed. The 5.0.14 Nanomuscular Swell upgrade and Energy Recharge ability still need their internal names before they can be added (#70)
* v2.12.0, June 24, 2026 -- adjust Gateway unit build times for Warpgate Research in patch 5.0.16
* v2.11.0, April 29, 2024 -- update ladder data for balance patch 5.0.12 and 5.0.13
* v2.10.0, February 13, 2023 -- update ladder data for balance patch 5.0.11
* v2.9.0, August 17, 2021 -- Fix Liberator build time, add more display names
* v2.8.0, October 28, 2020 -- add Mengsk
* v2.7.0, January 18, 2020 -- update ladder data for balance patch 4.11.0
* v2.6.1, October 14, 2019 -- bump sc2reader>=1.4.0, balance updates
* v2.6.0, August 9, 2019 -- add Stetmann, mark additional worker types
* v2.5.2, March 27, 2019 -- update Forge upgrade timing for March 25, 2019 balance update
* v2.5.1, March 8, 2019 -- remove changelings of Marines with Combat Shield
* v2.5.0, January 22, 2019 -- update ladder data for balance patch 4.8.2
* v2.4.0, November 21, 2018 -- update ladder data for balance patch 4.7.1
* v2.3.0, November 18, 2018 -- bump sc2reader==1.3.0 for StarCraft 4.7, add Zeratul
* v2.2.2, October 28, 2018 -- fix various LotV data, added more display names
* v2.2.1, October 24, 2018 -- fix pip packaging. Thanks Gusgus01
* v2.2.0, October 7, 2018 -- bump sc2reader==1.2.0 for StarCraft 4.6, add Tychus
* v2.1.0, June 13, 2018 -- fix Lair and Hive co-op build time, add Abathur building morph reduction, fix co-op generic build times, moved this file
* v2.0.0, May 18, 2018 -- continuous integration, StarCraft 2 4.0 support (new unit types, chronoboost, etc.), Co-op support
* v1.0.0, December 9, 2016 -- improved LotV chronoboost support, better unit type coverage, updated to LotV 3.8.0 data
* v0.2.1, December 12, 2015 -- Legacy of the Void support, HotS chrono boost
* v0.2.0, March 3, 2015 -- python3 support, analysis script examples, map details, caching
* v0.1.3, August 12, 2013 -- bump to sc2reader 0.6.0, unit tests, add unit change events to build order, add units lost, add ability extraction
* v0.1.2, June 15, 2013 -- Locking in sc2reader version, fix supply for it
* v0.1.1, May 12, 2013 -- Updating main to be accessible via the package, adding more metadata
* v0.1.0, May 12, 2013 -- Initial release
