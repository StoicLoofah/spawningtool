"""
spawningtool.coop_constants
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Co-op uses Blizzard time like HotS (16 FPS), so it's easier to base the data off of that.

Co-op also uses the LotV launch chronoboost that stays continuously on one building
"""

from spawningtool.hots_constants import *

BO_EXCLUDED = BO_EXCLUDED.copy()

BO_EXCLUDED.update([
    'Scarab',
    # Raynor
    'HyperionAdvancedPointDefenseDrone',
    'HyperionVoidCoop',  # summoned
    'DuskWing',  # summoned
    'SpiderMine',
    # Kerrigan
    'KerriganReviveCocoon',
    'KerriganVoidCoopEconDrop1',
    'KerriganVoidCoopEconDrop2',
    'KerriganVoidCoopEconDrop3',
    'KerriganVoidCoopEconDrop4',
    'KerriganVoidCoopEconDrop5',
    'KerriganVoidCoopEconDropLT1',
    'NydusNetworkAlly',
    'NydusCanalAlly',
    'GreaterNydusWormAlly',
    # Artanis
    'SOAPylonPowerAllyUnit',
    'SOAPylonPowerUnit',
    # Swann
    'VoidCoopARES',  # Calldown
    # Zagara
    'ZagaraReviveCocoon',
    'HunterKillerBurrowed',  # from Spawn Hunter Killers ability
    'HotSSplitterlingBig',  # Splitter probably from auto-spawn
    'HotSSplitterlingMedium',  # Splitter Baneling Spawn
    # Vorazun
    'VorazunShadowGuard',  # calldown
    # Karax
    'CarrierRepairDrone',
    'SOAThermalLanceTargeter',
    'SOAPurifierBeamUnit',
    # Abathur
    'BiomassPickup',
    'ToxicNest',
    'LocustFlying',
    'BrutaliskPlacement',  # Deep Tunnel
    'AbathurSymbioteBrutalisk',  # paired with building Brutalisk
    'AbathurSymbioteLeviathan',  # paired with building Leviathan

    # Alarak
    'AlarakReviveBeacon',
    'VoidRayTaldarim',  # Destroyers that spawn with the Mothership
    'AlarakSupplicantWarpTrainDummy',  # actual supplicants show up as well
    'AlarakSupplicantWarpTrainCreator',

    # Nova
    'NovaReviveBeacon',
    'SpiderMineBurrowed',
    'HealingDrone',
    'Marine_BlackOpsSpawnerUnit',
    'Liberator_BlackOpsSpawnerUnit',
    'Raven_BlackOpsSpawnerUnit',
    'Goliath_BlackOpsSpawnerUnit',
    'SiegeTank_BlackOpsSpawnerUnit',

    # Stukov
    # More accurate to track when cocoons started
    'SISCV',
    'SIOverlord',
    'SICocoonInfestedCivilian',
    'SIInfestedTrooper',
    'SIInfestedCivilian',
    'InfestedCivilianPlaceholder',
    'StukovInfestBroodling',
    'SIInfestedMarine',
    'SIInfestedDiamondback',  # TODO verify
    'SIInfestedSiegeTank',  # TODO verify
    'SIInfestedLiberator',  # TODO verify
    'StukovInfestedBanshee',
    'SIBroodQueen',  # TODO verify
    'StukovApocalisk',  # Calldown
    'SIVolatileInfested',  # not sure what this is but couldn't see it in-game
    'StukovAleksander',  # Calldown
    'ALEKSANDERCRASH_PLACEHOLDER',  # Calldown
    # Fenix
    'FenixCoop',
    'FenixDragoon',
    'FenixChampionTaldarinImmortal',
    'FenixChampionWarbringerColossus',
    'FenixAdeptShade',

    # Dehaka
    'EssencePickup',
    'DehakaCoopReviveCocoonFootPrint',
    'DehakaLocust',
    'LocustMPPrecursor',
    'DehakaNydusDestroyerTimedNoFood',
    # Calldowns
    'DehakaGlevig',
    'DehakaGlevigDeepTunnelPlacement',
    'CoopDehakaGlevigEggHydralisk',
    'CoopDehakaGlevigEggRoach',
    'CoopDehakaGlevigEggZergling',
    'DehakaMurvar',
    'DehakaDakrun',
    # using cocoons instead
    'DehakaDrone',
    'DehakaZerglingLevel2',
    'DehakaRoachLevel2',
    'DehakaHydraliskLevel2',
    'DehakaSwarmHost',
    'DehakaUltraliskLevel2',


    # Han and Horner
    'HHScrapPickup',
    'HHMagneticMine_SpawnerUnit',
    'HHMagneticMinePrep',
    'HHD8SingleCluster',
    'HHD8ClusterBomb',
    'HHD8CenterCluster',
    'HHWraith',
    'HHVikingFighter',
    'HHRaven',
    'HHBattlecruiser',
])

BO_CHANGED_EXCLUDED = BO_CHANGED_EXCLUDED.copy()

BO_CHANGED_EXCLUDED.update([
    # speculative
    'HHWidowMine',
    'HHVikingAssault',
    'HHVikingFighter',
    'HHViking',
    'HotsRaptor',
    'HotSSwarmling',

])



BO_UPGRADES_EXCLUDED = BO_UPGRADES_EXCLUDED.copy()

