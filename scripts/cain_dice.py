"""
CAIN 1.0 Dice & Exorcist Generation Engine
Handles authentic, non-deterministic random rolls for:
- Identity & Gender distribution (40% Male / 40% Female / 20% Variations: Children, Animals, Queer/NB/Trans)
- Gaussian Age generation (mean=21, stdev=3.5, min=16 for adults; 9-15 for children; 2-8 for animals)
- Blasphemy Strategy (50% Pure Specialist / 50% Hybrid Adaptor)
- Personalities, Nationalities, and Real-world Weaponry
- Sin Overflow resistance checks & Page 44 D66 Sin Marks table
- Squad Mission Simulation (4-5 operatives, Squad Avg CAT >= Sin CAT, ascending CAT progression)
"""

import sys
import random
import argparse
import json
import math

# Official Page 44 Sin Marks Table
SIN_MARKS_TABLE = {
    1: {
        "location": "EYES",
        "description": "Black or altered sclera, white iris, split, slit, or duplicate pupil.",
        "abilities": {
            1: "Telescopic Vision: See clearly up to extreme distance as if zoomed in.",
            2: "X-Ray Sight: See through walls and non-living matter within short distance.",
            3: "Aura Sense: When closed, sense ambient emotional states of nearby humans/exorcists. Once per mission, gain +1D or power when acting on this.",
            4: "Paralyzing Gaze: Once per mission, momentarily paralyze a human by maintaining eye contact until broken, 1 minute passes, or either suffers stress.",
            5: "Dark Adaptation: See clearly in absolute darkness; immune to obscurity, fog, or weather.",
            6: "Surveillance Synergy: Gain permanent +1D to Surveillance (can exceed normal maximum up to 4D)."
        }
    },
    2: {
        "location": "JAW",
        "description": "Split or extended jaw, pharyngeal jaw, fangs, black tongue, viscous saliva.",
        "abilities": {
            1: "Caustic Spit: Spit black venom up to short distance (mundane ranged weapon, equivalent to service pistol).",
            2: "Silver Tongue of Guilt: Gain 1d3 sin to re-roll any action requiring speech (second result is final).",
            3: "Wind Whisper: Whisper messages of 6 words or less into the wind, heard in the ear of a target within long distance.",
            4: "Subjugation Aura: Gain +1D when negotiating with, commanding, or convincing humans.",
            5: "Compelling Word: Once per mission, speak a one-word command that a human immediately attempts to obey (will not obey suicidal commands).",
            6: "Authority Synergy: Gain permanent +1D to Authority (can exceed normal maximum up to 4D)."
        }
    },
    3: {
        "location": "BACK OR CHEST",
        "description": "Spines, lesions, skin discoloration or warping, hardened/loose scales, vestigial wings, extra ribs.",
        "abilities": {
            1: "Feverish Recovery: Roll an extra resting die when resting; gain the same amount in sin.",
            2: "Internal Filter: No longer need to breathe; immune to mundane toxins, poisons, and alcohol intoxication.",
            3: "Expanded Cavity: Gain permanent +1 maximum Kit Point (KP).",
            4: "Unfeeling Flesh: 1 in 6 chance (roll a 6 on 1d6) to ignore any received injury.",
            5: "Adrenaline Purge: Automatically erase 1 stress whenever investigation pressure advances.",
            6: "Conditioning Synergy: Gain permanent +1D to Conditioning (can exceed normal maximum up to 4D)."
        }
    },
    4: {
        "location": "ARMS OR HANDS",
        "description": "Claws, split hand/arm, extra arm, twisting tendons/muscles, discoloration, extra fingers.",
        "abilities": {
            1: "Unnatural Leverage: Gain 1d3 sin during a feat of mundane strength to elevate the feat up to CAT 3.",
            2: "Flesh Assimilation: Once per mission, seamlessly merge a single handheld mundane item/weapon into your flesh to conceal or draw at will.",
            3: "Dissolution Touch: Once per mission, dissolve non-living matter in a room-sized cube into black sludge with a touch of your ring finger.",
            4: "Bone Blade: Once per mission, take 1d3+1 sin to morph arm/hand into a supernatural melee weapon for a scene (deals full damage to Sins).",
            5: "Brute Force Reroll: Re-roll any Force or Interfacing roll by gaining 1d3 sin (second result is final).",
            6: "Force Synergy: Gain permanent +1D to Force (can exceed normal maximum up to 4D)."
        }
    },
    5: {
        "location": "SKIN, HAIR, OR LEGS",
        "description": "Bleached or transparent skin, digitigrade/multiple legs, unnatural hair shift, patchiness.",
        "abilities": {
            1: "Preternatural Leap: Gain 1d3 sin to leap up to an object CAT size in height without rolling.",
            2: "Surface Adhesion: Touch bare flesh to vertical surfaces or ceilings to climb or walk normally.",
            3: "Sprinter's Stride: Gain +1D when running or sprinting on open ground.",
            4: "Flesh Glider: Gain 1 sin during an action roll to glide short distance through the air from an elevated vantage point.",
            5: "Chameleonic Vanish: Gain 1d3 sin to become completely invisible to mundane perception for the duration of an action roll.",
            6: "Covert Synergy: Gain permanent +1D to Covert (can exceed normal maximum up to 4D)."
        }
    }
}

