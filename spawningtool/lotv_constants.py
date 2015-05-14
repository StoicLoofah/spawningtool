"""
spawningtool.constants
~~~~~~~~~~~~~~~~~~~~~~
"""

FRAMES_PER_SECOND = 22

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
])

BO_CHANGED_EXCLUDED = set([
    'VikingAssault',  # various viking transforms
    'VikingFighter',
    'Viking',
    'WidowMine',  # burrowing
    'Zergling',  # generated when Banelings spawn
])

BUILD_TIMES = {
    # terran units
    'SCV': 12,
    'Marine': 18,
    'Marauder': 21,
    'Reaper': 32,
    'Ghost': 29,
    'BattleHellion': 21,  # Hellbat
    'Hellion': 21,
    'Hellbat': 21,
    'WidowMine': 29,
    'SiegeTank': 32,
    'Thor': 43,
    'Viking': 30,
    'VikingFighter': 30,  # all born as VikingFighters, but others in here for coverage
    'VikingAssault': 30,
    'Medivac': 30,
    'Raven': 43,
    'Banshee': 43,
    'Battlecruiser': 64,
    # protoss units
    'Probe': 12,
    'Zealot': 27,
    'Stalker': 30,
    'Sentry': 26,
    'MothershipCore': 21,
    'HighTemplar': 39,
    'DarkTemplar': 39,
    'Immortal': 39,
    'Colossus': 54,
    'Archon': 9,  # TODO guess
    'Observer': 21,
    'WarpPrism': 36,
    'Phoenix': 25,
    'VoidRay': 43,
    'Oracle': 36,
    'Tempest': 43,
    'Carrier': 64,  # 120 in HotS
    # zerg units
    'Drone': 12,
    'Queen': 36,
    'Zergling': 17,
    'Baneling': 14,
    'Roach': 19,
    'Hydralisk': 24,
    'SwarmHost': 29,
    'Infestor': 36,
    'Ultralisk': 39,
    'NydusWorm': 14,  # TODO guess
    'NydusCanal': 14,  # TODO guess
    'Overlord': 18,
    'Mutalisk': 24,
    'Corruptor': 29,
    'BroodLord': 24,
    'Viper': 29,
    # zerg upgrades
    'ZergMeleeWeaponsLevel1': 116, # TODO guess
    'ZergMeleeWeaponsLevel2': 138,  # TODO guess
    'ZergMeleeWeaponsLevel3': 159,  # TODO guess
    'ZergMissileWeaponsLevel1': 116, # TODO guess
    'ZergMissileWeaponsLevel2': 138,  # TODO guess
    'ZergMissileWeaponsLevel3': 159,  # TODO guess
    'ZergGroundArmorsLevel1': 116, # TODO guess
    'ZergGroundArmorsLevel2': 138,  # TODO guess
    'ZergGroundArmorsLevel3': 159,  # TODO guess
    'ZergFlyerWeaponsLevel1': 116, # TODO guess
    'ZergFlyerWeaponsLevel2': 138,  # TODO guess
    'ZergFlyerWeaponsLevel3': 159,  # TODO guess
    'ZergFlyerArmorsLevel1': 116, # TODO guess
    'ZergFlyerArmorsLevel2': 138,  # TODO guess
    'ZergFlyerArmorsLevel3': 159,  # TODO guess
    'zerglingmovementspeed': 80,  # TODO guess
    'zerglingattackspeed': 94,  # TODO guess
    'CentrificalHooks': 80,  # TODO guess
    'GlialReconstitution': 80,  # TODO guess
    'TunnelingClaws': 80,  # TODO guess
    'hydraliskspeed': 80,  # Grooved Spines
    'HydraliskSpeedUpgrade': 72,  # TODO guess  # Muscular Augments
    'overlordspeed': 43,  # TODO guess
    'overlordtransport': 94,  # TODO guess
    'Burrow': 72,  # TODO guess
    'InfestorEnergyUpgrade': 58,  # TODO guess
    'ChitinousPlating': 80,  # TODO guess
    'LocustLifetimeIncrease': 87,  # TODO guess
    # terran upgrades
    'TerranInfantryWeaponsLevel1': 116, # TODO guess
    'TerranInfantryWeaponsLevel2': 138,  # TODO guess
    'TerranInfantryWeaponsLevel3': 159,  # TODO guess
    'TerranInfantryArmorsLevel1': 116, # TODO guess
    'TerranInfantryArmorsLevel2': 138,  # TODO guess
    'TerranInfantryArmorsLevel3': 159,  # TODO guess
    'TerranVehicleWeaponsLevel1': 116, # TODO guess
    'TerranVehicleWeaponsLevel2': 138,  # TODO guess
    'TerranVehicleWeaponsLevel3': 159,  # TODO guess
    'TerranVehicleArmorsLevel1': 116, # TODO guess
    'TerranVehicleArmorsLevel2': 138,  # TODO guess
    'TerranVehicleArmorsLevel3': 159,  # TODO guess
    'TerranShipWeaponsLevel1': 116, # TODO guess
    'TerranShipWeaponsLevel2': 138,  # TODO guess
    'TerranShipWeaponsLevel3': 159,  # TODO guess
    'TerranShipArmorsLevel1': 116, # TODO guess
    'TerranShipArmorsLevel2': 138,  # TODO guess
    'TerranShipArmorsLevel3': 159,  # TODO guess
    'TerranVehicleAndShipWeaponsLevel1': 116, # TODO guess
    'TerranVehicleAndShipWeaponsLevel2': 138,  # TODO guess
    'TerranVehicleAndShipWeaponsLevel3': 159,  # TODO guess
    'TerranVehicleAndShipArmorsLevel1': 116, # TODO guess
    'TerranVehicleAndShipArmorsLevel2': 138,  # TODO guess
    'TerranVehicleAndShipArmorsLevel3': 159,  # TODO guess
    'HighCapacityBarrels': 80,  # TODO guess
    'Stimpack': 123,  # TODO guess
    'PunisherGrenades': 43,  # TODO guess
    'ShieldWall': 80,  # TODO guess  # ? Combat Shield?
    'MedivacCaduceusReactor': 58,  # TODO guess
    'PersonalCloaking': 87,  # TODO guess
    'GhostMoebiusReactor': 58,  # TODO guess
    'NeosteelFrame': 80,  # TODO guess
    'HiSecAutoTracking': 58,  # TODO guess
    'TerranBuildingArmor': 101,  # TODO guess
    'BansheeCloak': 80,  # TODO guess
    'DurableMaterials': 80,  # TODO guess
    'RavenCorvidReactor': 80,  # TODO guess
    'StrikeCannons': 80,  # TODO guess
    'DrillClaws': 80,  # TODO guess
    'TransformationServos': 80,  # TODO guess
    'BattlecruiserBehemothReactor': 58,  # TODO guess
    'BattlecruiserEnableSpecializations': 43,  # TODO guess
    # protoss upgrades
    'ProtossGroundWeaponsLevel1': 116, # TODO guess
    'ProtossGroundWeaponsLevel2': 138,  # TODO guess
    'ProtossGroundWeaponsLevel3': 159,  # TODO guess
    'ProtossGroundArmorsLevel1': 116, # TODO guess
    'ProtossGroundArmorsLevel2': 138,  # TODO guess
    'ProtossGroundArmorsLevel3': 159,  # TODO guess
    'ProtossShieldsLevel1': 116, # TODO guess
    'ProtossShieldsLevel2': 138,  # TODO guess
    'ProtossShieldsLevel3': 159,  # TODO guess
    'ProtossAirWeaponsLevel1': 116, # TODO guess
    'ProtossAirWeaponsLevel2': 138,  # TODO guess
    'ProtossAirWeaponsLevel3': 159,  # TODO guess
    'ProtossAirArmorsLevel1': 116, # TODO guess
    'ProtossAirArmorsLevel2': 138,  # TODO guess
    'ProtossAirArmorsLevel3': 159,  # TODO guess
    'WarpGateResearch': 116, # TODO guess
    'BlinkTech': 123,  # TODO guess
    'ObserverGraviticBooster': 80,
    'GraviticDrive': 58,  # TODO guess
    'ExtendedThermalLance': 101,  # TODO guess
    'Charge': 101,  # TODO guess
    'PsiStormTech': 80,  # TODO guess
    'PhoenixRangeUpgrade': 65,  # TODO guess
    'CarrierLaunchSpeedUpgrade': 58,  # TODO guess
    # unit change buildings
    'Lair': 58,  # TODO guess
    'Hive': 72,  # TODO guess
    'GreaterSpire': 72,  # TODO guess
    'OrbitalCommand': 25,  # TODO guess
    'PlanetaryFortress': 36,  # TODO guess
    'Overseer': 12,  # TODO guess
    # LotV Beta
    'Cyclone': 32,
    'HyperflightRotors': 94,  # TODO guess  # TODO check name, time
    'FlyingLocusts': 87,  # TODO guess, check name, time
    'Adept': 27,
    # Ravager - egg not itself because it is the start time, normal build time is 9
    'RavagerCocoon': 0,
    # Lurker - same logic as above, especially because burrow/unburrow counts, normal build time is 18
    'LurkerMPEgg': 0,
    'LurkerDenMP': 72,  # TODO check time
    'LurkerRange': 72,  # TODO check time
    'Disruptor': 43,

}

for key, value in BUILD_TIMES.items():
    BUILD_TIMES[key] *= FRAMES_PER_SECOND


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
