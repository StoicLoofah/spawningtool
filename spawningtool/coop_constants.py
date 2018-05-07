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
    'Marine_BlackOps',
    'Liberator_BlackOps',
    'Raven_BlackOps',
    'Goliath_BlackOps',
    'SiegeTank_BlackOps',
    'HellbatBlackOps',
    'Marauder_BlackOps',
    'Banshee_BlackOps',

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
    'FenixArbiter',
    'FenixChampionTaldarinImmortal',
    'FenixChampionWarbringerColossus',
    'FenixAdeptShade',
    'FenixTalisAdeptPhaseShift',
    'FenixClolarionInterceptor',
    'FenixClolarionBomber',

    # Dehaka
    'EssencePickup',
    'DehakaCoopReviveCocoonFootPrint',
    'DehakaLocust',
    'LocustMPPrecursor',
    'DehakaNydusDestroyerTimedNoFood',
    'DehakaPlacement',
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
    # Fenix
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
    # Kerrigan and Abathur
    'HotSRapidRegeneration': {
        'build_time': 60,
        'built_from': ['Spire', 'GreaterSpire'],
        'display_name': 'Rapid Regeneration',
    },
    'MutaliskSunderingGlave': {
        'build_time': 120,
        'built_from': ['Spire', 'GreaterSpire',],
        'display_name': 'Sundering Glave',
    },
    'HotSViciousGlaive': {
        'build_time': 90,
        'built_from': ['Spire', 'GreaterSpire'],
        'display_name': 'Vicious Glave',
    },
    # Artanis and Karax
    'ImmortalAiur': {
        'build_time': 55,
        'built_from': ['RoboticsFacility'],
        'display_name': 'Immortal',
        'race': 'Protoss',
        'type': 'Unit',
        'is_morph': False,
    },
    # Shared by at least Fenix and Karax
    'Charge': {
        'build_time': 60,
        'built_from': ['TwilightCouncil'],
        'display_name': 'Charge',
        'race': 'Protoss',
        'type': 'Upgrade',
        'is_morph': False,
    },
    'ObserverGraviticBooster': {
        'build_time': 60,
        'built_from': ['RoboticsBay'],
        'display_name': 'Gravitic Boosters',
        'race': 'Protoss',
        'race': 'Protoss',
        'type': 'Upgrade',
        'is_morph': False,
    },
    'ExtendedThermalLance': {
        'build_time': 90,
        'built_from': ['RoboticsBay'],
        'display_name': 'Extended Thermal Lance',
        'race': 'Protoss',
        'type': 'Upgrade',
        'is_morph': False,
    },
    # at least Nova
    'HighCapacityBarrels': {
        'build_time': 60,
        'built_from': ['TechLab'],
        'display_name': 'Infernal Pre-Igniter',
        'race': 'Terran',
        'type': 'Upgrade',
        'is_morph': False,
    },
    # Nova and Swann
    'AresClassWeaponsSystem': {
        'build_time': 60,
        'built_from': ['TechLab'],
        'display_name': 'Ares-Class Targeting System',
        'race': 'Terran',
        'type': 'Upgrade',
        'is_morph': False,
    },

})

