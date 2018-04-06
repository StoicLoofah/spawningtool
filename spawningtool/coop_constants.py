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

    # Karax
    'CarrierRepairDrone',
    'SOAThermalLanceTargeter',
    'SOAPurifierBeamUnit',
    # Abathur

    # Alarak

    # Nova

    # Stukov

    # Fenix

    # Dehaka

    # Han and Horner
])


BO_UPGRADES_EXCLUDED = BO_UPGRADES_EXCLUDED.copy()

BO_UPGRADES_EXCLUDED.update([
    'SprayTerran',
    'SprayProtoss',
    'SprayZerg',
    # Co-op
    'GameTimeGreaterthan5Seconds',
    'SOARepairBeamExtraTarget',
    'NydusNetworkCoopAllyLeft',
])

NEW_BUILD_DATA = {
    # Raynor
    'Medic': {  # Assume Rapid Recruitment
        'build_time': 10,
        'built_from': ['TechLab'],
    },
    'StabilizerMedPacks': {
        'build_time': 60,
        'built_from': ['TechLab'],
        'display_name': 'Stabilizer Medpacks'
    },
    'Vulture': {  # also rapid recruitment?
        'build_time': 10,
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
    },

    # Kerrigan
    'VoidCoopHeroicFortitude': {
        'build_time': 60,
        'built_from': ['EvolutionChamber'],
        'display_name': 'Heroic Fortitude',
    },
    'K5Cooldowns': {
        'build_time': 120,
        'built_from': ['EvolutionChamber'],
        'display_name': 'Ability Efficiency',
    },
    'K5ChainLightning': {
        'build_time': 90,
        'built_from': ['EvolutionChamber'],
        'display_name': 'Chain Reaction',
    },
    'HotSZerglingHealth': {
        'build_time': 90,
        'built_from': ['SpawningPool'],
        'display_name': 'Hardened Carapace',
    },
    'ZerglingArmorShred': {
        'build_time': 90,
        'built_from': ['SpawningPool'],
        'display_name': 'Shredding Claws',
    },
    'HotSViciousGlaive': {
        'build_time': 90,
        'built_from': ['Spire'],
        'display_name': 'Vicious Glave',
    },
    'HotSRapidRegeneration': {
        'build_time': 60,
        'built_from': ['Spire'],
        'display_name': 'Rapid Regeneration',
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
    'HydraliskLurker': {
        'build_time': 24,
        'built_from': [],
        'display_name': 'Hydralisk',
    },
    'QueenCoop': {
        'build_time': 50,
        'built_from': ['Hatchery', 'Lair', 'Hive'],
    },
    # Artanis
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
    # Swann
    'Hercules': {
        'build_time': 30,
        'built_from': ['Starport'],
    },
    'Goliath': {
        'build_time': 40,
        'built_from': ['Factory'],
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
    # Zagara
    'HotSSwarmling': {
        'build_time': 2,
        'built_from': [],
        'display_name': 'Swarmling: Zergling evolution',
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
    # Vorazun

    # Karax
    'ZealotPurifier': {
        'build_time': 38,
        'built_from': ['Gateway', 'WarpGate'],  # warpgate is necessary because of changing types
        'display_name': 'Sentinel',
        },
    'CarrierAiur': {
        'build_time': 86,
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
    'CarrierRepairDrones': {
        'build_time': 90,
        'built_from': ['FleetBeacon'],
        'display_name': 'Repair Drones',
    },
    # Abathur
    # Alarak

    # Nova

    # Stukov

    # Fenix

    # Dehaka

    # Han and Horner
}

for value in NEW_BUILD_DATA.values():
    value['build_time'] *= FRAMES_PER_SECOND

BUILD_DATA = BUILD_DATA.copy()
BUILD_DATA.update(NEW_BUILD_DATA)
