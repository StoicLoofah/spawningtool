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
        'build_time': 21,
        'built_from': ['Factory'],
        'display_name': 'Hellbat',
        },
    'Hellion': {
        'build_time': 21,
        'built_from': ['Factory'],
        },
    'Hellbat': {  # deprecated?
        'build_time': 21,
        'built_from': ['Factory'],
        },
    'WidowMine': {
        'build_time': 21,
        'built_from': ['Factory'],
        },
    'SiegeTank': {
        'build_time': 32,
        'built_from': ['Factory'],
        },
    'Cyclone': {
        'build_time': 32,
        'built_from': ['Factory'],
        },
    'Thor': {
        'build_time': 43,
        'built_from': ['Factory'],
        },
    'Viking': {  # not built as this
        'build_time': 30,
        'built_from': ['Starport'],
        },
    'VikingFighter': {
        'build_time': 30,  # all born as VikingFighters, but others in here for coverage
        'built_from': ['Starport'],
        },
    'VikingAssault': {  # not built as this
        'build_time': 30,
        'built_from': ['Starport'],
        },
    'Medivac': {
        'build_time': 30,
        'built_from': ['Starport'],
        },
    'Liberator': {
        'build_time': 60,
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
    'Nuke': {  # treat the Nuke like a unit
        'build_time': 43,
        'built_from': ['Ghost Academy'],
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
    'Adept': {
        'build_time': 27,
        'built_from': ['Gateway', 'WarpGate'],
        },
    'MothershipCore': {
        'build_time': 21,
        'built_from': ['Nexus'],
        },
    'Mothership': {
        'build_time': 114,
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
    'Disruptor': {
        'build_time': 36,
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
        'build_time': 37,
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
    'Viper': {
        'build_time': 29,
        'built_from': [],
        },
    'NydusWorm': {  # deprecated
        'build_time': 14,
        'built_from': ['NydusCanal'],
        },
    'NydusCanal': {
        'build_time': 14,
        'built_from': ['NydusNetwork'],
        },
    # zerg evolved units
    'Baneling': {
        'build_time': 14,
        'built_from': [],
        },
    'BroodLord': {
        'build_time': 24,
        'built_from': [],
        },
    'Overseer': {
        'build_time': 12,
        'built_from': ['Overlord'],
        },
    'RavagerCocoon': {  # Ravager - egg not itself because it is the start time, normal build time is 9
        'build_time': 0,
        'built_from': ['Roach'],
        'display_name': 'Ravager',
        },
    'LurkerMPEgg': {  # Lurker - same logic as above, especially because burrow/unburrow counts, normal build time is 18
        'build_time': 0,
        'built_from': ['Hydralisk'],
        'display_name': 'Lurker',
        },
    # zerg upgrades
    'ZergMeleeWeaponsLevel1': {
        'build_time': 114,
        'built_from': ['EvolutionChamber'],
        },
    'ZergMeleeWeaponsLevel2': {
        'build_time': 136,
        'built_from': ['EvolutionChamber'],
        },
    'ZergMeleeWeaponsLevel3': {
        'build_time': 157,
        'built_from': ['EvolutionChamber'],
        },
    'ZergMissileWeaponsLevel1': {
        'build_time': 114,
        'built_from': ['EvolutionChamber'],
        },
    'ZergMissileWeaponsLevel2': {
        'build_time': 136,
        'built_from': ['EvolutionChamber'],
        },
    'ZergMissileWeaponsLevel3': {
        'build_time': 157,
        'built_from': ['EvolutionChamber'],
        },
    'ZergGroundArmorsLevel1': {
        'build_time': 114,
        'built_from': ['EvolutionChamber'],
        },
    'ZergGroundArmorsLevel2': {
        'build_time': 136,
        'built_from': ['EvolutionChamber'],
        },
    'ZergGroundArmorsLevel3': {
        'build_time': 157,
        'built_from': ['EvolutionChamber'],
        },
    'ZergFlyerWeaponsLevel1': {
        'build_time': 114,
        'built_from': ['Spire', 'GreaterSpire'],
        },
    'ZergFlyerWeaponsLevel2': {
        'build_time': 136,
        'built_from': ['Spire', 'GreaterSpire'],
        },
    'ZergFlyerWeaponsLevel3': {
        'build_time': 157,
        'built_from': ['Spire', 'GreaterSpire'],
        },
    'ZergFlyerArmorsLevel1': {
        'build_time': 114,
        'built_from': ['Spire', 'GreaterSpire'],
        },
    'ZergFlyerArmorsLevel2': {
        'build_time': 136,
        'built_from': ['Spire', 'GreaterSpire'],
        },
    'ZergFlyerArmorsLevel3': {
        'build_time': 157,
        'built_from': ['Spire', 'GreaterSpire'],
        },
    'zerglingmovementspeed': {
        'build_time': 79,
        'built_from': ['SpawningPool'],
        },
    'zerglingattackspeed': {
        'build_time': 93,
        'built_from': ['SpawningPool'],
        },
    'CentrificalHooks': {
        'build_time': 79,
        'built_from': ['BanelingNest'],
        },
    'GlialReconstitution': {
        'build_time': 79,
        'built_from': ['RoachWarren'],
        },
    'TunnelingClaws': {
        'build_time': 79,
        'built_from': ['RoachWarren'],
        },
    'hydraliskspeed': {  # LotV Muscular Augments, deprecated 3.8
        'build_time': 71,
        'built_from': ['HydraliskDen'],
        },
    'HydraliskSpeedUpgrade': {  # HotS deprecated Muscular Augments
        'build_time': 71,
        'built_from': ['HydraliskDen'],
        },
    'EvolveGroovedSpines': {  # added 3.8
        'build_time': 71,
        'built_from': ['HydraliskDen'],
    },
    'EvolveMuscularAugments': {  # added 3.8
        'build_time': 71,
        'built_from': ['HydraliskDen'],
    },
    'overlordspeed': {
        'build_time': 43,
        'built_from': ['Hatchery', 'Lair', 'Hive'],
        },
    'overlordtransport': {  # deprecated
        'build_time': 93,
        'built_from': ['Hatchery', 'Lair', 'Hive'],
        },
    'Burrow': {
        'build_time': 71,
        'built_from': ['Hatchery', 'Lair', 'Hive'],
        },
    'InfestorEnergyUpgrade': {
        'build_time': 57,
        'built_from': ['InfestationPit'],
        },
    'LocustLifetimeIncrease': {  # deprecated
        'build_time': 87,
        'built_from': ['InfestationPit'],
        },
    'NeuralParasite': {
        'build_time': 79,
        'built_from': ['InfestationPit'],
        },
    'ChitinousPlating': {
        'build_time': 79,
        'built_from': ['UltraliskCavern'],
        },
    'DiggingClaws': {
        'build_time': 54,
        'build_from': ['LurkerDenMP'],
    },

    # terran upgrades
    'TerranInfantryWeaponsLevel1': {
        'build_time': 114,
        'built_from': ['EngineeringBay'],
        },
    'TerranInfantryWeaponsLevel2': {
        'build_time': 136,
        'built_from': ['EngineeringBay'],
        },
    'TerranInfantryWeaponsLevel3': {
        'build_time': 157,
        'built_from': ['EngineeringBay'],
        },
    'TerranInfantryArmorsLevel1': {
        'build_time': 114,
        'built_from': ['EngineeringBay'],
        },
    'TerranInfantryArmorsLevel2': {
        'build_time': 136,
        'built_from': ['EngineeringBay'],
        },
    'TerranInfantryArmorsLevel3': {
        'build_time': 157,
        'built_from': ['EngineeringBay'],
        },
    'TerranVehicleWeaponsLevel1': {
        'build_time': 114,
        'built_from': ['Armory'],
        },
    'TerranVehicleWeaponsLevel2': {
        'build_time': 136,
        'built_from': ['Armory'],
        },
    'TerranVehicleWeaponsLevel3': {
        'build_time': 157,
        'built_from': ['Armory'],
        },
    'TerranVehicleArmorsLevel1': {  # deprecated
        'build_time': 114,
        'built_from': ['Armory'],
        },
    'TerranVehicleArmorsLevel2': {  # deprecated
        'build_time': 136,
        'built_from': ['Armory'],
        },
    'TerranVehicleArmorsLevel3': {  # deprecated
        'build_time': 157,
        'built_from': ['Armory'],
        },
    'TerranShipWeaponsLevel1': {
        'build_time': 114,
        'built_from': ['Armory'],
        },
    'TerranShipWeaponsLevel2': {
        'build_time': 136,
        'built_from': ['Armory'],
        },
    'TerranShipWeaponsLevel3': {
        'build_time': 157,
        'built_from': ['Armory'],
        },
    'TerranShipArmorsLevel1': {  # deprecated
        'build_time': 114,
        'built_from': ['Armory'],
        },
    'TerranShipArmorsLevel2': {  # deprecated
        'build_time': 136,
        'built_from': ['Armory'],
        },
    'TerranShipArmorsLevel3': {  # deprecated
        'build_time': 157,
        'built_from': ['Armory'],
        },
    'TerranVehicleAndShipWeaponsLevel1': {  # deprecated
        'build_time': 114,
        'built_from': ['Armory'],
        },
    'TerranVehicleAndShipWeaponsLevel2': {  # deprecated
        'build_time': 136,
        'built_from': ['Armory'],
        },
    'TerranVehicleAndShipWeaponsLevel3': {  # deprecated
        'build_time': 157,
        'built_from': ['Armory'],
        },
    'TerranVehicleAndShipArmorsLevel1': {
        'build_time': 114,
        'built_from': ['Armory'],
        },
    'TerranVehicleAndShipArmorsLevel2': {
        'build_time': 136,
        'built_from': ['Armory'],
        },
    'TerranVehicleAndShipArmorsLevel3': {
        'build_time': 157,
        'built_from': ['Armory'],
        },
    # barracks tech lab
    'Stimpack': {
        'build_time': 121,
        'built_from': ['TechLab'],
        'display_name': 'Stimpack',
        },
    'PunisherGrenades': {
        'build_time': 43,
        'built_from': ['TechLab'],
        'display_name': 'Concussive Shells',
        },
    'ShieldWall': {
        'build_time': 79,
        'built_from': ['TechLab'],
        'display_name': 'Combat Shield',
        },
    # engineering bay
    'NeosteelFrame': {
        'build_time': 79,
        'built_from': ['EngineeringBay'],
        'display_name': 'Neosteel Frame',
        },
    'HiSecAutoTracking': {
        'build_time': 57,
        'built_from': ['EngineeringBay'],
        'display_name': 'Hi-Sec Auto Tracking',
        },
    'TerranBuildingArmor': {
        'build_time': 100,
        'built_from': ['EngineeringBay'],
        'display_name': 'Structure Armor',
        },
    # ghost academy
    'PersonalCloaking': {
        'build_time': 86,
        'built_from': ['GhostAcademy'],
        'display_name': 'Personal Cloaking',
        },
    'GhostMoebiusReactor': {  # deprecated
        'build_time': 57,
        'built_from': ['GhostAcademy'],
        },
    # factory tech lab
    'StrikeCannons': {  # deprecated
        'build_time': 79,
        'built_from': ['TechLab'],
        },
    'DrillClaws': {
        'build_time': 79,
        'built_from': ['TechLab'],
        'display_name': 'Drilling Claws',
        },
    'TransformationServos': {  # deprecated
        'build_time': 79,
        'built_from': ['TechLab'],
        },
    'HighCapacityBarrels': {
        'build_time': 79,
        'built_from': ['TechLab'],
        'display_name': 'Infernal Pre-Igniter',
        },
    'CycloneLockOnDamageUpgrade': {  # deprecated
        'build_time': 79,
        'built_from': ['TechLab'],
        'display_name': 'Mag-Field Accelerator',
        },
    'MagFieldLaunchers': {  # deprecated
        'build_time': 79,
        'built_from': ['TechLab'],
    },
    'CycloneRapidFireLaunchers': {
        'build_time': 79,
        'built_from': ['TechLab'],
        'display_name': 'Rapid Fire Launchers',
    },
    'SmartServos': {
        'build_time': 79,
        'built_from': ['TechLab'],
        'display_name': 'Smart Servos',
    },
    # starport tech lab
    'MedivacCaduceusReactor': {  # deprecated
        'build_time': 57,
        'built_from': ['TechLab'],
        },
    'MedivacIncreaseSpeedBoost': {
        'build_time': 57,
        'built_from': ['TechLab'],
        'display_name': 'High Capacity Fuel Tanks',
        },
    'RavenDamageUpgrade': {  # deprecated 3.8
        'build_time': 79,
        'built_from': ['TechLab'],
        'display_name': 'Explosive Shrapnel Shells',
        },
    'RavenRecalibratedExplosives': {  # deprecated
        'build_time': 79,
        'built_from': ['TechLab'],
        },
    'BansheeCloak': {
        'build_time': 79,
        'built_from': ['TechLab'],
        'display_name': 'Cloaking Field',
        },
    'DurableMaterials': {  # deprecated
        'build_time': 79,
        'built_from': ['TechLab'],
        },
    'RavenCorvidReactor': {
        'build_time': 79,
        'built_from': ['TechLab'],
        'display_name': 'Corvid Reactor',
        },
    'BansheeSpeed': {
        'build_time': 121,  # was 93 before 3.8.0
        'built_from': ['TechLab'],
        'display_name': 'Hyperflight Rotors',
        },
    'LiberatorAGRangeUpgrade': {
        'build_time': 79,
        'built_from': ['TechLab'],
        'display_name': 'Advanced Ballistics',
        },
    'RavenEnhancedMunitions': {
        'build_time': 79,
        'built_from': ['TechLab'],
    },
    # fusion core
    'BattlecruiserBehemothReactor': {
        'build_time': 57,
        'built_from': ['FusionCore'],
        },
    'BattlecruiserEnableSpecializations': {
        'build_time': 43,
        'built_from': ['FusionCore'],
        'display_name': 'Weapon Refit',
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
        'display_name': 'Warp Gate',
        },
    'Charge': {
        'build_time': 100,
        'built_from': ['TwilightCouncil'],
        'display_name': 'Charge',
        },
    'BlinkTech': {
        'build_time': 121,
        'built_from': ['TwilightCouncil'],
        'display_name': 'Blink',
        },
    'AdeptShieldUpgrade': {  # deprecated from LotV Beta
        'build_time': 57,
        'built_from': ['TwilightCouncil'],
        },
    'AdeptPiercingAttack': {
        'build_time': 100,
        'built_from': ['TwilightCouncil'],
        'display_name': 'Resonating Glaives',
        },
    'ObserverGraviticBooster': {
        'build_time': 57,
        'built_from': ['RoboticsBay'],
        'display_name': 'Gravitic Boosters',
        },
    'GraviticDrive': {
        'build_time': 57,
        'built_from': ['RoboticsBay'],
        'display_name': 'Gravitic Drive',
        },
    'ExtendedThermalLance': {
        'build_time': 100,
        'built_from': ['RoboticsBay'],
        'display_name': 'Extended Thermal Lance',
        },
    'PsiStormTech': {
        'build_time': 79,
        'built_from': ['TemplarArchives'],
        'display_name': 'Psionic Storm',
        },
    'PhoenixRangeUpgrade': {
        'build_time': 64,
        'built_from': ['FleetBeacon'],
        'display_name': 'Anion Pulse-Crystals',
        },
    'CarrierLaunchSpeedUpgrade': {
        'build_time': 57,
        'built_from': ['FleetBeacon'],
        'display_name': 'Graviton Catapult',
        },
    'DarkTemplarBlinkUpgrade': {
        'build_time': 121,
        'built_from': ['DarkShrine'],
        'display_name': 'Shadow Stride',
        },
    # unit change buildings
    'Lair': {
        'build_time': 57,
        'built_from': ['Hatchery'],
        },
    'Hive': {
        'build_time': 71,
        'built_from': ['Lair'],
        },
    'LurkerDenMP': {
        'build_time': 86,
        'built_from': ['HydraliskDen'],
        },
    'GreaterSpire': {
        'build_time': 71,
        'built_from': ['Spire'],
        },
    'OrbitalCommand': {
        'build_time': 25,
        'built_from': ['CommandCenter'],
        },
    'PlanetaryFortress': {
        'build_time': 36,
        'built_from': ['CommandCenter'],
        },
    # unofficial LotV Alpha only
    'HyperflightRotors': {
        'build_time': 93,
        'built_from': ['TechLab'],
        },
    'FlyingLocusts': {
        'build_time': 87,
        'built_from': ['InfestationPit'],
        },
    'LurkerRange': {
        'build_time': 72,
        'built_from': ['HydraliskDen', 'LurkerDenMP'],
        },
    'CycloneLockOnRangeUpgrade': {
        'build_time': 79,
        'built_from': ['TechLab'],
    },
    'CycloneAirUpgrade': {
        'build_time': 79,
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
