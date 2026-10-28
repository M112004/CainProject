---
name: cain-graph
description: Knowledge graph manager for CAIN. Use to query the AST graph, inspect wikilinks, explore communities, and run refresh_graph.ps1 to sync with Obsidian.
---

# CAIN Knowledge Graph Skill

Use this skill to navigate the interconnected knowledge base of CAIN rules, lore, blasphemies, and game tables.

## Key Files & Structure
- **Report**: `graphify-out/GRAPH_REPORT.md` (read first to identify high-degree hub nodes and community clusters).
- **Full AST Graph**: `graphify-out/graph.json`.
- **Interactive Obsidian Vault**: `graphify-out/obsidian/`.
- **Primary Source Docs**: `knowledge/`.

## Graph Refresh Command
To synchronize newly added markdown notes or wikilinks:
```powershell
./refresh_graph.ps1
```
Or manually:
```powershell
graphify extract . --allow-partial
graphify cluster-only .
graphify export obsidian
```

## Obsidian & Graph Navigation Rules
- Always use `[[Wikilinks]]` when connecting game concepts (e.g. `[[The_Action_Roll]]`, `[[Divine_Agony_and_Talismans]]`, `[[01_I_Ogre]]`).
- Check `graphify-out/GRAPH_REPORT.md` before performing broad text scans across the ruleset.
