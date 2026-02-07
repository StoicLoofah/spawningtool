"""
spawningtool.hots_constants
~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

FRAMES_PER_SECOND = 16

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
])

BO_CHANGED_EXCLUDED = set([
    'VikingAssault',  # various viking transforms
    'VikingFighter',
    'Viking',
    'WarpPrism',
    'WidowMine',  # burrowing
    'Zergling',  # generated when Banelings spawn
])

BO_UPGRADES_EXCLUDED = set()

BUILD_DATA = {
#terran units
    'SCV': {
        'build_time': 17,
        'built_from': ['Command Center',
            'Orbital Command'],
        'display_name': 'SCV',
        'race': 'Terran',
        'type': 'Unit',
        'is_morph': False
    },
    'Marine': {
        'build_time': 25,
        'built_from': ['Barracks'],
        'display_name': 'Marine',
        'race': 'Terran',
        'type': 'Unit',
        'is_morph': False
    },
    'Marauder': {
        'build_time': 30,
        'built_from': ['Barracks'],
        'display_name': 'Marauder',
        'race': 'Terran',
        'type': 'Unit',
        'is_morph': False
    },
    'Reaper': {
        'build_time': 40,
        'built_from': ['Barracks'],
        'display_name': 'Reaper',
        'race': 'Terran',
        'type': 'Unit',
        'is_morph': False
    },
    'Ghost': {
        'build_time': 40,
        'built_from': ['Barracks'],
        'display_name': 'Ghost',
        'race': 'Terran',
        'type': 'Unit',
        'is_morph': False
    },
    'BattleHellion': {
        'build_time': 30,
        'built_from': ['Factory'],
        'display_name': 'Hellbat',
        'race': 'Terran',
        'type': 'Unit',
        'is_morph': False
    },
    'Hellion': {
        'build_time': 30,
        'built_from': ['Factory'],
        'display_name': 'Hellion',
        'race': 'Terran',
        'type': 'Unit',
        'is_morph': False
    },
    'Hellbat': {
        'build_time': 30,
        'built_from': ['Factory'],
        'display_name': 'Hellbat',
        'race': 'Terran',
        'type': 'Unit',
        'is_morph': False
    },
    'WidowMine': {
        'build_time': 40,
        'built_from': ['Factory'],
        'display_name': 'Widow Mine',
        'race': 'Terran',
        'type': 'Unit',
        'is_morph': False
    },
    'SiegeTank': {
        'build_time': 45,
        'built_from': ['Factory'],
        'display_name': 'Siege Tank',
        'race': 'Terran',
        'type': 'Unit',
        'is_morph': False
    },
    'Thor': {
        'build_time': 60,
        'built_from': ['Factory'],
        'display_name': 'Thor',
        'race': 'Terran',
        'type': 'Unit',
        'is_morph': False
    },
    'Viking': {
        'build_time': 42,
        'built_from': ['Starport'],
        'display_name': 'Viking',
        'race': 'Terran',
        'type': 'Unit',
        'is_morph': False
    },
    'VikingFighter': {
        'build_time': 42, # all born as VikingFighters, but others in here for coverage
        'built_from': ['Starport'],
        'display_name': 'Viking',
        'race': 'Terran',
        'type': 'Unit',
        'is_morph': False
    },
    'VikingAssault': {
        'build_time': 42,
        'built_from': ['Starport'],
        'display_name': 'Viking',
        'race': 'Terran',
        'type': 'Unit',
        'is_morph': False
    },
    'Medivac': {
        'build_time': 42,
        'built_from': ['Starport'],
        'display_name': 'Medivac',
        'race': 'Terran',
        'type': 'Unit',
        'is_morph': False
    },
    'Raven': {
        'build_time': 60,
        'built_from': ['Starport'],
        'display_name': 'Raven',
        'race': 'Terran',
        'type': 'Unit',
        'is_morph': False
    },
    'Banshee': {
        'build_time': 60,
        'built_from': ['Starport'],
        'display_name': 'Banshee',
        'race': 'Terran',
        'type': 'Unit',
        'is_morph': False
    },
    'Battlecruiser': {
        'build_time': 90,
        'built_from': ['Starport'],
        'display_name': 'Battlecruiser',
        'race': 'Terran',
        'type': 'Unit',
        'is_morph': False
    },
    # protoss units
    'Probe': {
        'build_time': 17,
        'built_from': ['Nexus'],
        'display_name': 'Probe',
        'race': 'Protoss',
        'type': 'Unit',
        'is_morph': False
    },
    'Zealot': {
        'build_time': 38,
        'built_from': ['Gateway', 'WarpGate'], # warpgate is necessary because of changing types
        'display_name': 'Zealot',
        'race': 'Protoss',
        'type': 'Unit',
        'is_morph': False
    },
    'Stalker': {
        'build_time': 42,
        'built_from': ['Gateway',
            'WarpGate'],
        'display_name': 'Stalker',
        'race': 'Protoss',
        'type': 'Unit',
        'is_morph': False
    },
    'Sentry': {
        'build_time': 37,
        'built_from': ['Gateway',
            'WarpGate'],
        'display_name': 'Sentry',
        'race': 'Protoss',
        'type': 'Unit',
        'is_morph': False
    },
    'MothershipCore': {
        'build_time': 30,
        'built_from': ['Nexus'],
        'display_name': 'Mothership Core',
        'race': 'Protoss',
        'type': 'Unit',
        'is_morph': False
    },
    'HighTemplar': {
        'build_time': 55,
        'built_from': ['Gateway',
            'WarpGate'],
        'display_name': 'High Templar',
        'race': 'Protoss',
        'type': 'Unit',
        'is_morph': False
    },
    'DarkTemplar': {
        'build_time': 55,
        'built_from': ['Gateway',
            'WarpGate'],
        'display_name': 'Dark Templar',
        'race': 'Protoss',
        'type': 'Unit',
        'is_morph': False
    },
    'Immortal': {
        'build_time': 55,
        'built_from': ['RoboticsFacility'],
        'display_name': 'Immortal',
        'race': 'Protoss',
        'type': 'Unit',
        'is_morph': False
    },
    'Colossus': {
        'build_time': 75,
        'built_from': ['RoboticsFacility'],
        'display_name': 'Colossus',
        'race': 'Protoss',
        'type': 'Unit',
        'is_morph': False
    },
    'Archon': {
        'build_time': 12,
        'built_from': [],
        'display_name': 'Archon',
        'race': 'Protoss',
        'type': 'Unit',
        'is_morph': False
    },
    'Observer': {
        'build_time': 30,
        'built_from': ['RoboticsFacility'],
        'display_name': 'Observer',
        'race': 'Protoss',
        'type': 'Unit',
        'is_morph': False
    },
    'WarpPrism': {
        'build_time': 50,
        'built_from': ['RoboticsFacility'],
        'display_name': 'Warp Prism',
        'race': 'Protoss',
        'type': 'Unit',
        'is_morph': False
    },
    'Phoenix': {
        'build_time': 35,
        'built_from': ['Stargate'],
        'display_name': 'Phoenix',
        'race': 'Protoss',
        'type': 'Unit',
        'is_morph': False
    },
    'VoidRay': {
        'build_time': 60,
        'built_from': ['Stargate'],
        'display_name': 'Void Ray',
        'race': 'Protoss',
        'type': 'Unit',
        'is_morph': False
    },
    'Oracle': {
        'build_time': 50,
        'built_from': ['Stargate'],
        'display_name': 'Oracle',
        'race': 'Protoss',
        'type': 'Unit',
        'is_morph': False
    },
    'Tempest': {
        'build_time': 60,
        'built_from': ['Stargate'],
        'display_name': 'Tempest',
        'race': 'Protoss',
        'type': 'Unit',
        'is_morph': False
    },
    'Carrier': {
        'build_time': 120,
        'built_from': ['Stargate'],
        'display_name': 'Carrier',
        'race': 'Protoss',
        'type': 'Unit',
        'is_morph': False
    },
    # Zerg Units
    'Drone': {
        'build_time': 17,
        'built_from': [],
        'display_name': 'Drone',
        'race': 'Zerg',
        'type': 'Unit',
        'is_morph': False
    },
    'Queen': {
        'build_time': 50,
        'built_from': ['Hatchery', 'Lair', 'Hive'],
        'display_name': 'Queen',
        'race': 'Zerg',
        'type': 'Unit',
        'is_morph': False
    },
    'Zergling': {
        'build_time': 24,
        'built_from': [],
        'display_name': 'Zergling',
        'race': 'Zerg',
        'type': 'Unit',
        'is_morph': False
    },
    'Baneling': {
        'build_time': 20,
        'built_from': [],
        'display_name': 'Baneling',
        'race': 'Zerg',
        'type': 'Unit',
        'is_morph': True
    },
    'Roach': {
        'build_time': 27,
        'built_from': [],
        'display_name': 'Roach',
        'race': 'Zerg',
        'type': 'Unit',
        'is_morph': False
    },
    'Hydralisk': {
        'build_time': 33,
        'built_from': [],
        'display_name': 'Hydralisk',
        'race': 'Zerg',
        'type': 'Unit',
        'is_morph': False
    },
    'SwarmHost': {
        'build_time': 40,
        'built_from': [],
        'display_name': 'Swarm Host',
        'race': 'Zerg',
        'type': 'Unit',
        'is_morph': False
    },
    'Infestor': {
        'build_time': 50,
        'built_from': [],
        'display_name': 'Infestor',
        'race': 'Zerg',
        'type': 'Unit',
        'is_morph': False
    },
    'Ultralisk': {
        'build_time': 55,
        'built_from': [],
        'display_name': 'Ultralisk',
        'race': 'Zerg',
        'type': 'Unit',
        'is_morph': False
    },
    'NydusWorm': {
        'build_time': 20,
        'built_from': ['NydusCanal'],
        'display_name': 'Nydus Worm',
        'race': 'Zerg',
        'type': 'Building',
        'is_morph': False
    },
    'NydusCanal': {
        'build_time': 20,
        'built_from': [],
        'display_name': 'Nydus Canal',
        'race': 'Zerg',
        'type': 'Building',
        'is_morph': False
    },
    'Overlord': {
        'build_time': 25,
        'built_from': [],
        'display_name': 'Overlord',
        'race': 'Zerg',
        'type': 'Unit',
        'is_morph': False
    },
    'Mutalisk': {
        'build_time': 33,
        'built_from': [],
        'display_name': 'Mutalisk',
        'race': 'Zerg',
        'type': 'Unit',
        'is_morph': False
    },
    'Corruptor': {
        'build_time': 40,
        'built_from': [],
        'display_name': 'Corruptor',
        'race': 'Zerg',
        'type': 'Unit',
        'is_morph': False
    },
    'BroodLord': {
        'build_time': 34,
        'built_from': [],
        'display_name': 'Brood Lord',
        'race': 'Zerg',
        'type': 'Unit',
        'is_morph': True
    },
    'Viper': {
        'build_time': 40,
        'built_from': [],
        'display_name': 'Viper',
        'race': 'Zerg',
        'type': 'Unit',
        'is_morph': False
    },
    # Zerg Upgrades
    'ZergMeleeWeaponsLevel1': {
        'build_time': 160,
        'built_from': ['EvolutionChamber'],
        'display_name': 'Zerg Melee Weapons Level 1',
        'race': 'Zerg',
        'type': 'Upgrade',
        'is_morph': False
    },
    'ZergMeleeWeaponsLevel2': {
        'build_time': 190,
        'built_from': ['EvolutionChamber'],
        'display_name': 'Zerg Melee Weapons Level 2',
        'race': 'Zerg',
        'type': 'Upgrade',
        'is_morph': False
    },
    'ZergMeleeWeaponsLevel3': {
        'build_time': 220,
        'built_from': ['EvolutionChamber'],
        'display_name': 'Zerg Melee Weapons Level 3',
        'race': 'Zerg',
        'type': 'Upgrade',
        'is_morph': False
    },
    'ZergMissileWeaponsLevel1': {
        'build_time': 160,
        'built_from': ['EvolutionChamber'],
        'display_name': 'Zerg Missile Weapons Level 1',
        'race': 'Zerg',
        'type': 'Upgrade',
        'is_morph': False
    },
    'ZergMissileWeaponsLevel2': {
        'build_time': 190,
        'built_from': ['EvolutionChamber'],
        'display_name': 'Zerg Missile Weapons Level 2',
        'race': 'Zerg',
        'type': 'Upgrade',
        'is_morph': False
    },
    'ZergMissileWeaponsLevel3': {
        'build_time': 220,
        'built_from': ['EvolutionChamber'],
        'display_name': 'Zerg Missile Weapons Level 3',
        'race': 'Zerg',
        'type': 'Upgrade',
        'is_morph': False
    },
    'ZergGroundArmorsLevel1': {
        'build_time': 160,
        'built_from': ['EvolutionChamber'],
        'display_name': 'Zerg Ground Armor Level 1',
        'race': 'Zerg',
        'type': 'Upgrade',
        'is_morph': False
    },
    'ZergGroundArmorsLevel2': {
        'build_time': 190,
        'built_from': ['EvolutionChamber'],
        'display_name': 'Zerg Ground Armor Level 2',
        'race': 'Zerg',
        'type': 'Upgrade',
        'is_morph': False
    },
    'ZergGroundArmorsLevel3': {
        'build_time': 220,
        'built_from': ['EvolutionChamber'],
        'display_name': 'Zerg Ground Armor Level 3',
        'race': 'Zerg',
        'type': 'Upgrade',
        'is_morph': False
    },
    'ZergFlyerWeaponsLevel1': {
        'build_time': 160,
        'built_from': ['Spire', 'GreaterSpire'],
        'display_name': 'Zerg Flyer Weapons Level 1',
        'race': 'Zerg',
        'type': 'Upgrade',
        'is_morph': False
    },
    'ZergFlyerWeaponsLevel2': {
        'build_time': 190,
        'built_from': ['Spire', 'GreaterSpire'],
        'display_name': 'Zerg Flyer Weapons Level 2',
        'race': 'Zerg',
        'type': 'Upgrade',
        'is_morph': False
    },
    'ZergFlyerWeaponsLevel3': {
        'build_time': 220,
        'built_from': ['Spire', 'GreaterSpire'],
        'display_name': 'Zerg Flyer Weapons Level 3',
        'race': 'Zerg',
        'type': 'Upgrade',
        'is_morph': False
    },
    'ZergFlyerArmorsLevel1': {
        'build_time': 160,
        'built_from': ['Spire', 'GreaterSpire'],
        'display_name': 'Zerg Flyer Armor Level 1',
        'race': 'Zerg',
        'type': 'Upgrade',
        'is_morph': False
    },
    'ZergFlyerArmorsLevel2': {
        'build_time': 190,
        'built_from': ['Spire', 'GreaterSpire'],
        'display_name': 'Zerg Flyer Armor Level 2',
        'race': 'Zerg',
        'type': 'Upgrade',
        'is_morph': False
    },
    'ZergFlyerArmorsLevel3': {
        'build_time': 220,
        'built_from': ['Spire', 'GreaterSpire'],
        'display_name': 'Zerg Flyer Armor Level 3',
        'race': 'Zerg',
        'type': 'Upgrade',
        'is_morph': False
    },
    'zerglingmovementspeed': {
        'build_time': 110,
        'built_from': ['SpawningPool'],
        'display_name': 'Metabolic Boost',
        'race': 'Zerg',
        'type': 'Upgrade',
        'is_morph': False
    },
    'zerglingattackspeed': {
        'build_time': 130,
        'built_from': ['SpawningPool'],
        'display_name': 'Adrenal Glands',
        'race': 'Zerg',
        'type': 'Upgrade',
        'is_morph': False
    },
    'CentrificalHooks': {
        'build_time': 110,
        'built_from': ['BanelingNest'],
        'display_name': 'Centrifugal Hooks',
        'race': 'Zerg',
        'type': 'Upgrade',
        'is_morph': False
    },
    'GlialReconstitution': {
        'build_time': 110,
        'built_from': ['RoachWarren'],
        'display_name': 'Glial Reconstitution',
        'race': 'Zerg',
        'type': 'Upgrade',
        'is_morph': False
    },
    'TunnelingClaws': {
        'build_time': 110,
        'built_from': ['RoachWarren'],
        'display_name': 'Tunneling Claws',
        'race': 'Zerg',
        'type': 'Upgrade',
        'is_morph': False
    },
    'hydraliskspeed': {
        'build_time': 80,
        'built_from': ['HydraliskDen'],
        'display_name': 'Grooved Spines',
        'race': 'Zerg',
        'type': 'Upgrade',
        'is_morph': False
    },
    'HydraliskSpeedUpgrade': {
        'build_time': 100,
        'built_from': ['HydraliskDen'],
        'display_name': 'Muscular Augments',
        'race': 'Zerg',
        'type': 'Upgrade',
        'is_morph': False
    },
    'overlordspeed': {
        'build_time': 60,
        'built_from': ['Hatchery', 'Lair', 'Hive'],
        'display_name': 'Pneumatized Carapace',
        'race': 'Zerg',
        'type': 'Upgrade',
        'is_morph': False
    },
    'overlordtransport': {
        'build_time': 130,
        'built_from': ['Hatchery', 'Lair', 'Hive'],
        'display_name': 'Ventral Sacs',
        'race': 'Zerg',
        'type': 'Upgrade',
        'is_morph': False
    },
    'Burrow': {
        'build_time': 100,
        'built_from': ['Hatchery', 'Lair', 'Hive'],
        'display_name': 'Burrow',
        'race': 'Zerg',
        'type': 'Upgrade',
        'is_morph': False
    },
    'InfestorEnergyUpgrade': {
        'build_time': 80,
        'built_from': ['InfestationPit'],
        'display_name': 'Pathogen Glands',
        'race': 'Zerg',
        'type': 'Upgrade',
        'is_morph': False
    },
    'ChitinousPlating': {
        'build_time': 110,
        'built_from': ['UltraliskCavern'],
        'display_name': 'Chitinous Plating',
        'race': 'Zerg',
        'type': 'Upgrade',
        'is_morph': False
    },
    'LocustLifetimeIncrease': {
        'build_time': 120,
        'built_from': ['InfestationPit'],
        'display_name': 'Enduring Locusts',
        'race': 'Zerg',
        'type': 'Upgrade',
        'is_morph': False
    },
    'NeuralParasite': {
        'build_time': 110,
        'built_from': ['InfestationPit'],
        'display_name': 'Neural Parasite',
        'race': 'Zerg',
        'type': 'Upgrade',
        'is_morph': False
    },
    # Terran Upgrades
    'TerranInfantryWeaponsLevel1': {
        'build_time': 160,
        'built_from': ['EngineeringBay'],
        'display_name': 'Terran Infantry Weapons Level 1',
        'race': 'Terran',
        'type': 'Upgrade',
        'is_morph': False
    },
    'TerranInfantryWeaponsLevel2': {
        'build_time': 190,
        'built_from': ['EngineeringBay'],
        'display_name': 'Terran Infantry Weapons Level 2',
        'race': 'Terran',
        'type': 'Upgrade',
        'is_morph': False
    },
    'TerranInfantryWeaponsLevel3': {
        'build_time': 220,
        'built_from': ['EngineeringBay'],
        'display_name': 'Terran Infantry Weapons Level 3',
        'race': 'Terran',
        'type': 'Upgrade',
        'is_morph': False
    },
    'TerranInfantryArmorsLevel1': {
        'build_time': 160,
        'built_from': ['EngineeringBay'],
        'display_name': 'Terran Infantry Armor Level 1',
        'race': 'Terran',
        'type': 'Upgrade',
        'is_morph': False
    },
    'TerranInfantryArmorsLevel2': {
        'build_time': 190,
        'built_from': ['EngineeringBay'],
        'display_name': 'Terran Infantry Armor Level 2',
        'race': 'Terran',
        'type': 'Upgrade',
        'is_morph': False
    },
    'TerranInfantryArmorsLevel3': {
        'build_time': 220,
        'built_from': ['EngineeringBay'],
        'display_name': 'Terran Infantry Armor Level 3',
        'race': 'Terran',
        'type': 'Upgrade',
        'is_morph': False
    },
    'TerranVehicleWeaponsLevel1': {
        'build_time': 160,
        'built_from': ['Armory'],
        'display_name': 'Terran Vehicle Weapons Level 1',
        'race': 'Terran',
        'type': 'Upgrade',
        'is_morph': False
    },
    'TerranVehicleWeaponsLevel2': {
        'build_time': 190,
        'built_from': ['Armory'],
        'display_name': 'Terran Vehicle Weapons Level 2',
        'race': 'Terran',
        'type': 'Upgrade',
        'is_morph': False
    },
    'TerranVehicleWeaponsLevel3': {
        'build_time': 220,
        'built_from': ['Armory'],
        'display_name': 'Terran Vehicle Weapons Level 3',
        'race': 'Terran',
        'type': 'Upgrade',
        'is_morph': False
    },
    'TerranVehicleArmorsLevel1': {
        'build_time': 160,
        'built_from': ['Armory'],
        'display_name': 'Terran Vehicle Armor Level 1',
        'race': 'Terran',
        'type': 'Upgrade',
        'is_morph': False
    },
    'TerranVehicleArmorsLevel2': {
        'build_time': 190,
        'built_from': ['Armory'],
        'display_name': 'Terran Vehicle Armor Level 2',
        'race': 'Terran',
        'type': 'Upgrade',
        'is_morph': False
    },
    'TerranVehicleArmorsLevel3': {
        'build_time': 220,
        'built_from': ['Armory'],
        'display_name': 'Terran Vehicle Armor Level 3',
        'race': 'Terran',
        'type': 'Upgrade',
        'is_morph': False
    },
    'TerranShipWeaponsLevel1': {
        'build_time': 160,
        'built_from': ['Armory'],
        'display_name': 'Terran Ship Weapons Level 1',
        'race': 'Terran',
        'type': 'Upgrade',
        'is_morph': False
    },
    'TerranShipWeaponsLevel2': {
        'build_time': 190,
        'built_from': ['Armory'],
        'display_name': 'Terran Ship Weapons Level 2',
        'race': 'Terran',
        'type': 'Upgrade',
        'is_morph': False
    },
    'TerranShipWeaponsLevel3': {
        'build_time': 220,
        'built_from': ['Armory'],
        'display_name': 'Terran Ship Weapons Level 3',
        'race': 'Terran',
        'type': 'Upgrade',
        'is_morph': False
    },
    'TerranShipArmorsLevel1': {
        'build_time': 160,
        'built_from': ['Armory'],
        'display_name': 'Terran Ship Armor Level 1',
        'race': 'Terran',
        'type': 'Upgrade',
        'is_morph': False
    },
    'TerranShipArmorsLevel2': {
        'build_time': 190,
        'built_from': ['Armory'],
        'display_name': 'Terran Ship Armor Level 2',
        'race': 'Terran',
        'type': 'Upgrade',
        'is_morph': False
    },
    'TerranShipArmorsLevel3': {
        'build_time': 220,
        'built_from': ['Armory'],
        'display_name': 'Terran Ship Armor Level 3',
        'race': 'Terran',
        'type': 'Upgrade',
        'is_morph': False
    },
    'TerranVehicleAndShipWeaponsLevel1': {
        'build_time': 160,
        'built_from': ['Armory'],
        'display_name': 'Terran Vehicle and Ship Weapons Level 1',
        'race': 'Terran',
        'type': 'Upgrade',
        'is_morph': False
    },
    'TerranVehicleAndShipWeaponsLevel2': {
        'build_time': 190,
        'built_from': ['Armory'],
        'display_name': 'Terran Vehicle and Ship Weapons Level 2',
        'race': 'Terran',
        'type': 'Upgrade',
        'is_morph': False
    },
    'TerranVehicleAndShipWeaponsLevel3': {
        'build_time': 220,
        'built_from': ['Armory'],
        'display_name': 'Terran Vehicle and Ship Weapons Level 3',
        'race': 'Terran',
        'type': 'Upgrade',
        'is_morph': False
    },
    'TerranVehicleAndShipArmorsLevel1': {
        'build_time': 160,
        'built_from': ['Armory'],
        'display_name': 'Terran Vehicle And Ship Armor Level 1',
        'race': 'Terran',
        'type': 'Upgrade',
        'is_morph': False
    },
    'TerranVehicleAndShipArmorsLevel2': {
        'build_time': 190,
        'built_from': ['Armory'],
        'display_name': 'Terran Vehicle And Ship Armor Level 2',
        'race': 'Terran',
        'type': 'Upgrade',
        'is_morph': False
    },
    'TerranVehicleAndShipArmorsLevel3': {
        'build_time': 220,
        'built_from': ['Armory'],
        'display_name': 'Terran Vehicle And Ship Armor Level 3',
        'race': 'Terran',
        'type': 'Upgrade',
        'is_morph': False
    },
    'HighCapacityBarrels': {
        'build_time': 110,
        'built_from': ['TechLab'],
        'display_name': 'Infernal Pre-Igniter',
        'race': 'Terran',
        'type': 'Upgrade',
        'is_morph': False
    },
    'Stimpack': {
        'build_time': 170,
        'built_from': ['TechLab'],
        'display_name': 'Stimpack',
        'race': 'Terran',
        'type': 'Upgrade',
        'is_morph': False
    },
    'PunisherGrenades': {
        'build_time': 60,
        'built_from': ['TechLab'],
        'display_name': 'Concussive Shells',
        'race': 'Terran',
        'type': 'Upgrade',
        'is_morph': False
    },
    'ShieldWall': {
        'build_time': 110,
        'built_from': ['TechLab'],
        'display_name': 'Combat Shields',
        'race': 'Terran',
        'type': 'Upgrade',
        'is_morph': False
    },
    'MedivacCaduceusReactor': {
        'build_time': 80,
        'built_from': ['TechLab'],
        'display_name': 'Caduceus Reactor',
        'race': 'Terran',
        'type': 'Upgrade',
        'is_morph': False
    },
    'PersonalCloaking': {
        'build_time': 120,
        'built_from': ['TechLab'],
        'display_name': 'Personal Cloaking',
        'race': 'Terran',
        'type': 'Upgrade',
        'is_morph': False
    },
    'GhostMoebiusReactor': {
        'build_time': 80,
        'built_from': ['TechLab'],
        'display_name': 'Moebius Reactor',
        'race': 'Terran',
        'type': 'Upgrade',
        'is_morph': False
    },
    'NeosteelFrame': {
        'build_time': 110,
        'built_from': ['EngineeringBay'],
        'display_name': 'Neosteel Frame',
        'race': 'Terran',
        'type': 'Upgrade',
        'is_morph': False
    },
    'HiSecAutoTracking': {
        'build_time': 80,
        'built_from': ['EngineeringBay'],
        'display_name': 'Hi-Sec Auto Tracking',
        'race': 'Terran',
        'type': 'Upgrade',
        'is_morph': False
    },
    'TerranBuildingArmor': {
        'build_time': 140,
        'built_from': ['EngineeringBay'],
        'display_name': 'Neosteel Armor',
        'race': 'Terran',
        'type': 'Upgrade',
        'is_morph': False
    },
    'BansheeCloak': {
        'build_time': 110,
        'built_from': ['TechLab'],
        'display_name': 'Cloaking Field',
        'race': 'Terran',
        'type': 'Upgrade',
        'is_morph': False
    },
    'DurableMaterials': {
        'build_time': 110,
        'built_from': ['TechLab'],
        'display_name': 'Durable Materials',
        'race': 'Terran',
        'type': 'Upgrade',
        'is_morph': False
    },
    'RavenCorvidReactor': {
        'build_time': 110,
        'built_from': ['TechLab'],
        'display_name': 'Corvid Reactor',
        'race': 'Terran',
        'type': 'Upgrade',
        'is_morph': False
    },
    'StrikeCannons': {
        'build_time': 110,
        'built_from': ['TechLab'],
        'display_name': '250mm Strike Cannons',
        'race': 'Terran',
        'type': 'Upgrade',
        'is_morph': False
    },
    'DrillClaws': {
        'build_time': 110,
        'built_from': ['TechLab'],
        'display_name': 'Drilling Claws',
        'race': 'Terran',
        'type': 'Upgrade',
        'is_morph': False
    },
    'TransformationServos': {
        'build_time': 110,
        'built_from': ['TechLab'],
        'display_name': 'Transformation Servos',
        'race': 'Terran',
        'type': 'Upgrade',
        'is_morph': False
    },
    'BattlecruiserBehemothReactor': {
        'build_time': 80,
        'built_from': ['FusionCore'],
        'display_name': 'Behemoth Reactor',
        'race': 'Terran',
        'type': 'Upgrade',
        'is_morph': False
    },
    'BattlecruiserEnableSpecializations': {
        'build_time': 60,
        'built_from': ['FusionCore'],
        'display_name': 'Weapon Refit',
        'race': 'Terran',
        'type': 'Upgrade',
        'is_morph': False
    },
    # Protoss Upgrades
    'ProtossGroundWeaponsLevel1': {
        'build_time': 160,
        'built_from': ['Forge'],
        'display_name': 'Protoss Ground Weapons Level 1',
        'race': 'Protoss',
        'type': 'Upgrade',
        'is_morph': False
    },
    'ProtossGroundWeaponsLevel2': {
        'build_time': 190,
        'built_from': ['Forge'],
        'display_name': 'Protoss Ground Weapons Level 2',
        'race': 'Protoss',
        'type': 'Upgrade',
        'is_morph': False
    },
    'ProtossGroundWeaponsLevel3': {
        'build_time': 220,
        'built_from': ['Forge'],
        'display_name': 'Protoss Ground Weapons Level 3',
        'race': 'Protoss',
        'type': 'Upgrade',
        'is_morph': False
    },
    'ProtossGroundArmorsLevel1': {
        'build_time': 160,
        'built_from': ['Forge'],
        'display_name': 'Protoss Ground Armor Level 1',
        'race': 'Protoss',
        'type': 'Upgrade',
        'is_morph': False
    },
    'ProtossGroundArmorsLevel2': {
        'build_time': 190,
        'built_from': ['Forge'],
        'display_name': 'Protoss Ground Armor Level 2',
        'race': 'Protoss',
        'type': 'Upgrade',
        'is_morph': False
    },
    'ProtossGroundArmorsLevel3': {
        'build_time': 220,
        'built_from': ['Forge'],
        'display_name': 'Protoss Ground Armor Level 3',
        'race': 'Protoss',
        'type': 'Upgrade',
        'is_morph': False
    },
    'ProtossShieldsLevel1': {
        'build_time': 160,
        'built_from': ['Forge'],
        'display_name': 'Protoss Shields Level 1',
        'race': 'Protoss',
        'type': 'Upgrade',
        'is_morph': False
    },
    'ProtossShieldsLevel2': {
        'build_time': 190,
        'built_from': ['Forge'],
        'display_name': 'Protoss Shields Level 2',
        'race': 'Protoss',
        'type': 'Upgrade',
        'is_morph': False
    },
    'ProtossShieldsLevel3': {
        'build_time': 220,
        'built_from': ['Forge'],
        'display_name': 'Protoss Shields Level 3',
        'race': 'Protoss',
        'type': 'Upgrade',
        'is_morph': False
    },
    'ProtossAirWeaponsLevel1': {
        'build_time': 160,
        'built_from': ['CyberneticsCore'],
        'display_name': 'Protoss Air Weapons Level 1',
        'race': 'Protoss',
        'type': 'Upgrade',
        'is_morph': False
    },
    'ProtossAirWeaponsLevel2': {
        'build_time': 190,
        'built_from': ['CyberneticsCore'],
        'display_name': 'Protoss Air Weapons Level 2',
        'race': 'Protoss',
        'type': 'Upgrade',
        'is_morph': False
    },
    'ProtossAirWeaponsLevel3': {
        'build_time': 220,
        'built_from': ['CyberneticsCore'],
        'display_name': 'Protoss Air Weapons Level 3',
        'race': 'Protoss',
        'type': 'Upgrade',
        'is_morph': False
    },
    'ProtossAirArmorsLevel1': {
        'build_time': 160,
        'built_from': ['CyberneticsCore'],
        'display_name': 'Protoss Air Armor Level 1',
        'race': 'Protoss',
        'type': 'Upgrade',
        'is_morph': False
    },
    'ProtossAirArmorsLevel2': {
        'build_time': 190,
        'built_from': ['CyberneticsCore'],
        'display_name': 'Protoss Air Armor Level 2',
        'race': 'Protoss',
        'type': 'Upgrade',
        'is_morph': False
    },
    'ProtossAirArmorsLevel3': {
        'build_time': 220,
        'built_from': ['CyberneticsCore'],
        'display_name': 'Protoss Air Armor Level 3',
        'race': 'Protoss',
        'type': 'Upgrade',
        'is_morph': False
    },
    'WarpGateResearch': {
        'build_time': 160,
        'built_from': ['CyberneticsCore'],
        'display_name': 'Warp Gate',
        'race': 'Protoss',
        'type': 'Upgrade',
        'is_morph': False
    },
    'BlinkTech': {
        'build_time': 170,
        'built_from': ['TwilightCouncil'],
        'display_name': 'Blink',
        'race': 'Protoss',
        'type': 'Upgrade',
        'is_morph': False
    },
    'ObserverGraviticBooster': {
        'build_time': 80,
        'built_from': ['RoboticsBay'],
        'display_name': 'Gravitic Boosters',
        'race': 'Protoss',
        'type': 'Upgrade',
        'is_morph': False
    },
    'GraviticDrive': {
        'build_time': 80,
        'built_from': ['RoboticsBay'],
        'display_name': 'Gravitic Drive',
        'race': 'Protoss',
        'type': 'Upgrade',
        'is_morph': False
    },
    'ExtendedThermalLance': {
        'build_time': 140,
        'built_from': ['RoboticsBay'],
        'display_name': 'Extended Thermal Lance',
        'race': 'Protoss',
        'type': 'Upgrade',
        'is_morph': False
    },
    'Charge': {
        'build_time': 140,
        'built_from': ['TwilightCouncil'],
        'display_name': 'Charge',
        'race': 'Protoss',
        'type': 'Upgrade',
        'is_morph': False
    },
    'PsiStormTech': {
        'build_time': 110,
        'built_from': ['TemplarArchives'],
        'display_name': 'Psionic Storm',
        'race': 'Protoss',
        'type': 'Upgrade',
        'is_morph': False
    },
    'PhoenixRangeUpgrade': {
        'build_time': 90,
        'built_from': ['FleetBeacon'],
        'display_name': 'Anion Pulse-Crystals',
        'race': 'Protoss',
        'type': 'Upgrade',
        'is_morph': False
    },
    'CarrierLaunchSpeedUpgrade': {
        'build_time': 80,
        'built_from': ['FleetBeacon'],
        'display_name': 'Graviton Catapult',
        'race': 'Protoss',
        'type': 'Upgrade',
        'is_morph': False
    },
    # Unit Change Building
    'Lair': {
        'build_time': 80,
        'built_from': ['Hatchery'],
        'display_name': 'Lair',
        'race': 'Zerg',
        'type': 'Building',
        'is_morph': True
    },
    'Hive': {
        'build_time': 100,
        'built_from': ['Lair'],
        'display_name': 'Hive',
        'race': 'Zerg',
        'type': 'Building',
        'is_morph': True
    },
    'GreaterSpire': {
        'build_time': 100,
        'built_from': ['Spire'],
        'display_name': 'Greater Spire',
        'race': 'Zerg',
        'type': 'Building',
        'is_morph': True
    },
    'OrbitalCommand': {
        'build_time': 35,
        'built_from': ['CommandCenter'],
        'display_name': 'Orbital Command',
        'race': 'Terran',
        'type': 'Building',
        'is_morph': True
    },
    'PlanetaryFortress': {
        'build_time': 50,
        'built_from': ['CommandCenter'],
        'display_name': 'Planetary Fortress',
        'race': 'Terran',
        'type': 'Building',
        'is_morph': True
    },
    'Overseer': {
        'build_time': 17,
        'built_from': ['Overlord'],
        'display_name': 'Overseer',
        'race': 'Zerg',
        'type': 'Building',
        'is_morph': True
    },
    'HERC': {
        'build_time': 40,
        'built_from': ['Barracks'
        ]
    },
    'Cyclone': {
        'build_time': 45,
        'built_from': ['Factory'],
        'display_name': 'Cyclone',
        'race': 'Terran',
        'type': 'Unit',
        'is_morph': False
    },
    'ARCGun': {
        'build_time': 30,
        'built_from': ['TechLab'
        ]
    },
    'TargetingOptics': {
        'build_time': 110,
        'built_from': ['TechLab'
        ]
    },
    'HyperflightRotors': {
        'build_time': 130,
        'built_from': ['TechLab'],
        'display_name': 'Hyperflight Rotors',
        'race': 'Terran',
        'type': 'Upgrade',
        'is_morph': False
    },
    'PlogisterEgg': {
        'build_time': 0,
        'built_from': ['Roach'
        ]
    },
    'LurkerMPEgg': {
        'build_time': 0,
        'built_from': ['Hydralisk'],
        'display_name': 'Lurker',
        'race': 'Zerg',
        'type': 'Building',
        'is_morph': True
    },
    'LurkerDenMP': {
        'build_time': 100,
        'built_from': [],
        'display_name': 'Lurker Den',
        'race': 'Zerg',
        'type': 'Building',
        'is_morph': True
    },
    'SeismicSpines': {
        'build_time': 100,
        'built_from': ['HydraliskDen'],
        'race': 'Zerg',
        'type': 'Upgrade',
        'is_morph': True
    },
    'FlyingLocusts': {
        'build_time': 120,
        'built_from': ['InfestationPit'],
        'display_name': 'Flying Locusts',
        'race': 'Zerg',
        'type': 'Upgrade',
        'is_morph': False
    },
    'Disruptor': {
        'build_time': 60,
        'built_from': ['RoboticsFacility'],
        'display_name': 'Disruptor',
        'race': 'Protoss',
        'type': 'Unit',
        'is_morph': False
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
    'MassRecallMothership',
    'MothershipMassRecall',
    'MothershipCorePurifyNexus',
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
    'QueenTransfusion',
    'YamatoGun',
    'Abduct',
    'TemporalField',
    'Envision',
    # LotV Alpha - not worried about these for now
    # 'Grapple',
    # 'LockOn',
    # 'EmergencyRepair',
    # 'TacticalJump',
    # 'CorrosiveBile',
    # 'AggressiveMutation',
    # 'CausticSpray',
    # 'PurificationNova',
    # 'StasisWard',
    # 'Barrier',
    # 'Disintegration',
    # 'ReleaseInterceptors',
    ])
