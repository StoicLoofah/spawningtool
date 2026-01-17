"""
spawningtool.constants
~~~~~~~~~~~~~~~~~~~~~~
"""

FRAMES_PER_SECOND = 22.4

BO_EXCLUDED = set([
    'MULE',
    'ReaperPlaceholder',
    'Interceptor'
    'AutoTurret',
    'PointDefenseDrone',
    'Locust',
    'LocustMP',
    'LocustMPFlyer',  # LotV Alpha Mod
    'Changeling',
    'ChangelingMarine',
    'ChangelingMarineShield',
    'ChangelingZealot',
    'ChangelingZergling',
    'ChangelingZerglingWings',
    'InfestedTerran',
    'Overseer',
    'Broodling',
    'BroodlingEscort',  # the guys that fly with the Brood Lord
    'Larva',
    'CreepTumor',
    'CreepTumorQueen',
    'InfestedTerransEgg',
    'AutoTurret',
    'InfestedTerran',
    'Interceptor',
    'SwarmHostBurrowed',
    'InvisibleTargetDummy',  # LotV alpha mod
    'InterceptorFree',  # LotV alpha mod
    'AdeptPhaseShift',
    'OracleStasisTrap',
    'KD8Charge',
    'ReleaseInterceptorsBeacon',
    'SpecialNexus',
    'DisruptorPhased',  # Disruptor shots
    'ParasiticBombDummy',
    'ParasiticBombRelayDummy',
    'LocustMPPrecursor',
    'RavenRepairDrone',
])

BO_CHANGED_EXCLUDED = set([
    'Liberator',
    'SiegeTank',  # from dropping sieged tanks from medivacs
    'VikingAssault',  # various viking transforms
    'VikingFighter',
    'Viking',
    'WarpPrism',
    'WidowMine',  # burrowing
    'Zergling',  # generated when Banelings spawn
])

BO_UPGRADES_EXCLUDED = set([
    'SprayTerran',
    'SprayProtoss',
    'SprayZerg',
])