BO_UPGRADES_EXCLUDED.update([
    'SprayTerran',
    'SprayProtoss',
    'SprayZerg',
    # Co-op
    'GameTimeGreaterthan5Seconds',
    'NydusNetworkCoopAllyLeft',
    # Vorazun
    'MasteryVorazunTimeStopHasteModifyPlayer',
    # Dehaka
    'DehakaCoopStage2',
    'DehakaColossusLegs',
    'DehakaCoopStage3',
])

BUILD_DATA = BUILD_DATA.copy()

BUILD_DATA.update({
    # shared across at least Kerrigan and Zagara
    'overlordspeed': {
        'build_time': 60,  # TODO verify
        'built_from': ['Hatchery', 'Lair', 'Hive'],
        'display_name': 'Pneumatized Carapace',
    },
    'overlordtransport': {
        'build_time': 60,  # TODO verify
        'built_from': ['Hatchery', 'Lair', 'Hive'],
        'display_name': 'Ventral Sacs',
    },
    'zerglingmovementspeed': {
        'build_time': 60,
        'built_from': ['SpawningPool'],
        'display_name': 'Metabolic Boost',
        },
    'HotSZerglingHealth': {
        'build_time': 60,
        'built_from': ['SpawningPool'],
        'display_name': 'Hardened Carapace',
    },
    'zerglingattackspeed': {
        'build_time': 60,  # Called Adrenal Overload in co-op
        'built_from': ['SpawningPool'],
        },
    'ZerglingArmorShred': {
        'build_time': 90,
        'built_from': ['SpawningPool'],
        'display_name': 'Shredding Claws',
    },
    'QueenCoop': {
        'build_time': 50,
        'built_from': ['Hatchery', 'Lair', 'Hive'],
        'display_name': 'Queen',
    },
    'VoidCoopHeroicFortitude': {
        'build_time': 60,
        'built_from': ['EvolutionChamber'],
        'display_name': 'Heroic Fortitude',
    },
    'ChitinousPlating': {
        'build_time': 60,
        'built_from': ['UltraliskCavern'],
        'display_name': 'Chitinous Plating',
    },
    'BurrowCharge': {  # TODO verify
        'build_time': 60,  # TODO verify
        'built_from': ['UltraliskCavern'],
        'display_name': 'Burrow Charge',
    },
    'HotSTissueAssimilation': {
        'build_time': 60,
        'built_from': ['UltraliskCavern'],
        'display_name': 'Tissue Assimilation',
        'race': 'Zerg',
        'type': 'Upgrade',
        'is_morph': False,
    },
})

