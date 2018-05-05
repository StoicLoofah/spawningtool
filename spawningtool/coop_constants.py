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

    # Han and Horner
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
])

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
            'display_name': 'Firebar',
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
        'QueenCoop': {
            'build_time': 50,
            'built_from': ['Hatchery', 'Lair', 'Hive'],
            'display_name': 'Queen',
        },
        'overlordspeed': {
            'build_time': 60,  # TODO verify
            'built_from': ['Hatchery', 'Lair', 'Hive'],
            },
        'overlordtransport': {
            'build_time': 60,  # TODO verify
            'built_from': ['Hatchery', 'Lair', 'Hive'],
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
        'VoidCoopHeroicFortitude': {
            'build_time': 60,
            'built_from': ['EvolutionChamber'],
            'display_name': 'Heroic Fortitude',
        },
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
        'SeismicSpines': {  # TODO verify
            'build_time': 120,  # TODO verify
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
            'build_time': 120,  # TODO verify
            'built_from': ['Spire', 'GreaterSpire',],
            'display_name': 'Sundering Glave',
        },
        'PorousCartilage': {  # TODO verify
            'build_time': 120,  # TODO verify
            'built_from': ['Spire', 'GreaterSpire',],
            'display_name': 'Porous Cartilage',
            'display_name': '',
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
        'HotSSwarmling': {  # Zergling evolution
            'build_time': 2,
            'built_from': [],
            'display_name': 'Swarmling',
        },
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
        'Scourge': {
            'build_time': 12,
            'built_from': [],
            'display_name': 'Scourge',
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
        'InfestedAbomination': {
            'build_time': 12,
            'built_from': [],
            'display_name': 'Aberration',
        },
        'ZagaraVoidCoopAttackUpgrade': {
            'build_time': 90,
            'built_from': ['EvolutionChamber'],
            'display_name': 'Medusa Blades',
        },
        'ChitinousPlating': {
            'build_time': 60,
            'built_from': ['UltraliskCavern'],
        },
        'BurrowCharge': {  # TODO verify
            'build_time': 60,  # TODO verify
            'built_from': ['UltraliskCavern'],
            'display_name': 'Burrow Charge',
        },
        'TissueAssimilation': {  # TODO verify
            'build_time': 90,  # TODO verify
            'built_from': ['UltraliskCavern'],
            'display_name': 'Tissue Assimilation',
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
            'display_name': 'Zealot',  # Sentinel for Karax
            },
        'CarrierAiur': {
            'build_time': 120,
            'built_from': ['Stargate'],
            'display_name': 'Carrier',
        },
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
        'WarpPrismTaldarim': {
            'build_time': 50,  # TODO verify
            'built_from': ['Robotics Facility'],
            'display_name': 'Warp Prism',
        },
        'ColossusTaldarim': {
            'build_time': 75,  # TODO verify
            'built_from': ['RoboticsFacility'],
            'display_name': 'Wraithwalker',
        },
        'SOAMothershipv4': {
            'build_time': 120,
            'built_from': ['Stargate'],
            'display_name': 'Mothership',
        },
        'AlarakStalkerPhasingArmor': {
            'build_time': 90,  # TODO verify
            'built_from': ['TwilightCouncil'],
            'display_name': 'Phasing Armor',
        },
        'AlarakColossusChargedBlastAirAttack': {
            'build_time': 60,  # TODO verify
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
            'display_name': 'Zealot',  # Legionnaire for Fexnis
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
        # TODO sift through game
    },
    'Horner': {
        # TODO sift through game
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