BUILD_DATA = {
    # terran units
    "SCV": {
        "build_time": 12,
        "built_from": [ "Command Center", "Orbital Command" ],
        "display_name": "SCV",
        'race': 'Terran', 
        'type': 'Unit', # Building, Upgrade, Unit
        'is_morph': False 
    },
    "Marine": {
        "build_time": 18,
        "built_from": [ "Barracks" ],
        "display_name": "Marine",
        'race': 'Terran', 
        'type': 'Unit',
        'is_morph': False 
    },
    "Marauder": {
        "build_time": 21,
        "built_from": [ "Barracks" ],
        "display_name": "Marauder",
        'race': 'Terran', 
        'type': 'Unit',
        'is_morph': False 
    },
    "Reaper": {
        "build_time": 32,
        "built_from": [ "Barracks" ],
        "display_name": "Reaper",
        'race': 'Terran', 
        'type': 'Unit',
        'is_morph': False 
    },
    "Ghost": {
        "build_time": 29,
        "built_from": [ "Barracks" ],
        "display_name": "Ghost",
        'race': 'Terran', 
        'type': 'Unit',
        'is_morph': False 
    },
    "BattleHellion": {
        "build_time": 21,
        "built_from": [ "Factory" ],
        "display_name": "Hellbat",
        'race': 'Terran', 
        'type': 'Unit',
        'is_morph': False 
    },
    "Hellion": {
        "build_time": 21,
        "built_from": [ "Factory" ],
        "display_name": "Hellion",
        'race': 'Terran', 
        'type': 'Unit',
        'is_morph': False 
    },
    "Hellbat": { # deprecated?
        "build_time": 21,
        "built_from": [ "Factory" ],
        "display_name": "Hellbat",
        'race': 'Terran', 
        'type': 'Unit',
        'is_morph': False 
    },
    "WidowMine": {
        "build_time": 21,
        "built_from": [ "Factory" ],
        "display_name": "Widow Mine",
        'race': 'Terran', 
        'type': 'Unit',
        'is_morph': False 
    },
    "SiegeTank": {
        "build_time": 32,
        "built_from": [ "Factory" ],
        "display_name": "Siege Tank",
        'race': 'Terran', 
        'type': 'Unit',
        'is_morph': False 
    },
    "Cyclone": {
        "build_time": 32,
        "built_from": [ "Factory" ],
        "display_name": "Cyclone",
        'race': 'Terran', 
        'type': 'Unit',
        'is_morph': False 
    },
    "Thor": {
        "build_time": 43,
        "built_from": [ "Factory" ],
        "display_name": "Thor",
        'race': 'Terran', 
        'type': 'Unit',
        'is_morph': False 
    },
    'Viking': {  # not built as this
        "build_time": 30,
        "built_from": [ "Starport" ],
        "display_name": "Viking",
        'race': 'Terran', 
        'type': 'Unit',
        'is_morph': False 
    },
    "VikingFighter": {
        "build_time": 30,   # all born as VikingFighters, but others in here for coverage
        "built_from": [ "Starport" ],
        "display_name": "Viking",
        'race': 'Terran', 
        'type': 'Unit',
        'is_morph': False 
    },
    "VikingAssault": {  # not built as this
        "build_time": 30,
        "built_from": [ "Starport" ],
        "display_name": "Viking",
        'race': 'Terran', 
        'type': 'Unit',
        'is_morph': False 
    },
    "Medivac": {
        "build_time": 30,
        "built_from": [ "Starport" ],
        "display_name": "Medivac",
        'race': 'Terran', 
        'type': 'Unit',
        'is_morph': False 
    },
    "Liberator": {
        "build_time": 43,
        "built_from": [ "Starport" ],
        "display_name": "Liberator",
        'race': 'Terran', 
        'type': 'Unit',
        'is_morph': False 
    },
    "Raven": {
        "build_time": 34,  # 42.9 -> 34.3 in 5.0.11
        "built_from": [ "Starport" ],
        "display_name": "Raven",
        'race': 'Terran', 
        'type': 'Unit',
        'is_morph': False 
    },
    "Banshee": {
        "build_time": 43,
        "built_from": [ "Starport" ],
        "display_name": "Banshee",
        'race': 'Terran', 
        'type': 'Unit',
        'is_morph': False 
    },
    "Battlecruiser": {
        "build_time": 64,
        "built_from": [ "Starport" ],
        "display_name": "Battlecruiser",
        'race': 'Terran', 
        'type': 'Unit',
        'is_morph': False 
    },
    "Nuke": {  # treat the Nuke like a unit
        "build_time": 43,
        "built_from": [ "Ghost Academy" ],
        "display_name": "Nuke",
        'race': 'Terran', 
        'type': 'Unit',
        'is_morph': False 
    },
    # protoss units
    "Probe": {
        "build_time": 12,
        "built_from": [ "Nexus" ],
        "display_name": "Probe",
        'race': 'Protoss', 
        'type': 'Unit',
        'is_morph': False 
    },
    "Zealot": {
        "build_time": 27,
        "built_from": [ "Gateway", "WarpGate" ],  # warpgate is necessary because of changing types
        "display_name": "Zealot",
        'race': 'Protoss', 
        'type': 'Unit',
        'is_morph': False 
    },
    "Stalker": {
        "build_time": 30,
        "built_from": [ "Gateway", "WarpGate" ],
        "display_name": "Stalker",
        'race': 'Protoss', 
        'type': 'Unit',
        'is_morph': False 
    },
    "Sentry": {
        "build_time": 23,  # 26.4 -> 22.9 in 5.0.11
        "built_from": [ "Gateway", "WarpGate" ],
        "display_name": "Sentry",
        'race': 'Protoss', 
        'type': 'Unit',
        'is_morph': False 
    },
    "Adept": {
        "build_time": 30,  # 27 -> 30 in 4.8.2
        "built_from": [ "Gateway", "WarpGate" ],
        "display_name": "Adept",
        'race': 'Protoss', 
        'type': 'Unit',
        'is_morph': False 
    },
    "MothershipCore": {
        "build_time": 21,
        "built_from": [ "Nexus" ],
        "display_name": "Mothership Core",
        'race': 'Protoss', 
        'type': 'Unit',
        'is_morph': False 
    },
    "Mothership": {
        "build_time": 79,  # 114 -> 79 in 5.0.12
        "built_from": [ "Nexus" ],
        "display_name": "Mothership",
        'race': 'Protoss', 
        'type': 'Unit',
        'is_morph': False 
    },
    "HighTemplar": {
        "build_time": 39,
        "built_from": [ "Gateway", "WarpGate" ],
        "display_name": "High Templar",
        'race': 'Protoss', 
        'type': 'Unit',
        'is_morph': False 
    },
    "DarkTemplar": {
        "build_time": 39,
        "built_from": [ "Gateway", "WarpGate" ],
        "display_name": "Dark Templar",
        'race': 'Protoss', 
        'type': 'Unit',
        'is_morph': False 
    },
    "Immortal": {
        "build_time": 39,
        "built_from": [ "RoboticsFacility" ],
        "display_name": "Immortal",
        'race': 'Protoss', 
        'type': 'Unit',
        'is_morph': False 
    },
    "Disruptor": {
        "build_time": 36,
        "built_from": [ "RoboticsFacility" ],
        "display_name": "Disruptor",
        'race': 'Protoss', 
        'type': 'Unit',
        'is_morph': False 
    },
    "Colossus": {
        "build_time": 54,
        "built_from": [ "RoboticsFacility" ],
        "display_name": "Colossus",
        'race': 'Protoss', 
        'type': 'Unit',
        'is_morph': False 
    },
    "Archon": {
        "build_time": 9,
        "built_from": [],
        "display_name": "Archon",
        'race': 'Protoss', 
        'type': 'Unit',
        'is_morph': False 
    },
    "Observer": {
        "build_time": 18,  # 21 -> 18 in 5.0.13
        "built_from": [ "RoboticsFacility" ],
        "display_name": "Observer",
        'race': 'Protoss', 
        'type': 'Unit',
        'is_morph': False 
    },
    "WarpPrism": {
        "build_time": 36,
        "built_from": [ "RoboticsFacility" ],
        "display_name": "Warp Prism",
        'race': 'Protoss', 
        'type': 'Unit',
        'is_morph': False 
    },
    "Phoenix": {
        "build_time": 25,
        "built_from": [ "Stargate" ],
        "display_name": "Phoenix",
        'race': 'Protoss', 
        'type': 'Unit',
        'is_morph': False 
    },
    "VoidRay": {
        "build_time": 37,  # decreased 43 -> 37 in 5.0.9 Mar 15 2022
        "built_from": [ "Stargate" ],
        "display_name": "Void Ray",
        'race': 'Protoss', 
        'type': 'Unit',
        'is_morph': False 
    },
    "Oracle": {
        "build_time": 37,
        "built_from": [ "Stargate" ],
        "display_name": "Oracle",
        'race': 'Protoss', 
        'type': 'Unit',
        'is_morph': False 
    },
    "Tempest": {
        "build_time": 43,
        "built_from": [ "Stargate" ],
        "display_name": "Tempest",
        'race': 'Protoss', 
        'type': 'Unit',
        'is_morph': False 
    },
    "Carrier": {
        "build_time": 64,  # decreased 86 -> 64 in 4.7.1
        "built_from": [ "Stargate" ],
        "display_name": "Carrier",
        'race': 'Protoss', 
        'type': 'Unit',
        'is_morph': False 
    },
    # zerg units
    "Drone": {
        "build_time": 12,
        "built_from": [],
        "display_name": "Drone",
        'race': 'Zerg', 
        'type': 'Unit',
        'is_morph': False 
    },
    "Queen": {
        "build_time": 36,
        "built_from": [ "Hatchery", "Lair", "Hive" ],
        "display_name": "Queen",
        'race': 'Zerg', 
        'type': 'Unit',
        'is_morph': False 
    },
    "Zergling": {
        "build_time": 17,
        "built_from": [],
        "display_name": "Zergling",
        'race': 'Zerg', 
        'type': 'Unit',
        'is_morph': False 
    },
    "Roach": {
        "build_time": 19,
        "built_from": [],
        "display_name": "Roach",
        'race': 'Zerg', 
        'type': 'Unit',
        'is_morph': False 
    },
    "Hydralisk": {
        "build_time": 24,
        "built_from": [],
        "display_name": "Hydralisk",
        'race': 'Zerg', 
        'type': 'Unit',
        'is_morph': False 
    },
    "SwarmHost": {
        "build_time": 29,
        "built_from": [],
        "display_name": "Swarm Host",
        'race': 'Zerg', 
        'type': 'Unit',
        'is_morph': False 
    },
    "Infestor": {
        "build_time": 36,
        "built_from": [],
        "display_name": "Infestor",
        'race': 'Zerg', 
        'type': 'Unit',
        'is_morph': False 
    },
    "Ultralisk": {
        "build_time": 39,
        "built_from": [],
        "display_name": "Ultralisk",
        'race': 'Zerg', 
        'type': 'Unit',
        'is_morph': False 
    },
    "Overlord": {
        "build_time": 18,
        "built_from": [],
        "display_name": "Overlord",
        'race': 'Zerg', 
        'type': 'Unit',
        'is_morph': False 
    },
    "Mutalisk": {
        "build_time": 24,
        "built_from": [],
        "display_name": "Mutalisk",
        'race': 'Zerg', 
        'type': 'Unit',
        'is_morph': False 
    },
    "Corruptor": {
        "build_time": 29,
        "built_from": [],
        "display_name": "Corruptor",
        'race': 'Zerg', 
        'type': 'Unit',
        'is_morph': False 
    },
    "Viper": {
        "build_time": 29,
        "built_from": [],
        "display_name": "Viper",
        'race': 'Zerg', 
        'type': 'Unit',
        'is_morph': False 
    },
    "NydusWorm": {  # deprecated
        "build_time": 14,
        "built_from": [ "NydusCanal" ],
		"display_name": "Nydus Worm",
        'race': 'Zerg', 
        'type': 'Building',
        'is_morph': False 
    },
    "NydusCanal": {
        "build_time": 14,
        "built_from": [ "NydusNetwork" ],
        "display_name": "Nydus Canal",
        'race': 'Zerg', 
        'type': 'Building',
        'is_morph': False 
    },
    # zerg evolved units
    "Baneling": {
        "build_time": 14,
        "built_from": [],
        "display_name": "Baneling",
        'race': 'Zerg', 
        'type': 'Building',
        'is_morph': True 
    },
    "BroodLord": {
        "build_time": 24,
        "built_from": [],
        "display_name": "Brood Lord",
        'race': 'Zerg', 
        'type': 'Building',
        'is_morph': True 
    },
    "Overseer": {
        "build_time": 12,
        "built_from": [ "Overlord" ],
        "display_name": "Overseer",
        'race': 'Zerg', 
        'type': 'Building',
        'is_morph': True 
    },
    "RavagerCocoon": {  # Ravager - egg not itself because it is the start time, normal build time is 12 seconds
        # increased 8.57 -> 12.14 seconds in 5.0.11
        "build_time": 0,
        "built_from": [ "Roach" ],
        "display_name": "Ravager",
        'race': 'Zerg', 
        'type': 'Building',
        'is_morph': True 
    },
    "LurkerMPEgg": {  # Lurker - same logic as above, especially because burrow/unburrow counts, normal build time is 18
        "build_time": 0,
        "built_from": [ "Hydralisk" ],
        "display_name": "Lurker",
        'race': 'Zerg', 
        'type': 'Building',
        'is_morph': True 
    },
    # zerg upgrades
    "ZergMeleeWeaponsLevel1": {
        "build_time": 114,
        "built_from": [ "EvolutionChamber" ],
        "display_name": "Zerg Melee Weapons Level 1",
        'race': 'Zerg', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "ZergMeleeWeaponsLevel2": {
        "build_time": 136,
        "built_from": [ "EvolutionChamber" ],
        "display_name": "Zerg Melee Weapons Level 2",
        'race': 'Zerg', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "ZergMeleeWeaponsLevel3": {
        "build_time": 157,
        "built_from": [ "EvolutionChamber" ],
        "display_name": "Zerg Melee Weapons Level 3",
        'race': 'Zerg', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "ZergMissileWeaponsLevel1": {
        "build_time": 114,
        "built_from": [ "EvolutionChamber" ],
        "display_name": "Zerg Missile Weapons Level 1",
        'race': 'Zerg', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "ZergMissileWeaponsLevel2": {
        "build_time": 136,
        "built_from": [ "EvolutionChamber" ],
        "display_name": "Zerg Missile Weapons Level 2",
        'race': 'Zerg', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "ZergMissileWeaponsLevel3": {
        "build_time": 157,
        "built_from": [ "EvolutionChamber" ],
        "display_name": "Zerg Missile Weapons Level 3",
        'race': 'Zerg', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "ZergGroundArmorsLevel1": {
        "build_time": 114,
        "built_from": [ "EvolutionChamber" ],
        "display_name": "Zerg Ground Armor Level 1",
        'race': 'Zerg', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "ZergGroundArmorsLevel2": {
        "build_time": 136,
        "built_from": [ "EvolutionChamber" ],
        "display_name": "Zerg Ground Armor Level 2",
        'race': 'Zerg', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "ZergGroundArmorsLevel3": {
        "build_time": 157,
        "built_from": [ "EvolutionChamber" ],
        "display_name": "Zerg Ground Armor Level 3",
        'race': 'Zerg', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "ZergFlyerWeaponsLevel1": {
        "build_time": 114,
        "built_from": [ "Spire", "GreaterSpire" ],
        "display_name": "Zerg Flyer Weapons Level 1",
        'race': 'Zerg', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "ZergFlyerWeaponsLevel2": {
        "build_time": 136,
        "built_from": [ "Spire", "GreaterSpire" ],
        "display_name": "Zerg Flyer Weapons Level 2",
        'race': 'Zerg', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "ZergFlyerWeaponsLevel3": {
        "build_time": 157,
        "built_from": [ "Spire", "GreaterSpire" ],
        "display_name": "Zerg Flyer Weapons Level 3",
        'race': 'Zerg', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "ZergFlyerArmorsLevel1": {
        "build_time": 114,
        "built_from": [ "Spire", "GreaterSpire" ],
        "display_name": "Zerg Flyer Armor Level 1",
        'race': 'Zerg', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "ZergFlyerArmorsLevel2": {
        "build_time": 136,
        "built_from": [ "Spire", "GreaterSpire" ],
        "display_name": "Zerg Flyer Armor Level 2",
        'race': 'Zerg', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "ZergFlyerArmorsLevel3": {
        "build_time": 157,
        "built_from": [ "Spire", "GreaterSpire" ],
        "display_name": "Zerg Flyer Armor Level 3",
        'race': 'Zerg', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    # Spawning Pool Upgrades
    "zerglingmovementspeed": {
        "build_time": 79,
        "built_from": [ "SpawningPool" ],
        "display_name": "Metabolic Boost",
        'race': 'Zerg', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "zerglingattackspeed": {
        "build_time": 93,
        "built_from": [ "SpawningPool" ],
        "display_name": "Adrenal Glands",
        'race': 'Zerg', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    # Baneling Nest Upgrades
    "CentrificalHooks": {
        "build_time": 71,  # 79 -> 71 in 5.0.12
        "built_from": [ "BanelingNest" ],
        "display_name": "Centrifugal Hooks",
        'race': 'Zerg', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    # Roach Warren Upgrades
    "GlialReconstitution": {
        "build_time": 79,
        "built_from": [ "RoachWarren" ],
        "display_name": "Glial Reconstitution",
        'race': 'Zerg', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "TunnelingClaws": {
        "build_time": 79,
        "built_from": [ "RoachWarren" ],
        "display_name": "Tunneling Claws",
        'race': 'Zerg', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    # Hydralisk Den Upgrades
    "hydraliskspeed": {  # LotV Muscular Augments, deprecated 3.8
        "build_time": 71,
        "built_from": [ "HydraliskDen" ],
        "display_name": "Muscular Augments",
        'race': 'Zerg', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "HydraliskSpeedUpgrade": {  # HotS deprecated Muscular Augments
        "build_time": 71,
        "built_from": [ "HydraliskDen" ],
        "display_name": "Muscular Augments",
        'race': 'Zerg', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "EvolveGroovedSpines": {  # added 3.8
        "build_time": 50,  # 71 -> 50 in 5.0.12
        "built_from": [ "HydraliskDen" ],
        "display_name": "Grooved Spines",
        'race': 'Zerg', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "EvolveMuscularAugments": {  # added 3.8
        "build_time": 64,  # 71 -> 64 in 5.0.12
        "built_from": [ "HydraliskDen" ],
        "display_name": "Muscular Augments",
        'race': 'Zerg', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    # Hatchery Upgrades
    "overlordspeed": {
        "build_time": 43,
        "built_from": [ "Hatchery", "Lair", "Hive" ],
        "display_name": "Pneumatized Carapace",
        'race': 'Zerg', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "overlordtransport": {  # deprecated
        "build_time": 93,
        "built_from": [ "Hatchery", "Lair", "Hive" ],
        "display_name": "Ventral Sacs",
        'race': 'Zerg', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "Burrow": {
        "build_time": 71,
        "built_from": [ "Hatchery", "Lair", "Hive" ],
        "display_name": "Burrow",
        'race': 'Zerg', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    # Infestation Pit Upgrades
    "InfestorEnergyUpgrade": {  # Deprecated 5.0.12
        "build_time": 57,
        "built_from": [ "InfestationPit" ],
        "display_name": "Pathogen Glands",
        'race': 'Zerg', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "LocustLifetimeIncrease": {  # deprecated
        "build_time": 87,
        "built_from": [ "InfestationPit" ],
        "display_name": "Enduring Locusts",
        'race': 'Zerg', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "NeuralParasite": {
        "build_time": 79,
        "built_from": [ "InfestationPit" ],
        "display_name": "Neural Parasite",
        'race': 'Zerg', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "MicrobialShroud": {
        "build_time": 79,
        "built_from": [ "InfestationPit" ],
        "display_name": "Microbial Shroud",
        "race": "Zerg",
        "type": "Upgrade",
        "is_morph": False
    },
    # Ultralisk Cavern Upgrades
    "ChitinousPlating": {
        "build_time": 79,
        "built_from": [ "UltraliskCavern" ],
        "display_name": "Chitinous Plating",
        'race': 'Zerg', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "AnabolicSynthesis": {  # added in 4.7.1
        "build_time": 43,
        "built_from": [ "UltraliskCavern" ],
        "display_name": "Anabolic Synthesis",
        "race": "Zerg",
        "type": "Upgrade",
        "is_morph": False
    },
    # Lurker Den Upgrades
    "DiggingClaws": {
        "build_time": 57,
        "built_from": [ "LurkerDenMP" ],
        "display_name": "Adaptive Talons",
        "race": "Zerg",
        "type": "Upgrade",
        "is_morph": False
    },
    "LurkerRange": {
        "build_time": 57,
        "built_from": [ "LurkerDenMP" ],
        "display_name": "Seismic Spines",
        "race": "Zerg",
        "type": "Upgrade",
        "is_morph": False
    },

    # terran upgrades
    "TerranInfantryWeaponsLevel1": {
        "build_time": 114,
        "built_from": [ "EngineeringBay" ],
        "display_name": "Terran Infantry Weapons Level 1",
        'race': 'Terran', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "TerranInfantryWeaponsLevel2": {
        "build_time": 136,
        "built_from": [ "EngineeringBay" ],
        "display_name": "Terran Infantry Weapons Level 2",
        'race': 'Terran', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "TerranInfantryWeaponsLevel3": {
        "build_time": 157,
        "built_from": [ "EngineeringBay" ],
        "display_name": "Terran Infantry Weapons Level 3",
        'race': 'Terran', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "TerranInfantryArmorsLevel1": {
        "build_time": 114,
        "built_from": [ "EngineeringBay" ],
        "display_name": "Terran Infantry Armor Level 1",
        'race': 'Terran', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "TerranInfantryArmorsLevel2": {
        "build_time": 136,
        "built_from": [ "EngineeringBay" ],
        "display_name": "Terran Infantry Armor Level 2",
        'race': 'Terran', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "TerranInfantryArmorsLevel3": {
        "build_time": 157,
        "built_from": [ "EngineeringBay" ],
        "display_name": "Terran Infantry Armor Level 3",
        'race': 'Terran', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "TerranVehicleWeaponsLevel1": {
        "build_time": 114,
        "built_from": [ "Armory" ],
        "display_name": "Terran Vehicle Weapons Level 1",
        'race': 'Terran', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "TerranVehicleWeaponsLevel2": {
        "build_time": 136,
        "built_from": [ "Armory" ],
        "display_name": "Terran Vehicle Weapons Level 2",
        'race': 'Terran', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "TerranVehicleWeaponsLevel3": {
        "build_time": 157,
        "built_from": [ "Armory" ],
        "display_name": "Terran Vehicle Weapons Level 3",
        'race': 'Terran', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "TerranVehicleArmorsLevel1": {  # deprecated
        "build_time": 114,
        "built_from": [ "Armory" ],
        "display_name": "Terran Vehicle Armor Level 1",
        'race': 'Terran', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "TerranVehicleArmorsLevel2": {  # deprecated
        "build_time": 136,
        "built_from": [ "Armory" ],
        "display_name": "Terran Vehicle Armor Level 2",
        'race': 'Terran', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "TerranVehicleArmorsLevel3": {  # deprecated
        "build_time": 157,
        "built_from": [ "Armory" ],
        "display_name": "Terran Vehicle Armor Level 3",
        'race': 'Terran', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "TerranShipWeaponsLevel1": {
        "build_time": 114,
        "built_from": [ "Armory" ],
        "display_name": "Terran Ship Weapons Level 1",
        'race': 'Terran', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "TerranShipWeaponsLevel2": {
        "build_time": 136,
        "built_from": [ "Armory" ],
        "display_name": "Terran Ship Weapons Level 2",
        'race': 'Terran', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "TerranShipWeaponsLevel3": {
        "build_time": 157,
        "built_from": [ "Armory" ],
        "display_name": "Terran Ship Weapons Level 3",
        'race': 'Terran', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "TerranShipArmorsLevel1": {  # deprecated
        "build_time": 114,
        "built_from": [ "Armory" ],
        "display_name": "Terran Ship Armor Level 1",
        'race': 'Terran', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "TerranShipArmorsLevel2": {  # deprecated
        "build_time": 136,
        "built_from": [ "Armory" ],
        "display_name": "Terran Ship Armor Level 2",
        'race': 'Terran', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "TerranShipArmorsLevel3": {  # deprecated
        "build_time": 157,
        "built_from": [ "Armory" ],
        "display_name": "Terran Ship Armor Level 3",
        'race': 'Terran', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "TerranVehicleAndShipWeaponsLevel1": {  # deprecated
        "build_time": 114,
        "built_from": [ "Armory" ],
        "display_name": "Terran Vehicle and Ship Weapons Level 1",
        'race': 'Terran', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "TerranVehicleAndShipWeaponsLevel2": {  # deprecated
        "build_time": 136,
        "built_from": [ "Armory" ],
        "display_name": "Terran Vehicle and Ship Weapons Level 2",
        'race': 'Terran', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "TerranVehicleAndShipWeaponsLevel3": {  # deprecated
        "build_time": 157,
        "built_from": [ "Armory" ],
        "display_name": "Terran Vehicle and Ship Weapons Level 3",
        'race': 'Terran', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "TerranVehicleAndShipArmorsLevel1": {
        "build_time": 114,
        "built_from": [ "Armory" ],
        "display_name": "Terran Vehicle And Ship Armor Level 1",
        'race': 'Terran', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "TerranVehicleAndShipArmorsLevel2": {
        "build_time": 136,
        "built_from": [ "Armory" ],
        "display_name": "Terran Vehicle And Ship Armor Level 2",
        'race': 'Terran', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "TerranVehicleAndShipArmorsLevel3": {
        "build_time": 157,
        "built_from": [ "Armory" ],
        "display_name": "Terran Vehicle And Ship Armor Level 3",
        'race': 'Terran', 
        'type': 'Upgrade',
        'is_morph': False 
    },

    # barracks tech lab
    "Stimpack": {
        "build_time": 100,  # reduced from 121s to 100s 8/21/19
        "built_from": [ "TechLab" ],
        "display_name": "Stimpack",
        'race': 'Terran', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "PunisherGrenades": {
        "build_time": 43,
        "built_from": [ "TechLab" ],
        "display_name": "Concussive Shells",
        'race': 'Terran', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "ShieldWall": {
        "build_time": 79,
        "built_from": [ "TechLab" ],
        "display_name": "Combat Shield",
        'race': 'Terran', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    # engineering bay
    "NeosteelFrame": {  # deprecated in 4.7.1
        "build_time": 79,
        "built_from": [ "EngineeringBay" ],
        "display_name": "Neosteel Frame",
        "race": "Terran",
        "type": "Upgrade",
        "is_morph": False
    },
    "HiSecAutoTracking": {
        "build_time": 57,
        "built_from": [ "EngineeringBay" ],
        "display_name": "Hi-Sec Auto Tracking",
        "race": "Terran",
        "type": "Upgrade",
        "is_morph": False
    },
    "TerranBuildingArmor": {
        "build_time": 100,
        "built_from": [ "EngineeringBay" ],
        "display_name": "Neosteel Armor",  # renamed in 4.7.1
        "race": "Terran",
        "type": "Upgrade",
        "is_morph": False
    },
    # ghost academy
    "PersonalCloaking": {
        "build_time": 86,
        "built_from": [ "GhostAcademy" ],
        "display_name": "Personal Cloaking",
        'race': 'Terran', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "GhostMoebiusReactor": {  # deprecated
        "build_time": 57,
        "built_from": [ "GhostAcademy" ],
        "display_name": "Moebius Reactor",
        'race': 'Terran', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "EnhancedShockwaves": {  # deprecated in 5.0.11
        "build_time": 79,
        "built_from": [ "GhostAcademy" ],
        "display_name": "Enhanced Shockwaves",
        "race": "Terran",
        "type": "Upgrade",
        "is_morph": False
    },
    # factory tech lab
    "StrikeCannons": {  # deprecated
        "build_time": 79,
        "built_from": [ "TechLab" ],
        "display_name": "250mm Strike Cannons",
        'race': 'Terran', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "DrillClaws": {
        "build_time": 79,
        "built_from": [ "TechLab" ],
        "display_name": "Drilling Claws",
        'race': 'Terran', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "TransformationServos": {  # deprecated
        "build_time": 79,
        "built_from": [ "TechLab" ],
        "display_name": "Transformation Servos",
        'race': 'Terran', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "HighCapacityBarrels": {
        "build_time": 79,
        "built_from": [ "TechLab" ],
        "display_name": "Infernal Pre-Igniter",
        'race': 'Terran', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "CycloneLockOnDamageUpgrade": {  # re-introduced in 4.7.1, Deprecated in 5.0.12
        "build_time": 100,  # 79s -> 100s in 4.8.2
        "built_from": [ "TechLab" ],
        "display_name": "Mag-Field Accelerator",
        "race": "Terran",
        "type": "Upgrade",
        "is_morph": False
    },
    "MagFieldLaunchers": {  # deprecated
        "build_time": 79,
        "built_from": [ "TechLab" ],
        "display_name": "Mag-Field Launchers",
        'race': 'Terran', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "CycloneRapidFireLaunchers": {  # deprecated in 4.7.1
        "build_time": 79,
        "built_from": [ "TechLab" ],
        "display_name": "Rapid Fire Launchers",
        'race': 'Terran', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "HurricaneThrusters": {  # Added 5.0.12
        "build_time": 100,
        "built_from": [ "TechLab" ],
        "display_name": "Hurricane Engines",
        'race': 'Terran', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "SmartServos": {
        "build_time": 79,
        "built_from": [ "TechLab" ],
        "display_name": "Smart Servos",
        'race': 'Terran', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    # starport tech lab
    "RavenDamageUpgrade": {  # deprecated 3.8
        "build_time": 79,
        "built_from": [ "TechLab" ],
        "display_name": "Explosive Shrapnel Shells",
        'race': 'Terran', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "RavenRecalibratedExplosives": {  # deprecated
        "build_time": 79,
        "built_from": [ "TechLab" ],
        "display_name": "Recalibrated Explosives",
        'race': 'Terran', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "BansheeCloak": {
        "build_time": 79,
        "built_from": [ "TechLab" ],
        "display_name": "Cloaking Field",
        'race': 'Terran', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "DurableMaterials": {  # deprecated
        "build_time": 79,
        "built_from": [ "TechLab" ],
        "display_name": "Durable Materials",
        'race': 'Terran', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "RavenCorvidReactor": {  # deprecated in 5.0.11
        "build_time": 79,
        "built_from": [ "TechLab" ],
        "display_name": "Corvid Reactor",
        'race': 'Terran', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "BansheeSpeed": {
        "build_time": 121,  # 93 -> 121 in 3.8.0, 121.4 -> 100 in 5.0.11
        "built_from": [ "TechLab" ],
        "display_name": "Hyperflight Rotors",
        'race': 'Terran', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "RavenEnhancedMunitions": {
        "build_time": 79,
        "built_from": [ "TechLab" ],
        "display_name": "Enhanced Munitions",
        'race': 'Terran', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "InterferenceMatrix": {  # added 5.0.12
        "build_time": 57,
        "built_from": [ "TechLab" ],
        "display_name": "Interference Matrix",
        'race': 'Terran', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    # fusion core
    "BattlecruiserBehemothReactor": {
        "build_time": 57,
        "built_from": [ "FusionCore" ],
        "display_name": "Behemoth Reactor",
        'race': 'Terran', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "BattlecruiserEnableSpecializations": {
        "build_time": 100,  # 43 -> 100 in 4.8.2
        "built_from": [ "FusionCore" ],
        "display_name": "Weapon Refit",
        'race': 'Terran', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "LiberatorAGRangeUpgrade": {
        "build_time": 79,
        "built_from": [ "FusionCore" ],
        "display_name": "Advanced Ballistics",
        'race': 'Terran', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "MedivacIncreaseSpeedBoost": {  # Deprecated 5.0.12
        "build_time": 57,
        "built_from": [ "FusionCore" ],
        "display_name": "Rapid Reignition System",  # renamed in 4.7.1
        "race": "Terran",
        "type": "Upgrade",
        "is_morph": False
    },
    "MedivacCaduceusReactor": {  # deprecated, re-added 5.0.12
        "build_time": 57,
        "built_from": [ "FusionCore" ],  # previously built from TechLab
        "display_name": "Caduceus Reactor",
        'race': 'Terran', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    # protoss upgrades
    "ProtossGroundWeaponsLevel1": {
        "build_time": 122,  # 128.6 -> 121.6 in 5.0.11
        "built_from": [ "Forge" ],
        "display_name": "Protoss Ground Weapons Level 1",
        'race': 'Protoss', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "ProtossGroundWeaponsLevel2": {
        "build_time": 145,  # 153.6 -> 144.6 in 5.0.11
        "built_from": [ "Forge" ],
        "display_name": "Protoss Ground Weapons Level 2",
        'race': 'Protoss', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "ProtossGroundWeaponsLevel3": {
        "build_time": 168,  # 178.6 -> 167.9 in 5.0.11
        "built_from": [ "Forge" ],
        "display_name": "Protoss Ground Weapons Level 3",
        'race': 'Protoss', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "ProtossGroundArmorsLevel1": {
        "build_time": 122,  # 128.6 -> 121.6 in 5.0.11
        "built_from": [ "Forge" ],
        "display_name": "Protoss Ground Armor Level 1",
        'race': 'Protoss', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "ProtossGroundArmorsLevel2": {
        "build_time": 145,  # 153.6 -> 144.6 in 5.0.11
        "built_from": [ "Forge" ],
        "display_name": "Protoss Ground Armor Level 2",
        'race': 'Protoss', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "ProtossGroundArmorsLevel3": {
        "build_time": 168,  # 178.6 -> 167.9 in 5.0.11
        "built_from": [ "Forge" ],
        "display_name": "Protoss Ground Armor Level 3",
        'race': 'Protoss', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "ProtossShieldsLevel1": {
        "build_time": 122,  # 128.6 -> 121.6 in 5.0.11
        "built_from": [ "Forge" ],
        "display_name": "Protoss Shields Level 1",
        'race': 'Protoss', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "ProtossShieldsLevel2": {
        "build_time": 145,  # 153.6 -> 144.6 in 5.0.11
        "built_from": [ "Forge" ],
        "display_name": "Protoss Shields Level 2",
        'race': 'Protoss', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "ProtossShieldsLevel3": {
        "build_time": 168,  # 178.6 -> 167.9 in 5.0.11
        "built_from": [ "Forge" ],
        "display_name": "Protoss Shields Level 3",
        'race': 'Protoss', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "ProtossAirWeaponsLevel1": {
        "build_time": 114,
        "built_from": [ "CyberneticsCore" ],
        "display_name": "Protoss Air Weapons Level 1",
        'race': 'Protoss', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "ProtossAirWeaponsLevel2": {
        "build_time": 136,
        "built_from": [ "CyberneticsCore" ],
        "display_name": "Protoss Air Weapons Level 2",
        'race': 'Protoss', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "ProtossAirWeaponsLevel3": {
        "build_time": 157,
        "built_from": [ "CyberneticsCore" ],
        "display_name": "Protoss Air Weapons Level 3",
        'race': 'Protoss', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "ProtossAirArmorsLevel1": {
        "build_time": 114,
        "built_from": [ "CyberneticsCore" ],
        "display_name": "Protoss Air Armor Level 1",
        'race': 'Protoss', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "ProtossAirArmorsLevel2": {
        "build_time": 136,
        "built_from": [ "CyberneticsCore" ],
        "display_name": "Protoss Air Armor Level 2",
        'race': 'Protoss', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "ProtossAirArmorsLevel3": {
        "build_time": 157,
        "built_from": [ "CyberneticsCore" ],
        "display_name": "Protoss Air Armor Level 3",
        'race': 'Protoss', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "WarpGateResearch": {
        "build_time": 100,  # 114s -> 100s in 4.8.2
        "built_from": [ "CyberneticsCore" ],
        "display_name": "Warp Gate",
        'race': 'Protoss', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "Charge": {
        "build_time": 100,
        "built_from": [ "TwilightCouncil" ],
        "display_name": "Charge",
        'race': 'Protoss', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "BlinkTech": {
        "build_time": 121,
        "built_from": [ "TwilightCouncil" ],
        "display_name": "Blink",
        'race': 'Protoss', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "AdeptShieldUpgrade": {  # deprecated from LotV Beta
        "build_time": 57,
        "built_from": [ "TwilightCouncil" ],
        "display_name": "Shield Upgrade",
        'race': 'Protoss', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "AdeptPiercingAttack": {
        "build_time": 100,
        "built_from": [ "TwilightCouncil" ],
        "display_name": "Resonating Glaives",
        'race': 'Protoss', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "ObserverGraviticBooster": {
        "build_time": 57,
        "built_from": [ "RoboticsBay" ],
        "display_name": "Gravitic Boosters",
        'race': 'Protoss', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "GraviticDrive": {
        "build_time": 57,
        "built_from": [ "RoboticsBay" ],
        "display_name": "Gravitic Drive",
        'race': 'Protoss', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "ExtendedThermalLance": {
        "build_time": 100,
        "built_from": [ "RoboticsBay" ],
        "display_name": "Extended Thermal Lance",
        'race': 'Protoss', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "PsiStormTech": {
        "build_time": 79,
        "built_from": [ "TemplarArchives" ],
        "display_name": "Psionic Storm",
        'race': 'Protoss', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    # Fleet Beacon Upgrades
    "PhoenixRangeUpgrade": {
        "build_time": 64,
        "built_from": [ "FleetBeacon" ],
        "display_name": "Anion Pulse-Crystals",
        'race': 'Protoss', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "CarrierLaunchSpeedUpgrade": {  # deprecated in 4.7.1
        "build_time": 57,
        "built_from": [ "FleetBeacon" ],
        "display_name": "Graviton Catapult",
        'race': 'Protoss', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "VoidRaySpeedUpgrade": {
        "build_time": 57,
        "built_from": [ "Fleet Beacon" ],
        "display_name": "Flux Vanes",
        "race": "Protoss",
        "type": "Upgrade",
        "is_morph": False
    },
    # Dark Shrine Upgrades
    "DarkTemplarBlinkUpgrade": {
        "build_time": 100,  # decreased 121 -> 100 in 4.7.1
        "built_from": [ "DarkShrine" ],
        "display_name": "Shadow Stride",
        'race': 'Protoss', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    # unit change buildings
    "Lair": {
        "build_time": 57,
        "built_from": [ "Hatchery" ],
        "display_name": "Lair",
        'race': 'Zerg', 
        'type': 'Building',
        'is_morph': True 
    },
    "Hive": {
        "build_time": 71,
        "built_from": [ "Lair" ],
        "display_name": "Hive",
        'race': 'Zerg', 
        'type': 'Building',
        'is_morph': True 
    },
    "LurkerDenMP": {
        "build_time": 57,
        "built_from": [ "HydraliskDen" ],
        "display_name": "Lurker Den",
        'race': 'Zerg', 
        'type': 'Building',
        'is_morph': True 
    },
    "GreaterSpire": {
        "build_time": 71,
        "built_from": [ "Spire" ],
        "display_name": "Greater Spire",
        'race': 'Zerg', 
        'type': 'Building',
        'is_morph': True 
    },
    "OrbitalCommand": {
        "build_time": 25,
        "built_from": [ "CommandCenter" ],
        "display_name": "Orbital Command",
        'race': 'Terran', 
        'type': 'Building',
        'is_morph': True 
    },
    "PlanetaryFortress": {
        "build_time": 36,
        "built_from": [ "CommandCenter" ],
        "display_name": "Planetary Fortress",
        'race': 'Terran', 
        'type': 'Building',
        'is_morph': True 
    },
    # unofficial LotV Alpha only
    "HyperflightRotors": {
        "build_time": 93,
        "built_from": [ "TechLab" ],
        "display_name": "Hyperflight Rotors",
        'race': 'Terran', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "FlyingLocusts": {
        "build_time": 87,
        "built_from": [ "InfestationPit" ],
        "display_name": "Flying Locusts",
        'race': 'Zerg', 
        'type': 'Upgrade',
        'is_morph': False 
    },
    "CycloneLockOnRangeUpgrade": {
        "build_time": 79,
        "built_from": [ "TechLab" ],
        'race': 'Terran', 
        'type': 'BuildUpgradeing',
        'is_morph': True 
    },
    "CycloneAirUpgrade": {
        "build_time": 79,
        "built_from": [ "TechLab" ],
        'race': 'Terran', 
        'type': 'BuildUpgradeing',
        'is_morph': True 
    }
}

for value in BUILD_DATA.values():
    value['build_time'] *= FRAMES_PER_SECOND


TRACKED_ABILITIES = set([
    '250mmStrikeCannons',
    'BlindingCloud',
    'BuildAutoTurret',
    'CalldownMULE',
    'Contaminate',
    'Corruption',
    'EMPRound',
    'Feedback',
    'ForceField',
    'FungalGrowth',
    'GravitonBeam',
    'GuardianShield',
    'MassRecallMothership',  # Strategic Recall
    'MothershipMassRecall',
    'MothershipCorePurifyNexus',  # Photon Overcharge on Pylons
    'MassRecallMothershipCore',
    'InfestorNeuralParasite',
    'BuildPointDefenseDrone',
    'HallucinationArchon',
    'HallucinationColossus',
    'HallucinationHighTemplar',
    'HallucinationImmortal',
    'HallucinationPhoenix',
    'HallucinationProbe',
    'HallucinationStalker',
    'HallucinationVoidRay',
    'HallucinationWarpPrism',
    'HallucinationZealot',
    'PsionicStorm',
    'ScannerSweep',
    'SeekerMissile',
    'SniperRound',
    'SpawnLarva',
    'ExtraSupplies',
    'ChronoBoost',
    'ChronoBoostEnergyCost',
    'QueenTransfusion',
    'YamatoGun',
    'Abduct',
    'TemporalField',
    'Envision',
    'RavagerCorrosiveBile',
    # StarCraft 3.8
    'KD8Charge',  # Reaper - KD8 Charge
    'Hyperjump',  # BC - Tactical Jump
    'AdeptPhaseShift',  # Adept - Psionic Transfer
    #  'DarkTemplarBlink',  # DT - Shadow Stride
    'OracleStasisTrap',  # Oracle - Stasis Ward
    'CausticSpray',  # Corruptor - Caustic Spray
    'SpawnLocustsTargeted',  # Swarm Host - Spawn Locusts
    'LocustMPFlyingSwoop',  # Locust - Swoop
    # StarCraft 4.0
    'RavenShredderMissile',  # Anti-Armor Missile
    'RavenScramblerMissile',  # Interference Matrix
    'RavenRepairDrone',  # Repair Drone
    'ObserverMorphtoObserverSiege',  # Surveillance Mode
    'NexusMassRecall',  # new Mass Recall
    'OverseerMorphtoOverseerSiegeMode',  # Oversight
    # LotV Beta
    'LockOn',  # removed in 3.8
    'ReleaseInterceptors',  # removed in 3.8
    'PurificationNova',  # Deprecated?
    'Disintegration',  # Deprecated?
    ])

# these abilities have not been named to be extracted
# Immortal Barrier
# TempestDisruptionBlast
# Viper ParasiticBomb
