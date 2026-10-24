# PRS Research Arc — Manly P. Hall as CSS Lineage

**STATUS: ACTIVE.** Phase 1 (silent reconnaissance at PRS Los Feliz) is in progress. This is NOT a deferred north-star file — it's near-term active work that supports and elevates the CSS LACMA submission and dome installation.

**What this is:** Greg stepping into the role of researcher, using the Philosophical Research Society (PRS) in Los Feliz and the **Manly Palmer Hall collection of alchemical manuscripts, 1500–1825** at the Getty Research Institute, to ground the Cosmic Sonification System in historical and mathematical rigor.

**Parent project:** Cosmic Sonification System — see memory/projects/cosmic-sonification-system.md.
**Why now:** The CSS positioning sharpens dramatically when articulated as *the contemporary spatial-audio embodiment of Manly P. Hall's* The Secret Teachings of All Ages. That's a much more specific and defensible thesis than "informed by various ancient cosmological traditions." Hall did the synthesis; CSS makes the synthesis experiential.

## The thesis
The Cosmic Sonification System is, effectively, an interactive spatial-audio embodiment of Hall's *Secret Teachings of All Ages* (1928). To ground the system in historical and mathematical rigor — and to elevate its institutional legibility — the project is expanding to include formal archival research into Hall's work.

This isn't decorative lineage. The archival research has two immediate, technical applications to the POC and the eventual dome.

## How the research feeds the machine

### Application 1 — Geometry (Visuals)
Hall's 17th and 18th-century Hermetic, Rosicrucian, and alchemical manuscripts contain highly specific geometric diagrams and cosmological maps. The research action is:

- Extract mathematical ratios and structures from these manuscripts
- Map them into the WebGL Chladni shader
- Concrete example: use a specific Rosicrucian progression to dictate the *n / m* nodes in the p5.js Chladni equation

The result is a Chladni visual layer whose geometry has direct historical provenance — not generic sacred geometry, but specific geometry traceable to a named manuscript and a named tradition.

### Application 2 — The Sage (AI layer)
Hall's tone, vocabulary, and specific synthesis of Kabbalah, Tarot, and Hermeticism become the foundational training data for the CSS Sage(s). The research action is:

- Use Hall's prose as voice-tuning material for the Claude API prompt architecture
- Goal: the Sage speaks with the grounded, mythic, deeply-educated voice of Hall himself
- This addresses the credibility gap the Sage's prompt currently has — instead of generic "wise" voice, the Sage carries the literal voice of a 20th-century synthesizer of esoteric wisdom

## The 4-phase plan

### Phase 1 — Silent Reconnaissance (CURRENT)
**Objective:** Understand the physical and cultural ecosystem of PRS without making a formal pitch.
**Action:** Visit the PRS campus (open Thursdays / Fridays). Sit in the library. Experience the **Hansell Gallery** and the auditorium — gauge acoustic and spatial viability for a future CSS installation.
**Hard rule:** Do NOT show the POC yet. The web engine must be more refined before institutional exposure (see Phase 3).

### Phase 2 — Securing the Data (the Getty)
**Objective:** Gain access to the raw material.
**Action:** Apply for a qualified-researcher account at the Getty Research Institute to access the *Manly Palmer Hall collection of alchemical manuscripts, 1500–1825.*
**Credentialing strategy:** Use the pending LACMA Art+Technology Lab grant proposal as institutional backing. Frame the research as: *translating historic cosmological charts into a generative spatial audio installation.* That language threads the academic eye of the needle — it's defensible to a Getty archivist and exciting to a LACMA committee.

### Phase 3 — POC Refinement (the Workbench)
**Objective:** Upgrade the web POC so it is impenetrable before pitching to PRS.

- **Action 1 (Data):** Integrate a geocoding API to translate birth cities into exact coordinates. Enables math engine to calculate True Astrological Houses and the Ascendant — essential for 360-degree dome panning.
- **Action 2 (Audio):** Finalize the FM synthesis routing and tradition-specific master effects (the "cultural pedalboard" — each tradition has its own sonic signature treatment).
- **Action 3 (Visuals):** Upgrade the loading screen sequence (the "Astrolabe" engine) to create cinematic tension before the cymatic fields bloom.

