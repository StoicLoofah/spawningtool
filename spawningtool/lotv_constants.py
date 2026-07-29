"""
spawningtool.constants
~~~~~~~~~~~~~~~~~~~~~~
"""

from datetime import datetime, timezone

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

RACE_TERRAN = 'Terran'
RACE_PROTOSS = 'Protoss'
RACE_ZERG = 'Zerg'

TYPE_UNIT = 'Unit'
TYPE_BUILDING = 'Building'
TYPE_UPGRADE = 'Upgrade'

BUILD_DATA = {
    # terran units
    "SCV": {
        "build_time": 12,
        "built_from": [ "Command Center", "Orbital Command" ],
        "display_name": "SCV",
        'race': RACE_TERRAN, 
        'type': TYPE_UNIT, # Building, Upgrade, Unit
        'is_morph': False 
    },
    "Marine": {
        "build_time": 18,
        "built_from": [ "Barracks" ],
        "display_name": "Marine",
        'race': RACE_TERRAN, 
        'type': TYPE_UNIT,
        'is_morph': False 
    },
    "Marauder": {
        "build_time": 21,
        "built_from": [ "Barracks" ],
        "display_name": "Marauder",
        'race': RACE_TERRAN, 
        'type': TYPE_UNIT,
        'is_morph': False 
    },
    "Reaper": {
        "build_time": 34,
        "built_from": [ "Barracks" ],
        "display_name": "Reaper",
        'race': RACE_TERRAN, 
        'type': TYPE_UNIT,
        'is_morph': False 
    },
    "Ghost": {
        "build_time": 29,
        "built_from": [ "Barracks" ],
        "display_name": "Ghost",
        'race': RACE_TERRAN, 
        'type': TYPE_UNIT,
        'is_morph': False 
    },
    "BattleHellion": {
        "build_time": 21,
        "built_from": [ "Factory" ],
        "display_name": "Hellbat",
        'race': RACE_TERRAN, 
        'type': TYPE_UNIT,
        'is_morph': False 
    },
    "Hellion": {
        "build_time": 21,
        "built_from": [ "Factory" ],
        "display_name": "Hellion",
        'race': RACE_TERRAN, 
        'type': TYPE_UNIT,
        'is_morph': False 
    },
    "Hellbat": { # deprecated?
        "build_time": 21,
        "built_from": [ "Factory" ],
        "display_name": "Hellbat",
        'race': RACE_TERRAN, 
        'type': TYPE_UNIT,
        'is_morph': False 
    },
    "WidowMine": {
        "build_time": 21,
        "built_from": [ "Factory" ],
        "display_name": "Widow Mine",
        'race': RACE_TERRAN, 
        'type': TYPE_UNIT,
        'is_morph': False 
    },
    "SiegeTank": {
        "build_time": 32,
        "built_from": [ "Factory" ],
        "display_name": "Siege Tank",
        'race': RACE_TERRAN, 
        'type': TYPE_UNIT,
        'is_morph': False 
    },
    "Cyclone": {
        "build_time": 32,
        "built_from": [ "Factory" ],
        "display_name": "Cyclone",
        'race': RACE_TERRAN, 
        'type': TYPE_UNIT,
        'is_morph': False 
    },
    "Thor": {
        "build_time": 43,
        "built_from": [ "Factory" ],
        "display_name": "Thor",
        'race': RACE_TERRAN, 
        'type': TYPE_UNIT,
        'is_morph': False 
    },
    'Viking': {  # not built as this
        "build_time": 30,
        "built_from": [ "Starport" ],
        "display_name": "Viking",
        'race': RACE_TERRAN, 
        'type': TYPE_UNIT,
        'is_morph': False 
    },
    "VikingFighter": {
        "build_time": 30,   # all born as VikingFighters, but others in here for coverage
        "built_from": [ "Starport" ],
        "display_name": "Viking",
        'race': RACE_TERRAN, 
        'type': TYPE_UNIT,
        'is_morph': False 
    },
    "VikingAssault": {  # not built as this
        "build_time": 30,
        "built_from": [ "Starport" ],
        "display_name": "Viking",
        'race': RACE_TERRAN, 
        'type': TYPE_UNIT,
        'is_morph': False 
    },
    "Medivac": {
        "build_time": 30,
        "built_from": [ "Starport" ],
        "display_name": "Medivac",
        'race': RACE_TERRAN, 
        'type': TYPE_UNIT,
        'is_morph': False 
    },
    "Liberator": {
        "build_time": 43,
        "built_from": [ "Starport" ],
        "display_name": "Liberator",
        'race': RACE_TERRAN, 
        'type': TYPE_UNIT,
        'is_morph': False 
    },
    "Raven": {
        "build_time": 34,
        "built_from": [ "Starport" ],
        "display_name": "Raven",
        'race': RACE_TERRAN, 
        'type': TYPE_UNIT,
        'is_morph': False 
    },
    "Banshee": {
        "build_time": 43,
        "built_from": [ "Starport" ],
        "display_name": "Banshee",
        'race': RACE_TERRAN, 
        'type': TYPE_UNIT,
        'is_morph': False 
    },
    "Battlecruiser": {
        "build_time": 64,
        "built_from": [ "Starport" ],
        "display_name": "Battlecruiser",
        'race': RACE_TERRAN, 
        'type': TYPE_UNIT,
        'is_morph': False 
    },
    "Nuke": {  # treat the Nuke like a unit
        "build_time": 43,
        "built_from": [ "Ghost Academy" ],
        "display_name": "Nuke",
        'race': RACE_TERRAN, 
        'type': TYPE_UNIT,
        'is_morph': False 
    },
    # protoss units
    "Probe": {
        "build_time": 12,
        "built_from": [ "Nexus" ],
        "display_name": "Probe",
        'race': RACE_PROTOSS, 
        'type': TYPE_UNIT,
        'is_morph': False 
    },
    "Zealot": {
        "build_time": 27,
        "built_from": [ "Gateway", "WarpGate" ],  # warpgate is necessary because of changing types
        "display_name": "Zealot",
        'race': RACE_PROTOSS, 
        'type': TYPE_UNIT,
        'is_morph': False 
    },
    "Stalker": {
        "build_time": 27,
        "built_from": [ "Gateway", "WarpGate" ],
        "display_name": "Stalker",
        'race': RACE_PROTOSS, 
        'type': TYPE_UNIT,
        'is_morph': False 
    },
    "Sentry": {
        "build_time": 23,
        "built_from": [ "Gateway", "WarpGate" ],
        "display_name": "Sentry",
        'race': RACE_PROTOSS, 
        'type': TYPE_UNIT,
        'is_morph': False 
    },
    "Adept": {
        "build_time": 33,
        "built_from": [ "Gateway", "WarpGate" ],
        "display_name": "Adept",
        'race': RACE_PROTOSS, 
        'type': TYPE_UNIT,
        'is_morph': False 
    },
    "MothershipCore": {
        "build_time": 21,
        "built_from": [ "Nexus" ],
        "display_name": "Mothership Core",
        'race': RACE_PROTOSS, 
        'type': TYPE_UNIT,
        'is_morph': False 
    },
    "Mothership": {
        "build_time": 79,
        "built_from": [ "Nexus" ],
        "display_name": "Mothership",
        'race': RACE_PROTOSS, 
        'type': TYPE_UNIT,
        'is_morph': False 
    },
    "HighTemplar": {
        "build_time": 40,
        "built_from": [ "Gateway", "WarpGate" ],
        "display_name": "High Templar",
        'race': RACE_PROTOSS, 
        'type': TYPE_UNIT,
        'is_morph': False 
    },
    "DarkTemplar": {
        "build_time": 40,
        "built_from": [ "Gateway", "WarpGate" ],
        "display_name": "Dark Templar",
        'race': RACE_PROTOSS, 
        'type': TYPE_UNIT,
        'is_morph': False 
    },
    "Immortal": {
        "build_time": 39,
        "built_from": [ "RoboticsFacility" ],
        "display_name": "Immortal",
        'race': RACE_PROTOSS, 
        'type': TYPE_UNIT,
        'is_morph': False 
    },
    "Disruptor": {
        "build_time": 36,
        "built_from": [ "RoboticsFacility" ],
        "display_name": "Disruptor",
        'race': RACE_PROTOSS, 
        'type': TYPE_UNIT,
        'is_morph': False 
    },
    "Colossus": {
        "build_time": 54,
        "built_from": [ "RoboticsFacility" ],
        "display_name": "Colossus",
        'race': RACE_PROTOSS, 
        'type': TYPE_UNIT,
        'is_morph': False 
    },
    "Archon": {
        "build_time": 9,
        "built_from": [],
        "display_name": "Archon",
        'race': RACE_PROTOSS, 
        'type': TYPE_UNIT,
        'is_morph': False 
    },
    "Observer": {
        "build_time": 18,
        "built_from": [ "RoboticsFacility" ],
        "display_name": "Observer",
        'race': RACE_PROTOSS, 
        'type': TYPE_UNIT,
        'is_morph': False 
    },
    "WarpPrism": {
        "build_time": 36,
        "built_from": [ "RoboticsFacility" ],
        "display_name": "Warp Prism",
        'race': RACE_PROTOSS, 
        'type': TYPE_UNIT,
        'is_morph': False 
    },
    "Phoenix": {
        "build_time": 25,
        "built_from": [ "Stargate" ],
        "display_name": "Phoenix",
        'race': RACE_PROTOSS, 
        'type': TYPE_UNIT,
        'is_morph': False 
    },
    "VoidRay": {
        "build_time": 43,
        "built_from": [ "Stargate" ],
        "display_name": "Void Ray",
        'race': RACE_PROTOSS, 
        'type': TYPE_UNIT,
        'is_morph': False 
    },
    "Oracle": {
        "build_time": 37,
        "built_from": [ "Stargate" ],
        "display_name": "Oracle",
        'race': RACE_PROTOSS, 
        'type': TYPE_UNIT,
        'is_morph': False 
    },
    "Tempest": {
        "build_time": 43,
        "built_from": [ "Stargate" ],
        "display_name": "Tempest",
        'race': RACE_PROTOSS, 
        'type': TYPE_UNIT,
        'is_morph': False 
    },
    "Carrier": {
        "build_time": 64,
        "built_from": [ "Stargate" ],
        "display_name": "Carrier",
        'race': RACE_PROTOSS, 
        'type': TYPE_UNIT,
        'is_morph': False 
    },
    # zerg units
    "Drone": {
        "build_time": 12,
        "built_from": [],
        "display_name": "Drone",
        'race': RACE_ZERG, 
        'type': TYPE_UNIT,
        'is_morph': False 
    },
    "Queen": {
        "build_time": 36,
        "built_from": [ "Hatchery", "Lair", "Hive" ],
        "display_name": "Queen",
        'race': RACE_ZERG, 
        'type': TYPE_UNIT,
        'is_morph': False 
    },
    "Zergling": {
        "build_time": 17,
        "built_from": [],
        "display_name": "Zergling",
        'race': RACE_ZERG, 
        'type': TYPE_UNIT,
        'is_morph': False 
    },
    "Roach": {
        "build_time": 19,
        "built_from": [],
        "display_name": "Roach",
        'race': RACE_ZERG, 
        'type': TYPE_UNIT,
        'is_morph': False 
    },
    "Hydralisk": {
        "build_time": 24,
        "built_from": [],
        "display_name": "Hydralisk",
        'race': RACE_ZERG, 
        'type': TYPE_UNIT,
        'is_morph': False 
    },
    "SwarmHost": {
        "build_time": 29,
        "built_from": [],
        "display_name": "Swarm Host",
        'race': RACE_ZERG, 
        'type': TYPE_UNIT,
        'is_morph': False 
    },
    "Infestor": {
        "build_time": 36,
        "built_from": [],
        "display_name": "Infestor",
        'race': RACE_ZERG, 
        'type': TYPE_UNIT,
        'is_morph': False 
    },
    "Ultralisk": {
        "build_time": 39,
        "built_from": [],
        "display_name": "Ultralisk",
        'race': RACE_ZERG, 
        'type': TYPE_UNIT,
        'is_morph': False 
    },
    "Overlord": {
        "build_time": 18,
        "built_from": [],
        "display_name": "Overlord",
        'race': RACE_ZERG, 
        'type': TYPE_UNIT,
        'is_morph': False 
    },
    "Mutalisk": {
        "build_time": 24,
        "built_from": [],
        "display_name": "Mutalisk",
        'race': RACE_ZERG, 
        'type': TYPE_UNIT,
        'is_morph': False 
    },
    "Corruptor": {
        "build_time": 29,
        "built_from": [],
        "display_name": "Corruptor",
        'race': RACE_ZERG, 
        'type': TYPE_UNIT,
        'is_morph': False 
    },
    "Viper": {
        "build_time": 29,
        "built_from": [],
        "display_name": "Viper",
        'race': RACE_ZERG, 
        'type': TYPE_UNIT,
        'is_morph': False 
    },
    "NydusWorm": {  # deprecated
        "build_time": 14,
        "built_from": [ "NydusCanal" ],
		"display_name": "Nydus Worm",
        'race': RACE_ZERG, 
        'type': TYPE_BUILDING,
        'is_morph': False 
    },
    "NydusCanal": {
        "build_time": 14,
        "built_from": [ "NydusNetwork" ],
        "display_name": "Nydus Canal",
        'race': RACE_ZERG, 
        'type': TYPE_BUILDING,
        'is_morph': False 
    },
    # zerg evolved units
    "Baneling": {
        "build_time": 14,
        "built_from": [],
        "display_name": "Baneling",
        'race': RACE_ZERG, 
        'type': TYPE_UNIT,
        'is_morph': True 
    },
    "BroodLord": {
        "build_time": 24,
        "built_from": [],
        "display_name": "Brood Lord",
        'race': RACE_ZERG, 
        'type': TYPE_UNIT,
        'is_morph': True 
    },
    "Overseer": {
        "build_time": 12,
        "built_from": [ "Overlord" ],
        "display_name": "Overseer",
        'race': RACE_ZERG, 
        'type': TYPE_BUILDING,
        'is_morph': True 
    },
    "RavagerCocoon": {  # Ravager - egg not itself because it is the start time, normal build time is 12 seconds
        # increased 8.57 -> 12.14 seconds in 5.0.11
        "build_time": 0,
        "built_from": [ "Roach" ],
        "display_name": "Ravager",
        'race': RACE_ZERG, 
        'type': TYPE_BUILDING,
        'is_morph': True 
    },
    "LurkerMPEgg": {  # Lurker - same logic as above, especially because burrow/unburrow counts, normal build time is 18
        "build_time": 0,
        "built_from": [ "Hydralisk" ],
        "display_name": "Lurker",
        'race': RACE_ZERG, 
        'type': TYPE_BUILDING,
        'is_morph': True 
    },
    # zerg upgrades
    "ZergMeleeWeaponsLevel1": {
        "build_time": 114,
        "built_from": [ "EvolutionChamber" ],
        "display_name": "Zerg Melee Weapons Level 1",
        'race': RACE_ZERG, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "ZergMeleeWeaponsLevel2": {
        "build_time": 136,
        "built_from": [ "EvolutionChamber" ],
        "display_name": "Zerg Melee Weapons Level 2",
        'race': RACE_ZERG, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "ZergMeleeWeaponsLevel3": {
        "build_time": 157,
        "built_from": [ "EvolutionChamber" ],
        "display_name": "Zerg Melee Weapons Level 3",
        'race': RACE_ZERG, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "ZergMissileWeaponsLevel1": {
        "build_time": 114,
        "built_from": [ "EvolutionChamber" ],
        "display_name": "Zerg Missile Weapons Level 1",
        'race': RACE_ZERG, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "ZergMissileWeaponsLevel2": {
        "build_time": 136,
        "built_from": [ "EvolutionChamber" ],
        "display_name": "Zerg Missile Weapons Level 2",
        'race': RACE_ZERG, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "ZergMissileWeaponsLevel3": {
        "build_time": 157,
        "built_from": [ "EvolutionChamber" ],
        "display_name": "Zerg Missile Weapons Level 3",
        'race': RACE_ZERG, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "ZergGroundArmorsLevel1": {
        "build_time": 114,
        "built_from": [ "EvolutionChamber" ],
        "display_name": "Zerg Ground Armor Level 1",
        'race': RACE_ZERG, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "ZergGroundArmorsLevel2": {
        "build_time": 136,
        "built_from": [ "EvolutionChamber" ],
        "display_name": "Zerg Ground Armor Level 2",
        'race': RACE_ZERG, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "ZergGroundArmorsLevel3": {
        "build_time": 157,
        "built_from": [ "EvolutionChamber" ],
        "display_name": "Zerg Ground Armor Level 3",
        'race': RACE_ZERG, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "ZergFlyerWeaponsLevel1": {
        "build_time": 114,
        "built_from": [ "Spire", "GreaterSpire" ],
        "display_name": "Zerg Flyer Weapons Level 1",
        'race': RACE_ZERG, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "ZergFlyerWeaponsLevel2": {
        "build_time": 136,
        "built_from": [ "Spire", "GreaterSpire" ],
        "display_name": "Zerg Flyer Weapons Level 2",
        'race': RACE_ZERG, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "ZergFlyerWeaponsLevel3": {
        "build_time": 157,
        "built_from": [ "Spire", "GreaterSpire" ],
        "display_name": "Zerg Flyer Weapons Level 3",
        'race': RACE_ZERG, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "ZergFlyerArmorsLevel1": {
        "build_time": 114,
        "built_from": [ "Spire", "GreaterSpire" ],
        "display_name": "Zerg Flyer Armor Level 1",
        'race': RACE_ZERG, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "ZergFlyerArmorsLevel2": {
        "build_time": 136,
        "built_from": [ "Spire", "GreaterSpire" ],
        "display_name": "Zerg Flyer Armor Level 2",
        'race': RACE_ZERG, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "ZergFlyerArmorsLevel3": {
        "build_time": 157,
        "built_from": [ "Spire", "GreaterSpire" ],
        "display_name": "Zerg Flyer Armor Level 3",
        'race': RACE_ZERG, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    # Spawning Pool Upgrades
    "zerglingmovementspeed": {
        "build_time": 79,
        "built_from": [ "SpawningPool" ],
        "display_name": "Metabolic Boost",
        'race': RACE_ZERG, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "zerglingattackspeed": {
        "build_time": 93,
        "built_from": [ "SpawningPool" ],
        "display_name": "Adrenal Glands",
        'race': RACE_ZERG, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    # Baneling Nest Upgrades
    "CentrificalHooks": {
        "build_time": 71,
        "built_from": [ "BanelingNest" ],
        "display_name": "Centrifugal Hooks",
        'race': RACE_ZERG, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    # Roach Warren Upgrades
    "GlialReconstitution": {
        "build_time": 79,
        "built_from": [ "RoachWarren" ],
        "display_name": "Glial Reconstitution",
        'race': RACE_ZERG, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "TunnelingClaws": {
        "build_time": 79,
        "built_from": [ "RoachWarren" ],
        "display_name": "Tunneling Claws",
        'race': RACE_ZERG, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    # Hydralisk Den Upgrades
    "hydraliskspeed": {  # LotV Muscular Augments, deprecated 3.8
        "build_time": 71,
        "built_from": [ "HydraliskDen" ],
        "display_name": "Muscular Augments",
        'race': RACE_ZERG, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "HydraliskSpeedUpgrade": {  # HotS deprecated Muscular Augments
        "build_time": 71,
        "built_from": [ "HydraliskDen" ],
        "display_name": "Muscular Augments",
        'race': RACE_ZERG, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "EvolveGroovedSpines": {  # added 3.8
        "build_time": 50,
        "built_from": [ "HydraliskDen" ],
        "display_name": "Grooved Spines",
        'race': RACE_ZERG, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "EvolveMuscularAugments": {  # added 3.8
        "build_time": 64,
        "built_from": [ "HydraliskDen" ],
        "display_name": "Muscular Augments",
        'race': RACE_ZERG, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    # Hatchery Upgrades
    "overlordspeed": {
        "build_time": 43,
        "built_from": [ "Hatchery", "Lair", "Hive" ],
        "display_name": "Pneumatized Carapace",
        'race': RACE_ZERG, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "overlordtransport": {  # deprecated
        "build_time": 93,
        "built_from": [ "Hatchery", "Lair", "Hive" ],
        "display_name": "Ventral Sacs",
        'race': RACE_ZERG, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "Burrow": {
        "build_time": 71,
        "built_from": [ "Hatchery", "Lair", "Hive" ],
        "display_name": "Burrow",
        'race': RACE_ZERG, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    # Infestation Pit Upgrades
    "InfestorEnergyUpgrade": {  # Deprecated 5.0.12
        "build_time": 57,
        "built_from": [ "InfestationPit" ],
        "display_name": "Pathogen Glands",
        'race': RACE_ZERG, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "LocustLifetimeIncrease": {  # deprecated
        "build_time": 87,
        "built_from": [ "InfestationPit" ],
        "display_name": "Enduring Locusts",
        'race': RACE_ZERG, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "NeuralParasite": {
        "build_time": 79,
        "built_from": [ "InfestationPit" ],
        "display_name": "Neural Parasite",
        'race': RACE_ZERG, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    # stopped requiring research at some point after 4.11.0; 5.0.15 made it an
    # upgrade again (150/150, research time not restated, assumed unchanged)
    "MicrobialShroud": {
        "build_time": 79,
        "built_from": [ "InfestationPit" ],
        "display_name": "Microbial Shroud",
        "race": RACE_ZERG,
        "type": TYPE_UPGRADE,
        "is_morph": False
    },
    # Ultralisk Cavern Upgrades
    "ChitinousPlating": {
        "build_time": 79,
        "built_from": [ "UltraliskCavern" ],
        "display_name": "Chitinous Plating",
        'race': RACE_ZERG, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "AnabolicSynthesis": {  # added in 4.7.1
        "build_time": 43,
        "built_from": [ "UltraliskCavern" ],
        "display_name": "Anabolic Synthesis",
        "race": RACE_ZERG,
        "type": TYPE_UPGRADE,
        "is_morph": False
    },
    # Lurker Den Upgrades
    "DiggingClaws": {
        "build_time": 57,
        "built_from": [ "LurkerDenMP" ],
        "display_name": "Adaptive Talons",
        "race": RACE_ZERG,
        "type": TYPE_UPGRADE,
        "is_morph": False
    },
    "LurkerRange": {
        "build_time": 57,
        "built_from": [ "LurkerDenMP" ],
        "display_name": "Seismic Spines",
        "race": RACE_ZERG,
        "type": TYPE_UPGRADE,
        "is_morph": False
    },

    # terran upgrades
    "TerranInfantryWeaponsLevel1": {
        "build_time": 114,
        "built_from": [ "EngineeringBay" ],
        "display_name": "Terran Infantry Weapons Level 1",
        'race': RACE_TERRAN, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "TerranInfantryWeaponsLevel2": {
        "build_time": 136,
        "built_from": [ "EngineeringBay" ],
        "display_name": "Terran Infantry Weapons Level 2",
        'race': RACE_TERRAN, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "TerranInfantryWeaponsLevel3": {
        "build_time": 157,
        "built_from": [ "EngineeringBay" ],
        "display_name": "Terran Infantry Weapons Level 3",
        'race': RACE_TERRAN, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "TerranInfantryArmorsLevel1": {
        "build_time": 114,
        "built_from": [ "EngineeringBay" ],
        "display_name": "Terran Infantry Armor Level 1",
        'race': RACE_TERRAN, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "TerranInfantryArmorsLevel2": {
        "build_time": 136,
        "built_from": [ "EngineeringBay" ],
        "display_name": "Terran Infantry Armor Level 2",
        'race': RACE_TERRAN, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "TerranInfantryArmorsLevel3": {
        "build_time": 157,
        "built_from": [ "EngineeringBay" ],
        "display_name": "Terran Infantry Armor Level 3",
        'race': RACE_TERRAN, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "TerranVehicleWeaponsLevel1": {
        "build_time": 114,
        "built_from": [ "Armory" ],
        "display_name": "Terran Vehicle Weapons Level 1",
        'race': RACE_TERRAN, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "TerranVehicleWeaponsLevel2": {
        "build_time": 136,
        "built_from": [ "Armory" ],
        "display_name": "Terran Vehicle Weapons Level 2",
        'race': RACE_TERRAN, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "TerranVehicleWeaponsLevel3": {
        "build_time": 157,
        "built_from": [ "Armory" ],
        "display_name": "Terran Vehicle Weapons Level 3",
        'race': RACE_TERRAN, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "TerranVehicleArmorsLevel1": {  # deprecated
        "build_time": 114,
        "built_from": [ "Armory" ],
        "display_name": "Terran Vehicle Armor Level 1",
        'race': RACE_TERRAN, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "TerranVehicleArmorsLevel2": {  # deprecated
        "build_time": 136,
        "built_from": [ "Armory" ],
        "display_name": "Terran Vehicle Armor Level 2",
        'race': RACE_TERRAN, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "TerranVehicleArmorsLevel3": {  # deprecated
        "build_time": 157,
        "built_from": [ "Armory" ],
        "display_name": "Terran Vehicle Armor Level 3",
        'race': RACE_TERRAN, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "TerranShipWeaponsLevel1": {
        "build_time": 114,
        "built_from": [ "Armory" ],
        "display_name": "Terran Ship Weapons Level 1",
        'race': RACE_TERRAN, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "TerranShipWeaponsLevel2": {
        "build_time": 136,
        "built_from": [ "Armory" ],
        "display_name": "Terran Ship Weapons Level 2",
        'race': RACE_TERRAN, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "TerranShipWeaponsLevel3": {
        "build_time": 157,
        "built_from": [ "Armory" ],
        "display_name": "Terran Ship Weapons Level 3",
        'race': RACE_TERRAN, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "TerranShipArmorsLevel1": {  # deprecated
        "build_time": 114,
        "built_from": [ "Armory" ],
        "display_name": "Terran Ship Armor Level 1",
        'race': RACE_TERRAN, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "TerranShipArmorsLevel2": {  # deprecated
        "build_time": 136,
        "built_from": [ "Armory" ],
        "display_name": "Terran Ship Armor Level 2",
        'race': RACE_TERRAN, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "TerranShipArmorsLevel3": {  # deprecated
        "build_time": 157,
        "built_from": [ "Armory" ],
        "display_name": "Terran Ship Armor Level 3",
        'race': RACE_TERRAN, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "TerranVehicleAndShipWeaponsLevel1": {  # deprecated
        "build_time": 114,
        "built_from": [ "Armory" ],
        "display_name": "Terran Vehicle and Ship Weapons Level 1",
        'race': RACE_TERRAN, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "TerranVehicleAndShipWeaponsLevel2": {  # deprecated
        "build_time": 136,
        "built_from": [ "Armory" ],
        "display_name": "Terran Vehicle and Ship Weapons Level 2",
        'race': RACE_TERRAN, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "TerranVehicleAndShipWeaponsLevel3": {  # deprecated
        "build_time": 157,
        "built_from": [ "Armory" ],
        "display_name": "Terran Vehicle and Ship Weapons Level 3",
        'race': RACE_TERRAN, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "TerranVehicleAndShipArmorsLevel1": {
        "build_time": 114,
        "built_from": [ "Armory" ],
        "display_name": "Terran Vehicle And Ship Armor Level 1",
        'race': RACE_TERRAN, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "TerranVehicleAndShipArmorsLevel2": {
        "build_time": 136,
        "built_from": [ "Armory" ],
        "display_name": "Terran Vehicle And Ship Armor Level 2",
        'race': RACE_TERRAN, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "TerranVehicleAndShipArmorsLevel3": {
        "build_time": 157,
        "built_from": [ "Armory" ],
        "display_name": "Terran Vehicle And Ship Armor Level 3",
        'race': RACE_TERRAN, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },

    # barracks tech lab
    "Stimpack": {
        "build_time": 100,
        "built_from": [ "TechLab" ],
        "display_name": "Stimpack",
        'race': RACE_TERRAN, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "PunisherGrenades": {
        "build_time": 43,
        "built_from": [ "TechLab" ],
        "display_name": "Concussive Shells",
        'race': RACE_TERRAN, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "ShieldWall": {
        "build_time": 79,
        "built_from": [ "TechLab" ],
        "display_name": "Combat Shield",
        'race': RACE_TERRAN, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    # engineering bay
    "NeosteelFrame": {  # deprecated in 4.7.1
        "build_time": 79,
        "built_from": [ "EngineeringBay" ],
        "display_name": "Neosteel Frame",
        "race": RACE_TERRAN,
        "type": TYPE_UPGRADE,
        "is_morph": False
    },
    "HiSecAutoTracking": {
        "build_time": 57,
        "built_from": [ "EngineeringBay" ],
        "display_name": "Hi-Sec Auto Tracking",
        "race": RACE_TERRAN,
        "type": TYPE_UPGRADE,
        "is_morph": False
    },
    "TerranBuildingArmor": {
        "build_time": 100,
        "built_from": [ "EngineeringBay" ],
        "display_name": "Neosteel Armor",  # renamed in 4.7.1
        "race": RACE_TERRAN,
        "type": TYPE_UPGRADE,
        "is_morph": False
    },
    # ghost academy
    "PersonalCloaking": {
        "build_time": 86,
        "built_from": [ "GhostAcademy" ],
        "display_name": "Personal Cloaking",
        'race': RACE_TERRAN, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "GhostMoebiusReactor": {  # deprecated
        "build_time": 57,
        "built_from": [ "GhostAcademy" ],
        "display_name": "Moebius Reactor",
        'race': RACE_TERRAN, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "EnhancedShockwaves": {  # deprecated in 5.0.11
        "build_time": 79,
        "built_from": [ "GhostAcademy" ],
        "display_name": "Enhanced Shockwaves",
        "race": RACE_TERRAN,
        "type": TYPE_UPGRADE,
        "is_morph": False
    },
    # factory tech lab
    "StrikeCannons": {  # deprecated
        "build_time": 79,
        "built_from": [ "TechLab" ],
        "display_name": "250mm Strike Cannons",
        'race': RACE_TERRAN, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "DrillClaws": {
        "build_time": 79,
        "built_from": [ "TechLab" ],
        "display_name": "Drilling Claws",
        'race': RACE_TERRAN, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "TransformationServos": {  # deprecated
        "build_time": 79,
        "built_from": [ "TechLab" ],
        "display_name": "Transformation Servos",
        'race': RACE_TERRAN, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "HighCapacityBarrels": {
        "build_time": 79,
        "built_from": [ "TechLab" ],
        "display_name": "Infernal Pre-Igniter",
        'race': RACE_TERRAN, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    # re-introduced in 4.7.1, deprecated in 5.0.12, back in 5.0.14 when the
    # Cyclone was reverted to its 5.0.11 version
    "CycloneLockOnDamageUpgrade": {
        "build_time": 100,
        "built_from": [ "TechLab" ],
        "display_name": "Mag-Field Accelerator",
        "race": RACE_TERRAN,
        "type": TYPE_UPGRADE,
        "is_morph": False
    },
    "MagFieldLaunchers": {  # deprecated
        "build_time": 79,
        "built_from": [ "TechLab" ],
        "display_name": "Mag-Field Launchers",
        'race': RACE_TERRAN, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "CycloneRapidFireLaunchers": {  # deprecated in 4.7.1
        "build_time": 79,
        "built_from": [ "TechLab" ],
        "display_name": "Rapid Fire Launchers",
        'race': RACE_TERRAN, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    # added 5.0.12, removed in 5.0.14 with the revert to the 5.0.11 Cyclone
    "HurricaneThrusters": {
        "build_time": 100,
        "built_from": [ "TechLab" ],
        "display_name": "Hurricane Engines",
        'race': RACE_TERRAN, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "SmartServos": {
        "build_time": 79,
        "built_from": [ "TechLab" ],
        "display_name": "Smart Servos",
        'race': RACE_TERRAN, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    # starport tech lab
    "RavenDamageUpgrade": {  # deprecated 3.8
        "build_time": 79,
        "built_from": [ "TechLab" ],
        "display_name": "Explosive Shrapnel Shells",
        'race': RACE_TERRAN, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "RavenRecalibratedExplosives": {  # deprecated
        "build_time": 79,
        "built_from": [ "TechLab" ],
        "display_name": "Recalibrated Explosives",
        'race': RACE_TERRAN, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "BansheeCloak": {
        "build_time": 79,
        "built_from": [ "TechLab" ],
        "display_name": "Cloaking Field",
        'race': RACE_TERRAN, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "DurableMaterials": {  # deprecated
        "build_time": 79,
        "built_from": [ "TechLab" ],
        "display_name": "Durable Materials",
        'race': RACE_TERRAN, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "RavenCorvidReactor": {  # deprecated in 5.0.11
        "build_time": 79,
        "built_from": [ "TechLab" ],
        "display_name": "Corvid Reactor",
        'race': RACE_TERRAN, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "BansheeSpeed": {
        "build_time": 79,
        "built_from": [ "TechLab" ],
        "display_name": "Hyperflight Rotors",
        'race': RACE_TERRAN, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "RavenEnhancedMunitions": {
        "build_time": 79,
        "built_from": [ "TechLab" ],
        "display_name": "Enhanced Munitions",
        'race': RACE_TERRAN, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "InterferenceMatrix": {  # added 5.0.12
        "build_time": 57,
        "built_from": [ "TechLab" ],
        "display_name": "Interference Matrix",
        'race': RACE_TERRAN, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    # fusion core
    "BattlecruiserBehemothReactor": {
        "build_time": 57,
        "built_from": [ "FusionCore" ],
        "display_name": "Behemoth Reactor",
        'race': RACE_TERRAN, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "BattlecruiserEnableSpecializations": {
        "build_time": 100,
        "built_from": [ "FusionCore" ],
        "display_name": "Weapon Refit",
        'race': RACE_TERRAN, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "LiberatorAGRangeUpgrade": {
        "build_time": 79,
        "built_from": [ "FusionCore" ],
        "display_name": "Advanced Ballistics",
        'race': RACE_TERRAN, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "MedivacIncreaseSpeedBoost": {  # Deprecated 5.0.12
        "build_time": 57,
        "built_from": [ "FusionCore" ],
        "display_name": "Rapid Reignition System",  # renamed in 4.7.1
        "race": RACE_TERRAN,
        "type": TYPE_UPGRADE,
        "is_morph": False
    },
    "MedivacCaduceusReactor": {  # deprecated, re-added 5.0.12
        "build_time": 57,
        "built_from": [ "FusionCore" ],  # previously built from TechLab
        "display_name": "Caduceus Reactor",
        'race': RACE_TERRAN, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    # protoss upgrades
    "ProtossGroundWeaponsLevel1": {
        "build_time": 122,
        "built_from": [ "Forge" ],
        "display_name": "Protoss Ground Weapons Level 1",
        'race': RACE_PROTOSS, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "ProtossGroundWeaponsLevel2": {
        "build_time": 145,
        "built_from": [ "Forge" ],
        "display_name": "Protoss Ground Weapons Level 2",
        'race': RACE_PROTOSS, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "ProtossGroundWeaponsLevel3": {
        "build_time": 168,
        "built_from": [ "Forge" ],
        "display_name": "Protoss Ground Weapons Level 3",
        'race': RACE_PROTOSS, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "ProtossGroundArmorsLevel1": {
        "build_time": 122,
        "built_from": [ "Forge" ],
        "display_name": "Protoss Ground Armor Level 1",
        'race': RACE_PROTOSS, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "ProtossGroundArmorsLevel2": {
        "build_time": 145,
        "built_from": [ "Forge" ],
        "display_name": "Protoss Ground Armor Level 2",
        'race': RACE_PROTOSS, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "ProtossGroundArmorsLevel3": {
        "build_time": 168,
        "built_from": [ "Forge" ],
        "display_name": "Protoss Ground Armor Level 3",
        'race': RACE_PROTOSS, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "ProtossShieldsLevel1": {
        "build_time": 122,
        "built_from": [ "Forge" ],
        "display_name": "Protoss Shields Level 1",
        'race': RACE_PROTOSS, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "ProtossShieldsLevel2": {
        "build_time": 145,
        "built_from": [ "Forge" ],
        "display_name": "Protoss Shields Level 2",
        'race': RACE_PROTOSS, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "ProtossShieldsLevel3": {
        "build_time": 168,
        "built_from": [ "Forge" ],
        "display_name": "Protoss Shields Level 3",
        'race': RACE_PROTOSS, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "ProtossAirWeaponsLevel1": {
        "build_time": 129,
        "built_from": [ "CyberneticsCore" ],
        "display_name": "Protoss Air Weapons Level 1",
        'race': RACE_PROTOSS, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "ProtossAirWeaponsLevel2": {
        "build_time": 154,
        "built_from": [ "CyberneticsCore" ],
        "display_name": "Protoss Air Weapons Level 2",
        'race': RACE_PROTOSS, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "ProtossAirWeaponsLevel3": {
        "build_time": 179,
        "built_from": [ "CyberneticsCore" ],
        "display_name": "Protoss Air Weapons Level 3",
        'race': RACE_PROTOSS, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "ProtossAirArmorsLevel1": {
        "build_time": 129,
        "built_from": [ "CyberneticsCore" ],
        "display_name": "Protoss Air Armor Level 1",
        'race': RACE_PROTOSS, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "ProtossAirArmorsLevel2": {
        "build_time": 154,
        "built_from": [ "CyberneticsCore" ],
        "display_name": "Protoss Air Armor Level 2",
        'race': RACE_PROTOSS, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "ProtossAirArmorsLevel3": {
        "build_time": 179,
        "built_from": [ "CyberneticsCore" ],
        "display_name": "Protoss Air Armor Level 3",
        'race': RACE_PROTOSS, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "WarpGateResearch": {
        "build_time": 100,
        "built_from": [ "CyberneticsCore" ],
        "display_name": "Warp Gate",
        'race': RACE_PROTOSS, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "Charge": {
        "build_time": 100,
        "built_from": [ "TwilightCouncil" ],
        "display_name": "Charge",
        'race': RACE_PROTOSS, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "BlinkTech": {
        "build_time": 121,
        "built_from": [ "TwilightCouncil" ],
        "display_name": "Blink",
        'race': RACE_PROTOSS, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "AdeptShieldUpgrade": {  # deprecated from LotV Beta
        "build_time": 57,
        "built_from": [ "TwilightCouncil" ],
        "display_name": "Shield Upgrade",
        'race': RACE_PROTOSS, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "AdeptPiercingAttack": {
        "build_time": 100,
        "built_from": [ "TwilightCouncil" ],
        "display_name": "Resonating Glaives",
        'race': RACE_PROTOSS, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "ObserverGraviticBooster": {
        "build_time": 57,
        "built_from": [ "RoboticsBay" ],
        "display_name": "Gravitic Boosters",
        'race': RACE_PROTOSS, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "GraviticDrive": {
        "build_time": 57,
        "built_from": [ "RoboticsBay" ],
        "display_name": "Gravitic Drive",
        'race': RACE_PROTOSS, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "ExtendedThermalLance": {
        "build_time": 100,
        "built_from": [ "RoboticsBay" ],
        "display_name": "Extended Thermal Lance",
        'race': RACE_PROTOSS, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "PsiStormTech": {
        "build_time": 79,
        "built_from": [ "TemplarArchives" ],
        "display_name": "Psionic Storm",
        'race': RACE_PROTOSS, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    # Fleet Beacon Upgrades
    "PhoenixRangeUpgrade": {
        "build_time": 64,
        "built_from": [ "FleetBeacon" ],
        "display_name": "Anion Pulse-Crystals",
        'race': RACE_PROTOSS, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "CarrierLaunchSpeedUpgrade": {  # deprecated in 4.7.1
        "build_time": 57,
        "built_from": [ "FleetBeacon" ],
        "display_name": "Graviton Catapult",
        'race': RACE_PROTOSS, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "VoidRaySpeedUpgrade": {
        "build_time": 57,
        "built_from": [ "Fleet Beacon" ],
        "display_name": "Flux Vanes",
        "race": RACE_PROTOSS,
        "type": TYPE_UPGRADE,
        "is_morph": False
    },
    # Dark Shrine Upgrades
    "DarkTemplarBlinkUpgrade": {
        "build_time": 100,
        "built_from": [ "DarkShrine" ],
        "display_name": "Shadow Stride",
        'race': RACE_PROTOSS, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    # unit change buildings
    "Lair": {
        "build_time": 57,
        "built_from": [ "Hatchery" ],
        "display_name": "Lair",
        'race': RACE_ZERG, 
        'type': TYPE_BUILDING,
        'is_morph': True 
    },
    "Hive": {
        "build_time": 71,
        "built_from": [ "Lair" ],
        "display_name": "Hive",
        'race': RACE_ZERG, 
        'type': TYPE_BUILDING,
        'is_morph': True 
    },
    "LurkerDenMP": {
        "build_time": 57,
        "built_from": [ "HydraliskDen" ],
        "display_name": "Lurker Den",
        'race': RACE_ZERG, 
        'type': TYPE_BUILDING,
        'is_morph': True 
    },
    "GreaterSpire": {
        "build_time": 71,
        "built_from": [ "Spire" ],
        "display_name": "Greater Spire",
        'race': RACE_ZERG, 
        'type': TYPE_BUILDING,
        'is_morph': True 
    },
    "OrbitalCommand": {
        "build_time": 25,
        "built_from": [ "CommandCenter" ],
        "display_name": "Orbital Command",
        'race': RACE_TERRAN, 
        'type': TYPE_BUILDING,
        'is_morph': True 
    },
    "PlanetaryFortress": {
        "build_time": 36,
        "built_from": [ "CommandCenter" ],
        "display_name": "Planetary Fortress",
        'race': RACE_TERRAN, 
        'type': TYPE_BUILDING,
        'is_morph': True 
    },
    # unofficial LotV Alpha only
    "HyperflightRotors": {
        "build_time": 93,
        "built_from": [ "TechLab" ],
        "display_name": "Hyperflight Rotors",
        'race': RACE_TERRAN, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "FlyingLocusts": {
        "build_time": 87,
        "built_from": [ "InfestationPit" ],
        "display_name": "Flying Locusts",
        'race': RACE_ZERG, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "CycloneLockOnRangeUpgrade": {
        "build_time": 79,
        "built_from": [ "TechLab" ],
        'race': RACE_TERRAN, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    },
    "CycloneAirUpgrade": {
        "build_time": 79,
        "built_from": [ "TechLab" ],
        'race': RACE_TERRAN, 
        'type': TYPE_UPGRADE,
        'is_morph': False 
    }
}


# Balance patch history
# =====================
#
# BUILD_DATA above holds the CURRENT build times. This section records when each
# of those values changed, so a replay is scored with the build time that was
# actually live on the day it was played rather than with today's value. Balance
# hotfixes don't always bump the replay build number, so the played date is what
# tells them apart (cf. the chronoboost handling in parser.py, which also keys
# off unix_timestamp).
#
# Each entry is (patch_label, effective_date, {unit: (old_seconds, new_seconds)}).
# Entries are in chronological order, and each unit's `old` value must equal the
# `new` value of the previous entry that touched it, with the last `new` value
# matching BUILD_DATA. That chain is verified at import (see below), which is
# what catches a patch being recorded without its predecessor -- e.g. High/Dark
# Templar going 39 -> 43 in 5.0.16 and only then 43 -> 40 in the hotfix.
#
# HOW FAR BACK THIS GOES
# ----------------------
# Coverage starts at patch 3.8.0 (2016-11-22). A replay played before that date
# gets the oldest value recorded here for each unit, which is only correct as far
# back as whenever that value became live -- so LotV launch (2015-11-10), the
# LotV beta/alpha, and the first year of LotV are NOT accurately covered, and
# neither is anything from WoL or HotS (those use hots_constants, which has no
# date handling at all). Replays from that era are scored with early-2016 values.
#
# Within the covered range, every patch that this repo has ever recorded a build
# time change for has been checked against Blizzard's notes. Patches that this
# repo never tracked have only been spot-checked, and at least two of them
# (5.0.14, 5.0.15) did contain changes that were missed for years -- so a gap in
# a patch series here is not proof that nothing changed. As of this writing the
# following have not been swept: 4.0-4.6, 4.8.0/4.8.1/4.8.3/4.8.4, 4.9.x,
# 4.10.x other than the 2019-08-21 balance update, 5.0.0/5.0.1, 5.0.3-5.0.8,
# 5.0.10, and the 5.0.11 hotfixes.
#
# Some of those unswept ranges are nonetheless pinned by test replays, which
# lock in whatever this table says for the date they were played: 4.6.0
# (2018-09-08), 4.9.2 (2019-06-27), 5.0.4 (2020-11-05), 5.0.10 (2022-11-19),
# 5.0.13 (2024-09-06) and 5.0.14 (2025-04-29), plus 3.8.0 and the 5.0.16 series.
# Those tests fail if this table is changed or bypassed, so they will catch a
# regression here even where the notes haven't been read.
#
# Sources are the patch notes off https://news.blizzard.com/en-us/feed/starcraft-2.
# Blizzard quotes build times in the same units this file uses, so their numbers
# are copied directly, rounded to whole seconds to match BUILD_DATA's style; the
# exact figure is noted in a comment where it differs. Dates are the NA release
# date at 00:00 UTC -- patches roll out to EU/KR a day later, so a replay played
# within a day of a patch may be scored with the adjacent value.
#
# Deliberately NOT recorded here: changes to this file that corrected wrong data
# rather than tracking a game change. Those must not be rolled back for old
# replays, because the older value was never live. They include the 2015-2016
# rounding cleanups (116 -> 114, 80 -> 79, 58 -> 57, ... when FRAMES_PER_SECOND
# was refined), the Liberator 60 -> 43 fix (2020), and the Carrier 64 -> 86 and
# Disruptor 43 -> 36 corrections made against the LotV release build.
BUILD_TIME_CHANGES = [
    ('3.8.0', '2016-11-22', {
        'BansheeSpeed': (93, 121),  # Hyperflight Rotors
    }),
    ('Balance Update', '2017-12-18', {
        'Oracle': (43, 37),
        'WidowMine': (29, 21),  # 28.6 -> 21.4
    }),
    ('4.7.1', '2018-11-20', {
        'Carrier': (86, 64),
        'DarkTemplarBlinkUpgrade': (121, 100),  # Shadow Stride
    }),
    ('4.8.2', '2019-01-22', {
        'Adept': (27, 30),
        'BattlecruiserEnableSpecializations': (43, 100),  # Weapon Refit
        'CycloneLockOnDamageUpgrade': (79, 100),  # Mag-Field Accelerator
        'WarpGateResearch': (114, 100),
    }),
    # "Forge/Cybernetics Core: Level 1/2/3 upgrade times increased by
    # 15/18/22 seconds" -- both structures, so the Cybernetics Core air upgrades
    # went up alongside the Forge ground ones. Only the Forge upgrades came back
    # down in 5.0.11, which is why air and ground differ today.
    ('Balance Update', '2019-03-25', {
        'ProtossGroundWeaponsLevel1': (114, 129),
        'ProtossGroundWeaponsLevel2': (136, 154),
        'ProtossGroundWeaponsLevel3': (157, 179),
        'ProtossGroundArmorsLevel1': (114, 129),
        'ProtossGroundArmorsLevel2': (136, 154),
        'ProtossGroundArmorsLevel3': (157, 179),
        'ProtossShieldsLevel1': (114, 129),
        'ProtossShieldsLevel2': (136, 154),
        'ProtossShieldsLevel3': (157, 179),
        'ProtossAirWeaponsLevel1': (114, 129),
        'ProtossAirWeaponsLevel2': (136, 154),
        'ProtossAirWeaponsLevel3': (157, 179),
        'ProtossAirArmorsLevel1': (114, 129),
        'ProtossAirArmorsLevel2': (136, 154),
        'ProtossAirArmorsLevel3': (157, 179),
    }),
    ('Balance Update', '2019-08-21', {
        'Stimpack': (121, 100),
    }),
    ('4.11.0', '2019-11-26', {
        'DiggingClaws': (54, 57),  # Adaptive Talons
        'LurkerDenMP': (86, 57),
    }),
    # Blizzard published no separate live notes for 5.0.9 (a community balance
    # patch, so the PTR notes stood as the notes), which made this pair the one
    # entry here without a live primary source. Both halves are instead
    # confirmed by the test replays: patch_5_0_10_pvz has six unchronoboosted
    # Void Rays at exactly 43.0s, and patch_5_0_4_pvt has one produced in 25.1s,
    # which is below the 28.7s floor a 43s unit has even under chronoboost.
    ('5.0.2', '2020-08-06', {
        'VoidRay': (43, 37),
    }),
    ('5.0.9', '2022-03-15', {
        'VoidRay': (37, 43),  # reverted the 5.0.2 reduction
    }),
    ('5.0.11', '2023-01-23', {
        'BansheeSpeed': (121, 100),  # 121.4 -> 100, Hyperflight Rotors
        'Raven': (43, 34),  # 42.9 -> 34.3
        'Sentry': (26, 23),  # 26.4 -> 22.9
        'ProtossGroundWeaponsLevel1': (129, 122),  # 128.6 -> 121.6
        'ProtossGroundWeaponsLevel2': (154, 145),  # 153.6 -> 144.6
        'ProtossGroundWeaponsLevel3': (179, 168),  # 178.6 -> 167.9
        'ProtossGroundArmorsLevel1': (129, 122),
        'ProtossGroundArmorsLevel2': (154, 145),
        'ProtossGroundArmorsLevel3': (179, 168),
        'ProtossShieldsLevel1': (129, 122),
        'ProtossShieldsLevel2': (154, 145),
        'ProtossShieldsLevel3': (179, 168),
    }),
    ('5.0.12', '2023-09-29', {
        'CentrificalHooks': (79, 71),
        'EvolveGroovedSpines': (71, 50),
        'EvolveMuscularAugments': (71, 64),
        'Mothership': (114, 79),
    }),
    ('5.0.13', '2024-03-26', {
        'Observer': (21, 18),  # 21.4 -> 17.9
    }),
    ('5.0.14', '2024-11-25', {
        'Stalker': (30, 27),  # train time from Gateway
    }),
    ('5.0.15', '2025-09-30', {
        'BansheeSpeed': (100, 79),  # Hyperflight Rotors
    }),
    # 5.0.16 reworked Gateway production: Warp Gate Research became a flat
    # percentage reduction (see WARPGATE_MODIFIERS) instead of separate warp-in
    # timings. The High/Dark Templar increase is not stated outright in the
    # 5.0.16 notes, but the hotfix a week later reduced them "from 43", and the
    # 5.0.16 post-Warpgate figure of 26s matches 43 * 0.6.
    ('5.0.16', '2026-06-22', {
        'HighTemplar': (39, 43),
        'DarkTemplar': (39, 43),
    }),
    ('5.0.16 hotfix', '2026-06-30', {
        'Adept': (30, 33),
        'DarkTemplar': (43, 40),
        'HighTemplar': (43, 40),
        'Reaper': (32, 34),
    }),
]


def _patch_timestamp(date):
    """
    Unix timestamp (UTC) for a 'YYYY-MM-DD' patch date.
    """
    return int(datetime.strptime(date, '%Y-%m-%d').replace(tzinfo=timezone.utc).timestamp())


def _build_history(changes):
    """
    Turn BUILD_TIME_CHANGES into {unit: [(superseded_timestamp, build_time)]},
    where build_time is the value that was live until that timestamp, oldest
    first. Raises ValueError if the recorded chain doesn't line up with
    BUILD_DATA, which means a patch is missing or has the wrong before/after
    value.
    """
    history = {}
    latest = {}
    previous_timestamp = None

    for label, date, units in changes:
        timestamp = _patch_timestamp(date)
        if previous_timestamp is not None and timestamp < previous_timestamp:
            raise ValueError('BUILD_TIME_CHANGES is not in chronological order at {}'.format(label))
        previous_timestamp = timestamp

        for unit_name, (old, new) in units.items():
            if unit_name not in BUILD_DATA:
                raise ValueError('{} ({}) is not in BUILD_DATA'.format(unit_name, label))
            expected = latest.get(unit_name)
            if expected is not None and expected != old:
                raise ValueError(
                    '{} enters {} at {}s but the previous change left it at {}s'.format(
                        unit_name, label, old, expected))
            history.setdefault(unit_name, []).append((timestamp, old))
            latest[unit_name] = new

    for unit_name, new in latest.items():
        if BUILD_DATA[unit_name]['build_time'] != new:
            raise ValueError(
                '{} ends its patch history at {}s but BUILD_DATA says {}s'.format(
                    unit_name, new, BUILD_DATA[unit_name]['build_time']))

    return history


# Previous build times per unit, oldest first, as
# (timestamp_at_which_the_value_was_superseded, build_time). Built from
# BUILD_TIME_CHANGES while BUILD_DATA is still in seconds, then converted to
# frames alongside it.
BUILD_DATA_HISTORY = _build_history(BUILD_TIME_CHANGES)

for value in BUILD_DATA.values():
    value['build_time'] *= FRAMES_PER_SECOND

for unit_name in BUILD_DATA_HISTORY:
    BUILD_DATA_HISTORY[unit_name] = [
        (timestamp, build_time * FRAMES_PER_SECOND)
        for timestamp, build_time in BUILD_DATA_HISTORY[unit_name]
    ]


def build_data_for_timestamp(timestamp):
    """
    Return BUILD_DATA adjusted for the balance patches that were live when the
    replay was played (timestamp is unix seconds, UTC). Units in
    BUILD_DATA_HISTORY are rolled back to their historical build time for
    replays played before a change took effect; everything else keeps the
    current value. A replay played before any recorded change (i.e. most of the
    existing corpus) therefore pays for a copy of BUILD_DATA; the shared dict is
    returned as-is when nothing needs rolling back. A missing timestamp falls
    back to the current values.
    """
    adjusted = None
    for unit_name, history in BUILD_DATA_HISTORY.items():
        for superseded, build_time in history:
            if timestamp and timestamp < superseded:
                if adjusted is None:
                    adjusted = {key: dict(value) for key, value in BUILD_DATA.items()}
                adjusted[unit_name]['build_time'] = build_time
                break
    return adjusted if adjusted is not None else BUILD_DATA


# Warp Gate Research speeds up Gateway unit production once complete, as a
# fraction of the normal build time. Introduced in 5.0.16 at 40% off (0.6x);
# 5.0.16b increased it to 50% off (0.5x). Oldest first, same shape as
# BUILD_TIME_CHANGES: (patch_label, effective_date, modifier). Gateway units
# warped in before 5.0.16 used separate warp-in timings rather than a percentage,
# which is why the parser also gates this on the 5.0.16 build number.
WARPGATE_MODIFIERS = [
    ('5.0.16', '2026-06-22', 0.6),
    ('5.0.16b', '2026-07-16', 0.5),
]

_WARPGATE_MODIFIERS = [
    (_patch_timestamp(date), modifier) for _, date, modifier in WARPGATE_MODIFIERS
]


def warpgate_build_time_modifier(timestamp):
    """
    Fraction of the normal build time a Gateway unit takes once Warp Gate
    Research finishes, based on when the replay was played (unix seconds, UTC).
    A missing timestamp falls back to the current value, matching
    build_data_for_timestamp.
    """
    if not timestamp:
        return _WARPGATE_MODIFIERS[-1][1]

    modifier = _WARPGATE_MODIFIERS[0][1]
    for effective, current in _WARPGATE_MODIFIERS:
        if timestamp < effective:
            break
        modifier = current
    return modifier


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