CANONICAL_AGENDAS = [
    "BEAST", "DOOMED", "FIREBUG", "GUARDIAN", "LONER", 
    "HARDLINE", "MACHINE", "MOTH", "TEMPERANCE", "TORCH", 
    "DEPARTED", "SHADOW", "SORCERER", "SONGBIRD", "SURVIVOR"
]

CANONICAL_BLASPHEMIES = [
    "Tension", "Ardence", "Flux", "Vector", "Gate", "Smother",
    "Whisper", "Edit", "Bind", "Jaunt", "Palace", "Sympathy"
]

PERSONALITY_ARCHETYPES = [
    "Compulsive Chain-Smoking Gambler (bets on squad survival margins, treats hunts like poker hands)",
    "Morbidly Cheerful Dark-Humorist (laughs under artillery fire, names severed body parts)",
    "Cynical Exhausted Pragmatist (counts rounds, hates bureaucracy, drinks lukewarm black coffee)",
    "Fanatical Apocalyptic Zealot (interprets Sins as divine judgment, recites scripture under stress)",
    "Flamboyant Theatrical Narcissist (treats psychic combat as high art, demands dramatic entrances)",
    "Paranoid Superstitious Hermit (obsessively checks locks, carries salt pouches, whispers to shadows)",
    "Manic Scientific Perfectionist (collects biological tissue samples mid-firefight, talks at 200 wpm)",
    "Vindictive Grudge-Keeper (keeps a notebook of every slight from CASTLE officers and sins)",
    "Melancholic Classical Romantic (recites poetry during debriefs, mourns both humans and hosts)",
    "Deadpan Streetwise Nihilist (unimpressed by cosmic horror, treats reality tears like broken plumbing)"
]

NATIONALITIES_POOL = [
    {"country": "Poland", "sample_names": ["Vance Kowalski", "Stanislaw Lem", "Katarzyna Wozniak", "Marek Brzozowski"]},
    {"country": "Germany", "sample_names": ["Klaus Vander", "Odette Brandt", "Maximilian Richter", "Greta Weiss"]},
    {"country": "United Kingdom", "sample_names": ["Arthur Vance", "Eleanor Cross", "Declan Price", "Gideon Graves"]},
    {"country": "Japan", "sample_names": ["Kenzo Takahashi", "Rei Asuka", "Shiro Muramasa", "Yoko Shinozaki"]},
    {"country": "Brazil", "sample_names": ["Renato Silva", "Beatriz Costa", "Tiago Mendes", "Camila Rocha"]},
    {"country": "Nigeria", "sample_names": ["Oluwaseun Adeyemi", "Chidi Okonkwo", "Amina Bello", "Emeka Danladi"]},
    {"country": "Mexico", "sample_names": ["Dolores Reyes", "Javier Morales", "Valeria Salgado", "Rodrigo Esparza"]},
    {"country": "South Korea", "sample_names": ["Park Jin-Woo", "Kang Min-Seo", "Bae Da-Eun", "Choi Yoon-Sik"]},
    {"country": "United States", "sample_names": ["Caleb Shaw", "Cassidy Sterling", "Jackson Cole", "Marilyn Ford"]},
    {"country": "France", "sample_names": ["Julien Laurent", "Camille Moreau", "Gaspard Font", "Solange Mercier"]}
]