### Phase 4 — The PRS Pitch
**Objective:** Secure a formal collaboration, residency, or exhibition space at PRS.
**Action:** Once the POC is locked, submit a formal program proposal to PRS. Pitch the CSS not as a tech demo, but as a **modern, immersive continuation of Hall's core mission:** translating the architecture of the cosmos into an experience people can actually feel.

## What this changes about CSS positioning

Before the Hall pivot, CSS was framed as "informed by Pythagoras, Kepler, Cousto, the seven wisdom traditions, etc." — a constellation of references. After, CSS becomes: **the contemporary spatial-audio embodiment of a specific synthesis Hall already accomplished.** That's:

- **More defensible academically** — Hall did the cross-tradition synthesis; CSS isn't claiming to do it ex nihilo. It's standing on a named scholar's shoulders.
- **More legible institutionally** — PRS, Getty, LACMA, HARMONICS reviewers all recognize Hall. "Hall's *Secret Teachings* made experiential" lands in a way "data sonification through wisdom traditions" doesn't.
- **More specific** — particular manuscripts → particular Chladni geometry → particular sonic results. No more arm-waving about "ancient wisdom."
- **More credible for the Sage voice** — instead of vague mystical tone, a specific authorial voice with a public record of writing and lectures.

## Where the PDF lives
Greg has a PDF of Hall's *Secret Teachings of All Ages* in his Drive `CSS` folder (renamed from "Planetary Music" in June 2026 — that folder is now the canonical CSS research archive home). Referenced in CLAUDE.md as a source-of-truth doc. As Phase 2 of this research arc delivers material from the Getty (manuscript scans, notes, transcriptions), they should also live in this folder structure.

## Implications for adjacent work

- **HARMONICS abstract** — if accepted, the Hall research arc becomes a credible angle for the talk. "Translating Hall's cosmological diagrams into spatial audio" is a sharper title hook than "computational framework for therapeutic spatial audio."
- **LACMA submission** — the Hall research arc can be referenced in any LACMA follow-up communication as evidence of academic rigor. Don't add it to the submitted application unless asked.
- **CSS Wisdom School roadmap** (deferred) — when the wisdom school app activates, Hall is the voice anchor for the Sage. Update memory/projects/css-wisdom-school.md when Phase 2 completes.
- **The Talk (Architecting Resonance)** — Hall's lineage adds a credible "intellectual ancestor" beat to the spiritual-tier version of the talk.
- **Souls in Drag retrospective** — Hall could become a referenced influence in the philosophical/intellectual-ancestry layer of the 50-year retrospective. Possibly his own room or installation segment if it fits the EPCOT-Horizons-meets-dystopian-carnival aesthetic.

## Open questions
- **Timing of Getty application** — apply before or after LACMA decision? (Application can reference the pending LACMA grant either way.)
- **Manuscript prioritization** — once Getty access is granted, which 3–5 manuscripts get prioritized for ratio/geometry extraction?
- **Hall's voice license** — Hall's works are largely in the public domain or held by PRS itself. Worth confirming before training the Sage on his prose at scale.
- **PRS pitch timing** — Phase 4 is gated on Phase 3 POC refinement. What's the honest timeline to lock the POC?
- **Hansell Gallery acoustic + spatial viability** — Phase 1 deliverable. Document with photos / notes after visit.

## Cross-references
- `memory/projects/cosmic-sonification-system.md` — parent project; now references this file under "Active research arc"
- `memory/projects/css-wisdom-school.md` — deferred product expansion; Hall is the Sage voice anchor when activated
- `memory/context/wisdom-school-frame.md` — the term "wisdom school" has direct lineage from Hall's milieu; this file adds historical grounding to that frame
- `memory/projects/the-talk.md` — Hall lineage useful for the spiritual-tier Talk variant
- `memory/projects/souls-in-drag.md` — Hall as potential retrospective influence
- `CLAUDE.md` — PRS research arc now in Tier 1 active priority stack
