# ⚔️ Brutal Dark Medieval Fantasy Worldbuilding Prompts

This module contains specialized lore-building prompts designed for tabletop RPGs, narrative design, and worldbuilding in a **Brutal Dark Medieval Fantasy** setting.

---

<a id="top"></a>
## 📋 Table of Contents
- [📁 Subcategories & Prompts](#-subcategories--prompts)
  - [🐉 Entities & Beings (`entities/`)](#subcat-entities) ([`📁 entities/`](file:///home/sysadmin/Downloads/shed-prompts/worldbuilding/entities/))
  - [🏰 Factions & Beliefs (`factions-beliefs/`)](#subcat-factions-beliefs) ([`📁 factions-beliefs/`](file:///home/sysadmin/Downloads/shed-prompts/worldbuilding/factions-beliefs/))
  - [📜 Lore & Systems (`lore-systems/`)](#subcat-lore-systems) ([`📁 lore-systems/`](file:///home/sysadmin/Downloads/shed-prompts/worldbuilding/lore-systems/))
- [⚡ Recommended Worldbuilding Campaign Pipeline](#pipeline)

---


## 📁 Subcategories & Prompts

<a id="subcat-entities"></a>
### 🐉 Entities & Beings (`entities/`)
| Prompt | Target Artifact | Description |
|---|---|---|
| [`bestiary.md`](file:///home/sysadmin/Downloads/shed-prompts/worldbuilding/entities/bestiary.md) | Bestiary Entry | Clinical, biologically grounded creature/monster lore with in-universe artifact. |
| [`character.md`](file:///home/sysadmin/Downloads/shed-prompts/worldbuilding/entities/character.md) | Character Dossier | NPC, legendary figure, tyrant, or folk hero with fatal flaw and relationships. |


[⬆ Back to Top](#top)

---
<a id="subcat-factions-beliefs"></a>
### 🏰 Factions & Beliefs (`factions-beliefs/`)
| Prompt | Target Artifact | Description |
|---|---|---|
| [`bloodline.md`](file:///home/sysadmin/Downloads/shed-prompts/worldbuilding/factions-beliefs/bloodline.md) | Dynasty Chronicle | Noble house, dynasty, or cursed lineage with hereditary trait and secrets. |
| [`faction.md`](file:///home/sysadmin/Downloads/shed-prompts/worldbuilding/factions-beliefs/faction.md) | Institutional Lore | Military order, merchant guild, cabal, or empire with internal schism. |
| [`pantheon.md`](file:///home/sysadmin/Downloads/shed-prompts/worldbuilding/factions-beliefs/pantheon.md) | Cosmic Lorebook | Deities, eldritch powers, divine hierarchy, and planar origin. |
| [`religion.md`](file:///home/sysadmin/Downloads/shed-prompts/worldbuilding/factions-beliefs/religion.md) | Theological Lore | Faith, church, cult, or heresy with dogma, rituals, and tithes. |


[⬆ Back to Top](#top)

---
<a id="subcat-lore-systems"></a>
### 📜 Lore & Systems (`lore-systems/`)
| Prompt | Target Artifact | Description |
|---|---|---|
| [`artifact.md`](file:///home/sysadmin/Downloads/shed-prompts/worldbuilding/lore-systems/artifact.md) | Antiquarian Record | Relic, cursed weapon, or ancient mechanism with provenance and price. |
| [`event.md`](file:///home/sysadmin/Downloads/shed-prompts/worldbuilding/lore-systems/event.md) | War Chronicle | Historical battle, plague, siege, or cataclysm with tactical consequences. |
| [`location.md`](file:///home/sysadmin/Downloads/shed-prompts/worldbuilding/lore-systems/location.md) | Cartographic Record | Fortress, ruined city, dungeon, or region with environmental hazards. |
| [`magic.md`](file:///home/sysadmin/Downloads/shed-prompts/worldbuilding/lore-systems/magic.md) | Arcane Grimoire | Mechanically rigorous magic system defined by finite Source and Toll. |
| [`world-timeline-chronicle.md`](file:///home/sysadmin/Downloads/shed-prompts/worldbuilding/lore-systems/world-timeline-chronicle.md) | `WORLD_TIMELINE_CHRONICLE.md` | Autonomous fictional historical timeline chronicle, era designation synthesizer, and causality map generator. |

---


[⬆ Back to Top](#top)

---
<a id="pipeline"></a>
## ⚡ Recommended Worldbuilding Campaign Pipeline

```mermaid
graph TD
    A["pantheon.md"] --> B["religion.md"]
    B --> C["faction.md"]
    C --> D["bloodline.md"]
    D --> E["character.md"]
    E --> F["magic.md"]
    F --> G["location.md"]
    G --> H["bestiary.md"]
```

[⬆ Back to Top](#top)
