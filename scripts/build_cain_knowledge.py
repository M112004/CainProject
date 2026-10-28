import os
import re
from pathlib import Path
import pymupdf
import pymupdf4llm

ROOT_DIR = Path("E:/CainProject")
PDF_PATH = ROOT_DIR / "CAIN_1.0.pdf"
KNOWLEDGE_DIR = ROOT_DIR / "knowledge"
IMAGES_DIR = ROOT_DIR / "assets" / "images"
TABLES_DIR = ROOT_DIR / "assets" / "tables"

# Define document modules and their page ranges (1-indexed)
SECTIONS = [
    {
        "folder": "00_Overview_and_Quick_Reference",
        "file": "INDEX.md",
        "title": "CAIN 1.0 Master Vault Index",
        "pages": [],  # custom generated index
        "wikilinks": ["Quick_Reference_Guide", "Character_and_Sin_Sheets", "As_Above_So_Below", "Core_Mechanics_and_Action_Roll", "Exorcist_Overview_and_Skills", "The_Twelve_Blasphemies", "Phases_of_The_Hunt", "The_Sins_and_Bestiary"],
        "tables": []
    },
    {
        "folder": "00_Overview_and_Quick_Reference",
        "file": "Quick_Reference_Guide.md",
        "title": "CAIN Quick Reference Guide & Adjudication Tables",
        "pages": [78],
        "wikilinks": ["Core_Mechanics_and_Action_Roll", "Consequences_and_Upsides", "Divine_Agony_and_Talismans", "Category_and_Mundane_vs_Supernatural"],
        "tables": ["rules_index_table_p78.png"]
    },
    {
        "folder": "00_Overview_and_Quick_Reference",
        "file": "Character_and_Sin_Sheets.md",
        "title": "Official Character, Ability & Talisman Sheets",
        "pages": [79, 80, 81],
        "wikilinks": ["Exorcist_Overview_and_Skills", "Agendas", "The_Twelve_Blasphemies", "Divine_Agony_and_Talismans"],
        "tables": ["character_sheet_advancement_p79.png", "character_sheet_abilities_p80.png", "talisman_investigation_sheet_p81.png"]
    },
    {
        "folder": "01_Lore_and_Setting",
        "file": "01_As_Above_So_Below.md",
        "title": "As Above, So Below - The World of CAIN",
        "pages": [1, 2, 3, 4, 5],
        "wikilinks": ["The_Shadow_War_and_The_Legion", "Sins_and_The_Flesh", "Core_Mechanics_and_Action_Roll"],
        "tables": []
    },
    {
        "folder": "01_Lore_and_Setting",
        "file": "02_The_Shadow_War_and_The_Legion.md",
        "title": "The Shadow War, The Legion & CAIN Protocol",
        "pages": [50, 51],
        "wikilinks": ["01_As_Above_So_Below", "Sins_and_The_Flesh", "Phases_of_The_Hunt"],
        "tables": []
    },
    {
        "folder": "01_Lore_and_Setting",
        "file": "03_Sins_and_The_Flesh.md",
        "title": "Sins, The Psychic Sea, and The Flesh",
        "pages": [51, 52, 53, 54, 55],
        "wikilinks": ["Category_and_Mundane_vs_Supernatural", "The_Twelve_Blasphemies", "Investigation_and_Traumas", "The_Sins_and_Bestiary"],
        "tables": []
    },
    {
        "folder": "02_Rules_and_System",
        "file": "01_Core_Mechanics_and_Action_Roll.md",
        "title": "Core Mechanics & The Action Roll",
        "pages": [6, 7],
        "wikilinks": ["Consequences_and_Upsides", "Divine_Agony_and_Talismans", "Category_and_Mundane_vs_Supernatural"],
        "tables": []
    },
    {
        "folder": "02_Rules_and_System",
        "file": "02_Consequences_and_Upsides.md",
        "title": "Consequences, Complications & Upsides",
        "pages": [8],
        "wikilinks": ["Core_Mechanics_and_Action_Roll", "Divine_Agony_and_Talismans", "The_Body_Stress_and_Injuries"],
        "tables": []
    },
    {
        "folder": "02_Rules_and_System",
        "file": "03_Divine_Agony_and_Talismans.md",
        "title": "Divine Agony & Talismans (Clocks & Seals)",
        "pages": [9],
        "wikilinks": ["Core_Mechanics_and_Action_Roll", "The_Body_Stress_and_Injuries", "Conflict_Scenes"],
        "tables": []
    },
    {
        "folder": "02_Rules_and_System",
        "file": "04_Category_and_Mundane_vs_Supernatural.md",
        "title": "Category Scales & Mundane vs Supernatural Disparity",
        "pages": [10],
        "wikilinks": ["Core_Mechanics_and_Action_Roll", "The_Twelve_Blasphemies", "Sins_and_The_Flesh"],
        "tables": []
    },
    {
        "folder": "03_The_Exorcist",
        "file": "01_Exorcist_Overview_and_Skills.md",
        "title": "The Exorcist & The Nine Skills",
        "pages": [11, 12, 13],
        "wikilinks": ["Agendas", "The_Twelve_Blasphemies", "The_Body_Stress_and_Injuries", "Character_Creation_and_Advances"],
        "tables": []
    },
    {
        "folder": "03_The_Exorcist",
        "file": "02_Agendas.md",
        "title": "Agendas, Roles & Trigger Mechanics",
        "pages": [14, 24, 25, 26],
        "wikilinks": ["Exorcist_Overview_and_Skills", "Character_Creation_and_Advances"],
        "tables": []
    },
    {
        "folder": "03_The_Exorcist",
        "file": "03_The_Body_Stress_and_Injuries.md",
        "title": "The Body: Stress, Injuries, Death & Afflictions",
        "pages": [16, 17],
        "wikilinks": ["Divine_Agony_and_Talismans", "Sin_Marks", "Conflict_Scenes"],
        "tables": []
    },
    {
        "folder": "03_The_Exorcist",
        "file": "04_Kit_and_Weapons.md",
        "title": "Kit, Weapons, Armor & Expansion",
        "pages": [17, 40, 41, 42, 43],
        "wikilinks": ["Exorcist_Overview_and_Skills", "Category_and_Mundane_vs_Supernatural", "Conflict_Scenes"],
        "tables": ["weapons_and_kit_table_p43.png"]
    },
    {
        "folder": "03_The_Exorcist",
        "file": "05_Sin_Marks.md",
        "title": "Sin Marks & Flesh Mutations (D66 Table)",
        "pages": [16, 44],
        "wikilinks": ["The_Body_Stress_and_Injuries", "Sins_and_The_Flesh", "The_Twelve_Blasphemies"],
        "tables": ["sin_marks_table_p44.png"]
    },
    {
        "folder": "03_The_Exorcist",
        "file": "06_Character_Creation_and_Advances.md",
        "title": "Character Creation, Advances & XP Progression",
        "pages": [23],
        "wikilinks": ["Exorcist_Overview_and_Skills", "Agendas", "The_Twelve_Blasphemies", "Character_and_Sin_Sheets"],
        "tables": []
    },
    {
        "folder": "04_The_Twelve_Blasphemies",
        "file": "01_Blasphemies_System.md",
        "title": "Blasphemies System: Psyche, Psyche Burst, Blast & Tags",
        "pages": [14, 15, 27],
        "wikilinks": ["Category_and_Mundane_vs_Supernatural", "Divine_Agony_and_Talismans", "02_Tension", "03_Ardence"],
        "tables": []
    },
    {
        "folder": "04_The_Twelve_Blasphemies",
        "file": "02_Tension.md",
        "title": "Blasphemy 01: Tension (Wires, Cords & Kinetic Pull)",
        "pages": [28],
        "wikilinks": ["01_Blasphemies_System", "Conflict_Scenes"],
        "tables": []
    },
    {
        "folder": "04_The_Twelve_Blasphemies",
        "file": "03_Ardence.md",
        "title": "Blasphemy 02: Ardence (Psychic Fire & Solar Pyre)",
        "pages": [29],
        "wikilinks": ["01_Blasphemies_System", "Conflict_Scenes"],
        "tables": []
    },
    {
        "folder": "04_The_Twelve_Blasphemies",
        "file": "04_Flux.md",
        "title": "Blasphemy 03: Flux (Liquefaction & Blood Transmutation)",
        "pages": [30],
        "wikilinks": ["01_Blasphemies_System", "Conflict_Scenes"],
        "tables": []
    },
    {
        "folder": "04_The_Twelve_Blasphemies",
        "file": "05_Vector.md",
        "title": "Blasphemy 04: Vector (Directional Force & Acceleration)",
        "pages": [31],
        "wikilinks": ["01_Blasphemies_System", "Conflict_Scenes"],
        "tables": []
    },
    {
        "folder": "04_The_Twelve_Blasphemies",
        "file": "06_Gate.md",
        "title": "Blasphemy 05: Gate (Spatial Rifts & Portal Punctures)",
        "pages": [32],
        "wikilinks": ["01_Blasphemies_System", "Conflict_Scenes"],
        "tables": []
    },
    {
        "folder": "04_The_Twelve_Blasphemies",
        "file": "07_Smother.md",
        "title": "Blasphemy 06: Smother (Acoustic Silence & Void Dampening)",
        "pages": [33],
        "wikilinks": ["01_Blasphemies_System", "Conflict_Scenes"],
        "tables": []
    },
    {
        "folder": "04_The_Twelve_Blasphemies",
        "file": "08_Whisper.md",
        "title": "Blasphemy 07: Whisper (Telepathy, Memetics & Hallucinations)",
        "pages": [34, 35],
        "wikilinks": ["01_Blasphemies_System", "Investigation_and_Traumas"],
        "tables": []
    },
    {
        "folder": "04_The_Twelve_Blasphemies",
        "file": "09_Bind.md",
        "title": "Blasphemy 08: Bind (Psychic Chains & Gravitational Anchor)",
        "pages": [36],
        "wikilinks": ["01_Blasphemies_System", "Conflict_Scenes"],
        "tables": []
    },
    {
        "folder": "04_The_Twelve_Blasphemies",
        "file": "10_Palace.md",
        "title": "Blasphemy 09: Palace (Pocket Dimension & Mental Sanctuary)",
        "pages": [37],
        "wikilinks": ["01_Blasphemies_System", "Investigation_and_Traumas"],
        "tables": []
    },
    {
        "folder": "04_The_Twelve_Blasphemies",
        "file": "11_Jaunt.md",
        "title": "Blasphemy 10: Jaunt (Micro-Teleportation & Dimension Stride)",
        "pages": [38],
        "wikilinks": ["01_Blasphemies_System", "Conflict_Scenes"],
        "tables": []
    },
    {
        "folder": "04_The_Twelve_Blasphemies",
        "file": "12_Sympathy.md",
        "title": "Blasphemy 11: Sympathy (Shared Resonance & Pain Reflection)",
        "pages": [39],
        "wikilinks": ["01_Blasphemies_System", "The_Body_Stress_and_Injuries"],
        "tables": []
    },
    {
        "folder": "05_The_Hunt",
        "file": "01_Phases_of_The_Hunt.md",
        "title": "The Six Phases of The Hunt",
        "pages": [18, 19, 20, 21],
        "wikilinks": ["Investigation_and_Traumas", "Conflict_Scenes", "Creating_Investigations"],
        "tables": []
    },
    {
        "folder": "05_The_Hunt",
        "file": "02_Investigation_and_Traumas.md",
        "title": "Investigation, Traumas & Clue Unraveling",
        "pages": [19, 20],
        "wikilinks": ["Phases_of_The_Hunt", "Divine_Agony_and_Talismans", "Sins_and_The_Flesh"],
        "tables": []
    },
    {
        "folder": "05_The_Hunt",
        "file": "03_Conflict_Scenes.md",
        "title": "Conflict Scenes, Rounds, Positioning & Actions",
        "pages": [21, 22],
        "wikilinks": ["Core_Mechanics_and_Action_Roll", "Divine_Agony_and_Talismans", "The_Sins_and_Bestiary"],
        "tables": []
    },
    {
        "folder": "06_Directing_CAIN",
        "file": "01_Running_CAIN_and_Safety.md",
        "title": "Director Principles, Safety First & Pacing",
        "pages": [45, 46, 47],
        "wikilinks": ["Creating_Investigations", "Designing_Sins", "Phases_of_The_Hunt"],
        "tables": []
    },
    {
        "folder": "06_Directing_CAIN",
        "file": "02_Creating_Investigations.md",
        "title": "Creating Investigations, Clue Webs & Pressure Clocks",
        "pages": [48, 49],
        "wikilinks": ["Running_CAIN_and_Safety", "Designing_Sins", "Investigation_and_Traumas"],
        "tables": []
    },
    {
        "folder": "06_Directing_CAIN",
        "file": "03_Designing_Sins.md",
        "title": "Designing Sins: Domains, Palaces, Tension Moves & Execution Talismans",
        "pages": [53, 54, 55],
        "wikilinks": ["Sins_and_The_Flesh", "The_Sins_and_Bestiary", "Divine_Agony_and_Talismans"],
        "tables": []
    },
    {
        "folder": "07_The_Sins_and_Bestiary",
        "file": "01_I_Ogre.md",
        "title": "Sin I: Ogre - Anatomical Ruin, Brute Carnage & Sunder",
        "pages": [56, 57, 58],
        "wikilinks": ["Designing_Sins", "Conflict_Scenes", "Divine_Agony_and_Talismans"],
        "tables": ["sin_ogre_stat_block_p56.png", "sin_ogre_talismans_p57.png"]
    },
    {
        "folder": "07_The_Sins_and_Bestiary",
        "file": "02_II_Idol.md",
        "title": "Sin II: Idol - Hypnotic Vanity, Devotion & Aesthetic Mutilation",
        "pages": [59, 60, 61],
        "wikilinks": ["Designing_Sins", "Conflict_Scenes", "Investigation_and_Traumas"],
        "tables": ["sin_idol_stat_block_p59.png", "sin_idol_talismans_p60.png"]
    },
    {
        "folder": "07_The_Sins_and_Bestiary",
        "file": "03_III_Hound.md",
        "title": "Sin III: Hound - Pursuit Predator, Blood Tracking & Ambush",
        "pages": [62, 63, 64],
        "wikilinks": ["Designing_Sins", "Conflict_Scenes", "Phases_of_The_Hunt"],
        "tables": ["sin_hound_stat_block_p62.png", "sin_hound_talismans_p63.png"]
    },
    {
        "folder": "07_The_Sins_and_Bestiary",
        "file": "04_IV_Centipede.md",
        "title": "Sin IV: Centipede - Segmented Infestation, Burrowing & Swarm",
        "pages": [65, 66, 67],
        "wikilinks": ["Designing_Sins", "Conflict_Scenes", "Investigation_and_Traumas"],
        "tables": ["sin_centipede_stat_block_p65.png", "sin_centipede_talismans_p66.png"]
    },
    {
        "folder": "07_The_Sins_and_Bestiary",
        "file": "05_V_Toad.md",
        "title": "Sin V: Toad - Gluttony, Corrosive Bile & Swallowing Maw",
        "pages": [68, 69, 70],
        "wikilinks": ["Designing_Sins", "Conflict_Scenes", "The_Body_Stress_and_Injuries"],
        "tables": ["sin_toad_stat_block_p68.png", "sin_toad_talismans_p69.png"]
    },
    {
        "folder": "07_The_Sins_and_Bestiary",
        "file": "06_VI_Lord.md",
        "title": "Sin VI: Lord - Psychic Domination, Puppetry & Royal Blasphemy",
        "pages": [71, 72, 73],
        "wikilinks": ["Designing_Sins", "Conflict_Scenes", "08_Whisper"],
        "tables": ["sin_lord_stat_block_p71.png", "sin_lord_talismans_p72.png"]
    },
    {
        "folder": "07_The_Sins_and_Bestiary",
        "file": "07_Mundane_Opponents_and_Binders.md",
        "title": "Mundane Opponents, Security Operatives & Binders (Human Occultists)",
        "pages": [74, 75, 76, 77],
        "wikilinks": ["Conflict_Scenes", "The_Shadow_War_and_The_Legion"],
        "tables": ["mundane_opponents_table_p76.png", "binders_stat_table_p77.png"]
    },
    {
        "folder": "08_Reference_and_Index",
        "file": "01_Back_Cover_and_Credits.md",
        "title": "CAIN Credits & Overview Pitch",
        "pages": [82],
        "wikilinks": ["01_As_Above_So_Below", "Quick_Reference_Guide"],
        "tables": []
    }
]

