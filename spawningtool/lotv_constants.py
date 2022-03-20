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
        "display_name": "SCV"
    },
    "Marine": {
        "build_time": 18,
        "built_from": [ "Barracks" ],
        "display_name": "Marine"
    },
    "Marauder": {
        "build_time": 21,
        "built_from": [ "Barracks" ],
        "display_name": "Marauder"
    },
    "Reaper": {
        "build_time": 32,
        "built_from": [ "Barracks" ],
        "display_name": "Reaper"
    },
    "Ghost": {
        "build_time": 29,
        "built_from": [ "Barracks" ],
        "display_name": "Ghost"
    },
    "BattleHellion": {
        "build_time": 21,
        "built_from": [ "Factory" ],
        "display_name": "Hellbat"
    },
    "Hellion": {
        "build_time": 21,
        "built_from": [ "Factory" ],
        "display_name": "Hellion"
    },
    "Hellbat": { # deprecated?
        "build_time": 21,
        "built_from": [ "Factory" ],
        "display_name": "Hellbat"
    },
    "WidowMine": {
        "build_time": 21,
        "built_from": [ "Factory" ],
        "display_name": "Widow Mine"
    },
    "SiegeTank": {
        "build_time": 32,
        "built_from": [ "Factory" ],
        "display_name": "Siege Tank"
    },
    "Cyclone": {
        "build_time": 32,
        "built_from": [ "Factory" ],
        "display_name": "Cyclone"
    },
    "Thor": {
        "build_time": 43,
        "built_from": [ "Factory" ],
        "display_name": "Thor"
    },
    'Viking': {  # not built as this
        "build_time": 30,
        "built_from": [ "Starport" ],
        "display_name": "Viking"
    },
    "VikingFighter": {
        "build_time": 30,   # all born as VikingFighters, but others in here for coverage
        "built_from": [ "Starport" ],
        "display_name": "Viking"
    },
    "VikingAssault": {  # not built as this
        "build_time": 30,
        "built_from": [ "Starport" ],
        "display_name": "Viking"
    },
    "Medivac": {
        "build_time": 30,
        "built_from": [ "Starport" ],
        "display_name": "Medivac"
    },
    "Liberator": {
        "build_time": 43,
        "built_from": [ "Starport" ],
        "display_name": "Liberator"
    },
    "Raven": {
        "build_time": 43,
        "built_from": [ "Starport" ],
        "display_name": "Raven"
    },
    "Banshee": {
        "build_time": 43,
        "built_from": [ "Starport" ],
        "display_name": "Banshee"
    },
    "Battlecruiser": {
        "build_time": 64,
        "built_from": [ "Starport" ],
        "display_name": "Battlecruiser"
    },
    "Nuke": {  # treat the Nuke like a unit
        "build_time": 43,
        "built_from": [ "Ghost Academy" ],
        "display_name": "Nuke"
    },
    # protoss units
    "Probe": {
        "build_time": 12,
        "built_from": [ "Nexus" ],
        "display_name": "Probe"
    },
    "Zealot": {
        "build_time": 27,
        "built_from": [ "Gateway", "WarpGate" ],  # warpgate is necessary because of changing types
        "display_name": "Zealot"
    },
    "Stalker": {
        "build_time": 30,
        "built_from": [ "Gateway", "WarpGate" ],
        "display_name": "Stalker"
    },
    "Sentry": {
        "build_time": 26,
        "built_from": [ "Gateway", "WarpGate" ],
        "display_name": "Sentry"
    },
    "Adept": {
        "build_time": 30,  # 27 -> 30 in 4.8.2
        "built_from": [ "Gateway", "WarpGate" ],
        "display_name": "Adept"
    },
    "MothershipCore": {
        "build_time": 21,
        "built_from": [ "Nexus" ],
        "display_name": "Mothership Core"
    },
    "Mothership": {
        "build_time": 114,
        "built_from": [ "Nexus" ],
        "display_name": "Mothership"
    },
    "HighTemplar": {
        "build_time": 39,
        "built_from": [ "Gateway", "WarpGate" ],
        "display_name": "High Templar"
    },
    "DarkTemplar": {
        "build_time": 39,
        "built_from": [ "Gateway", "WarpGate" ],
        "display_name": "Dark Templar"
    },
    "Immortal": {
        "build_time": 39,
        "built_from": [ "RoboticsFacility" ],
        "display_name": "Immortal"
    },
    "Disruptor": {
        "build_time": 36,
        "built_from": [ "RoboticsFacility" ],
        "display_name": "Disruptor"
    },
    "Colossus": {
        "build_time": 54,
        "built_from": [ "RoboticsFacility" ],
        "display_name": "Colossus"
    },
    "Archon": {
        "build_time": 9,
        "built_from": [],
        "display_name": "Archon"
    },
    "Observer": {
        "build_time": 21,
        "built_from": [ "RoboticsFacility" ],
        "display_name": "Observer"
    },
    "WarpPrism": {
        "build_time": 36,
        "built_from": [ "RoboticsFacility" ],
        "display_name": "Warp Prism"
    },
    "Phoenix": {
        "build_time": 25,
        "built_from": [ "Stargate" ],
        "display_name": "Phoenix"
    },
    "VoidRay": {
        "build_time": 37,  # decreased 43 -> 37 in 5.0.9 Mar 15 2022
        "built_from": [ "Stargate" ],
        "display_name": "Void Ray"
    },
    "Oracle": {
        "build_time": 37,
        "built_from": [ "Stargate" ],
        "display_name": "Oracle"
    },
    "Tempest": {
        "build_time": 43,
        "built_from": [ "Stargate" ],
        "display_name": "Tempest"
    },
    "Carrier": {
        "build_time": 64,  # decreased 86 -> 64 in 4.7.1
        "built_from": [ "Stargate" ],
        "display_name": "Carrier"
    },
    # zerg units
    "Drone": {
        "build_time": 12,
        "built_from": [],
        "display_name": "Drone"
    },
    "Queen": {
        "build_time": 36,
        "built_from": [ "Hatchery", "Lair", "Hive" ],
        "display_name": "Queen"
    },
    "Zergling": {
        "build_time": 17,
        "built_from": [],
        "display_name": "Zergling"
    },
    "Roach": {
        "build_time": 19,
        "built_from": [],
        "display_name": "Roach"
    },
    "Hydralisk": {
        "build_time": 24,
        "built_from": [],
        "display_name": "Hydralisk"
    },
    "SwarmHost": {
        "build_time": 29,
        "built_from": [],
        "display_name": "Swarm Host"
    },
    "Infestor": {
        "build_time": 36,
        "built_from": [],
        "display_name": "Infestor"
    },
    "Ultralisk": {
        "build_time": 39,
        "built_from": [],
        "display_name": "Ultralisk"
    },
    "Overlord": {
        "build_time": 18,
        "built_from": [],
        "display_name": "Overlord"
    },
    "Mutalisk": {
        "build_time": 24,
        "built_from": [],
        "display_name": "Mutalisk"
    },
    "Corruptor": {
        "build_time": 29,
        "built_from": [],
        "display_name": "Corruptor"
    },
    "Viper": {
        "build_time": 29,
        "built_from": [],
        "display_name": "Viper"
    },
    "NydusWorm": {  # deprecated
        "build_time": 14,
        "built_from": [ "NydusCanal" ],
		"display_name": "Nydus Worm"
    },
    "NydusCanal": {
        "build_time": 14,
        "built_from": [ "NydusNetwork" ],
        "display_name": "Nydus Canal"
    },
    # zerg evolved units
    "Baneling": {
        "build_time": 14,
        "built_from": [],
        "display_name": "Baneling"
    },
    "BroodLord": {
        "build_time": 24,
        "built_from": [],
        "display_name": "Brood Lord"
    },
    "Overseer": {
        "build_time": 12,
        "built_from": [ "Overlord" ],
        "display_name": "Overseer"
    },
    "RavagerCocoon": {  # Ravager - egg not itself because it is the start time, normal build time is 9
        "build_time": 0,
        "built_from": [ "Roach" ],
        "display_name": "Ravager"
    },
    "LurkerMPEgg": {  # Lurker - same logic as above, especially because burrow/unburrow counts, normal build time is 18
        "build_time": 0,
        "built_from": [ "Hydralisk" ],
        "display_name": "Lurker"
    },
    # zerg upgrades
    "ZergMeleeWeaponsLevel1": {
        "build_time": 114,
        "built_from": [ "EvolutionChamber" ],
        "display_name": "Zerg Melee Weapons Level 1"
    },
    "ZergMeleeWeaponsLevel2": {
        "build_time": 136,
        "built_from": [ "EvolutionChamber" ],
        "display_name": "Zerg Melee Weapons Level 2"
    },
    "ZergMeleeWeaponsLevel3": {
        "build_time": 157,
        "built_from": [ "EvolutionChamber" ],
        "display_name": "Zerg Melee Weapons Level 3"
    },
    "ZergMissileWeaponsLevel1": {
        "build_time": 114,
        "built_from": [ "EvolutionChamber" ],
        "display_name": "Zerg Missile Weapons Level 1"
    },
    "ZergMissileWeaponsLevel2": {
        "build_time": 136,
        "built_from": [ "EvolutionChamber" ],
        "display_name": "Zerg Missile Weapons Level 2"
    },
    "ZergMissileWeaponsLevel3": {
        "build_time": 157,
        "built_from": [ "EvolutionChamber" ],
        "display_name": "Zerg Missile Weapons Level 3"
    },
    "ZergGroundArmorsLevel1": {
        "build_time": 114,
        "built_from": [ "EvolutionChamber" ],
        "display_name": "Zerg Ground Armor Level 1"
    },
    "ZergGroundArmorsLevel2": {
        "build_time": 136,
        "built_from": [ "EvolutionChamber" ],
        "display_name": "Zerg Ground Armor Level 2"
    },
    "ZergGroundArmorsLevel3": {
        "build_time": 157,
        "built_from": [ "EvolutionChamber" ],
        "display_name": "Zerg Ground Armor Level 3"
    },
    "ZergFlyerWeaponsLevel1": {
        "build_time": 114,
        "built_from": [ "Spire", "GreaterSpire" ],
        "display_name": "Zerg Flyer Weapons Level 1"
    },
    "ZergFlyerWeaponsLevel2": {
        "build_time": 136,
        "built_from": [ "Spire", "GreaterSpire" ],
        "display_name": "Zerg Flyer Weapons Level 2"
    },
    "ZergFlyerWeaponsLevel3": {
        "build_time": 157,
        "built_from": [ "Spire", "GreaterSpire" ],
        "display_name": "Zerg Flyer Weapons Level 3"
    },
    "ZergFlyerArmorsLevel1": {
        "build_time": 114,
        "built_from": [ "Spire", "GreaterSpire" ],
        "display_name": "Zerg Flyer Armor Level 1"
    },
    "ZergFlyerArmorsLevel2": {
        "build_time": 136,
        "built_from": [ "Spire", "GreaterSpire" ],
        "display_name": "Zerg Flyer Armor Level 2"
    },
    "ZergFlyerArmorsLevel3": {
        "build_time": 157,
        "built_from": [ "Spire", "GreaterSpire" ],
        "display_name": "Zerg Flyer Armor Level 3"
    },
    # Spawning Pool Upgrades
    "zerglingmovementspeed": {
        "build_time": 79,
        "built_from": [ "SpawningPool" ],
        "display_name": "Metabolic Boost"
    },
    "zerglingattackspeed": {
        "build_time": 93,
        "built_from": [ "SpawningPool" ],
        "display_name": "Adrenal Glands"
    },
    # Baneling Nest Upgrades
    "CentrificalHooks": {
        "build_time": 79,
        "built_from": [ "BanelingNest" ],
        "display_name": "Centrifugal Hooks"
    },
    # Roach Warren Upgrades
    "GlialReconstitution": {
        "build_time": 79,
        "built_from": [ "RoachWarren" ],
        "display_name": "Glial Reconstitution"
    },
    "TunnelingClaws": {
        "build_time": 79,
        "built_from": [ "RoachWarren" ],
        "display_name": "Tunneling Claws"
    },
    # Hydralisk Den Upgrades
    "hydraliskspeed": {  # LotV Muscular Augments, deprecated 3.8
        "build_time": 71,
        "built_from": [ "HydraliskDen" ],
        "display_name": "Muscular Augments"
    },
    "HydraliskSpeedUpgrade": {  # HotS deprecated Muscular Augments
        "build_time": 71,
        "built_from": [ "HydraliskDen" ],
        "display_name": "Muscular Augments"
    },
    "EvolveGroovedSpines": {  # added 3.8
        "build_time": 71,
        "built_from": [ "HydraliskDen" ],
        "display_name": "Grooved Spines"
    },
    "EvolveMuscularAugments": {  # added 3.8
        "build_time": 71,
        "built_from": [ "HydraliskDen" ],
        "display_name": "Muscular Augments"
    },
    # Hatchery Upgrades
    "overlordspeed": {
        "build_time": 43,
        "built_from": [ "Hatchery", "Lair", "Hive" ],
        "display_name": "Pneumatized Carapace"
    },
    "overlordtransport": {  # deprecated
        "build_time": 93,
        "built_from": [ "Hatchery", "Lair", "Hive" ],
        "display_name": "Ventral Sacs"
    },
    "Burrow": {
        "build_time": 71,
        "built_from": [ "Hatchery", "Lair", "Hive" ],
        "display_name": "Burrow"
    },
    # Infestation Pit Upgrades
    "InfestorEnergyUpgrade": {
        "build_time": 57,
        "built_from": [ "InfestationPit" ],
        "display_name": "Pathogen Glands"
    },
    "LocustLifetimeIncrease": {  # deprecated
        "build_time": 87,
        "built_from": [ "InfestationPit" ],
        "display_name": "Enduring Locusts"
    },
    "NeuralParasite": {
        "build_time": 79,
        "built_from": [ "InfestationPit" ],
        "display_name": "Neural Parasite"
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
        "display_name": "Chitinous Plating"
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
        "display_name": "Terran Infantry Weapons Level 1"
    },
    "TerranInfantryWeaponsLevel2": {
        "build_time": 136,
        "built_from": [ "EngineeringBay" ],
        "display_name": "Terran Infantry Weapons Level 2"
    },
    "TerranInfantryWeaponsLevel3": {
        "build_time": 157,
        "built_from": [ "EngineeringBay" ],
        "display_name": "Terran Infantry Weapons Level 3"
    },
    "TerranInfantryArmorsLevel1": {
        "build_time": 114,
        "built_from": [ "EngineeringBay" ],
        "display_name": "Terran Infantry Armor Level 1"
    },
    "TerranInfantryArmorsLevel2": {
        "build_time": 136,
        "built_from": [ "EngineeringBay" ],
        "display_name": "Terran Infantry Armor Level 2"
    },
    "TerranInfantryArmorsLevel3": {
        "build_time": 157,
        "built_from": [ "EngineeringBay" ],
        "display_name": "Terran Infantry Armor Level 3"
    },
    "TerranVehicleWeaponsLevel1": {
        "build_time": 114,
        "built_from": [ "Armory" ],
        "display_name": "Terran Vehicle Weapons Level 1"
    },
    "TerranVehicleWeaponsLevel2": {
        "build_time": 136,
        "built_from": [ "Armory" ],
        "display_name": "Terran Vehicle Weapons Level 2"
    },
    "TerranVehicleWeaponsLevel3": {
        "build_time": 157,
        "built_from": [ "Armory" ],
        "display_name": "Terran Vehicle Weapons Level 3"
    },
    "TerranVehicleArmorsLevel1": {  # deprecated
        "build_time": 114,
        "built_from": [ "Armory" ],
        "display_name": "Terran Vehicle Armor Level 1"
    },
    "TerranVehicleArmorsLevel2": {  # deprecated
        "build_time": 136,
        "built_from": [ "Armory" ],
        "display_name": "Terran Vehicle Armor Level 2"
    },
    "TerranVehicleArmorsLevel3": {  # deprecated
        "build_time": 157,
        "built_from": [ "Armory" ],
        "display_name": "Terran Vehicle Armor Level 3"
    },
    "TerranShipWeaponsLevel1": {
        "build_time": 114,
        "built_from": [ "Armory" ],
        "display_name": "Terran Ship Weapons Level 1"
    },
    "TerranShipWeaponsLevel2": {
        "build_time": 136,
        "built_from": [ "Armory" ],
        "display_name": "Terran Ship Weapons Level 2"
    },
    "TerranShipWeaponsLevel3": {
        "build_time": 157,
        "built_from": [ "Armory" ],
        "display_name": "Terran Ship Weapons Level 3"
    },
    "TerranShipArmorsLevel1": {  # deprecated
        "build_time": 114,
        "built_from": [ "Armory" ],
        "display_name": "Terran Ship Armor Level 1"
    },
    "TerranShipArmorsLevel2": {  # deprecated
        "build_time": 136,
        "built_from": [ "Armory" ],
        "display_name": "Terran Ship Armor Level 2"
    },
    "TerranShipArmorsLevel3": {  # deprecated
        "build_time": 157,
        "built_from": [ "Armory" ],
        "display_name": "Terran Ship Armor Level 3"
    },
    "TerranVehicleAndShipWeaponsLevel1": {  # deprecated
        "build_time": 114,
        "built_from": [ "Armory" ],
        "display_name": "Terran Vehicle and Ship Weapons Level 1"
    },
    "TerranVehicleAndShipWeaponsLevel2": {  # deprecated
        "build_time": 136,
        "built_from": [ "Armory" ],
        "display_name": "Terran Vehicle and Ship Weapons Level 2"
    },
    "TerranVehicleAndShipWeaponsLevel3": {  # deprecated
        "build_time": 157,
        "built_from": [ "Armory" ],
        "display_name": "Terran Vehicle and Ship Weapons Level 3"
    },
    "TerranVehicleAndShipArmorsLevel1": {
        "build_time": 114,
        "built_from": [ "Armory" ],
        "display_name": "Terran Vehicle And Ship Armor Level 1"
    },
    "TerranVehicleAndShipArmorsLevel2": {
        "build_time": 136,
        "built_from": [ "Armory" ],
        "display_name": "Terran Vehicle And Ship Armor Level 2"
    },
    "TerranVehicleAndShipArmorsLevel3": {
        "build_time": 157,
        "built_from": [ "Armory" ],
        "display_name": "Terran Vehicle And Ship Armor Level 3"
    },

    # barracks tech lab
    "Stimpack": {
        "build_time": 100,  # reduced from 121s to 100s 8/21/19
        "built_from": [ "TechLab" ],
        "display_name": "Stimpack"
    },
    "PunisherGrenades": {
        "build_time": 43,
        "built_from": [ "TechLab" ],
        "display_name": "Concussive Shells"
    },
    "ShieldWall": {
        "build_time": 79,
        "built_from": [ "TechLab" ],
        "display_name": "Combat Shield"
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
        "display_name": "Personal Cloaking"
    },
    "GhostMoebiusReactor": {  # deprecated
        "build_time": 57,
        "built_from": [ "GhostAcademy" ],
        "display_name": "Moebius Reactor"
    },
    "EnhancedShockwaves": {
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
        "display_name": "250mm Strike Cannons"
    },
    "DrillClaws": {
        "build_time": 79,
        "built_from": [ "TechLab" ],
        "display_name": "Drilling Claws"
    },
    "TransformationServos": {  # deprecated
        "build_time": 79,
        "built_from": [ "TechLab" ],
        "display_name": "Transformation Servos"
    },
    "HighCapacityBarrels": {
        "build_time": 79,
        "built_from": [ "TechLab" ],
        "display_name": "Infernal Pre-Igniter"
    },
    "CycloneLockOnDamageUpgrade": {  # re-introduced in 4.7.1
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
        "display_name": "Mag-Field Launchers"
    },
    "CycloneRapidFireLaunchers": {  # deprecated in 4.7.1
        "build_time": 79,
        "built_from": [ "TechLab" ],
        "display_name": "Rapid Fire Launchers"
    },
    "SmartServos": {
        "build_time": 79,
        "built_from": [ "TechLab" ],
        "display_name": "Smart Servos"
    },
    # starport tech lab
    "MedivacCaduceusReactor": {  # deprecated
        "build_time": 57,
        "built_from": [ "TechLab" ],
        "display_name": "Caduceus Reactor"
    },
    "RavenDamageUpgrade": {  # deprecated 3.8
        "build_time": 79,
        "built_from": [ "TechLab" ],
        "display_name": "Explosive Shrapnel Shells"
    },
    "RavenRecalibratedExplosives": {  # deprecated
        "build_time": 79,
        "built_from": [ "TechLab" ],
        "display_name": "Recalibrated Explosives"
    },
    "BansheeCloak": {
        "build_time": 79,
        "built_from": [ "TechLab" ],
        "display_name": "Cloaking Field"
    },
    "DurableMaterials": {  # deprecated
        "build_time": 79,
        "built_from": [ "TechLab" ],
        "display_name": "Durable Materials"
    },
    "RavenCorvidReactor": {
        "build_time": 79,
        "built_from": [ "TechLab" ],
        "display_name": "Corvid Reactor"
    },
    "BansheeSpeed": {
        "build_time": 121,  # was 93 before 3.8.0
        "built_from": [ "TechLab" ],
        "display_name": "Hyperflight Rotors"
    },
    "RavenEnhancedMunitions": {
        "build_time": 79,
        "built_from": [ "TechLab" ],
        "display_name": "Enhanced Munitions"
    },
    # fusion core
    "BattlecruiserBehemothReactor": {
        "build_time": 57,
        "built_from": [ "FusionCore" ],
        "display_name": "Behemoth Reactor"
    },
    "BattlecruiserEnableSpecializations": {
        "build_time": 100,  # 43 -> 100 in 4.8.2
        "built_from": [ "FusionCore" ],
        "display_name": "Weapon Refit"
    },
    "LiberatorAGRangeUpgrade": {
        "build_time": 79,
        "built_from": [ "FusionCore" ],
        "display_name": "Advanced Ballistics"
    },
    "MedivacIncreaseSpeedBoost": {
        "build_time": 57,
        "built_from": [ "FusionCore" ],
        "display_name": "Rapid Reignition System",  # renamed in 4.7.1
        "race": "Terran",
        "type": "Upgrade",
        "is_morph": False
    },
    # protoss upgrades
    "ProtossGroundWeaponsLevel1": {
        "build_time": 129,
        "built_from": [ "Forge" ],
        "display_name": "Protoss Ground Weapons Level 1"
    },
    "ProtossGroundWeaponsLevel2": {
        "build_time": 154,
        "built_from": [ "Forge" ],
        "display_name": "Protoss Ground Weapons Level 2"
    },
    "ProtossGroundWeaponsLevel3": {
        "build_time": 179,
        "built_from": [ "Forge" ],
        "display_name": "Protoss Ground Weapons Level 3"
    },
    "ProtossGroundArmorsLevel1": {
        "build_time": 129,
        "built_from": [ "Forge" ],
        "display_name": "Protoss Ground Armor Level 1"
    },
    "ProtossGroundArmorsLevel2": {
        "build_time": 154,
        "built_from": [ "Forge" ],
        "display_name": "Protoss Ground Armor Level 2"
    },
    "ProtossGroundArmorsLevel3": {
        "build_time": 179,
        "built_from": [ "Forge" ],
        "display_name": "Protoss Ground Armor Level 3"
    },
    "ProtossShieldsLevel1": {
        "build_time": 129,
        "built_from": [ "Forge" ],
        "display_name": "Protoss Shields Level 1"
    },
    "ProtossShieldsLevel2": {
        "build_time": 154,
        "built_from": [ "Forge" ],
        "display_name": "Protoss Shields Level 2"
    },
    "ProtossShieldsLevel3": {
        "build_time": 179,
        "built_from": [ "Forge" ],
        "display_name": "Protoss Shields Level 3"
    },
    "ProtossAirWeaponsLevel1": {
        "build_time": 114,
        "built_from": [ "CyberneticsCore" ],
        "display_name": "Protoss Air Weapons Level 1"
    },
    "ProtossAirWeaponsLevel2": {
        "build_time": 136,
        "built_from": [ "CyberneticsCore" ],
        "display_name": "Protoss Air Weapons Level 2"
    },
    "ProtossAirWeaponsLevel3": {
        "build_time": 157,
        "built_from": [ "CyberneticsCore" ],
        "display_name": "Protoss Air Weapons Level 3"
    },
    "ProtossAirArmorsLevel1": {
        "build_time": 114,
        "built_from": [ "CyberneticsCore" ],
        "display_name": "Protoss Air Armor Level 1"
    },
    "ProtossAirArmorsLevel2": {
        "build_time": 136,
        "built_from": [ "CyberneticsCore" ],
        "display_name": "Protoss Air Armor Level 2"
    },
    "ProtossAirArmorsLevel3": {
        "build_time": 157,
        "built_from": [ "CyberneticsCore" ],
        "display_name": "Protoss Air Armor Level 3"
    },
    "WarpGateResearch": {
        "build_time": 100,  # 114s -> 100s in 4.8.2
        "built_from": [ "CyberneticsCore" ],
        "display_name": "Warp Gate"
    },
    "Charge": {
        "build_time": 100,
        "built_from": [ "TwilightCouncil" ],
        "display_name": "Charge"
    },
    "BlinkTech": {
        "build_time": 121,
        "built_from": [ "TwilightCouncil" ],
        "display_name": "Blink"
    },
    "AdeptShieldUpgrade": {  # deprecated from LotV Beta
        "build_time": 57,
        "built_from": [ "TwilightCouncil" ],
        "display_name": "Shield Upgrade"
    },
    "AdeptPiercingAttack": {
        "build_time": 100,
        "built_from": [ "TwilightCouncil" ],
        "display_name": "Resonating Glaives"
    },
    "ObserverGraviticBooster": {
        "build_time": 57,
        "built_from": [ "RoboticsBay" ],
        "display_name": "Gravitic Boosters"
    },
    "GraviticDrive": {
        "build_time": 57,
        "built_from": [ "RoboticsBay" ],
        "display_name": "Gravitic Drive"
    },
    "ExtendedThermalLance": {
        "build_time": 100,
        "built_from": [ "RoboticsBay" ],
        "display_name": "Extended Thermal Lance"
    },
    "PsiStormTech": {
        "build_time": 79,
        "built_from": [ "TemplarArchives" ],
        "display_name": "Psionic Storm"
    },
    # Fleet Beacon Upgrades
    "PhoenixRangeUpgrade": {
        "build_time": 64,
        "built_from": [ "FleetBeacon" ],
        "display_name": "Anion Pulse-Crystals"
    },
    "CarrierLaunchSpeedUpgrade": {  # deprecated in 4.7.1
        "build_time": 57,
        "built_from": [ "FleetBeacon" ],
        "display_name": "Graviton Catapult"
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
        "display_name": "Shadow Stride"
    },
    # unit change buildings
    "Lair": {
        "build_time": 57,
        "built_from": [ "Hatchery" ],
        "display_name": "Lair"
    },
    "Hive": {
        "build_time": 71,
        "built_from": [ "Lair" ],
        "display_name": "Hive"
    },
    "LurkerDenMP": {
        "build_time": 57,
        "built_from": [ "HydraliskDen" ],
        "display_name": "Lurker Den"
    },
    "GreaterSpire": {
        "build_time": 71,
        "built_from": [ "Spire" ],
        "display_name": "Greater Spire"
    },
    "OrbitalCommand": {
        "build_time": 25,
        "built_from": [ "CommandCenter" ],
        "display_name": "Orbital Command"
    },
    "PlanetaryFortress": {
        "build_time": 36,
        "built_from": [ "CommandCenter" ],
        "display_name": "Planetary Fortress"
    },
    # unofficial LotV Alpha only
    "HyperflightRotors": {
        "build_time": 93,
        "built_from": [ "TechLab" ],
        "display_name": "Hyperflight Rotors"
    },
    "FlyingLocusts": {
        "build_time": 87,
        "built_from": [ "InfestationPit" ],
        "display_name": "Flying Locusts"
    },
    "CycloneLockOnRangeUpgrade": {
        "build_time": 79,
        "built_from": [ "TechLab" ]
    },
    "CycloneAirUpgrade": {
        "build_time": 79,
        "built_from": [ "TechLab" ]
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
