# CAIN: Claude CLI Project & TTRPG Knowledge Vault

An interconnected Markdown knowledge vault, AI agent skill suite, and character repository for **CAIN 1.0**, the tabletop role-playing game of psychic horror, anomaly investigation, and brutal exorcism created by Tom Parkinson-Morgan (Tom Bloom).

---

## Quick CLI Access

Open this project directly in Claude Code from any Windows terminal prompt (CMD or PowerShell):

```cmd
CAIN
```

*(Configured via `C:\Users\mique\.local\bin\cain.cmd`)*

---

## Project Structure

```text
E:\CainProject/
├── CLAUDE.md                   # Operational directives, tone rules, and skill mappings
├── refresh_graph.ps1           # Knowledge graph and Obsidian vault synchronization script
├── .gitignore                  # Git exclusions (PDF source rulebooks, Python caches, temp files)
├── .claude/
│   └── skills/                 # Custom Claude CLI skill suite
│       ├── cain-sin/           # Sin creation engine (Auto, Prompt, Guided), rules, and traumas
│       ├── cain-rules/         # Action rolls, consequences, agony, talismans, and category scaling
│       ├── cain-exorcist/      # Exorcist creation and advancement (Reducido, Promedio, Primario)
│       ├── cain-mission/       # Hunt phases, clue networks, traumas, and Sin encounter design
│       └── cain-graph/         # Graphify AST queries, wikilinks, and Obsidian sync
├── Exorcistas/                 # Exorcist operative character repository
│   ├── Auto/                   # Operatives generated via Automatic mode
│   │   ├── Exorcist-Reducido-KlausVander-2026-10-28/
│   │   └── Exorcist-Promedio-MayaLin-2026-10-28/
│   ├── Guiado/                 # Operatives generated via Guided Interview mode
│   ├── Prompt/                 # Operatives generated via Prompt Seed mode
│   └── Template/               # Master template and reference exemplar
│       ├── TEMPLATE_EXORCIST.md
│       └── Exorcist-Primario-VanceKowalski-2026-10-28/
├── Pecados/                    # Anomaly and Sin repository
│   ├── Auto/                   # Sins generated via Automatic mode
│   │   ├── Sin-Hound-DoloresReyes-2026-10-28/
│   │   └── Sin-Toad-DesmondFerreira-2026-10-28/
│   ├── Guiado/                 # Sins generated via Guided Interview mode
│   ├── Prompt/                 # Sins generated via Prompt Seed mode
│   └── Template/               # Master template and reference exemplar
│       ├── TEMPLATE_SIN.md
│       └── Sin-Ogre-ArthurVance-2026-10-28/
├── knowledge/                  # Modular Markdown vault for LLM ingestion
│   ├── 00_Overview_and_Quick_Reference/ # Master index and quick reference sheets
│   ├── 01_Lore_and_Setting/    # As Above So Below, Shadow War, Sins, and The Flesh
│   ├── 02_Rules_and_System/    # Action Roll, Consequences, Agony, and Category
│   ├── 03_The_Exorcist/        # Skills, Agendas, The Body, Kit, and Sin Marks (D66)
│   ├── 04_The_Twelve_Blasphemies/ # Tension, Ardence, Flux, Vector, Gate, and all disciplines
│   ├── 05_The_Hunt/            # 6 Hunt phases, Investigations, and Conflict Scenes
│   ├── 06_Directing_CAIN/      # Director principles, mystery structure, and Sin design
│   ├── 07_The_Sins_and_Bestiary/ # Ogre, Idol, Hound, Centipede, Toad, Lord, and Binders
│   └── 08_Reference_and_Index/ # Rulebook credits, pitch, and canonical index
├── assets/
│   ├── images/                 # Native rulebook images and visual references
│   └── tables/                 # High-resolution visual table crops and sheets
└── scripts/
    ├── build_cain_knowledge.py # Pipeline extracting Markdown, tables, and wikilinks
    ├── cain_dice.py            # Python CLI dice engine (identity, Sin marks, overflow, squad simulation)
    └── extract_tables_crops.py # Renderer for high-res visual table and sheet crops
```

---

## Claude CLI Skills

The repository includes specialized command skills tailored to CAIN 1.0 mechanics:

- `/cain-sin`: Generate and validate Sins across three creation modes (Auto, Prompt, Guided). Enforces canonical three-trauma questions, domains, palaces, and limitations. Saves output directly to `Pecados/`.
- `/cain-rules`: Adjudicate action rolls (Hard, Risky, Straight), consequences, upsides, Divine Agony, and Category scaling.
- `/cain-exorcist`: Build, advance, validate, and equip Exorcists across three Depth Profiles (Reducido, Promedio, Primario). Enforces Level 1 baselines, organic mission leveling up to target CAT, canonical skills, Blasphemies, Agendas, and Sin Mark mutations.
- `/cain-mission`: Structure procedural horror investigations, clue networks, Traumas, and Execution Talismans.
- `/cain-graph`: Inspect wikilinks, topological clusters, and execute knowledge sync.

---

## Python Mechanics & Dice CLI

The `scripts/cain_dice.py` script provides authentic, non-deterministic random rolls for character generation and mission progression:

```bash
# Roll 40/40/20 identity, Gaussian age, personality, and real weapons
py scripts/cain_dice.py identity

# Roll a canonical D66 Sin Mark mutation (Page 44)
py scripts/cain_dice.py sin-mark

# Check Sin Overflow resistance
py scripts/cain_dice.py resistance --sin 4 --dice 3

# Simulate squad mission progression and organic leveling
py scripts/cain_dice.py simulate --target-cat 3
```

---

## Knowledge Graph & Obsidian Vault

To refresh the AST Knowledge Graph and regenerate the Obsidian Vault:

```powershell
./refresh_graph.ps1
```

- Open `graphify-out/obsidian/` in **Obsidian** to view the live interactive wikilink graph, canvas, and community clusters.
- Inspect `graphify-out/GRAPH_REPORT.md` for fast, token-efficient topological analysis of the ruleset.

---

## Credits & Attribution

- **CAIN** is written and designed by **Tom Parkinson-Morgan** (Tom Bloom / @Orbitaldropkick / Massif Press).
- This repository is a companion tool, knowledge vault, and AI-assisted character manager. It does not replace the official rulebook.
