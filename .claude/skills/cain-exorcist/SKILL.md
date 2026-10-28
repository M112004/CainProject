---
name: cain-exorcist
description: Complete creation, validation, organic advancement, and loadout engine for CAIN 1.0 Exorcists. Incorporates 40/40/20 identity distribution, Gaussian age (~21, min 16; children 9-15; animals 2-8), 50/50 Blasphemy strategy, real-world weapon models, 15 canonical Agendas (Moth, Temperance, Beast, etc.), squad-balanced ascending missions, Python dice-driven Sin Marks (p. 44) aligned with narrative, first-person narrative voice, multicultural backgrounds, and diverse personalities. Saves files in Exorcistas/{Auto,Guiado,Prompt}/Exorcist-(Profundidad)-(Nombre)-(YYYY-MM-DD)/EXORCIST_[NOMBRE].md.
---

# CAIN Exorcist Creation & Advancement Engine (`/cain-exorcist`)

Use this skill whenever creating, validating, upgrading, or inspecting Exorcist operatives for CAIN 1.0 hunts. Every generated Exorcist must balance rich psychological verisimilitude and evocative first-person voice with strict adherence to the CAIN 1.0 rulebook mechanics.

---

## The Identity & Generation Core

When initiating exorcist creation, run or simulate `python scripts/cain_dice.py identity` to establish:

### 1. Gender & Demographic Distribution (40 / 40 / 20)
- **40% Male (Hombre)**: Standard human male operative.
- **40% Female (Mujer)**: Standard human female operative.
- **20% Variations**:
  - *Child Prodigy with Grace* (Ages 9 to 15): Precocious youth taken as wards by CASTLE, highly volatile grace.
  - *Grace-Touched Animal Vessel* (Ages 2 to 8): Uplifted carrion ravens, mutated hounds, or grace-conductive feral cats with an internal sinseed.
  - *Queer / Non-Binary / Transgender Operatives* (Ages 16+): Distinct gender-nonconforming identities.

### 2. Gaussian Age Calibration
- Human life expectancy in CAIN is brutally short. An exorcist over 35 is an extraordinary, grizzled statistical miracle.
- **Adult Operatives (16+)**: Determined via Gaussian curve (Mean = 21.0, Standard Deviation = 3.5, clamped at minimum 16). Most operatives are 18-24.
- **Child Prodigies**: Explicitly 9 to 15 years old.
- **Animal Vessels**: Explicitly 2 to 8 years old.
- *Rule*: Age is independent of Depth Profile (Reducido, Promedio, Primario). A CAT 3 veteran can be a 21-year-old survivor who endured two horrifying hunts.

### 3. Multiculturalism & Verisimilitude
- Operatives must reflect authentic global diversity: Poland, Germany, Japan, Nigeria, Brazil, France, Mexico, United Kingdom, South Korea, United States, etc.
- Cultural background shapes their idiom, upbringing, and pre-CAIN life without cartoonish caricature.

### 4. Personality Diversity
- Move beyond uniform grim soldiers. CAIN operatives exhibit colorful, unhinged psychological coping mechanisms:
  - *Compulsive Chain-Smoking Gambler*: Bets on casualty rates and treats hunts like card hands.
  - *Morbidly Cheerful Dark-Humorist*: Cracks gallows humor in burning basements, names severed limbs.
  - *Cynical Exhausted Pragmatist*: Counts ammo, hates paperwork, drinks cold black coffee.
  - *Fanatical Apocalyptic Zealot*: Views Sins as biblical scourges, recites scripture under fire.
  - *Flamboyant Theatrical Narcissist*: Treats psychic violence as performance art, demands dramatic entrances.
  - *Paranoid Superstitious Hermit*: Carries salt vials, checks locks six times, whispers to wall corners.
  - *Manic Scientific Perfectionist*: Collects tissue samples mid-firefight, speaks at frantic speed.

### 5. Blasphemy Doctrine (50 / 50 Dice Roll)
- **50% Pure Specialist**: Devotes 100% of psychic focus to a single primary Blasphemy, unlocking deep powers and keeping Sin Overflow cap intact.
- **50% Hybrid Adaptor**: Spends an advance to incorporate a secondary Blasphemy (reduces Sin Overflow cap by -1 and increases advance XP requirement by +1).

### 6. Real-World Armory & Unique Gear
- Exorcists must never carry generic "service weapons". Specify concrete, real-world firearm and melee models:
  - *Handguns*: SIG Sauer P226 Nitron 9mm, Glock 19 Gen 5, Heckler & Koch USP .45 ACP, Colt Python 4" .357 Magnum, Beretta 92FS, CZ 75 SP-01 Shadow, Browning Hi-Power, Walther PPK/S.
  - *Long Arms*: Benelli M4 Super 90 12ga, Mossberg 590A1, Heckler & Koch MP5A3, Steyr AUG A3, Franchi SPAS-12, Colt M4A1 SOPMOD, Lee-Enfield No. 4 Mk I.
  - *Melee*: Fairbairn-Sykes British Commando Dagger, Ontario Mark 3 Mod 0 Dive Stiletto, Ka-Bar USMC Fighting Knife, Telescoping hardened-steel breaching bar, Cold Steel Trench Hawk.

---

## Canonical Agendas Matrix (Official 15)