REAL_WEAPONS_CATALOG = {
    "handguns": [
        "SIG Sauer P226 Nitron 9mm (15-round, service grade, heavy alloy frame)",
        "Glock 19 Gen 5 9mm (polymer frame, waterproof tactical striker)",
        "Heckler & Koch USP .45 ACP (high-recoil suppressor-ready frame)",
        "Colt Python 4.25\" .357 Magnum (hand-polished stainless steel wheelgun)",
        "Beretta 92FS Brigadier 9mm (braced slide, match-grade trigger)",
        "CZ 75 SP-01 Shadow 9mm (steel ergonomic frame, fiber optic sight)",
        "Browning Hi-Power 9mm (vintage single-action, checkered walnut grips)",
        "Walther PPK/S .380 ACP (compact concealment, mirror blued finish)"
    ],
    "long_guns": [
        "Benelli M4 Super 90 12-gauge (auto-regulating gas piston combat shotgun)",
        "Mossberg 590A1 Tactical 12-gauge (heavy-walled barrel, bayonet lug)",
        "Heckler & Koch MP5A3 9mm (roller-delayed submachine gun with collapsing stock)",
        "Steyr AUG A3 M1 5.56mm (bullpup carbine, integrated 3x optic)",
        "Remington 700 Police .308 Win (heavy tactical barrel, HS Precision stock)",
        "Franchi SPAS-12 Dual-mode 12-gauge (folding metal arm stock with hook)",
        "Colt M4A1 SOPMOD 5.56mm (quad-rail handguard, SureFire suppressor)",
        "Lee-Enfield No. 4 Mk I .303 British (cut-down 'Tanker' pattern scout rifle)"
    ],
    "melee_weapons": [
        "Fairbairn-Sykes British Commando Dagger (carbon steel needle point)",
        "Ontario Mark 3 Mod 0 Navy Dive Stiletto (serrated phosphate blade)",
        "Ka-Bar USMC Fighting Knife 7\" (stacked leather washer grip)",
        "Extrema Ratio Misericordia Tactical Spike (reinforced skull-crusher pommel)",
        "Telescoping hardened-steel ASP breaching bar (tungsten pry-edge)",
        "Cold Steel Trench Hawk (drop-forged 5150 carbon steel spike axe)",
        "Swedish Wetterlings Bushcraft Hatchet (hand-hammered carbon head)"
    ]
}

def roll_d6():
    return random.randint(1, 6)

def roll_d3():
    return random.randint(1, 3)

def roll_identity_profile():
    """
    Rolls identity with 40/40/20 distribution:
    - 1-40: Male (40%)
    - 41-80: Female (40%)
    - 81-100: Variations (20%):
      - 81-88: Queer / Non-Binary / Transgender Operative (Age: Gaussian >= 16)
      - 89-94: Child Prodigy with Grace (Age: 9-15)
      - 95-100: Grace-touched Animal Vessel (Age: 2-8, e.g. Raven, Hound, Stray Cat)
    """
    d100 = random.randint(1, 100)
    
    if d100 <= 40:
        gender_type = "Male"
        subtype = "Human Operative"
        raw_age = random.gauss(21.0, 3.5)
        age = max(16, int(round(raw_age)))
    elif d100 <= 80:
        gender_type = "Female"
        subtype = "Human Operative"
        raw_age = random.gauss(21.0, 3.5)
        age = max(16, int(round(raw_age)))
    else:
        var_sub = random.randint(1, 100)
        if var_sub <= 40:
            gender_type = "Queer / Non-Binary / Transgender"
            subtype = random.choice(["Non-Binary Operative (they/them)", "Transgender Woman (she/her)", "Transgender Man (he/him)", "Agender Operative (it/they)"])
            raw_age = random.gauss(20.5, 3.2)
            age = max(16, int(round(raw_age)))
        elif var_sub <= 70:
            gender_type = "Child Prodigy"
            subtype = random.choice([
                "Ward of CASTLE Intake (orphan manifesting precocious grace)",
                "Runaway Telekinetic Minor (intake flagged for extreme volatility)",
                "Juvenile Sinseed Host (unstable early manifestation)"
            ])
            age = random.randint(9, 15)
        else:
            gender_type = "Grace-Touched Animal Vessel"
            animal_species = random.choice([
                "Uplifted Carrion Raven (sinseed nestled in cranial cavity, mimics human speech)",
                "Mutated Cast-off Hound (bulky brindle mastiff carrying psychic kinetic field)",
                "Feral Tomcat (grace-conductive blackened claws, prowls investigation perimeters)"
            ])
            subtype = animal_species
            age = random.randint(2, 8)

    # Pick multicultural nationality
    nat = random.choice(NATIONALITIES_POOL)
    personality = random.choice(PERSONALITY_ARCHETYPES)
    
    # 50/50 Blasphemy strategy
    blasphemy_strategy = "Pure Specialist" if random.random() < 0.5 else "Hybrid Adaptor"

    # Select real weaponry
    weapon_hg = random.choice(REAL_WEAPONS_CATALOG["handguns"])
    weapon_melee = random.choice(REAL_WEAPONS_CATALOG["melee_weapons"])
    weapon_long = random.choice(REAL_WEAPONS_CATALOG["long_guns"])

    return {
        "roll_d100": d100,
        "gender_type": gender_type,
        "subtype": subtype,
        "age": age,
        "nationality": nat["country"],
        "name_suggestions": nat["sample_names"],
        "personality": personality,
        "blasphemy_strategy": blasphemy_strategy,
        "real_weapons": {
            "sidearm": weapon_hg,
            "melee": weapon_melee,
            "primary_long_arm": weapon_long
        }
    }

