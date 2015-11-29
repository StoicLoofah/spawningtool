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
    'SpecialNexus'
])

BO_CHANGED_EXCLUDED = set([
    'Liberator',
    'VikingAssault',  # various viking transforms
    'VikingFighter',
    'Viking',
    'WarpPrism',
    'WidowMine',  # burrowing
    'Zergling',  # generated when Banelings spawn
])


BUILD_DATA = {
    # terran units
    'SCV': {
        'build_time': 12,
        'built_from': ['Command Center', 'Orbital Command'],
        },
    'Marine': {
        'build_time': 18,
        'built_from': ['Barracks'],
        },
    'Marauder': {
        'build_time': 21,
        'built_from': ['Barracks'],
        },
    'Reaper': {
        'build_time': 32,
        'built_from': ['Barracks'],
        },
    'Ghost': {
        'build_time': 29,
        'built_from': ['Barracks'],
        },
    'BattleHellion': {
        'build_time': 21,  # Hellbat
        'built_from': ['Factory'],
        },
    'Hellion': {
        'build_time': 21,
        'built_from': ['Factory'],
        },
    'Hellbat': {
        'build_time': 21,
        'built_from': ['Factory'],
        },
    'WidowMine': {
        'build_time': 29,
        'built_from': ['Factory'],
        },
    'SiegeTank': {
        'build_time': 32,
        'built_from': ['Factory'],
        },
    'Thor': {
        'build_time': 43,
        'built_from': ['Factory'],
        },
    'Viking': {
        'build_time': 30,
        'built_from': ['Starport'],
        },
    'VikingFighter': {
        'build_time': 30,  # all born as VikingFighters, but others in here for coverage
        'built_from': ['Starport'],
        },
    'VikingAssault': {
        'build_time': 30,
        'built_from': ['Starport'],
        },
    'Medivac': {
        'build_time': 30,
        'built_from': ['Starport'],
        },
    'Raven': {
        'build_time': 43,
        'built_from': ['Starport'],
        },
    'Banshee': {
        'build_time': 43,
        'built_from': ['Starport'],
        },
    'Battlecruiser': {
        'build_time': 64,
        'built_from': ['Starport'],
        },
    # protoss units
    'Probe': {
        'build_time': 12,
        'built_from': ['Nexus'],
        },
    'Zealot': {
        'build_time': 27,
        'built_from': ['Gateway', 'WarpGate'],  # warpgate is necessary because of changing types
        },
    'Stalker': {
        'build_time': 30,
        'built_from': ['Gateway', 'WarpGate'],
        },
    'Sentry': {
        'build_time': 26,
        'built_from': ['Gateway', 'WarpGate'],
        },
    'MothershipCore': {
        'build_time': 21,
        'built_from': ['Nexus'],
        },
    'HighTemplar': {
        'build_time': 39,
        'built_from': ['Gateway', 'WarpGate'],
        },
    'DarkTemplar': {
        'build_time': 39,
        'built_from': ['Gateway', 'WarpGate'],
        },
    'Immortal': {
        'build_time': 39,
        'built_from': ['RoboticsFacility'],
        },
    'Colossus': {
        'build_time': 54,
        'built_from': ['RoboticsFacility'],
        },
    'Archon': {
        'build_time': 9,
        'built_from': [],
        },
    'Observer': {
        'build_time': 21,
        'built_from': ['RoboticsFacility'],
        },
    'WarpPrism': {
        'build_time': 36,
        'built_from': ['RoboticsFacility'],
        },
    'Phoenix': {
        'build_time': 25,
        'built_from': ['Stargate'],
        },
    'VoidRay': {
        'build_time': 43,
        'built_from': ['Stargate'],
        },
    'Oracle': {
        'build_time': 36,
        'built_from': ['Stargate'],
        },
    'Tempest': {
        'build_time': 43,
        'built_from': ['Stargate'],
        },
    'Carrier': {
        'build_time': 86,
        'built_from': ['Stargate'],
        },
    # zerg units
    'Drone': {
        'build_time': 12,
        'built_from': [],
        },
    'Queen': {
        'build_time': 36,
        'built_from': ['Hatchery', 'Lair', 'Hive'],
        },
    'Zergling': {
        'build_time': 17,
        'built_from': [],
        },
    'Baneling': {
        'build_time': 14,
        'built_from': [],
        },
    'Roach': {
        'build_time': 19,
        'built_from': [],
        },
    'Hydralisk': {
        'build_time': 24,
        'built_from': [],
        },
    'SwarmHost': {
        'build_time': 29,
        'built_from': [],
        },
    'Infestor': {
        'build_time': 36,
        'built_from': [],
        },
    'Ultralisk': {
        'build_time': 39,
        'built_from': [],
        },
    'NydusWorm': {
        'build_time': 14,  # TODO guess
        'built_from': ['NydusCanal'],
        },
    'NydusCanal': {
        'build_time': 14,  # TODO guess
        'built_from': [],
        },
    'Overlord': {
        'build_time': 18,
        'built_from': [],
        },
    'Mutalisk': {
        'build_time': 24,
        'built_from': [],
        },
    'Corruptor': {
        'build_time': 29,
        'built_from': [],
        },
    'BroodLord': {
        'build_time': 24,
        'built_from': [],
        },
    'Viper': {
        'build_time': 29,
        'built_from': [],
        },
    # zerg upgrades
    'ZergMeleeWeaponsLevel1': {
        'build_time': 114, # TODO guess
        'built_from': ['EvolutionChamber'],
        },
    'ZergMeleeWeaponsLevel2': {
        'build_time': 136, # TODO guess
        'built_from': ['EvolutionChamber'],
        },
    'ZergMeleeWeaponsLevel3': {
        'build_time': 157, # TODO guess
        'built_from': ['EvolutionChamber'],
        },
    'ZergMissileWeaponsLevel1': {
        'build_time': 114, # TODO guess
        'built_from': ['EvolutionChamber'],
        },
    'ZergMissileWeaponsLevel2': {
        'build_time': 136, # TODO guess
        'built_from': ['EvolutionChamber'],
        },
    'ZergMissileWeaponsLevel3': {
        'build_time': 157, # TODO guess
        'built_from': ['EvolutionChamber'],
        },
    'ZergGroundArmorsLevel1': {
        'build_time': 114, # TODO guess
        'built_from': ['EvolutionChamber'],
        },
    'ZergGroundArmorsLevel2': {
        'build_time': 136, # TODO guess
        'built_from': ['EvolutionChamber'],
        },
    'ZergGroundArmorsLevel3': {
        'build_time': 157, # TODO guess
        'built_from': ['EvolutionChamber'],
        },
    'ZergFlyerWeaponsLevel1': {
        'build_time': 114, # TODO guess
        'built_from': ['Spire', 'GreaterSpire'],
        },
    'ZergFlyerWeaponsLevel2': {
        'build_time': 136, # TODO guess
        'built_from': ['Spire', 'GreaterSpire'],
        },
    'ZergFlyerWeaponsLevel3': {
        'build_time': 157, # TODO guess
        'built_from': ['Spire', 'GreaterSpire'],
        },
    'ZergFlyerArmorsLevel1': {
        'build_time': 114, # TODO guess
        'built_from': ['Spire', 'GreaterSpire'],
        },
    'ZergFlyerArmorsLevel2': {
        'build_time': 136, # TODO guess
        'built_from': ['Spire', 'GreaterSpire'],
        },
    'ZergFlyerArmorsLevel3': {
        'build_time': 157, # TODO guess
        'built_from': ['Spire', 'GreaterSpire'],
        },
    'zerglingmovementspeed': {
        'build_time': 80, # TODO guess
        'built_from': ['SpawningPool'],
        },
    'zerglingattackspeed': {
        'build_time': 94, # TODO guess
        'built_from': ['SpawningPool'],
        },
    'CentrificalHooks': {
        'build_time': 80, # TODO guess
        'built_from': ['BanelingNest'],
        },
    'GlialReconstitution': {
        'build_time': 80, # TODO guess
        'built_from': ['RoachWarren'],
        },
    'TunnelingClaws': {
        'build_time': 80, # TODO guess
        'built_from': ['RoachWarren'],
        },
    'hydraliskspeed': {
        'build_time': 80,  # Grooved Spines
        'built_from': ['HydraliskDen'],
        },
    'HydraliskSpeedUpgrade': {
        'build_time': 72, # TODO guess  # Muscular Augments
        'built_from': ['HydraliskDen'],
        },
    'overlordspeed': {
        'build_time': 43, # TODO guess
        'built_from': ['Hatchery', 'Lair', 'Hive'],
        },
    'overlordtransport': {
        'build_time': 94, # TODO guess
        'built_from': ['Hatchery', 'Lair', 'Hive'],
        },
    'Burrow': {
        'build_time': 72, # TODO guess
        'built_from': ['Hatchery', 'Lair', 'Hive'],
        },
    'InfestorEnergyUpgrade': {
        'build_time': 57, # TODO guess
        'built_from': ['InfestationPit'],
        },
    'ChitinousPlating': {
        'build_time': 80, # TODO guess
        'built_from': ['UltraliskCavern'],
        },
    'LocustLifetimeIncrease': {
        'build_time': 87, # TODO guess
        'built_from': ['InfestationPit'],
        },
    'NeuralParasite': {
        'build_time': 80,
        'built_from': ['InfestationPit'],
        },
    # terran upgrades
    'TerranInfantryWeaponsLevel1': {
        'build_time': 114, # TODO guess
        'built_from': ['EngineeringBay'],
        },
    'TerranInfantryWeaponsLevel2': {
        'build_time': 136, # TODO guess
        'built_from': ['EngineeringBay'],
        },
    'TerranInfantryWeaponsLevel3': {
        'build_time': 157, # TODO guess
        'built_from': ['EngineeringBay'],
        },
    'TerranInfantryArmorsLevel1': {
        'build_time': 114, # TODO guess
        'built_from': ['EngineeringBay'],
        },
    'TerranInfantryArmorsLevel2': {
        'build_time': 136, # TODO guess
        'built_from': ['EngineeringBay'],
        },
    'TerranInfantryArmorsLevel3': {
        'build_time': 157, # TODO guess
        'built_from': ['EngineeringBay'],
        },
    'TerranVehicleWeaponsLevel1': {
        'build_time': 114, # TODO guess
        'built_from': ['Armory'],
        },
    'TerranVehicleWeaponsLevel2': {
        'build_time': 136, # TODO guess
        'built_from': ['Armory'],
        },
    'TerranVehicleWeaponsLevel3': {
        'build_time': 157, # TODO guess
        'built_from': ['Armory'],
        },
    'TerranVehicleArmorsLevel1': {
        'build_time': 114, # TODO guess
        'built_from': ['Armory'],
        },
    'TerranVehicleArmorsLevel2': {
        'build_time': 136, # TODO guess
        'built_from': ['Armory'],
        },
    'TerranVehicleArmorsLevel3': {
        'build_time': 157, # TODO guess
        'built_from': ['Armory'],
        },
    'TerranShipWeaponsLevel1': {
        'build_time': 114, # TODO guess
        'built_from': ['Armory'],
        },
    'TerranShipWeaponsLevel2': {
        'build_time': 136, # TODO guess
        'built_from': ['Armory'],
        },
    'TerranShipWeaponsLevel3': {
        'build_time': 157, # TODO guess
        'built_from': ['Armory'],
        },
    'TerranShipArmorsLevel1': {
        'build_time': 114, # TODO guess
        'built_from': ['Armory'],
        },
    'TerranShipArmorsLevel2': {
        'build_time': 136, # TODO guess
        'built_from': ['Armory'],
        },
    'TerranShipArmorsLevel3': {
        'build_time': 157, # TODO guess
        'built_from': ['Armory'],
        },
    'TerranVehicleAndShipWeaponsLevel1': {
        'build_time': 114, # TODO guess
        'built_from': ['Armory'],
        },
    'TerranVehicleAndShipWeaponsLevel2': {
        'build_time': 136, # TODO guess
        'built_from': ['Armory'],
        },
    'TerranVehicleAndShipWeaponsLevel3': {
        'build_time': 157, # TODO guess
        'built_from': ['Armory'],
        },
    'TerranVehicleAndShipArmorsLevel1': {
        'build_time': 114, # TODO guess
        'built_from': ['Armory'],
        },
    'TerranVehicleAndShipArmorsLevel2': {
        'build_time': 136, # TODO guess
        'built_from': ['Armory'],
        },
    'TerranVehicleAndShipArmorsLevel3': {
        'build_time': 157, # TODO guess
        'built_from': ['Armory'],
        },
    'HighCapacityBarrels': {
        'build_time': 80, # TODO guess
        'built_from': ['TechLab'],
        },
    'Stimpack': {
        'build_time': 123, # TODO guess
        'built_from': ['TechLab'],
        },
    'PunisherGrenades': {
        'build_time': 43, # TODO guess
        'built_from': ['TechLab'],
        },
    'ShieldWall': {
        'build_time': 80, # TODO guess  # ? Combat Shield?
        'built_from': ['TechLab'],
        },
    'MedivacCaduceusReactor': {
        'build_time': 57, # TODO guess
        'built_from': ['TechLab'],
        },
    'PersonalCloaking': {
        'build_time': 87, # TODO guess
        'built_from': ['TechLab'],
        },
    'GhostMoebiusReactor': {
        'build_time': 57, # TODO guess
        'built_from': ['TechLab'],
        },
    'NeosteelFrame': {
        'build_time': 80, # TODO guess
        'built_from': ['EngineeringBay'],
        },
    'HiSecAutoTracking': {
        'build_time': 57, # TODO guess
        'built_from': ['EngineeringBay'],
        },
    'TerranBuildingArmor': {
        'build_time': 100, # TODO guess
        'built_from': ['EngineeringBay'],
        },
    'BansheeCloak': {
        'build_time': 80, # TODO guess
        'built_from': ['TechLab'],
        },
    'DurableMaterials': {
        'build_time': 80, # TODO guess
        'built_from': ['TechLab'],
        },
    'RavenCorvidReactor': {
        'build_time': 80, # TODO guess
        'built_from': ['TechLab'],
        },
    'StrikeCannons': {
        'build_time': 80, # TODO guess
        'built_from': ['TechLab'],
        },
    'DrillClaws': {
        'build_time': 80, # TODO guess
        'built_from': ['TechLab'],
        },
    'TransformationServos': {
        'build_time': 80, # TODO guess
        'built_from': ['TechLab'],
        },
    'BattlecruiserBehemothReactor': {
        'build_time': 57, # TODO guess
        'built_from': ['FusionCore'],
        },
    'BattlecruiserEnableSpecializations': {
        'build_time': 43, # TODO guess
        'built_from': ['FusionCore'],
        },
    # protoss upgrades
    'ProtossGroundWeaponsLevel1': {
        'build_time': 114,
        'built_from': ['Forge'],
        },
    'ProtossGroundWeaponsLevel2': {
        'build_time': 136,
        'built_from': ['Forge'],
        },
    'ProtossGroundWeaponsLevel3': {
        'build_time': 157,
        'built_from': ['Forge'],
        },
    'ProtossGroundArmorsLevel1': {
        'build_time': 114,
        'built_from': ['Forge'],
        },
    'ProtossGroundArmorsLevel2': {
        'build_time': 136,
        'built_from': ['Forge'],
        },
    'ProtossGroundArmorsLevel3': {
        'build_time': 157,
        'built_from': ['Forge'],
        },
    'ProtossShieldsLevel1': {
        'build_time': 114,
        'built_from': ['Forge'],
        },
    'ProtossShieldsLevel2': {
        'build_time': 136,
        'built_from': ['Forge'],
        },
    'ProtossShieldsLevel3': {
        'build_time': 157,
        'built_from': ['Forge'],
        },
    'ProtossAirWeaponsLevel1': {
        'build_time': 114,
        'built_from': ['CyberneticsCore'],
        },
    'ProtossAirWeaponsLevel2': {
        'build_time': 136,
        'built_from': ['CyberneticsCore'],
        },
    'ProtossAirWeaponsLevel3': {
        'build_time': 157,
        'built_from': ['CyberneticsCore'],
        },
    'ProtossAirArmorsLevel1': {
        'build_time': 114,
        'built_from': ['CyberneticsCore'],
        },
    'ProtossAirArmorsLevel2': {
        'build_time': 136,
        'built_from': ['CyberneticsCore'],
        },
    'ProtossAirArmorsLevel3': {
        'build_time': 157,
        'built_from': ['CyberneticsCore'],
        },
    'WarpGateResearch': {
        'build_time': 114,
        'built_from': ['CyberneticsCore'],
        },
    'BlinkTech': {
        'build_time': 121,
        'built_from': ['TwilightCouncil'],
        },
    'ObserverGraviticBooster': {
        'build_time': 57,
        'built_from': ['RoboticsBay'],
        },
    'GraviticDrive': {
        'build_time': 57,
        'built_from': ['RoboticsBay'],
        },
    'ExtendedThermalLance': {
        'build_time': 100,
        'built_from': ['RoboticsBay'],
        },
    'Charge': {
        'build_time': 100,
        'built_from': ['TwilightCouncil'],
        },
    'PsiStormTech': {
        'build_time': 80,
        'built_from': ['TemplarArchives'],
        },
    'PhoenixRangeUpgrade': {
        'build_time': 64,
        'built_from': ['FleetBeacon'],
        },
    'CarrierLaunchSpeedUpgrade': {
        'build_time': 57,
        'built_from': ['FleetBeacon'],
        },
    'AdeptShieldUpgrade': {  # deprecated from LotV Beta
        'build_time': 57,
        'built_from': ['TwilightCouncil'],
        },
    'AdeptPiercingAttack': {
        'build_time': 100,
        'built_from': ['TwilightCouncil'],
        },
    # unit change buildings
    'Lair': {
        'build_time': 57, # TODO guess
        'built_from': ['Hatchery'],
        },
    'Hive': {
        'build_time': 72, # TODO guess
        'built_from': ['Lair'],
        },
    'GreaterSpire': {
        'build_time': 72, # TODO guess
        'built_from': ['Spire'],
        },
    'OrbitalCommand': {
        'build_time': 25, # TODO guess
        'built_from': ['CommandCenter'],
        },
    'PlanetaryFortress': {
        'build_time': 36, # TODO guess
        'built_from': ['CommandCenter'],
        },
    'Overseer': {
        'build_time': 12, # TODO guess
        'built_from': ['Overlord'],
        },
    # LotV Alpha
    'Cyclone': {
        'build_time': 32,
        'built_from': ['Factory'],
        },
    'HyperflightRotors': {
        'build_time': 94,  # TODO guess, check name/time
        'built_from': ['TechLab'],
        },
    'FlyingLocusts': {
        'build_time': 87,  # TODO guess, check name/time
        'built_from': ['InfestationPit'],
        },
    'Adept': {
        'build_time': 27,
        'built_from': ['Gateway', 'WarpGate'],
        },
    'RavagerCocoon': {
        'build_time': 0,  # Ravager - egg not itself because it is the start time, normal build time is 9
        'built_from': ['Roach'],
        },
    'LurkerMPEgg': {
        'build_time': 0,  # Lurker - same logic as above, especially because burrow/unburrow counts, normal build time is 33
        'built_from': ['Hydralisk'],
        },
    'LurkerDenMP': {
        'build_time': 72,  # TODO check time
        'built_from': ['HydraliskDen'],
        },
    'LurkerRange': {
        'build_time': 72,  # TODO check time
        'built_from': ['HydraliskDen', 'LurkerDenMP'],
        },
    'Disruptor': {
        'build_time': 36,
        'built_from': ['RoboticsFacility'],
        },
    'Liberator': {
        'build_time': 60,
        'built_from': ['Starport'],
        },
    'CycloneLockOnRangeUpgrade': {
        'build_time': 79,  # TODO probably wrong, fix this
        'built_from': ['TechLab'],
    },
    'CycloneAirUpgrade': {
        'build_time': 79,  # TODO probably wrong, fix this
        'built_from': ['TechLab'],
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
    # LotV Beta
    'LockOn',  # TODO check name
    'TacticalJump',  # TODO check name
    'CorrosiveBile',  # TODO check name
    'CausticSpray',  # TODO check name
    'SpawnLocusts',  # TODO check name
    'Swoop',  # TODO check name
    'ParasiticBomb',  # TODO check name
    'PsionicTransfer',  # TODO check name
    'PurificationNova',  # TODO check name
    'StasisWard',  # TODO check name
    'Barrier',  # TODO check name
    'Disintegration',  # TODO check name
    'ReleaseInterceptors',  # TODO check name
    # TODO reaper KD8Charge ability?
    ])