Ensure all Agendas use their exact canonical names from the rulebook:
1. **BEAST** (Triggers: *Get into a fight* / *Hold Back*) — Abilities: Insects!!!, I'll take you down with me, Rule of Nature, Red Muscle, Bare Teeth.
2. **DOOMED** (Triggers: *Demonstrate your humanity* / *Demonstrate your distance from humanity*. Requires a Sin Mark) — Abilities: Xenoflesh, Humanity's Last Breath, Quickening, Sympathetic Mutation, Metamorphosis.
3. **FIREBUG** (Triggers: *Solve Problems Creatively* / *Take the simple solution*) — Abilities: Jack!, Always a way, Oilfinger, Extra Parts, Weak Spot.
4. **GUARDIAN** (Triggers: *Protect your people* / *Leave nobody behind*) — Abilities: Iron Wall, The Excessive Agony of Moving Forward, Castle, Centerweight, Painkiller.
5. **LONER** (Triggers: *Demonstrate your superior skill* / *Let the mask slip*) — Abilities: Dust to Dust, Silent Strike, I'll do it myself, Rook, It's Nothing.
6. **HARDLINE** (Triggers: *Follow Orders* / *Disobey Orders*) — Abilities: Black Suit, Mea Culpa, Eliminate the Stain, Single Minded, By the Book.
7. **MACHINE** (Triggers: *Put the work before your own needs* / *Take a break*) — Abilities: The Work, Brain Burst, Second Wind, Overtime, Neat Little Universe.
8. **MOTH** (Triggers: *Uncover hidden or uncomfortable truths about the world* / *Uncover hidden or uncomfortable truths about yourself*) — Abilities: Psyche Jewel, Alienation (+3 Sin Cap), Rapture, Larval, Unveil.
9. **TEMPERANCE** (Triggers: *Put people before the mission* / *Harm someone intentionally*) — Abilities: Healer, Focused, Savior Complex, Care, Gentleness.
10. **TORCH** (Triggers: *Lead from the front* / *Let another take the lead*) — Abilities: Joy Luck Wind Thrower, Hot Blooded, Font of Power, Recollect, Strive.
11. **DEPARTED** (Special agenda for dead characters: *That Terrible Weight*).
12. **SHADOW** (Triggers: *Outshine your rival* / *Let your rival outshine you*. Requires picking a rival) — Abilities: Catch Up, Synchronize, You Can't Die Now, Shadow Seed, Pincer Technique.
13. **SORCERER** (Triggers: *Demonstrate flashy displays of power* / *Invite catastrophe*) — Abilities: Perfect Technique, Cantrip, Finishing Move, Mimic technique, Weave.
14. **SONGBIRD** (Triggers: *Get someone to do your bidding* / *Do something selfless*) — Abilities: Codependency, Spiral, Strings, White Fiber, Fascination.
15. **SURVIVOR** (Triggers: *Survive*. Passive: *Will to Live* — +1 max stress, 1 in 6 chance of ignoring instant death).

---

## Narrative Voice: Hybrid Immersive Format

- **First-Person Voice (`I / My`)**:
  - *The Five Inquiries*: Written directly in the character's voice.
  - *Dossier & Narrative Profile*: Personal evaluation, internal thoughts on CASTLE, psychological drive.
  - *Mission Ledger*: First-person chronicle of each hunt, tactical blunders, and psychological scars.
- **Third-Person Functional Character Sheet**:
  - The 10 Skills, Abilities, Blasphemies, Kit, and Health Trackers maintain clean game tables with first-person operational notes.
- **Language**: English strictly for the character file, regardless of user prompt language or character nationality.

---

## Squad Missions & Ascending CAT Progression

When generating past missions for Promedio or Primario characters:
1. **Squad Composition**: Always show 4 to 5 operatives per hunt.
2. **Squad Balance Rule**: The squad's average CAT must be **EQUAL TO OR GREATER** than the Sin's CAT:
   $$\text{Squad Average CAT} \ge \text{Target Sin CAT}$$
3. **Ascending Progression**: Missions must progress chronologically from lower CAT to higher CAT (e.g. Mission 1 against CAT 1; Mission 2 against CAT 2; later missions against CAT 3-5).

---

## Sin Marks & Narrative Alignment Rule

- All Sin Marks must be rolled using `scripts/cain_dice.py sin-mark`.
- **Strict Anatomical Alignment**: If an exorcist sustains a Sin Mark, the physical mutation and Question 4 (*"Is your hand your hand?"*) MUST strictly match the rolled body location:
  - *Location 1 (EYES)*: Sclera, pupils, second sight.
  - *Location 2 (JAW)*: Teeth, pharyngeal jaw, venom, speech.
  - *Location 3 (BACK OR CHEST)*: Spines, ribs, scales, organ filtering.
  - *Location 4 (ARMS OR HANDS)*: Fingers, claws, tendons, bone blades.
  - *Location 5 (SKIN, HAIR, LEGS)*: Digitigrade gait, leaping, wall-climbing, skin translucency.
  *Never describe hand mutations in Question 4 if the mechanical Sin Mark is in the legs or eyes!*

---

## File Storage & Directory Architecture

```
Exorcistas/
├── Auto/                     # Generated via Automatic mode
│   └── Exorcist-(Profundidad)-(Nombre)-(YYYY-MM-DD)/
│       └── EXORCIST_[NOMBRE].md
├── Guiado/                   # Generated via Guided Interview mode
│   └── Exorcist-(Profundidad)-(Nombre)-(YYYY-MM-DD)/
│       └── EXORCIST_[NOMBRE].md
├── Prompt/                   # Generated via Prompt Seed mode
│   └── Exorcist-(Profundidad)-(Nombre)-(YYYY-MM-DD)/
│       └── EXORCIST_[NOMBRE].md
└── Template/                 # Master template and reference exemplar
    ├── TEMPLATE_EXORCIST.md
    └── Exorcist-Primario-VanceKowalski-2026-10-28/
        └── EXORCIST_VANCE_KOWALSKI.md
```

### Folder & File Naming Protocol
1. **Subfolder Name**: Strictly `Exorcist-(Profundidad)-(Nombre)-(FechaCreacion)`
2. **Main File Inside**: Strictly `EXORCIST_[NOMBRE].md`