def check_sin_overflow_resistance(current_marks=0):
    die = roll_d6()
    total = die + current_marks
    passed = (die == 1) or (total <= 6)
    return {
        "die_roll": die,
        "marks_modifier": current_marks,
        "total": total,
        "passed": passed,
        "status": "CONTROL RETAINED (Gain Sin Mark)" if passed else "OVERFLOW DEFEAT (Transform into Sin)"
    }

def roll_sin_mark(existing_marks=None):
    if existing_marks is None:
        existing_marks = {}

    loc_die = roll_d6()
    chosen_by_roller = False
    if loc_die == 6:
        chosen_by_roller = True
        loc_die = random.randint(1, 5)

    location_data = SIN_MARKS_TABLE[loc_die]
    loc_name = location_data["location"]

    acquired_abilities = existing_marks.get(loc_name, [])
    available_abilities = [i for i in range(1, 7) if i not in acquired_abilities]

    if not available_abilities:
        for alt_loc in range(1, 6):
            if alt_loc != loc_die:
                alt_avail = [i for i in range(1, 7) if i not in existing_marks.get(SIN_MARKS_TABLE[alt_loc]["location"], [])]
                if alt_avail:
                    loc_die = alt_loc
                    location_data = SIN_MARKS_TABLE[loc_die]
                    loc_name = location_data["location"]
                    available_abilities = alt_avail
                    break

    ability_die = roll_d6()
    if ability_die in acquired_abilities and available_abilities:
        ability_die = random.choice(available_abilities)

    ability_text = location_data["abilities"][ability_die]
    is_evolution = len(acquired_abilities) > 0

    return {
        "location_die": 6 if chosen_by_roller else loc_die,
        "resolved_location_index": loc_die,
        "location": loc_name,
        "manifestation": location_data["description"],
        "ability_die": ability_die,
        "ability_description": ability_text,
        "is_evolution": is_evolution
    }

