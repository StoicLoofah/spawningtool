"""
spawningtool.coop_constants
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Co-op uses Blizzard time like HotS (16 FPS), so it's easier to base the data off of that.

Co-op also uses the LotV launch chronoboost that stays continuously on one building
"""

from hots_constants import *

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
    'StabilizerMedPacks': { # Stabilizer Medpacks
        'build_time': 60,
        'built_from': ['TechLab'],
    },
    'Vulture': {  # also rapid recruitment?
        'build_time': 10,
        'built_from': ['Factory'],
    },
    'NanoConstructor': {  # Replenishable Magazine
        'build_time': 60,
        'built_from': ['TechLab'],
    },
    'CerberusMines': {
        'build_time': 60,
        'built_from': ['TechLab'],
    },

    # Kerrigan
    'VoidCoopHeroicFortitude': {  # Heroic Fortitude
        'build_time': 60,
        'built_from': ['EvolutionChamber'],
    },
    'K5Cooldowns': {  # Ability Efficiency
        'build_time': 120,
        'built_from': ['EvolutionChamber'],
    },
    'K5ChainLightning': {  # Chain Reaction
        'build_time': 90,
        'built_from': ['EvolutionChamber'],
    },
    'HotSZerglingHealth': {  # Hardened Carapace
        'build_time': 90,
        'built_from': ['SpawningPool'],
    },
    'ZerglingArmorShred': {  # Shredding Claws
        'build_time': 90,
        'built_from': ['SpawningPool'],
    },
    'HotSViciousGlaive': {  # Vicious Glave
        'build_time': 90,
        'built_from': ['Spire'],
    },
    'HotSRapidRegeneration': {  # Rapid Regeneration
        'build_time': 60,
        'built_from': ['Spire'],
    },
    'HotSHydraliskHealth': {  # Ancillary Carapace
        'build_time': 90,
        'built_from': ['HydraliskDen'],
    },
    'HydraliskFrenzy': {  # Frenzy
        'build_time': 120,
        'built_from': ['HydraliskDen'],
    },
    'HydraliskLurker': {  # Hydralisk
        'build_time': 24,
        'built_from': [],
    },
    'QueenCoop': {
        'build_time': 50,
        'built_from': ['Hatchery', 'Lair', 'Hive'],
    },
    # Artanis
    'ZealotResearchWhirlwind': {  # Whirlwind
        'build_time': 90,
        'built_from': ['TwilightCouncil'],
    },
    'StalkerResearchDragoonRange': {  # Singularity Charge
        'build_time': 60,
        'built_from': ['TwilightCouncil'],
    },
    'StalkerResearchDragoonHealth': {  # Trillic Compresion Mesh
        'build_time': 90,
        'built_from': ['TwilightCouncil'],
    },
    'HighTemplarKhaydarinAmulet': {  # Khaydarin Amulet
        'build_time': 120,
        'built_from': ['TemplarArchives'],
    },
    'HealingPsionicStorm': {  # Plasma Surge
        'build_time': 90,
        'built_from': ['TemplarArchives'],
    },
    'TempestDisintegration': {  # Disintegration
        'build_time': 90,
        'built_from': ['FleetBeacon'],
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
    'AresClassWeaponsSystem': {  # Ares-Class Targeting System
        'build_time': 60,
        'built_from': ['TechLab'],
    },
    'MultilockTargetingSystems': {  # Multi-Lock Weapons System
        'build_time': 90,
        'built_from': ['TechLab'],
    },
    'MaelstromRounds': {  # Maelstrom Rounds
        'build_time': 60,
        'built_from': ['TechLab'],
    },
    'ScienceVessel': {
        'build_time': 60,
        'built_from': ['Starport'],
    },
    'ScienceVesselResearchDefensiveMatrix': {  # Defensive Matrix
        'build_time': 90,
        'built_from': ['TechLab'],
    },

    'ScienceVesselFreeRepair': {  # Improved Nano-Repair
        'build_time': 60,
        'built_from': ['TechLab'],
    },
    'DrakkenLaserDrillBFG': {  # Upgrade Laser Drill Level 1
        'build_time': 190,
        'built_from': [],  # ?
    },
    'DrakkenLaserDrillNuke': {  # Upgrade Laser Drill Level 2
        'build_time': 220,
        'built_from': [],  # ?
    },
    # Zagara
    'HotSSwarmling': {  # Swarmling: Zergling evolution
        'build_time': 2,
        'built_from': [],
    },
    'HotSBanelingCorrosiveBile': {  # Corrosive Acid
        'build_time': 90,
        'built_from': ['BanelingNest'],
    },
    'HotSRupture': {  # Rupture
        'build_time': 90,
        'built_from': ['BanelingNest'],
    },
    'Scourge': {
        'build_time': 12,
        'built_from': [],
    },
    'ScourgeGasCostReduction': {  # Simplified Genome
        'build_time': 60,
        'built_from': ['ScourgeNest'],
    },
    'ScourgeSplashDamage': {  # Virulent Spores
        'build_time': 60,
        'built_from': ['ScourgeNest'],
    },
    'InfestedAbomination': {  # Aberration
        'build_time': 12,
        'built_from': [],
    },
    # Vorazun

    # Karax
    'ZealotPurifier': {  # Sentinel
        'build_time': 38,
        'built_from': ['Gateway', 'WarpGate'],  # warpgate is necessary because of changing types
        },
    'CarrierAiur': {  # Carrier
        'build_time': 86,
        'built_from': ['Stargate'],
    },
    'SolarEfficiencyLevel1': {  # Solar Efficiency Level 1
        'build_time': 90,
        'built_from': ['SolarForge'],
    },
    'SolarEfficiencyLevel2': {  # Solar Efficiency Level 2
        'build_time': 120,
        'built_from': ['SolarForge'],
    },
    'SolarEfficiencyLevel3': {  # Solar Efficiency Level 3
        'build_time': 180,
        'built_from': ['SolarForge'],
    },
    'CarrierRepairDrones': {  # Repair Drones
        'build_time': 90,
        'built_from': ['FleetBeacon'],
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