def get_page_images(page_idx):
    """Find all images matching page_idx+1 in IMAGES_DIR."""
    prefix = f"page_{page_idx+1:02d}_"
    imgs = [f.name for f in IMAGES_DIR.glob(f"{prefix}*")]
    return sorted(imgs)

def generate_index_content():
    content = [
        "# CAIN 1.0 Master Knowledge Vault & Rules Directive",
        "",
        "> **CAIN**: A tabletop role-playing game of psychic horror, anomaly investigation, and brutal exorcism.",
        "> Created by **Tom Parkinson-Morgan** (Tom Bloom), 2024.",
        "",
        "## Vault Structure & Navigation",
        "",
        "### 00. Overview & Reference Sheets",
        "- [[Quick_Reference_Guide]]: Core adjudication formulas, roll ladders, consequences, and quick index.",
        "- [[Character_and_Sin_Sheets]]: Official character sheet, ability registration sheet, and talisman tracking grids.",
        "",
        "### 01. Lore & Setting",
        "- [[01_As_Above_So_Below]]: World foundation, the psychic sea, human trauma, and the emergence of Sins.",
        "- [[02_The_Shadow_War_and_The_Legion]]: CAIN supranational authority, Legion operatives, and containment protocol.",
        "- [[03_Sins_and_The_Flesh]]: Nature of Sins, Categories, Domains, Palaces, and Traumas.",
        "",
        "### 02. Rules & System Engine",
        "- [[01_Core_Mechanics_and_Action_Roll]]: Action Rolls, Hard / Risky / Straight rolls, Admin & Fate rolls.",
        "- [[02_Consequences_and_Upsides]]: Adjudicating failure, ticking clocks, complications, and upsides.",
        "- [[03_Divine_Agony_and_Talismans]]: Burning wounds for psychic breakthroughs and talisman segment resolution.",
        "- [[04_Category_and_Mundane_vs_Supernatural]]: Category scale (CAT 0 to 5) and supernatural disparity rules.",
        "",
        "### 03. The Exorcist",
        "- [[01_Exorcist_Overview_and_Skills]]: Character archetype and the 9 physical, mental, and spiritual skills.",
        "- [[02_Agendas]]: Roles, triggers, and experience advancement paths.",
        "- [[03_The_Body_Stress_and_Injuries]]: Tracking Stress, lethal Injuries, instant death, and afflictions.",
        "- [[04_Kit_and_Weapons]]: Loadouts, equipment tags, armor, and weapon damage categories.",
        "- [[05_Sin_Marks]]: The D66 Flesh mutation and corruption table.",
        "- [[06_Character_Creation_and_Advances]]: Step-by-step character generation and career survival.",
        "",
        "### 04. The Twelve Blasphemies",
        "- [[01_Blasphemies_System]]: Psyche reserves, Psyche Burst, Blast, and manifestation tags.",
        "- [[02_Tension]]: Tension - Kinetic wire manipulation and suspension.",
        "- [[03_Ardence]]: Ardence - Thermic combustion and radiant pyres.",
        "- [[04_Flux]]: Flux - Fluid transmutation and biological liquefaction.",
        "- [[05_Vector]]: Vector - Directional momentum and kinetic redirection.",
        "- [[06_Gate]]: Gate - Dimensional tears and spatial punctures.",
        "- [[07_Smother]]: Smother - Sensory void and acoustic dampening.",
        "- [[08_Whisper]]: Whisper - Telepathic intrusion and cognitive memetics.",
        "- [[09_Bind]]: Bind - Gravitational shackles and supernatural anchors.",
        "- [[10_Palace]]: Palace - Pocket sanctum and mindscape architecture.",
        "- [[11_Jaunt]]: Jaunt - Micro-teleportation and planar stride.",
        "- [[12_Sympathy]]: Sympathy - Shared bio-resonance and mirrored injury.",
        "",
        "### 05. The Hunt",
        "- [[01_Phases_of_The_Hunt]]: The 6 canonical phases from Briefing to Execution.",
        "- [[02_Investigation_and_Traumas]]: Unraveling clue webs and cracking psychic traumas.",
        "- [[03_Conflict_Scenes]]: Turn order, spatial tactical positioning, and combat execution.",
        "",
        "### 06. Directing CAIN",
        "- [[01_Running_CAIN_and_Safety]]: Safety tools, table principles, and pacing guidelines.",
        "- [[02_Creating_Investigations]]: Designing mystery structures, clue networks, and time pressure.",
        "- [[03_Designing_Sins]]: Building unique Sins, tension moves, and custom Execution Talismans.",
        "",
        "### 07. Sins Bestiary & Opponents",
        "- [[01_I_Ogre]]: Sin I - Ogre (Brute carnage, crushing weight, sunder).",
        "- [[02_II_Idol]]: Sin II - Idol (Hypnotic devotion, mass adoration, aesthetic agony).",
        "- [[03_III_Hound]]: Sin III - Hound (Relentless stalker, blood pursuit, ambush).",
        "- [[04_IV_Centipede]]: Sin IV - Centipede (Burrowing horror, segmented vermin, swarm).",
        "- [[05_V_Toad]]: Sin V - Toad (Gluttonous maw, caustic slime, corrosive digestion).",
        "- [[06_VI_Lord]]: Sin VI - Lord (Psychic thralls, marionette manipulation, royal decree).",
        "- [[07_Mundane_Opponents_and_Binders]]: Paramilitary squads, armed cultists, and rogue human Binders.",
        "",
        "### 08. Reference & Credits",
        "- [[01_Back_Cover_and_Credits]]: Rulebook back matter, publishing credits, and licensing.",
        ""
    ]
    return "\n".join(content)

