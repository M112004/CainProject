---
name: cain-sin
description: Complete creation, validation, and adjudication engine for CAIN 1.0 Sins (Pecados). Supports Automatic generation, Prompt-driven generation, and Guided interview mode (/grill-me style). Strictly enforces canonical rules, the exact 3 trauma questions per Sin type, canonical domains, palaces, specific limitations, and organizes files into Pecados/{Auto,Guiado,Prompt}/Sin-(TipoPecado)-(NombreHost)-(YYYY-MM-DD)/SIN_[TYPE]_[NAME].md based on Pecados/Template/TEMPLATE_SIN.md.
---

# CAIN Sin Creation & Adjudication Engine (`/cain-sin`)

Use this skill whenever creating, reviewing, or validating Sins (*Pecados*) for CAIN 1.0 hunts. Every generated Sin must balance rich creative lore with strict mathematical and mechanical compliance with the CAIN 1.0 rulebook.

---

## The Three Creation Modes

When invoked or requested by the user, determine the desired creation mode:

### 1. Automatic Mode (`auto`)
- **Use Case**: The Director needs an immediate, fully fleshed-out Sin without prep time.
- **Workflow**:
  1. Determine or randomly select Sin Type (Ogre, Idol, Hound, Centipede, Toad, Lord) and Category (default CAT 2-3).
  2. Generate a cohesive host backstory, tragic inciting incident, and atmospheric manifestation.
  3. Answer the **exact 3 canonical trauma questions** for that type with clear forensic investigation clues.
  4. Select **3 canonical domains** that synergize with the lore, noting their canonical names and reskinned visual flavor.
  5. Structure the Palace, Pressure escalation, Traces, Combat Profile, and Severe Attack.
  6. Create directory: `Pecados/Auto/Sin-(TipoPecado)-(NombreHost)-(YYYY-MM-DD)/` (e.g. `Sin-Centipede-CalebShaw-2026-10-28`).
  7. Save the file immediately inside that folder as `SIN_[TYPE]_[NAME].md` in English, matching `Pecados/Template/TEMPLATE_SIN.md`.

### 2. User Prompt Seed Mode (`prompt`)
- **Use Case**: The user provides a brief creative premise (e.g., *"Un Hound nacido de un bombero traicionado por su jefe"* or *"A CAT 4 Toad running a high-end luxury art auction"*).
- **Workflow**:
  1. Parse the user's creative core and anchor it to the most appropriate canonical Sin Type.
  2. Adapt the host and lore around the user's premise while upholding the Sin's emotional core.
  3. Formulate truthful answers and clues for the **exact 3 canonical trauma questions** without changing a single word of the questions.
  4. Pick the 3 most fitting canonical domains from that Sin's 8 options.
  5. Complete all mechanical sheets (Execution Talisman = 6 + CAT, Pressure track, Severe Attack).
  6. Create directory: `Pecados/Prompt/Sin-(TipoPecado)-(NombreHost)-(YYYY-MM-DD)/` (e.g. `Sin-Hound-DoloresReyes-2026-10-28`).
  7. Save the final file inside as `SIN_[TYPE]_[NAME].md` and present a structured summary.

### 3. Guided Interview Mode (`guided`)
- **Use Case**: Interactive collaborative design where the user wants to make every key creative and tactical decision (similar to `/grill-me`).
- **Workflow**:
  - Walk down the design tree **one question at a time**:
    - **Step 1**: Choose Sin Type (I-VI), Form (I-III), and Category (CAT 1-5).
    - **Step 2**: Define the Host (name, background, trauma, relationship with Sin).
    - **Step 3**: Answer the 3 Canonical Trauma Questions (present the exact rulebook questions and brainstorm answers).
    - **Step 4**: Design the Palace (entrance location, interior mindscape, sensory keywords).
    - **Step 5**: Select 3 Canonical Domains (present the 8 canonical options and define their visual flair).
    - **Step 6**: Review limitations and confirm final details.
  - Create directory: `Pecados/Guiado/Sin-(TipoPecado)-(NombreHost)-(YYYY-MM-DD)/` (e.g. `Sin-Lord-ElenaRostova-2026-10-28`).
  - Compile and save the finished Sin inside as `SIN_[TYPE]_[NAME].md`.

---

## Canonical Rules & Constraints Matrix