COMMANDER_BUILD_DATA = {
    'Raynor': {
        'Marine': {
            'build_time': 13,  # TODO verify others
            'built_from': ['Barracks'],
        },
        'Marauder': {
            'build_time': 15,  # TODO verify others
            'built_from': ['Barracks'],
            },
        'Firebat': {
            'build_time': 15,  # TODO verify others
            'built_from': ['Barracks'],
            'display_name': 'Firebat',
        },
        'Medic': {
            'build_time': 13,  # TODO verify others
            'built_from': ['Barracks'],
            'display_name': 'Medic',
        },
        'StabilizerMedPacks': {
            'build_time': 60,
            'built_from': ['TechLab'],
            'display_name': 'Stabilizer Medpacks',
        },
        'Vulture': {
            'build_time': 13,  # TODO verify others
            'built_from': ['Factory'],
            'display_name': 'Vulture',
        },
        'SiegeTank': {
            'build_time': 23,  # TODO verify others
            'built_from': ['Factory'],
            },
        # Buildings
        'SupplyDepotDrop': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Supply Depot',
            'race': 'Terran',
            'type': 'Building',
            'is_morph': False,
        },
        # Upgrades
        'FirebatJuggernautPlating': {
            'build_time': 60,
            'built_from': ['TechLab'],
            'display_name': 'Juggernaut Plating',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'BearclawNozzles': {
            'build_time': 60,
            'built_from': ['TechLab'],
            'display_name': 'Incinerator Gauntlets',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'RaynorTalentedTerranInfantryArmorLevel1': {
            'build_time': 160,
            'built_from': ['EngineeringBay'],
            'display_name': 'Terran Infantry Armor Level 1',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'RaynorTalentedTerranInfantryArmorLevel2': {
            'build_time': 190,
            'built_from': ['EngineeringBay'],
            'display_name': 'Terran Infantry Armor Level 2',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'RaynorTalentedTerranInfantryArmorLevel3': {
            'build_time': 220,
            'built_from': ['EngineeringBay'],
            'display_name': 'Terran Infantry Armor Level 3',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'NanoConstructor': {
            'build_time': 60,
            'built_from': ['TechLab'],
            'display_name': 'Replenishable Magazine',
        },
        'CerberusMines': {
            'build_time': 60,
            'built_from': ['TechLab'],
            'display_name': 'Cerberus Mines',
        },

    },
    'Kerrigan': {
        # TODO extra Zerglings in the build order?
        'HotSRaptor': {
            'build_time': 24,
            'built_from': [],
            'display_name': 'Zergling',
        },
        'Hydralisk': {
            'build_time': 30,
            'built_from': [],
            },
        'HydraliskLurker': {
            'build_time': 24,
            'built_from': [],
            'display_name': 'Hydralisk',
        },
        'Lurker': {
            'build_time': 15,
            'built_from': ['Hydralisk'],
            'display_name': 'Lurker',
            'race': 'Zerg',
            'type': 'Unit',
            'is_morph': True,
        },
        'HotSTorrasque': {
            'build_time': 55,
            'built_from': [],
            'display_name': 'Ultralisk',  # Torrasque strain
            'race': 'Zerg',
            'type': 'Unit',
            'is_morph': False,
        },
        # Buildings
        'GreaterNydusWorm': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Omega Worm',
            'race': 'Zerg',
            'type': 'Building',
            'is_morph': False,
        },
        # Upgrades
        'K5ChainLightning': {
            'build_time': 90,
            'built_from': ['EvolutionChamber'],
            'display_name': 'Chain Reaction',
        },
        'K5Cooldowns': {
            'build_time': 120,
            'built_from': ['EvolutionChamber'],
            'display_name': 'Ability Efficiency',
        },
        'hydraliskspeed': {
            'build_time': 60,
            'built_from': ['HydraliskDen'],
            'display_name': 'Muscular Augments',
            },
        'HotSHydraliskHealth': {
            'build_time': 90,
            'built_from': ['HydraliskDen'],
            'display_name': 'Ancillary Carapace',
        },
        'HydraliskFrenzy': {
            'build_time': 120,
            'built_from': ['HydraliskDen'],
            'display_name': 'Frenzy',
        },
        'SeismicSpines': {
            'build_time': 120,
            'built_from': ['HydraliskDen'],
            'display_name': 'Seismic Spines',
        },
        'HotSRapidRegeneration': {
            'build_time': 60,
            'built_from': ['Spire', 'GreaterSpire'],
            'display_name': 'Rapid Regeneration',
        },
        'HotSViciousGlaive': {
            'build_time': 90,
            'built_from': ['Spire', 'GreaterSpire'],
            'display_name': 'Vicious Glave',
        },
        'MutaliskSunderingGlave': {
            'build_time': 120,
            'built_from': ['Spire', 'GreaterSpire',],
            'display_name': 'Sundering Glave',
        },
        'PorousCartilage': {  # TODO verify
            'build_time': 60,
            'built_from': ['Spire', 'GreaterSpire',],
            'display_name': 'Porous Cartilage',
        },
    },
    'Artanis': {
        # TODO verify
        'ZealotAiur': {
            'build_time': 38,
            'built_from': ['Gateway', 'WarpGate'],  # warpgate is necessary because of changing types
            'display_name': 'Zealot',
        },
        'ZealotResearchWhirlwind': {
            'build_time': 90,
            'built_from': ['TwilightCouncil'],
            'display_name': 'Whirlwind',
        },
        'StalkerResearchDragoonRange': {
            'build_time': 60,
            'built_from': ['TwilightCouncil'],
            'display_name': 'Singularity Charge',
        },
        'StalkerResearchDragoonHealth': {
            'build_time': 90,
            'built_from': ['TwilightCouncil'],
            'display_name': 'Trillic Compresion Mesh',
        },
        'HighTemplarKhaydarinAmulet': {
            'build_time': 120,
            'built_from': ['TemplarArchives'],
            'display_name': 'Khaydarin Amulet',
        },
        'HealingPsionicStorm': {
            'build_time': 90,
            'built_from': ['TemplarArchives'],
            'display_name': 'Plasma Surge',
        },
        'TempestDisintegration': {
            'build_time': 90,
            'built_from': ['FleetBeacon'],
            'display_name': 'Disintegration',
        },
    },
    'Swann': {
        # TODO verify
        'Hercules': {
            'build_time': 30,
            'built_from': ['Starport'],
            'display_name': 'Hercules',
        },
        'Goliath': {
            'build_time': 40,
            'built_from': ['Factory'],
            'display_name': 'Goliath',
        },
        'AresClassWeaponsSystem': {
            'build_time': 60,
            'built_from': ['TechLab'],
            'display_name': 'Ares-Class Targeting System',
        },
        'MultilockTargetingSystems': {
            'build_time': 90,
            'built_from': ['TechLab'],
            'display_name': 'Multi-Lock Weapons System',
        },
        'MaelstromRounds': {
            'build_time': 60,
            'built_from': ['TechLab'],
            'display_name': 'Maelstrom Rounds',
        },
        'ScienceVessel': {
            'build_time': 60,
            'built_from': ['Starport'],
            'display_name': 'Science Vessel',
        },
        'ScienceVesselResearchDefensiveMatrix': {
            'build_time': 90,
            'built_from': ['TechLab'],
            'display_name': 'Defensive Matrix',
        },

        'ScienceVesselFreeRepair': {
            'build_time': 60,
            'built_from': ['TechLab'],
            'display_name': 'Improved Nano-Repair',
        },
        'DrakkenLaserDrillBFG': {
            'build_time': 190,
            'built_from': [],  # ?
            'display_name': 'Upgrade Laser Drill Level 1',
        },
        'DrakkenLaserDrillNuke': {
            'build_time': 220,
            'built_from': [],  # ?
            'display_name': 'Upgrade Laser Drill Level 2',
        },
        # SCVs now benefits from the Level 1 Vehicle Specialist upgrade, which reduces the SCV's build time by 20%.
        # Targeting Optics research time decreased from 90 seconds to 60 seconds.
        # Mag-Field Accelerator upgrade research time decreased from 120 seconds to 90 seconds.
    },
    'Zagara': {
        # TODO verify
        'Drone': {
            'build_time': 26,
            'built_from': [],
        },
        'Zergling': {
            'build_time': 9,
            'built_from': [],
            'display_name': 'Zergling',
        },
        'HotSSwarmling': {  # Zergling evolution
            'build_time': 2,  # TODO verify
            'built_from': [],
            'display_name': 'Swarmling',
        },
        'InfestedAbomination': {
            'build_time': 12,
            'built_from': [],
            'display_name': 'Aberration',
        },
        'Scourge': {
            'build_time': 12,
            'built_from': [],
            'display_name': 'Scourge',
        },
        'Corruptor': {
            'build_time': 16,
            'built_from': [],
            'display_name': 'Corruptor',
        },
        # Upgrades
        'ZagaraVoidCoopAttackUpgrade': {
            'build_time': 90,
            'built_from': ['EvolutionChamber'],
            'display_name': 'Medusa Blades',
        },
        # TODO Protective Cover
        'HotSBanelingCorrosiveBile': {
            'build_time': 90,
            'built_from': ['BanelingNest'],
            'display_name': 'Corrosive Acid',
        },
        'HotSRupture': {
            'build_time': 90,
            'built_from': ['BanelingNest'],
            'display_name': 'Rupture',
        },
        'ScourgeGasCostReduction': {
            'build_time': 60,
            'built_from': ['ScourgeNest'],
            'display_name': 'Simplified Genome',
        },
        'ScourgeSplashDamage': {
            'build_time': 60,
            'built_from': ['ScourgeNest'],
            'display_name': 'Virulent Spores',
        },
    },
    'Vorazun': {
        # TODO verify
        'StalkerShakuras': {
            'build_time': 42,
            'built_from': ['Gateway', 'WarpGate'],
            'display_name': 'Stalker',
        },
        'DarkTemplarShakuras': {
            'build_time': 55,
            'built_from': ['Gateway', 'WarpGate'],
            'display_name': 'Dark Templar',
        },
        'DarkTemplarResearchShadowDash': {
            'build_time': 100,  # wikia was incorrect and had 60 when I last checked
            'built_from': ['DarkShrine'],
            'display_name': 'Blink',
        },
        'DarkTemplarResearchShadowFury': {
            'build_time': 120,
            'built_from': ['DarkShrine'],
            'display_name': 'Shadow Fury',
        },
        'StalkerResearchBlinkShieldRestore': {
            'build_time': 90,
            'built_from': ['TwilightCouncil'],
            'display_name': 'Phase Reactor',
        },
        'CorsairMP': {
            'build_time': 35,
            'built_from': ['Stargate'],
            'display_name': 'Corsair',
        },
        'CorsairPermanentCloak': {
            'build_time': 90,
            'built_from': ['FleetBeacon'],
            'display_name': 'Stealth Drive',
        },
        'CorsairDisruptionWeb': {
            'build_time': 60,
            'built_from': ['FleetBeacon'],
            'display_name': 'Disruption Web',
        },
    },
    'Karax': {
        'ZealotPurifier': {
            'build_time': 38,
            'built_from': ['Gateway', 'WarpGate'],
            'display_name': 'Sentinel',
            'race': 'Protoss',
            'type': 'Unit',
            'is_morph': False,
            },
        'CarrierAiur': {
            'build_time': 120,
            'built_from': ['Stargate'],
            'display_name': 'Carrier',
        },
        # Buildings
        'KhaydarinMonolith': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Khaydarin Monolith',
            'race': 'Protoss',
            'type': 'Building',
            'is_morph': False,
        },
        # Upgrades
        'SolarEfficiencyLevel1': {
            'build_time': 90,
            'built_from': ['SolarForge'],
            'display_name': 'Solar Efficiency Level 1',
        },
        'SolarEfficiencyLevel2': {
            'build_time': 120,
            'built_from': ['SolarForge'],
            'display_name': 'Solar Efficiency Level 2',
        },
        'SolarEfficiencyLevel3': {
            'build_time': 180,
            'built_from': ['SolarForge'],
            'display_name': 'Solar Efficiency Level 3',
        },
        'SOARepairBeamExtraTarget': {
            'build_time': 90,
            'built_from': ['SolarForge'],
            'display_name': 'Advanced Repair Systems',
        },
        'PhaseDetonation': {  # TODO verify
            'build_time': 120,
            'built_from': ['SolarForge'],
            'display_name': 'Phase Detonation',
        },
        'SolarFlare': {  # TODO verify
            'build_time': 120,
            'built_from': ['SolarForge'],
            'display_name': 'Solar Flare',
        },
        'Charge': {
            'build_time': 60,
            'built_from': ['TwilightCouncil'],
            'display_name': 'Charge',
        },
        'Reconstruction': {  # TODO verify
            'build_time': 90,
            'built_from': ['TwilightCouncil'],
            'display_name': 'Reconstruction',
        },
        'RapidRecharging': {  # TODO verify
            'build_time': 90,
            'built_from': ['TwilightCouncil'],
            'display_name': 'Rapid Recharging',
        },
        'Reclamation': {  # TODO verify
            'build_time': 120,
            'built_from': ['TwilightCouncil'],
            'display_name': 'Reclamation',
        },
        'PhoenixRangeUpgrade': {
            'build_time': 60,
            'built_from': ['FleetBeacon'],
            'display_name': 'Anion Pulse-Crystals',
        },
        'PhasingArmor': {  # TODO verify
            'build_time': 90,
            'built_from': ['FleetBeacon'],
            'display_name': 'Phasing Armor',
        },
        'CarrierRepairDrones': {
            'build_time': 120,
            'built_from': ['FleetBeacon'],
            'display_name': 'Repair Drones',
        },
        # TODO verify Robotics Facility units times
        # TODO verify Robotics Bay upgrade times
    },
    'Abathur': {
        # TODO verify
        'RoachVile': {
            'build_time': 27,
            'built_from': [],
            'display_name': 'Roach',
        },
        'Brutalisk': {  # actually the cocoon morph from roach
            'build_time': 5,
            'built_from': [],
            'display_name': 'Brutalisk',
        },
        'HotSLeviathan': {  # actually the cocoon morph from mutalisk
            'build_time': 5,
            'built_from': [],
            'display_name': 'Leviathan',
        },
        'AbathurBioMechanicalTransfusion': {
            'build_time': 60,
            'built_from': ['Evolution Chamber'],
            'display_name': 'Bio-Mechanical Transfusion',
        },
        'Devourer': {
            'build_time': 15,
            'built_from': [],
            'display_name': 'Devourer',
        },
        'DevourerAoEDamage': {
            'build_time': 90,
            'built_from': ['Spire', 'GreaterSpire'],
            'display_name': 'Corrosive Spray',
        },
    },
    'Alarak': {
        # TODO verify
        'Supplicant': {
            'build_time': 28,
            'built_from': ['Gateway', 'WarpGate'],
            'display_name': 'Supplicant',
            'race': 'Protoss',
            'type': 'Unit',
            'is_morph': False,
        },
        'Monitor': {
            'build_time': 37,
            'built_from': ['Gateway', 'WarpGate'],
            'display_name': 'Havoc',
            'race': 'Protoss',
            'type': 'Unit',
            'is_morph': False,
        },
        'ImmortalTaldarim': {
            'build_time': 55,
            'built_from': ['Robotics Facility'],
            'display_name': 'Vanguard',
            'race': 'Protoss',
            'type': 'Unit',
            'is_morph': False,
        },
        'WarpPrismTaldarim': {
            'build_time': 50,
            'built_from': ['Robotics Facility'],
            'display_name': 'Warp Prism',
            'race': 'Protoss',
            'type': 'Unit',
            'is_morph': False,
        },
        'ColossusTaldarim': {
            'build_time': 75,
            'built_from': ['RoboticsFacility'],
            'display_name': 'Wraithwalker',
            'race': 'Protoss',
            'type': 'Unit',
            'is_morph': False,
        },
        'SOAMothershipv4': {
            'build_time': 120,
            'built_from': ['Stargate'],
            'display_name': 'Mothership',
        },
        # Upgrades
        # TODO Imposing Presence
        # TODO Telekinesis
        'AlarackHavocPermanentCloak': {
            'build_time': 60,
            'built_from': ['CyberneticsCore'],
            'display_name': 'Cloaking Module',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        # TODO Bloodshard Resonance
        # TODO Detect Weakness
        'AlarakSupplicantShieldArmor': {
            'build_time': 60,
            'built_from': ['TwilightCouncil'],
            'display_name': 'Blood Shields',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        # TODO Soul Augmentation
        'AlarakStalkerPhasingArmor': {
            'build_time': 90,  # TODO verify
            'built_from': ['TwilightCouncil'],
            'display_name': 'Phasing Armor',
        },
        'VanguardArmoredDamage': {
            'build_time': 60,
            'built_from': ['RoboticsBay'],
            'display_name': 'Fusion Mortars',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        # TODO Matter Dispersion
        'AlarakColossusChargedBlastAirAttack': {
            'build_time': 60,
            'built_from': ['RoboticsBay'],
            'display_name': 'Aerial Tracking',
        },
        'AlarakColossusChargedBlastChargeTime': {
            'build_time': 60,  # TODO verify
            'built_from': ['RoboticsBay'],
            'display_name': 'Rapid Power Cycling',
        },
    },
    'Nova': {
        # TODO verify
        'Marine_BlackOps': {
            'build_time': 0,  # calldown
            'built_from': ['Barracks'],
            'display_name': 'Elite Marine',
        },
        # TODO Marauder commando
        # TODO Spec ops ghost
        # TODO Hellion
        # TODO Hellbat ranger
        'Goliath_BlackOps': {
            'build_time': 0,  # calldown
            'built_from': ['Factory'],
            'display_name': 'Strike Goliath',
        },
        'SiegeTank_BlackOps': {
            'build_time': 0,  # calldown
            'built_from': ['Factory'],
            'display_name': 'Heavy Siege Tank',
        },
        'Liberator_BlackOps': {
            'build_time': 0,  # calldown
            'built_from': ['Starport'],
            'display_name': 'Raid Liberator',
        },
        'Raven_BlackOps': {
            'build_time': 0,  # calldown
            'built_from': ['Starport'],
            'display_name': 'Raven Type-II',
        },
        # TODO Covert Banshee
        # TODO Railgun Turret
        # TODO Missile Turret
        'MarineSuperStim': {
            'build_time': 90,  # TODO verify
            'built_from': ['TechLab'],  # TODO verify
            'display_name': 'Super Stimpack',
        },
        'LiberatorStructureAttack': {
            'build_time': 90,  # TODO verify
            'built_from': ['TechLab'],  # TODO verify
            'display_name': 'Raid Artillery',
        },
    },
    'Stukov': {
        # Track cocoons instead of units for more accurate start times
        'SICocoonInfestedSCV': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Infested SCV',
        },
        'SICocoonInfestedOverlord': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Overlord',
        },
        'SICocoonInfestedMarine': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Infested Marine',
        },
        'SICocoonInfestedDiamondback': {  # TODO verify
            'build_time': 0,
            'built_from': [],
            'display_name': 'Infested Diamondback',
        },
        'SICocoonInfestedSiegeTank': {  # TODO verify
            'build_time': 0,
            'built_from': [],
            'display_name': 'Infested Siege Tank',
        },
        'SICocoonInfestedLiberator': {  # TODO verify
            'build_time': 0,
            'built_from': [],
            'display_name': 'Infested Liberator',
        },
        'SICocoonInfestedBanshee': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Infested Banshee',
        },
        'SICocoonBroodQueen': {  # TODO verify
            'build_time': 0,
            'built_from': [],
            'display_name': 'Brood Queen',
        },
        'HeavyInfestation': {
            'build_time': 90,
            'built_from': ['SICommandCenter'],
            'display_name': 'Aggressive Incubation',
        },
        'SIBarracksTrainInfestedCivilianLevel2': {
            'build_time': 120,
            'built_from': ['SIColonistCompound'],  # TODO verify
            'display_name': 'Infestation Level 1',
        },
        'SIBarracksTrainInfestedCivilianLevel3': {
            'build_time': 120,
            'built_from': ['SIColonistCompound'],  # TODO verify
            'display_name': 'Infestation Level 2',
        },
        'SIBarracksTrainInfestedCivilianLevel4': {
            'build_time': 120,
            'built_from': ['SIColonistCompound'],  # TODO verify
            'display_name': 'Infestation Level 3',
        },
        'StukovInfestedInfestedCivilianLeapAttack': {
            'build_time': 60,
            'built_from': ['SIColonistCompound'],  # TODO verify
            'display_name': 'Anaerobic Enhancement',
        },
        'StukovInfestedCivilianSpawnBroodlingOnDeath': {  # TODO verify
            'build_time': 90,
            'built_from': ['SIColonistCompound'],  # TODO verify
            'display_name': 'Broodling Gestation',
        },
        'SIMarinePlaguedMunitions': {
            'build_time': 90,
            'built_from': ['SIBarracksTechLab'],
            'display_name': 'Plagued Munitions',
        },
        'SIMarineTrooperRange': {
            'build_time': 60,
            'built_from': ['SIBarracksTechLab'],
            'display_name': 'Retinal Augmentation',
        },
        'SIBunkerLifeRegen': {
            'build_time': 60,
            'built_from': ['SIEngineeringBay'],
            'display_name': 'Regenerative Plating',
        },
        'SIBunkerArmor': {
            'build_time': 60,
            'built_from': ['SIEngineeringBay'],
            'display_name': 'Calcified Armor',
        },
        'SIInfantryWeaponsLevel1': {
            'build_time': 160,
            'built_from': ['SIEngineeringBay'],
            'display_name': 'Stukov Infantry Weapons Level 1',
            },
        'SIInfantryWeaponsLevel2': {
            'build_time': 190,
            'built_from': ['SIEngineeringBay'],
            'display_name': 'Stukov Infantry Weapons Level 2',
            },
        'SIInfantryWeaponsLevel3': {
            'build_time': 220,
            'built_from': ['SIEngineeringBay'],
            'display_name': 'Stukov Infantry Weapons Level 3',
            },
        'SIInfantryArmorLevel1': {
            'build_time': 160,
            'built_from': ['SIEngineeringBay'],
            'display_name': 'Stukov Infantry Armor Level 1',
            },
        'SIInfantryArmorLevel2': {
            'build_time': 190,
            'built_from': ['SIEngineeringBay'],
            'display_name': 'Stukov Infantry Armor Level 2',
            },
        'SIInfantryArmorLevel3': {
            'build_time': 220,
            'built_from': ['SIEngineeringBay'],
            'display_name': 'Stukov Infantry Armor Level 3',
            },
        # TODO Stukov Factory Tech Lab
        # TODO Stukov Starport Tech Lab
        'SITerranVehicleWeaponsLevel1': {
            'build_time': 160,
            'built_from': ['SIArmory'],
            'display_name': 'Stukov Vehicle and Ship Weapons Level 1',
            },
        'SITerranVehicleWeaponsLevel2': {
            'build_time': 190,
            'built_from': ['SIArmory'],
            'display_name': 'Stukov Vehicle and Ship Weapons Level 2',
            },
        'SITerranVehicleWeaponsLevel3': {
            'build_time': 220,
            'built_from': ['SIArmory'],
            'display_name': 'Stukov Vehicle and Ship Weapons Level 3',
            },
        'SITerranVehicleArmorLevel1': {
            'build_time': 160,
            'built_from': ['SIArmory'],
            'display_name': 'Stukov Vehicle and Ship Armor Level 1',
            },
        'SITerranVehicleArmorLevel2': {
            'build_time': 190,
            'built_from': ['SIArmory'],
            'display_name': 'Stukov Vehicle and Ship Armor Level 2',
            },
        'SITerranVehicleArmorLevel3': {
            'build_time': 220,
            'built_from': ['SIArmory'],
            'display_name': 'Stukov Vehicle and Ship Armor Level 3',
        },
    },
    'Fenix': {
        'ZealotPurifier': {
            'build_time': 30,
            'built_from': ['Gateway', 'WarpGate'],
            'display_name': 'Legionnaire',
            'race': 'Protoss',
            'type': 'Unit',
            'is_morph': False,
            },
        'SentryFenix': {
            'build_time': 37,
            'built_from': ['Gateway', 'WarpGate'],
            'display_name': 'Sentry',
        },
        'AdeptFenix': {
            'build_time': 38,
            'built_from': ['Gateway', 'WarpGate'],
            'display_name': 'Adept',
        },
        'ColossusPurifier': {
            'build_time': 75,
            'built_from': ['RoboticsFacility'],
            'display_name': 'Colossus',
        },
        # TODO Disruptor
        'Scout': {
            'build_time': 30,
            'built_from': ['Stargate'],
            'display_name': 'Scout',
        },
        'AStrongHeart': {
            'build_time': 10,
            'built_from': ['Forge'],
            'display_name': 'A Strong Heart',
        },
        'Charge': {
            'build_time': 60,
            'built_from': ['TwilightCouncil'],
            },
        'AdeptFenixShadeSpawn': {
            'build_time': 60,
            'built_from': ['TwilightCouncil'],
            'display_name': 'Psionic Projection',
        },
        # TODO Empowered Blades
        # TODO Debilitation System
        'ObserverGraviticBooster': {
            'build_time': 60,
            'built_from': ['RoboticsBay'],
            },
        'ExtendedThermalLance': {
            'build_time': 90,
            'built_from': ['RoboticsBay'],
            },
        # TODO Cloaknig Module
        # TODO Purification Echo
        # TODO Gravimetric Overload
        # TODO Purification Blast
        'FenixScoutWeaponRange': {
            'build_time': 60,
            'built_from': ['FleetBeacon'],
            'display_name': 'Combat Sensor Array',
        },
        # TODO Suppression Procedure
        # TODO Interdictors
    },
    'Dehaka': {
        # Units
        'DehakaTrainEggDrone': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Primal Drone',
            'race': 'Zerg',
            'type': 'Unit',
            'is_morph': False,
        },
        'DehakaTrainEggZergling': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Primal Zergling',
            'race': 'Zerg',
            'type': 'Unit',
            'is_morph': False,
        },
        'DehakaTrainEggRoach': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Primal Roach',
            'race': 'Zerg',
            'type': 'Unit',
            'is_morph': False,
        },
        'DehakaTrainEggHydralisk': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Primal Hydralisk',
            'race': 'Zerg',
            'type': 'Unit',
            'is_morph': False,
        },
        'DehakaTrainEggSwarmHost': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Primal Swarm Host',
            'race': 'Zerg',
            'type': 'Unit',
            'is_morph': False,
        },
        'DehakaTrainEggUltralisk': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Primal Ultralisk',
            'race': 'Zerg',
            'type': 'Unit',
            'is_morph': False,
        },



        # Buildings
        'DehakaBarracks': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Primal Warden',
            'race': 'Zerg',
            'type': 'Building',
            'is_morph': False,
        },
        'DehakaHatchery': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Primal Hive',
            'race': 'Zerg',
            'type': 'Building',
            'is_morph': False,
        },
        'DehakaGlevigStructure': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Glevig\'s Den',
            'race': 'Zerg',
            'type': 'Building',
            'is_morph': False,
        },
        'DehakaMurvarStructure': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Murvar\'s Den',
            'race': 'Zerg',
            'type': 'Building',
            'is_morph': False,
        },
        'DehakaDakrunStructure': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Dakrun\'s Den',
            'race': 'Zerg',
            'type': 'Building',
            'is_morph': False,
        },
        'DehakaNydusDestroyer': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Primal Wurm',
            'race': 'Zerg',
            'type': 'Building',
            'is_morph': False,
        },
        # Upgrades
        'DehakaPrimalWeaponsLevel1': {
            'build_time': 160,
            'built_from': ['DehakaHatchery'],
            'display_name': 'Primal Attacks Level 1',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'DehakaPrimalWeaponsLevel2': {
            'build_time': 190,
            'built_from': ['DehakaHatchery'],
            'display_name': 'Primal Attacks Level 2',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'DehakaPrimalWeaponsLevel3': {
            'build_time': 220,
            'built_from': ['DehakaHatchery'],
            'display_name': 'Primal Attacks Level 3',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'DehakaPrimalArmorLevel1': {
            'build_time': 160,
            'built_from': ['DehakaHatchery'],
            'display_name': 'Primal Carapace Level 1',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'DehakaPrimalArmorLevel2': {
            'build_time': 190,
            'built_from': ['DehakaHatchery'],
            'display_name': 'Primal Carapace Level 2',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'DehakaPrimalArmorLevel3': {
            'build_time': 220,
            'built_from': ['DehakaHatchery'],
            'display_name': 'Primal Carapace Level 3',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'DehakaRoachMoveSpeed': {
            'build_time': 60,
            'built_from': ['DehakaGlevigStructure'],
            'display_name': 'Glial Reconstitution',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'DehakaHydraliskSpeed': {
            'build_time': 60,
            'built_from': ['DehakaGlevigStructure'],
            'display_name': 'Muscular Augments',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'DehakaUltraliskCrashingCharge': {
            'build_time': 60,
            'built_from': ['DehakaDakrunStructure'],
            'display_name': 'Brutal Charge',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'DehakaUltraliskRegen': {
            'build_time': 60,
            'built_from': ['DehakaDakrunStructure'],
            'display_name': 'Healing Adaptation',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },

    },
    'Horner': {
        'HHSCV': {
            'build_time': 17,
            'built_from': ['CommandCenter'],
            'display_name': 'SCV',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },
        'HHReaper': {
            'build_time': 14,
            'built_from': ['HHMercStarportNoArmy'],
            'display_name': 'Reaper',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },
        'HHWidowMine': {
            'build_time': 21,
            'built_from': ['HHMercStarportNoArmy'],
            'display_name': 'Widow Mine',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },
        'HHHellion': {
            'build_time': 14,
            'built_from': ['HHMercStarportNoArmy'],
            'display_name': 'Hellion',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },
        'HHHellionTank': {
            'build_time': 14,
            'built_from': ['HHMercStarportNoArmy'],
            'display_name': 'Hellbat',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },
        # Calldowns
        'HHWraith_SpawnerUnit': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Asteria Wraith',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },
        'HHViking_SpawnerUnit': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Deimos Viking',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },
        'HHRaven_SpawnerUnit': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Theia Raven',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },
        'HHBattlecruiser_SpawnerUnit': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Sovereign Battlecruiser',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },


        # Buildings
        'HHMercStarportNoArmy': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Assault Galleon',
            'race': 'Terran',
            'type': 'Building',
            'is_morph': False,
        },
        'HHMercCompound': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Engineering Bay',
            'race': 'Terran',
            'type': 'Building',
            'is_morph': False,
        },
        # TODO Strike Fighter Platform
        # Upgrades
        'HHReaperG4ClusterBombs': {
            'build_time': 60,
            'built_from': ['HHMercCompound'],
            'display_name': 'LE9 Cluster Charges',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        # TODO Jetpack Overdrive
        'HHWidowMineDeathBlossom': {
            'build_time': 60,
            'built_from': ['HHMercCompound'],
            'display_name': 'Executioner Missiles',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'HHHellionStimDeath': {
            'build_time': 60,
            'built_from': ['HHMercCompound'],
            'display_name': 'Aerosol Stim Emitters',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        # TODO Black Market Launchers
        'HHHellionFearDeath': {
            'build_time': 60,
            'built_from': ['HHMercCompound'],
            'display_name': 'Wildfire Explosives',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        # TODO Tar Bombs
        # TODO Immolation Fluid
        'HHWraithPermaCloak': {
            'build_time': 90,
            'built_from': ['StarportTechLab'],
            'display_name': 'Unregistered Cloak System',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        # TODO Trigger Override
        'HHVikingRockets': {
            'build_time': 90,
            'built_from': ['StarportTechLab'],
            'display_name': 'W.I.L.D. Missiles',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        # TODO Shredder Rounds
        'FleetwideJump': {
            'build_time': 90,
            'built_from': ['StarportTechLab'],
            'display_name': 'Tactical Jump',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        # TODO Multi-Threaded Sensors
        'HHVehicleAndShipWeaponsLevel1': {
            'build_time': 160,
            'built_from': ['Armory'],
            'display_name': 'Horner Weapons Level 1',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'HHVehicleAndShipWeaponsLevel2': {
            'build_time': 190,
            'built_from': ['Armory'],
            'display_name': 'Horner Weapons Level 2',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'HHVehicleAndShipWeaponsLevel3': {
            'build_time': 220,
            'built_from': ['Armory'],
            'display_name': 'Horner Weapons Level 3',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'HHVehicleAndShipArmorsLevel1': {
            'build_time': 160,
            'built_from': ['Armory'],
            'display_name': 'Horner Armor Level 1',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'HHVehicleAndShipArmorsLevel2': {
            'build_time': 190,
            'built_from': ['Armory'],
            'display_name': 'Horner Armor Level 2',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'HHVehicleAndShipArmorsLevel3': {
            'build_time': 220,
            'built_from': ['Armory'],
            'display_name': 'Horner Armor Level 3',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        # TODO Overcharged Reactor
        # TODO Napalm Payload
    },
}

# adjust by the FPS
for commander_data in COMMANDER_BUILD_DATA.values():
    for value in commander_data.values():
        value['build_time'] *= FRAMES_PER_SECOND

# take the base data and incorporate commander data
for commander in COMMANDER_BUILD_DATA:
    combined_data = BUILD_DATA.copy()
    combined_data.update(COMMANDER_BUILD_DATA[commander])
    COMMANDER_BUILD_DATA[commander] = combined_data