def main():
    print("Beginning CAIN 1.0 Knowledge Extraction Pipeline...")
    doc = pymupdf.open(str(PDF_PATH))
    total_pages = len(doc)
    print(f"Loaded {PDF_PATH.name} ({total_pages} pages)")

    for sec in SECTIONS:
        folder_path = KNOWLEDGE_DIR / sec["folder"]
        folder_path.mkdir(parents=True, exist_ok=True)
        file_path = folder_path / sec["file"]
        
        print(f"\nProcessing: [{sec['folder']}] {sec['file']} (Pages: {sec['pages']})...")
        
        if sec["file"] == "INDEX.md":
            content = generate_index_content()
            file_path.write_text(content, encoding="utf-8")
            print(f"  -> Generated Master INDEX.md")
            continue
            
        md_chunks = []
        for p in sec["pages"]:
            p_idx = p - 1
            page_md = pymupdf4llm.to_markdown(str(PDF_PATH), pages=[p_idx])
            
            # Clean header duplicates or weird publisher artifacts
            cleaned_md = page_md.strip()
            
            # Find images for this page
            p_imgs = get_page_images(p_idx)
            img_links = []
            for img_name in p_imgs:
                img_links.append(f"![{img_name}](../../assets/images/{img_name})")
            
            md_chunks.append(f"\n---\n### Page {p} Source Content\n")
            md_chunks.append(cleaned_md)
            
            if img_links:
                md_chunks.append("\n\n#### Extracted Visual Elements (Page " + str(p) + ")\n")
                md_chunks.append("\n".join(img_links))

        # Build table links
        table_section = []
        if sec["tables"]:
            table_section.append("\n\n## High-Resolution Graphical Tables & Sheets\n")
            for t_file in sec["tables"]:
                table_section.append(f"![{t_file}](../../assets/tables/{t_file})\n")

        # Build related wikilinks
        related_section = []
        if sec["wikilinks"]:
            related_section.append("\n\n## Related Knowledge Nodes\n")
            for wl in sec["wikilinks"]:
                related_section.append(f"- [[{wl}]]")

        full_content = (
            f"# {sec['title']}\n\n"
            f"> Source: CAIN 1.0 Rulebook (Pages {', '.join(map(str, sec['pages']))})\n"
            + "\n".join(md_chunks)
            + "\n" + "\n".join(table_section)
            + "\n" + "\n".join(related_section)
            + "\n"
        )

        file_path.write_text(full_content, encoding="utf-8")
        print(f"  -> Wrote {file_path.name} ({len(full_content)} bytes)")

    print("\nKnowledge Extraction Pipeline Completed Successfully!")

if __name__ == "__main__":
    main()