def simulate_squad_progression(target_cat=2, depth="Promedio"):
    """
    Simulates mission history to reach target_cat.
    CAT 1: 0 missions
    CAT 2: 1 mission
    CAT 3: 2 missions
    CAT 4: 4 missions
    CAT 5: 7 missions

    Enforces:
    - Squad size: 4-5 operatives.
    - Ascending CAT progression.
    - Squad Average CAT >= Sin CAT.
    """
    cat_mission_thresholds = {1: 0, 2: 1, 3: 2, 4: 4, 5: 7}
    num_missions = cat_mission_thresholds.get(target_cat, 0)
    
    missions = []
    total_xp = 0
    total_scrip = 0
    sin_marks = {}
    current_marks_count = 0

    sin_types = ["Ogre", "Idol", "Hound", "Centipede", "Toad", "Lord"]

    for m_idx in range(1, num_missions + 1):
        # Determine character's CAT at time of mission
        if m_idx == 1:
            char_cat = 1
        elif m_idx == 2:
            char_cat = 2
        elif m_idx <= 4:
            char_cat = 3
        else:
            char_cat = 4

        # Squad size: 4 or 5 operatives
        squad_size = random.choice([4, 5])
        
        # Determine allies' CATs around char_cat
        allies_cats = [char_cat]
        for _ in range(squad_size - 1):
            ally_cat = random.choice([max(1, char_cat - 1), char_cat, char_cat + 1])
            allies_cats.append(ally_cat)
        
        squad_avg_cat = sum(allies_cats) / squad_size
        
        # Sin CAT must be <= Squad Avg CAT (rounded or floored)
        # Sins scale upward across mission career
        max_possible_sin_cat = int(math.floor(squad_avg_cat))
        sin_cat = max(1, min(max_possible_sin_cat, 1 + (m_idx // 2)))
        
        target_sin = random.choice(sin_types)
        outcome = random.choices(["Execute", "Spare", "Hard Victory"], weights=[70, 20, 10])[0]
        earned_scrip = 5 if outcome == "Execute" else (3 if outcome == "Spare" else 2)
        total_scrip += earned_scrip

        # XP checklist
        earned_xp = random.randint(3, 4)
        total_xp += earned_xp

        # Sin Overflow check
        overflow_chance = 0.05 if depth == "Reducido" else (0.15 if depth == "Promedio" else 0.25)
        had_overflow = random.random() < overflow_chance
        overflow_result = None

        if had_overflow:
            res = check_sin_overflow_resistance(current_marks_count)
            if res["passed"]:
                mark = roll_sin_mark(sin_marks)
                loc = mark["location"]
                if loc not in sin_marks:
                    sin_marks[loc] = []
                sin_marks[loc].append(mark["ability_die"])
                current_marks_count += 1
                overflow_result = {
                    "event": "Resisted Sin Overflow",
                    "resistance_roll": res,
                    "gained_mark": mark
                }
            else:
                overflow_result = {
                    "event": "Critical Near-Overflow Traumatism",
                    "note": "Operative dragged back from the psychic brink by squad intervention; severe psychological scar sustained."
                }

        missions.append({
            "mission_number": m_idx,
            "target_sin": f"CAT {sin_cat} {target_sin}",
            "squad_size": squad_size,
            "allies_cats": allies_cats,
            "squad_avg_cat": round(squad_avg_cat, 2),
            "outcome": outcome,
            "scrip_earned": earned_scrip,
            "xp_earned": earned_xp,
            "overflow_event": overflow_result
        })

    advances_earned = total_xp // 4

    return {
        "target_cat": target_cat,
        "missions_survived": num_missions,
        "total_xp": total_xp,
        "advances_earned": advances_earned,
        "total_scrip": total_scrip,
        "sin_marks": sin_marks,
        "current_marks_count": current_marks_count,
        "mission_log": missions
    }

def main():
    parser = argparse.ArgumentParser(description="CAIN 1.0 Exorcist Mechanics & Dice Helper")
    subparsers = parser.add_subparsers(dest="command")

    # Command: identity
    subparsers.add_parser("identity", help="Roll 40/40/20 identity, Gaussian age, personality, and real weapons")

    # Command: sin-mark
    subparsers.add_parser("sin-mark", help="Roll a random Sin Mark mutation (Page 44)")

    # Command: resistance
    res_parser = subparsers.add_parser("resistance", help="Roll a Sin Overflow resistance check")
    res_parser.add_argument("--marks", type=int, default=0, help="Current number of Sin Marks")

    # Command: simulate
    sim_parser = subparsers.add_parser("simulate", help="Simulate balanced squad missions and organic leveling")
    sim_parser.add_argument("--cat", type=int, default=2, choices=[1, 2, 3, 4, 5], help="Target Category")
    sim_parser.add_argument("--depth", type=str, default="Promedio", choices=["Reducido", "Promedio", "Primario"])

    args = parser.parse_args()

    if args.command == "identity":
        ident = roll_identity_profile()
        print(json.dumps(ident, indent=2))
    elif args.command == "sin-mark":
        mark = roll_sin_mark()
        print(json.dumps(mark, indent=2))
    elif args.command == "resistance":
        res = check_sin_overflow_resistance(args.marks)
        print(json.dumps(res, indent=2))
    elif args.command == "simulate":
        sim = simulate_squad_progression(args.cat, args.depth)
        print(json.dumps(sim, indent=2))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
