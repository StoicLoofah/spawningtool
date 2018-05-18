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
    # terran units
    'SCV': {
        'build_time': 17,
        'built_from': ['Command Center', 'Orbital Command'],
        },
    'Marine': {
        'build_time': 25,
        'built_from': ['Barracks'],
        },
    'Marauder': {
        'build_time': 30,
        'built_from': ['Barracks'],
        },
    'Reaper': {
        'build_time': 40,
        'built_from': ['Barracks'],
        },
    'Ghost': {
        'build_time': 40,
        'built_from': ['Barracks'],
        },
    'BattleHellion': {
        'build_time': 30,
        'built_from': ['Factory'],
        'display_name': 'Hellbat',
        },
    'Hellion': {
        'build_time': 30,
        'built_from': ['Factory'],
        },
    'Hellbat': {
        'build_time': 30,
        'built_from': ['Factory'],
        },
    'WidowMine': {
        'build_time': 40,
        'built_from': ['Factory'],
        },
    'SiegeTank': {
        'build_time': 45,
        'built_from': ['Factory'],
        },
    'Thor': {
        'build_time': 60,
        'built_from': ['Factory'],
        },
    'Viking': {
        'build_time': 42,
        'built_from': ['Starport'],
        },
    'VikingFighter': {
        'build_time': 42,  # all born as VikingFighters, but others in here for coverage
        'built_from': ['Starport'],
        },
    'VikingAssault': {
        'build_time': 42,
        'built_from': ['Starport'],
        },
    'Medivac': {
        'build_time': 42,
        'built_from': ['Starport'],
        },
    'Raven': {
        'build_time': 60,
        'built_from': ['Starport'],
        },
    'Banshee': {
        'build_time': 60,
        'built_from': ['Starport'],
        },
    'Battlecruiser': {
        'build_time': 90,
        'built_from': ['Starport'],
        },
    # protoss units
    'Probe': {
        'build_time': 17,
        'built_from': ['Nexus'],
        },
    'Zealot': {
        'build_time': 38,
        'built_from': ['Gateway', 'WarpGate'],  # warpgate is necessary because of changing types
        },
    'Stalker': {
        'build_time': 42,
        'built_from': ['Gateway', 'WarpGate'],
        },
    'Sentry': {
        'build_time': 37,
        'built_from': ['Gateway', 'WarpGate'],
        },
    'MothershipCore': {
        'build_time': 30,
        'built_from': ['Nexus'],
        },
    'HighTemplar': {
        'build_time': 55,
        'built_from': ['Gateway', 'WarpGate'],
        },
    'DarkTemplar': {
        'build_time': 55,
        'built_from': ['Gateway', 'WarpGate'],
        },
    'Immortal': {
        'build_time': 55,
        'built_from': ['RoboticsFacility'],
        },
    'Colossus': {
        'build_time': 75,
        'built_from': ['RoboticsFacility'],
        },
    'Archon': {
        'build_time': 12,
        'built_from': [],
        },
    'Observer': {
        'build_time': 30,
        'built_from': ['RoboticsFacility'],
        },
    'WarpPrism': {
        'build_time': 50,
        'built_from': ['RoboticsFacility'],
        },
    'Phoenix': {
        'build_time': 35,
        'built_from': ['Stargate'],
        },
    'VoidRay': {
        'build_time': 60,
        'built_from': ['Stargate'],
        },
    'Oracle': {
        'build_time': 50,
        'built_from': ['Stargate'],
        },
    'Tempest': {
        'build_time': 60,
        'built_from': ['Stargate'],
        },
    'Carrier': {
        'build_time': 120,
        'built_from': ['Stargate'],
        },
    # zerg units
    'Drone': {
        'build_time': 17,
        'built_from': [],
        },
    'Queen': {
        'build_time': 50,
        'built_from': ['Hatchery', 'Lair', 'Hive'],
        },
    'Zergling': {
        'build_time': 24,
        'built_from': [],
        },
    'Baneling': {
        'build_time': 20,
        'built_from': [],
        },
    'Roach': {
        'build_time': 27,
        'built_from': [],
        },
    'Hydralisk': {
        'build_time': 33,
        'built_from': [],
        },
    'SwarmHost': {
        'build_time': 40,
        'built_from': [],
        },
    'Infestor': {
        'build_time': 50,
        'built_from': [],
        },
    'Ultralisk': {
        'build_time': 55,
        'built_from': [],
        },
    'NydusWorm': {
        'build_time': 20,
        'built_from': ['NydusCanal'],
        },
    'NydusCanal': {
        'build_time': 20,
        'built_from': [],
        },
    'Overlord': {
        'build_time': 25,
        'built_from': [],
        },
    'Mutalisk': {
        'build_time': 33,
        'built_from': [],
        },
    'Corruptor': {
        'build_time': 40,
        'built_from': [],
        },
    'BroodLord': {
        'build_time': 34,
        'built_from': [],
        },
    'Viper': {
        'build_time': 40,
        'built_from': [],
        },
    # zerg upgrades
    'ZergMeleeWeaponsLevel1': {
        'build_time': 160,
        'built_from': ['EvolutionChamber'],
        },
    'ZergMeleeWeaponsLevel2': {
        'build_time': 190,
        'built_from': ['EvolutionChamber'],
        },
    'ZergMeleeWeaponsLevel3': {
        'build_time': 220,
        'built_from': ['EvolutionChamber'],
        },
    'ZergMissileWeaponsLevel1': {
        'build_time': 160,
        'built_from': ['EvolutionChamber'],
        },
    'ZergMissileWeaponsLevel2': {
        'build_time': 190,
        'built_from': ['EvolutionChamber'],
        },
    'ZergMissileWeaponsLevel3': {
        'build_time': 220,
        'built_from': ['EvolutionChamber'],
        },
    'ZergGroundArmorsLevel1': {
        'build_time': 160,
        'built_from': ['EvolutionChamber'],
        },
    'ZergGroundArmorsLevel2': {
        'build_time': 190,
        'built_from': ['EvolutionChamber'],
        },
    'ZergGroundArmorsLevel3': {
        'build_time': 220,
        'built_from': ['EvolutionChamber'],
        },
    'ZergFlyerWeaponsLevel1': {
        'build_time': 160,
        'built_from': ['Spire', 'GreaterSpire'],
        },
    'ZergFlyerWeaponsLevel2': {
        'build_time': 190,
        'built_from': ['Spire', 'GreaterSpire'],
        },
    'ZergFlyerWeaponsLevel3': {
        'build_time': 220,
        'built_from': ['Spire', 'GreaterSpire'],
        },
    'ZergFlyerArmorsLevel1': {
        'build_time': 160,
        'built_from': ['Spire', 'GreaterSpire'],
        },
    'ZergFlyerArmorsLevel2': {
        'build_time': 190,
        'built_from': ['Spire', 'GreaterSpire'],
        },
    'ZergFlyerArmorsLevel3': {
        'build_time': 220,
        'built_from': ['Spire', 'GreaterSpire'],
        },
    'zerglingmovementspeed': {
        'build_time': 110,
        'built_from': ['SpawningPool'],
        },
    'zerglingattackspeed': {
        'build_time': 130,
        'built_from': ['SpawningPool'],
        },
    'CentrificalHooks': {
        'build_time': 110,
        'built_from': ['BanelingNest'],
        },
    'GlialReconstitution': {
        'build_time': 110,
        'built_from': ['RoachWarren'],
        },
    'TunnelingClaws': {
        'build_time': 110,
        'built_from': ['RoachWarren'],
        },
    'hydraliskspeed': {
        'build_time': 80,
        'built_from': ['HydraliskDen'],
        'display_name': 'Grooved Spines',
        },
    'HydraliskSpeedUpgrade': {
        'build_time': 100,
        'built_from': ['HydraliskDen'],
        'display_name': 'Muscular Augments',
        },
    'overlordspeed': {
        'build_time': 60,
        'built_from': ['Hatchery', 'Lair', 'Hive'],
        },
    'overlordtransport': {
        'build_time': 130,
        'built_from': ['Hatchery', 'Lair', 'Hive'],
        },
    'Burrow': {
        'build_time': 100,
        'built_from': ['Hatchery', 'Lair', 'Hive'],
        },
    'InfestorEnergyUpgrade': {
        'build_time': 80,
        'built_from': ['InfestationPit'],
        },
    'ChitinousPlating': {
        'build_time': 110,
        'built_from': ['UltraliskCavern'],
        },
    'LocustLifetimeIncrease': {
        'build_time': 120,
        'built_from': ['InfestationPit'],
        },
    'NeuralParasite': {
        'build_time': 110,
        'built_from': ['InfestationPit'],
        },
    # terran upgrades
    'TerranInfantryWeaponsLevel1': {
        'build_time': 160,
        'built_from': ['EngineeringBay'],
        },
    'TerranInfantryWeaponsLevel2': {
        'build_time': 190,
        'built_from': ['EngineeringBay'],
        },
    'TerranInfantryWeaponsLevel3': {
        'build_time': 220,
        'built_from': ['EngineeringBay'],
        },
    'TerranInfantryArmorsLevel1': {
        'build_time': 160,
        'built_from': ['EngineeringBay'],
        },
    'TerranInfantryArmorsLevel2': {
        'build_time': 190,
        'built_from': ['EngineeringBay'],
        },
    'TerranInfantryArmorsLevel3': {
        'build_time': 220,
        'built_from': ['EngineeringBay'],
        },
    'TerranVehicleWeaponsLevel1': {
        'build_time': 160,
        'built_from': ['Armory'],
        },
    'TerranVehicleWeaponsLevel2': {
        'build_time': 190,
        'built_from': ['Armory'],
        },
    'TerranVehicleWeaponsLevel3': {
        'build_time': 220,
        'built_from': ['Armory'],
        },
    'TerranVehicleArmorsLevel1': {
        'build_time': 160,
        'built_from': ['Armory'],
        },
    'TerranVehicleArmorsLevel2': {
        'build_time': 190,
        'built_from': ['Armory'],
        },
    'TerranVehicleArmorsLevel3': {
        'build_time': 220,
        'built_from': ['Armory'],
        },
    'TerranShipWeaponsLevel1': {
        'build_time': 160,
        'built_from': ['Armory'],
        },
    'TerranShipWeaponsLevel2': {
        'build_time': 190,
        'built_from': ['Armory'],
        },
    'TerranShipWeaponsLevel3': {
        'build_time': 220,
        'built_from': ['Armory'],
        },
    'TerranShipArmorsLevel1': {
        'build_time': 160,
        'built_from': ['Armory'],
        },
    'TerranShipArmorsLevel2': {
        'build_time': 190,
        'built_from': ['Armory'],
        },
    'TerranShipArmorsLevel3': {
        'build_time': 220,
        'built_from': ['Armory'],
        },
    'TerranVehicleAndShipWeaponsLevel1': {
        'build_time': 160,
        'built_from': ['Armory'],
        },
    'TerranVehicleAndShipWeaponsLevel2': {
        'build_time': 190,
        'built_from': ['Armory'],
        },
    'TerranVehicleAndShipWeaponsLevel3': {
        'build_time': 220,
        'built_from': ['Armory'],
        },
    'TerranVehicleAndShipArmorsLevel1': {
        'build_time': 160,
        'built_from': ['Armory'],
        },
    'TerranVehicleAndShipArmorsLevel2': {
        'build_time': 190,
        'built_from': ['Armory'],
        },
    'TerranVehicleAndShipArmorsLevel3': {
        'build_time': 220,
        'built_from': ['Armory'],
        },
    'HighCapacityBarrels': {
        'build_time': 110,
        'built_from': ['TechLab'],
        },
    'Stimpack': {
        'build_time': 170,
        'built_from': ['TechLab'],
        },
    'PunisherGrenades': {
        'build_time': 60,
        'built_from': ['TechLab'],
        },
    'ShieldWall': {
        'build_time': 110,
        'built_from': ['TechLab'],
        'display_name': 'Combat Shields',
        },
    'MedivacCaduceusReactor': {
        'build_time': 80,
        'built_from': ['TechLab'],
        },
    'PersonalCloaking': {
        'build_time': 120,
        'built_from': ['TechLab'],
        },
    'GhostMoebiusReactor': {
        'build_time': 80,
        'built_from': ['TechLab'],
        },
    'NeosteelFrame': {
        'build_time': 110,
        'built_from': ['EngineeringBay'],
        },
    'HiSecAutoTracking': {
        'build_time': 80,
        'built_from': ['EngineeringBay'],
        },
    'TerranBuildingArmor': {
        'build_time': 140,
        'built_from': ['EngineeringBay'],
        },
    'BansheeCloak': {
        'build_time': 110,
        'built_from': ['TechLab'],
        },
    'DurableMaterials': {
        'build_time': 110,
        'built_from': ['TechLab'],
        },
    'RavenCorvidReactor': {
        'build_time': 110,
        'built_from': ['TechLab'],
        },
    'StrikeCannons': {
        'build_time': 110,
        'built_from': ['TechLab'],
        },
    'DrillClaws': {
        'build_time': 110,
        'built_from': ['TechLab'],
        },
    'TransformationServos': {
        'build_time': 110,
        'built_from': ['TechLab'],
        },
    'BattlecruiserBehemothReactor': {
        'build_time': 80,
        'built_from': ['FusionCore'],
        },
    'BattlecruiserEnableSpecializations': {
        'build_time': 60,
        'built_from': ['FusionCore'],
        },
    # protoss upgrades
    'ProtossGroundWeaponsLevel1': {
        'build_time': 160,
        'built_from': ['Forge'],
        },
    'ProtossGroundWeaponsLevel2': {
        'build_time': 190,
        'built_from': ['Forge'],
        },
    'ProtossGroundWeaponsLevel3': {
        'build_time': 220,
        'built_from': ['Forge'],
        },
    'ProtossGroundArmorsLevel1': {
        'build_time': 160,
        'built_from': ['Forge'],
        },
    'ProtossGroundArmorsLevel2': {
        'build_time': 190,
        'built_from': ['Forge'],
        },
    'ProtossGroundArmorsLevel3': {
        'build_time': 220,
        'built_from': ['Forge'],
        },
    'ProtossShieldsLevel1': {
        'build_time': 160,
        'built_from': ['Forge'],
        },
    'ProtossShieldsLevel2': {
        'build_time': 190,
        'built_from': ['Forge'],
        },
    'ProtossShieldsLevel3': {
        'build_time': 220,
        'built_from': ['Forge'],
        },
    'ProtossAirWeaponsLevel1': {
        'build_time': 160,
        'built_from': ['CyberneticsCore'],
        },
    'ProtossAirWeaponsLevel2': {
        'build_time': 190,
        'built_from': ['CyberneticsCore'],
        },
    'ProtossAirWeaponsLevel3': {
        'build_time': 220,
        'built_from': ['CyberneticsCore'],
        },
    'ProtossAirArmorsLevel1': {
        'build_time': 160,
        'built_from': ['CyberneticsCore'],
        },
    'ProtossAirArmorsLevel2': {
        'build_time': 190,
        'built_from': ['CyberneticsCore'],
        },
    'ProtossAirArmorsLevel3': {
        'build_time': 220,
        'built_from': ['CyberneticsCore'],
        },
    'WarpGateResearch': {
        'build_time': 160,
        'built_from': ['CyberneticsCore'],
        },
    'BlinkTech': {
        'build_time': 170,
        'built_from': ['TwilightCouncil'],
        },
    'ObserverGraviticBooster': {
        'build_time': 80,
        'built_from': ['RoboticsBay'],
        },
    'GraviticDrive': {
        'build_time': 80,
        'built_from': ['RoboticsBay'],
        },
    'ExtendedThermalLance': {
        'build_time': 140,
        'built_from': ['RoboticsBay'],
        },
    'Charge': {
        'build_time': 140,
        'built_from': ['TwilightCouncil'],
        },
    'PsiStormTech': {
        'build_time': 110,
        'built_from': ['TemplarArchives'],
        },
    'PhoenixRangeUpgrade': {
        'build_time': 90,
        'built_from': ['FleetBeacon'],
        'display_name': 'Anion Pulse-Crystals',
        },
    'CarrierLaunchSpeedUpgrade': {
        'build_time': 80,
        'built_from': ['FleetBeacon'],
        },
    # unit change buildings
    'Lair': {
        'build_time': 80,
        'built_from': ['Hatchery'],
        },
    'Hive': {
        'build_time': 100,
        'built_from': ['Lair'],
        },
    'GreaterSpire': {
        'build_time': 100,
        'built_from': ['Spire'],
        },
    'OrbitalCommand': {
        'build_time': 35,
        'built_from': ['CommandCenter'],
        },
    'PlanetaryFortress': {
        'build_time': 50,
        'built_from': ['CommandCenter'],
        },
    'Overseer': {
        'build_time': 17,
        'built_from': ['Overlord'],
        },
    # LotV Alpha
    'HERC': {
        'build_time': 40,
        'built_from': ['Barracks'],
        },
    'Cyclone': {
        'build_time': 45,
        'built_from': ['Factory'],
        },
    'ARCGun': {
        'build_time': 30,
        'built_from': ['TechLab'],
        },
    'TargetingOptics': {
        'build_time': 110,
        'built_from': ['TechLab'],
        },
    'HyperflightRotors': {
        'build_time': 130,
        'built_from': ['TechLab'],
        },
    'PlogisterEgg': {
        'build_time': 0,  # Ravager - egg not itself because it is the start time, normal build time is 11
        'built_from': ['Roach'],
        },
    'LurkerMPEgg': {
        'build_time': 0,  # Lurker - same logic as above, especially because burrow/unburrow counts, normal build time is 33
        'built_from': ['Hydralisk'],
        },
    'LurkerDenMP': {
        'build_time': 100,
        'built_from': [],
        },
    'SeismicSpines': {
        'build_time': 100,
        'built_from': ['HydraliskDen'],
        },
    'FlyingLocusts': {
        'build_time': 120,
        'built_from': ['InfestationPit'],
        },
    'Disruptor': {
        'build_time': 60,
        'built_from': ['RoboticsFacility'],
        },
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