### 1. Universal Sin Mechanics (Non-Negotiable)
- **Execution Talisman**: Always equals `6 + CAT` segments.
- **Palace Retreat Rule**: If a Sin takes 4 slashes or is reduced to 0 slashes **outside its Palace**, it retreats to its Palace until Pressure increases, healing 1 (or 2d3 if full). **A Sin can never be executed outside its Palace.**
- **Tension Talisman**: Always 3 segments. Ticks on scene transitions or a '1' on risk dice. When full, Director triggers a Tension Move.
- **Pressure Talisman**: Always 6 segments. Ticks when Tension overflows. At 6+, the situation goes Out of Control: **CAT increases by +1** and triggers the Sin-specific catastrophic escalation.
- **Trauma Questions**: Always **exactly 3 questions** taken verbatim from the Sin's reference markdown. Answering a question grants Exorcists a **Counter** (rolls 1d3 to reduce stress and slash the execution clock).
- **Domains**: Always **exactly 3 domains** chosen from the 8 canonical options of that Sin type. The underlying mechanical rules must not be altered; theming is reskinned to match the Sin's lore.

---

### 2. Comprehensive Sin Type Specifications

```
+---------------+-------------------+-----------------------+-----------------------------+-----------------------------+
| Sin Type      | Primary Emotion   | Pressure Mechanic     | Traces                      | Severe Attack (1/hunt)      |
+---------------+-------------------+-----------------------+-----------------------------+-----------------------------+
| I. OGRE       | Despair           | Miasma (0-6)          | Stumblers (Talisman 2/4/6)  | Pulverize (Severed limbs)   |
| II. IDOL      | Desire            | Cult (0-6)            | Cultists (Talisman 2/4/6)   | Marriage (Fleshy fusion)    |
| III. HOUND    | Vengeance         | Grudge (3 Targets)    | Myrmidons (Talisman 2/4/6)  | Apoplexy (Flayed skin)      |
| IV. CENTIPEDE | Hatred            | Infestation (0-6)     | Infested (Talisman 1/3/5/7) | Vitriol (Acid scars)        |
| V. TOAD       | Indulgence        | Hoard (0-6)           | Toadspawn (Talisman 1/3/5)  | Grand Finesse (Steal powers)|
| VI. LORD      | Fear              | Kingdom (0-6)         | Guards (Talisman 2/4/6)     | Judgement (Holy fire/Sin)   |
+---------------+-------------------+-----------------------+-----------------------------+-----------------------------+
```

---

#### I. OGRE ([[01_I_Ogre]])
- **The 3 Canonical Trauma Questions (Verbatim)**:
  1. *Who or what pushed you into this hole?*
  2. *Who or what is keeping you from going over the edge?*
  3. *What are you most ashamed of?*