COMMANDER_BUILD_DATA = {
    'Raynor': {
        # Rapid Recruitment halves all build times
        'Marine': {
            'build_time': 13,
            'built_from': ['Barracks'],
            'display_name': 'Marine',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },
        'Marauder': {
            'build_time': 15,
            'built_from': ['Barracks'],
            'display_name': 'Marauder',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
            },
        'Firebat': {
            'build_time': 15,
            'built_from': ['Barracks'],
            'display_name': 'Firebat',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },
        'Medic': {
            'build_time': 13,
            'built_from': ['Barracks'],
            'display_name': 'Medic',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },
        'Vulture': {
            'build_time': 13,
            'built_from': ['Factory'],
            'display_name': 'Vulture',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },
        'SiegeTank': {
            'build_time': 23,
            'built_from': ['Factory'],
            'display_name': 'Siege Tank',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },
        'VikingFighter': {
            'build_time': 21,
            'built_from': ['Starport'],
            'display_name': 'Viking',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },
        'Banshee': {
            'build_time': 30,
            'built_from': ['Starport'],
            'display_name': 'Banshee',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },
        'Battlecruiser': {
            'build_time': 45,
            'built_from': ['Starport'],
            'display_name': 'Battlecruiser',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
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
        'StabilizerMedPacks': {
            'build_time': 60,
            'built_from': ['TechLab'],
            'display_name': 'Stabilizer Medpacks',
        },
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
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'CerberusMines': {
            'build_time': 60,
            'built_from': ['TechLab'],
            'display_name': 'Cerberus Mines',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'AresClassWeaponsSystemViking': {
            'build_time': 60,
            'built_from': ['TechLab'],
            'display_name': 'Phobos Weapons System',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        # TODO Shockwave Missile Battery
        # TODO Viking Ripwave Missiles
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
        'PorousCartilage': {  # TODO verify
            'build_time': 60,
            'built_from': ['Spire', 'GreaterSpire',],
            'display_name': 'Porous Cartilage',
        },
    },
    'Artanis': {
        'ZealotAiur': {
            'build_time': 38,
            'built_from': ['Gateway', 'WarpGate'],  # warpgate is necessary because of changing types
            'display_name': 'Zealot',
        },
        'Dragoon': {
            'build_time': 42,
            'built_from': ['Gateway', 'WarpGate'],  # warpgate is necessary because of changing types
            'display_name': 'Dragoon',
            'race': 'Protoss',
            'type': 'Unit',
            'is_morph': False,
        },
        'PhoenixAiur': {
            'build_time': 35,
            'built_from': ['Stargate'],
            'display_name': 'Phoenix',
            'race': 'Protoss',
            'type': 'Unit',
            'is_morph': False,
        },

        # Upgrades
        'ZealotResearchWhirlwind': {
            'build_time': 90,
            'built_from': ['TwilightCouncil'],
            'display_name': 'Whirlwind',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'StalkerResearchDragoonRange': {
            'build_time': 60,
            'built_from': ['TwilightCouncil'],
            'display_name': 'Singularity Charge',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'StalkerResearchDragoonHealth': {
            'build_time': 90,
            'built_from': ['TwilightCouncil'],
            'display_name': 'Trillic Compresion Mesh',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'ImmortalResearchBarrierAdvanced': {
            'build_time': 60,
            'built_from': ['RoboticsBay'],
            'display_name': 'Improved Barrier',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        # TODO Scarab Housing
        # TODO Solarite Payload
        'HighTemplarKhaydarinAmulet': {
            'build_time': 120,
            'built_from': ['TemplarArchives'],
            'display_name': 'Khaydarin Amulet',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'HealingPsionicStorm': {
            'build_time': 90,
            'built_from': ['TemplarArchives'],
            'display_name': 'Plasma Surge',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'TempestDisintegration': {
            'build_time': 90,
            'built_from': ['FleetBeacon'],
            'display_name': 'Disintegration',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
    },
    'Swann': {
        # SCVs now benefits from the Level 1 Vehicle Specialist upgrade, which reduces the SCV's build time by 20%.
        'SCV': {
            'build_time': 14,  # TODO verify change in April 2018
            'built_from': ['CommandCenter'],
            'display_name': 'SCV',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },
        'Hellbat': {
            'build_time': 24,
            'built_from': ['Factory'],
        },
        'Goliath': {
            'build_time': 32,
            'built_from': ['Factory'],
            'display_name': 'Goliath',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },
        'SiegeTank': {
            'build_time': 36,
            'built_from': ['Factory'],
        },
        'Cyclone': {
            'build_time': 36,
            'built_from': ['Factory'],
        },
        'Thor': {
            'build_time': 48,
            'built_from': ['Factory'],
        },
        'Hellion': {
            'build_time': 24,
            'built_from': ['Factory'],
        },
        'Wraith': {
            'build_time': 40,
            'built_from': ['Starport'],
            'display_name': 'Wraith',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },
        'Hercules': {
            'build_time': 32,
            'built_from': ['Starport'],
            'display_name': 'Hercules',
        },
        'ScienceVessel': {
            'build_time': 48,
            'built_from': ['Starport'],
            'display_name': 'Science Vessel',
        },
        # Buildings
        'KelMorianGrenadeTurret': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Devastation Turret',
            'race': 'Terran',
            'type': 'Building',
            'is_morph': False,
        },
        'PerditionTurret': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Perdition Turret',
            'race': 'Terran',
            'type': 'Building',
            'is_morph': False,
        },
        # Upgrades
        'HellbatHellArmor': {
            'build_time': 60,
            'built_from': ['TechLab'],
            'display_name': 'Infernal Plating',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'MultilockTargetingSystems': {
            'build_time': 90,
            'built_from': ['TechLab'],
            'display_name': 'Multi-Lock Weapons System',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'MaelstromRounds': {
            'build_time': 60,
            'built_from': ['TechLab'],
            'display_name': 'Maelstrom Rounds',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'CycloneLockOnRangeUpgrade': {
            'build_time': 60,  # reduced ~ April 2018
            'built_from': ['TechLab'],
            'display_name': 'Targeting Optics',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        # TODO Mag-Field Accelerator now 90s
        # TODO 330mm Barrage Cannon
        'WraithImprovedBurstLaser': {
            'build_time': 60,
            'built_from': ['TechLab'],
            'display_name': 'Pulse Amplifier',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        # TODO Displacement FIeld
        'ScienceVesselFreeRepair': {
            'build_time': 60,
            'built_from': ['TechLab'],
            'display_name': 'Improved Nano-Repair',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'ScienceVesselResearchDefensiveMatrix': {
            'build_time': 90,
            'built_from': ['TechLab'],
            'display_name': 'Defensive Matrix',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
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
        'SentryPurifier': {
            'build_time': 37,
            'built_from': ['Gateway', 'WarpGate'],
            'display_name': 'Energizer',
            'race': 'Protoss',
            'type': 'Unit',
            'is_morph': False,
            },
        'ColossusPurifier': {
            'build_time': 75,
            'built_from': ['Gateway', 'WarpGate'],
            'display_name': 'Immortal',
            'race': 'Protoss',
            'type': 'Unit',
            'is_morph': False,
            },
        'PhoenixPurifier': {
            'build_time': 35,
            'built_from': ['Stargate'],
            'display_name': 'Mirage',
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
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'SolarEfficiencyLevel2': {
            'build_time': 120,
            'built_from': ['SolarForge'],
            'display_name': 'Solar Efficiency Level 2',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'SolarEfficiencyLevel3': {
            'build_time': 180,
            'built_from': ['SolarForge'],
            'display_name': 'Solar Efficiency Level 3',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'SOARepairBeamExtraTarget': {
            'build_time': 90,
            'built_from': ['SolarForge'],
            'display_name': 'Advanced Repair Systems',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'SOAOrbitalStrikeUpgrade': {
            'build_time': 120,
            'built_from': ['SolarForge'],
            'display_name': 'Phase Detonation',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'SOASolarLanceUpgrade': {
            'build_time': 120,
            'built_from': ['SolarForge'],
            'display_name': 'Solar Flare',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        # TODO Enhanced Targeting 120
        # TODO Optimized Ordinance 120
        # TODO Fortificiation Barrier 60
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
        # TODO Fire Beam 120
        # TODO Shadow Cannon 120
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
    },
    'Abathur': {
        # TODO verify
        'RoachVile': {
            'build_time': 27,
            'built_from': [],
            'display_name': 'Roach',
        },
        'RavagerAbathur': {
            'build_time': 9,
            'built_from': [],
            'display_name': 'Ravager',
            'race': 'Zerg',
            'type': 'Unit',
            'is_morph': True,
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
        'Devourer': {
            'build_time': 15,
            'built_from': [],
            'display_name': 'Devourer',
        },

        'AbathurBioMechanicalTransfusion': {
            'build_time': 60,
            'built_from': ['EvolutionChamber'],
            'display_name': 'Bio-Mechanical Transfusion',
        },
        'HotSRoachDamage': {
            'build_time': 110,
            'built_from': ['EvolutionChamber'],
            'display_name': 'Hydriodic Bile',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
        # TODO Adaptive Plating
        'RavagerCorrosiveBileRadiusIncrease': {
            'build_time': 90,
            'built_from': ['EvolutionChamber'],
            'display_name': 'Bloated Bile Ducts',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
        # TODO Potent Bile
        # TODO Prolonged Dispersion
        'DevourerAoEDamage': {
            'build_time': 90,
            'built_from': ['Spire', 'GreaterSpire'],
            'display_name': 'Corrosive Spray',
        },
        'HotSPressurizedGlands': {
            'build_time': 90,
            'built_from': ['InfestationPit'],
            'display_name': 'Pressurized Glands',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
        #TODO Virulent Microbes
        # TODO Deep TUnnel
        # TODO Paralytic Barbs
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
        'Marine_BlackOpsSpawnerUnit': {
            'build_time': 0,  # calldown
            'built_from': ['Barracks'],
            'display_name': 'Elite Marine',
        },
        'Marauder_BlackOpsSpawnerUnit': {
            'build_time': 0,  # calldown
            'built_from': ['Barracks'],
            'display_name': 'Hellbat Rangers',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },
        # TODO Spec ops ghost
        'Hellbat_BlackOpsSpawnerUnit': {
            'build_time': 0,  # calldown
            'built_from': ['Factory'],
            'display_name': 'Hellbat Rangers',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },
        'Goliath_BlackOpsSpawnerUnit': {
            'build_time': 0,  # calldown
            'built_from': ['Factory'],
            'display_name': 'Strike Goliath',
        },
        'SiegeTank_BlackOpsSpawnerUnit': {
            'build_time': 0,  # calldown
            'built_from': ['Factory'],
            'display_name': 'Heavy Siege Tank',
        },
        'Liberator_BlackOpsSpawnerUnit': {
            'build_time': 0,  # calldown
            'built_from': ['Starport'],
            'display_name': 'Raid Liberator',
        },
        'Raven_BlackOpsSpawnerUnit': {
            'build_time': 0,  # calldown
            'built_from': ['Starport'],
            'display_name': 'Raven Type-II',
        },
        'Banshee_BlackOpsSpawnerUnit': {
            'build_time': 0,  # calldown
            'built_from': ['Starport'],
            'display_name': 'Covert Banshee',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },
        # TODO Railgun Turret
        # TODO Missile Turret
        'LaserTargetingSystemNova': {
            'build_time': 60,
            'built_from': ['TechLab'],
            'display_name': 'Laser Targeting System',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'MarineSuperStim': {
            'build_time': 90,  # TODO verify
            'built_from': ['TechLab'],  # TODO verify
            'display_name': 'Super Stimpack',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'NovaConcussiveShells': {
            'build_time': 60,
            'built_from': ['TechLab'],
            'display_name': 'Suppression Shells',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        # TODO Magrail Munitions
        'GhostBlackOpsEMP': {
            'build_time': 60,
            'built_from': ['TechLab'],
            'display_name': 'EMP Round',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        # TODO Triple Tap
        # TODO Jump Jet Assault
        # TODO Lockdown Missiles
        'DeploySpiderMines': {
            'build_time': 60,
            'built_from': ['TechLab'],
            'display_name': 'Spider Mines',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        # TODO Graduating Range
        'BansheePermaCloak': {
            'build_time': 60,
            'built_from': ['TechLab'],
            'display_name': 'Advanced Cloaking Field',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        # TODO Rocket Barrage
        'LiberatorStructureAttack': {
            'build_time': 90,  # TODO verify
            'built_from': ['TechLab'],  # TODO verify
            'display_name': 'Raid Artillery',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        # TODO Smart Servos
        # TODO Covert Triage
        # TODO Enhanced Manufacturing
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
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
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
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
            },
        'SIInfantryWeaponsLevel2': {
            'build_time': 190,
            'built_from': ['SIEngineeringBay'],
            'display_name': 'Stukov Infantry Weapons Level 2',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
            },
        'SIInfantryWeaponsLevel3': {
            'build_time': 220,
            'built_from': ['SIEngineeringBay'],
            'display_name': 'Stukov Infantry Weapons Level 3',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
            },
        'SIInfantryArmorLevel1': {
            'build_time': 160,
            'built_from': ['SIEngineeringBay'],
            'display_name': 'Stukov Infantry Armor Level 1',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
            },
        'SIInfantryArmorLevel2': {
            'build_time': 190,
            'built_from': ['SIEngineeringBay'],
            'display_name': 'Stukov Infantry Armor Level 2',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
            },
        'SIInfantryArmorLevel3': {
            'build_time': 220,
            'built_from': ['SIEngineeringBay'],
            'display_name': 'Stukov Infantry Armor Level 3',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
            },
        # TODO Stukov Factory Tech Lab
        # TODO Stukov Starport Tech Lab
        'SITerranVehicleWeaponsLevel1': {
            'build_time': 160,
            'built_from': ['SIArmory'],
            'display_name': 'Stukov Vehicle and Ship Weapons Level 1',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
            },
        'SITerranVehicleWeaponsLevel2': {
            'build_time': 190,
            'built_from': ['SIArmory'],
            'display_name': 'Stukov Vehicle and Ship Weapons Level 2',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
            },
        'SITerranVehicleWeaponsLevel3': {
            'build_time': 220,
            'built_from': ['SIArmory'],
            'display_name': 'Stukov Vehicle and Ship Weapons Level 3',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
            },
        'SITerranVehicleArmorsLevel1': {
            'build_time': 160,
            'built_from': ['SIArmory'],
            'display_name': 'Stukov Vehicle and Ship Armor Level 1',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
            },
        'SITerranVehicleArmorsLevel2': {
            'build_time': 190,
            'built_from': ['SIArmory'],
            'display_name': 'Stukov Vehicle and Ship Armor Level 2',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
            },
        'SITerranVehicleArmorsLevel3': {
            'build_time': 220,
            'built_from': ['SIArmory'],
            'display_name': 'Stukov Vehicle and Ship Armor Level 3',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
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
            'race': 'Protoss',
            'type': 'Unit',
            'is_morph': False,
        },
        'AdeptFenix': {
            'build_time': 38,
            'built_from': ['Gateway', 'WarpGate'],
            'display_name': 'Adept',
            'race': 'Protoss',
            'type': 'Unit',
            'is_morph': False,
        },
        'ColossusPurifier': {
            'build_time': 75,
            'built_from': ['RoboticsFacility'],
            'display_name': 'Colossus',
            'race': 'Protoss',
            'type': 'Unit',
            'is_morph': False,
        },
        # TODO Disruptor
        'Scout': {
            'build_time': 30,
            'built_from': ['Stargate'],
            'display_name': 'Scout',
            'race': 'Protoss',
            'type': 'Unit',
            'is_morph': False,
        },
        'FenixSuitAttackDamage': {
            'build_time': 90,
            'built_from': ['Forge'],
            'display_name': 'Purifier Armaments',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'AStrongHeart': {
            'build_time': 10,
            'built_from': ['Forge'],
            'display_name': 'A Strong Heart',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'FenixArbiterDetection': {
            'build_time': 60,
            'built_from': ['Forge'],
            'display_name': 'Observation Protocol',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'AdeptFenixShadeSpawn': {
            'build_time': 60,
            'built_from': ['TwilightCouncil'],
            'display_name': 'Psionic Projection',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'FenixKaldalisCleave': {
            'build_time': 60,
            'built_from': ['TwilightCouncil'],
            'display_name': 'Empowered Blades',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'FenixChampionTalisAdeptBounceShotUpgrade': {
            'build_time': 60,
            'built_from': ['TwilightCouncil'],
            'display_name': 'Debilitation System',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        # TODO Cloaknig Module 60
        # TODO Purification Echo 90
        'FenixImmortalDetonationShot': {
            'build_time': 90,
            'built_from': ['RoboticsBay'],
            'display_name': 'Gravimetric Overload',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'FenixWarbringerColossusPowerShot': {
            'build_time': 90,
            'built_from': ['RoboticsBay'],
            'display_name': 'Purification Blast',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'FenixScoutWeaponRange': {
            'build_time': 60,
            'built_from': ['FleetBeacon'],
            'display_name': 'Combat Sensor Array',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'FenixChampionScoutAOEMissiles': {
            'build_time': 60,
            'built_from': ['FleetBeacon'],
            'display_name': 'Suppression Procedure',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'FenixChampionCarrierBombers': {
            'build_time': 90,
            'built_from': ['FleetBeacon'],
            'display_name': 'Interdictors',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'FenixChampionTaldarinImmortal': {
            'build_time': 60,
            'built_from': ['PurifierConclave'],  # TODO verify
            'display_name': 'Taldarin\'s A.I. Personality',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'FenixChampionWarbringerColossus': {
            'build_time': 60,
            'built_from': ['PurifierConclave'],  # TODO verify
            'display_name': 'Warbringer\'s A.I. Personality',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'FenixChampionKaldalisZealot': {
            'build_time': 40,
            'built_from': ['PurifierConclave'],  # TODO verify
            'display_name': 'Kaldalis\' A.I. Personality',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'FenixChampionMojoScout': {
            'build_time': 60,
            'built_from': ['PurifierConclave'],  # TODO verify
            'display_name': 'Mojo\'s A.I. Personality',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'FenixChampionTalisAdept': {
            'build_time': 60,
            'built_from': ['PurifierConclave'],  # TODO verify
            'display_name': 'Talis\' A.I. Personality',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'FenixChampionClolarionCarrier': {
            'build_time': 60,
            'built_from': ['PurifierConclave'],  # TODO verify
            'display_name': 'Clolarion\'s A.I. Personality',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
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
        'DehakaRavasaur': {  # Zergling morph
            'build_time': 8,
            'built_from': [],
            'display_name': 'Ravasaur',
            'race': 'Zerg',
            'type': 'Unit',
            'is_morph': True,
        },
        'DehakaTrainEggRoach': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Primal Roach',
            'race': 'Zerg',
            'type': 'Unit',
            'is_morph': False,
        },
        'DehakaRoachLevel3': {
            'build_time': 8,
            'built_from': [],
            'display_name': 'Primal Igniter',
            'race': 'Zerg',
            'type': 'Unit',
            'is_morph': True,
        },
        'DehakaTrainEggHydralisk': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Primal Hydralisk',
            'race': 'Zerg',
            'type': 'Unit',
            'is_morph': False,
        },
        'DehakaMutaliskLevel3FightMorph': {  # morph from Hydralisk
            'build_time': 8,
            'built_from': [],
            'display_name': 'Primal Mutalisk',
            'race': 'Zerg',
            'type': 'Unit',
            'is_morph': True,
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
        'DehakaRavasaurVSArmor': {
            'build_time': 60,
            'built_from': ['DehakaGlevigStructure'],
            'display_name': 'Dissolving Acid',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'DehakaRavasaurRange': {
            'build_time': 60,
            'built_from': ['DehakaGlevigStructure'],
            'display_name': 'Enlarged Parotid Glands',
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
        # TODO Concentrated Fire
        'DehakaHydraliskSpeed': {
            'build_time': 60,
            'built_from': ['DehakaGlevigStructure'],
            'display_name': 'Muscular Augments',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
        # TODO Tenderize
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
        # TODO Slicing Glave 60
        # TODO Shifting Carapace 60
        # TODO Primal Reconsitution 90
        # TODO Explosive Spores 60
        # TODO Primordial Fury 60
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