- **The 8 Canonical Domains (Choose 3)**:
  1. `Hostile Door Patterns` (Erases doors/vehicles; maze navigation)
  2. `The Unseeing of Things` (Invisible in dark; lights fail)
  3. `The Grinding of Wheels` (Inflicts Despair affliction; group distrust)
  4. `That Awful Flesh` (Rapid regeneration on '1' risk; resists non-fire harm)
  5. `The Inevitable Place of Meat` (Rotting objects and flesh; accelerates decay)
  6. `The Lash Calls you Brother` (Crusher trace formed from exorcist's shame)
  7. `Where You Belong` (Sludge translocation; sub-zero hostile blizzard)
  8. `The Agony` (Sunken affliction; heart-in-this test)
- **Specific Limitations**:
  - Highly anti-social, self-deprecating, and conflict-averse; prefers being left alone.
  - Emotionally co-dependent with host; rarely manifests post-mortem.
  - Relies on crushing physical force; vulnerable to fire, acid, and bright illumination.

---

#### II. IDOL ([[02_II_Idol]])
- **The 3 Canonical Trauma Questions (Verbatim)**:
  1. *What is your dream?*
  2. *Why did you give up on your dream?*
  3. *Why do you think you are incapable of being loved?*
- **The 8 Canonical Domains (Choose 3)**:
  1. `Toys for Men` (Puppet strings; Collect Doll affliction)
  2. `Elevation of the Innumerable Mass` (Apostle trace with mutated blades)
  3. `Hold My Darlings` (Transfers harm to cultists; sees through cultist eyes)
  4. `That Pliable Flesh` (Shapeshifts into NPC or duplicated Exorcist)
  5. `Slumbering, I Saw a Shape in the Door` (Intrudes on rests; forced nightmares)
  6. `Taking the Ears` (Enthralls crowds; deafening unspeakable word)
  7. `The Glory` (Blinding divine form; non-cultists fall unconscious)
  8. `The Strong Scented Lips of a Whispering God` (Exposure talisman; media fallout)
- **Specific Limitations**:
  - Visible to graceless humans; seeks adulation and vanity.
  - Relies on cultists as meat shields; deeply vulnerable when isolated from devotees.
  - Emotional and psychic fragility when confronted with its unlovable core.

---

#### III. HOUND ([[03_III_Hound]])
- **The 3 Canonical Trauma Questions (Verbatim)**:
  1. *Who wronged you?*
  2. *How were you wronged?*
  3. *What are you unwilling to sacrifice?*
- **The 8 Canonical Domains (Choose 3)**:
  1. `A Shuddering Thing Through a Dark Hall` (Feeds on terror; fear suppression test)
  2. `Turning Blades, I Laughed at their Brittleness` (Armored hide; fortune roll ignores slashes)
  3. `The Catching of the Doe` (Stalks target across scenes; free opening reaction)
  4. `The Annihilation of the Wicked` (Firearms integration; absorbs guns)
  5. `The Fattening of Rage` (Grows stronger when killing grudge targets)
  6. `Rile Against Heaven` (Provokes hostility; sows feuds between exorcists)
  7. `The Measured Weight of Death` (Supernatural resilience bypassed by mythological weakness: silver, iron, heat, cold, water, sunlight)
  8. `Bloodying the Steel` (Infectious Grudge; immune to mundane weapons)
- **Specific Limitations**:
  - Least communicative; animalistic fury, twitching spasms, boiling body temperature.
  - Single-mindedly focused on its 3 designated Grudge targets.
  - Reckless aggression makes it predictable and susceptible to tactical traps and setups.

---

#### IV. CENTIPEDE ([[04_IV_Centipede]])
- **The 3 Canonical Trauma Questions (Verbatim)**:
  1. *What are you trying to escape?*
  2. *What do you hate the most about humanity?*
  3. *What do you regret the most?*
- **The 8 Canonical Domains (Choose 3)**:
  1. `The Heralds of Venom` (Pressurized sniper spit; Blinding Ague affliction)
  2. `Crumbling Into the Darkling Womb` (Corrosive aerosol melts structures)
  3. `The Knights of Decay` (Armored Juggernaut trace; acidic cloud)
  4. `Gently Rolling Down the Slope of the Abyss` (Accelerated 20% infection rate)
  5. `My Children Crawl Quietly` (Stealthy Stalker traces in pairs)
  6. `At the Core, My Rot Unfurls` (Last-stand final form upon clock fill)
  7. `I Hide My Knife in the Soft Supple Walls` (Infested flesh traps in rooms)
  8. `Making Friends With the Abattoir` (Expands clock by slaughtering bystanders)
- **Specific Limitations**:
  - Hatred manifest; hates humanity, the world, and especially its host.
  - Perversely protective of host: imprisons them alive in its Palace dungeon to force them to witness the carnage.
  - 100% CAIN execution mandate due to catastrophic viral vector.
  - Venom loses efficacy and evaporates upon the Centipede's death.

---

#### V. TOAD ([[05_V_Toad]])
- **The 3 Canonical Trauma Questions (Verbatim)**:
  1. *What do you deserve that was denied to you?*
  2. *While you were starving, who was feasting?*
  3. *Where do you draw the line?*
- **The 8 Canonical Domains (Choose 3)**:
  1. `Hotel for One` (Swallows victims into extra-dimensional gullet prison)
  2. `Greasing the Palms` (Perfumed sticky or slippery caustic bile)
  3. `The Granting of Gifts` (Regurgitates stolen weapons, vehicles, explosives)
  4. `Wolf Down the Earth` (Burrows through solid matter; devours scenery)
  5. `Sticky Fingers` (Lifts items or KP on strike)
  6. `The Artful Dodger` (Contingency flashbacks mitigate harm or deal stress)
  7. `Keeper of the Ludic Menagerie` (Pulls brainwashed servile humans from maw)
  8. `The Great Glittering Adversary` (Midan Touch; transmutes matter to gold/gems)
- **Specific Limitations**:
  - Sharp-tongued, vain, and witty; prefers verbal sparring and gloating over fleeing.
  - Greedy and impatient; can be baited or distracted by physical or conceptual wealth.
  - Relies heavily on mobility (leaping, squeezing) and gullet capacity.

---

#### VI. LORD ([[06_VI_Lord]])
- **The 3 Canonical Trauma Questions (Verbatim)**:
  1. *What did you lose?*
  2. *What is the main thing you would fix about the world?*
  3. *Who did you regret leaving behind when you ascended to your Kingdom?*
- **The 8 Canonical Domains (Choose 3)**:
  1. `Stricture of Manifestation` (Inverts gravity; shifts weather; alters architecture)
  2. `Stricture of Superiority` (Stances: Honorable Fighting, Grand Melee, Duel)
  3. `Stricture of Banishment` (Banished affliction; phasing through reality)
  4. `Stricture of Control` (Taboo list: forbids swearing, names, skin, prayer)
  5. `Stricture of Memory` (Regresses reality to historical era; alters tech)
  6. `Stricture of Narrative` (Rewinds and vetoes Exorcist roll outcomes)
  7. `Stricture of Alignment` (Enforces feudal role afflictions: Peasant, Knight, etc.)
  8. `Stricture of The Flaming Sword` (Axiomatic Guardian construct)
- **Specific Limitations**:
  - Bound to operate within or through its Kingdom construct.
  - Strictly bound by moral righteousness and legalistic strictures; cannot break its own decrees.
  - Collapses completely if the host is forced to emotionally confront the irreversibility of their tragedy.

---

## File Storage & Directory Architecture

Every Sin generated by the engine is classified into one of the four core folders inside `Pecados/`:

```
Pecados/
├── Auto/                     # Generated via Automatic mode
│   └── Sin-(Type)-(Host)-(YYYY-MM-DD)/
│       └── SIN_[TYPE]_[NAME].md
├── Guiado/                   # Generated via Guided Interview mode
│   └── Sin-(Type)-(Host)-(YYYY-MM-DD)/
│       └── SIN_[TYPE]_[NAME].md
├── Prompt/                   # Generated via User Prompt Seed mode
│   └── Sin-(Type)-(Host)-(YYYY-MM-DD)/
│       └── SIN_[TYPE]_[NAME].md
└── Template/                 # Master templates and canonical exemplars
    ├── TEMPLATE_SIN.md
    └── Sin-Ogre-ArthurVance-2026-10-28/
        └── SIN_OGRE_COLD_HEARTH.md
```

### Folder & File Naming Protocol
1. **Subfolder Name**: Strictly `Sin-(TipoPecado)-(NombreHost)-(FechaCreacion)`
   - Format: `Sin-[Ogre|Idol|Hound|Centipede|Toad|Lord]-[HostFirstNameHostLastName]-[YYYY-MM-DD]`
   - Example: `Sin-Ogre-ArthurVance-2026-10-28`
   - Example: `Sin-Hound-DoloresReyes-2026-10-28`
2. **Main File Inside**: Strictly `SIN_[TYPE]_[NAME].md`
   - Example: `SIN_OGRE_COLD_HEARTH.md`
   - Example: `SIN_HOUND_KILL_FLOOR.md`

---

## File Storage & Verification Checklist

When generating a Sin file, ensure:
1. Classification folder is selected (`Auto`, `Guiado`, or `Prompt`).
2. Directory created: `Pecados/[Category]/Sin-(TipoPecado)-(NombreHost)-(YYYY-MM-DD)/`.
3. Saved inside as: `SIN_[TYPE]_[NAME].md`.
4. Matches the exact structure of `Pecados/Template/TEMPLATE_SIN.md`.
5. Language is English for all mechanics, lore, and stat blocks.
6. The 3 Trauma questions are copied verbatim from the bestiary rules.
7. All 3 Domains explicitly state: `Based on: [[Canonical Domain Name]]`.
8. Execution Talisman is mathematically accurate: `6 + CAT`.
9. Palace specifies the 4-slash retreat rule and interior mindscape tags.
10. Includes wikilinks (`[[01_I_Ogre]]`, `[[Designing_Sins]]`, etc.) for Obsidian/Graphify integration.
