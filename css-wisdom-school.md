# CSS Wisdom School — Product Roadmap

**STATUS:** Captured north star. **Deferred until post-LACMA decision** (per the discipline note in the source doc and per CLAUDE.md anti-pattern: "starting new projects before finishing current ones"). Active CSS work is finishing the dome POC + LACMA submission. This file exists so the vision isn't lost — not so it gets built today.

**Parent project:** Cosmic Sonification System — see memory/projects/cosmic-sonification-system.md.
**Larger frame this fits inside:** memory/context/wisdom-school-frame.md (the wisdom-school structure applies across DR/SiD, not just CSS).
**Updated:** June 2026 — incorporates the retention-engine / daily-loop, no-birth-time UX, model-tier strategy, and imagery-strategy sections from the latest CSS POC chat roadmap.

## The vision in one line
The dome is the temple; the app is the digital wisdom school that lives beside it — a place where a person doesn't just receive a cosmic reading but can study it, going as deep into each tradition as they choose, guided by a sage.

This is not a separate product from the LACMA installation. It's the same idea in its scalable, monetizable form — the literal embodiment of the "wisdom school attached to the dome experience" already named in the grant. The dome reaches dozens at a time in one city; the app reaches anyone, anywhere, and funds the next dome.

## The three movements of the experience

1. **The Portal (free).** Enter your birth moment; the sky resolves into your dominant resonance, your cymatic geometry, your personalized frequency, and a reading across the traditions. This is the hook — what the POC does today.
2. **The Study (membership).** Go deeper. Your full chart — degrees, aspects, houses, dignities — laid open. The conversational Sage for each tradition. Guided courses through each cosmology. This is the wisdom school.
3. **The Temple (live / premium).** The dome itself — the full-body cymatic, vibroacoustic, spatial-audio experience. Live events. The app is how people find their way to the temple, and how the temple's reach extends past the room.

## The Sage — the heart of it
Each tradition has a sage: an AI guide that speaks in that tradition's voice, grounded in your specific chart. The Kabbalist walks you through your Tree of Life placements. The Jyotishi explains your bija mantras and elemental balance. The Tarot reader traces your mythic road.

**Status:** seeded in the POC now. The sage is built and conversational across the three wired traditions, grounded in live chart data (positions, dominant resonance, aspects). It is the single clearest bridge from "immersive demo" to "product someone subscribes to" — because a one-time reading is a moment, but a sage you can return to and learn from is a relationship.

**Where it grows:**
- Per-tradition depth: from "explain my chart" to structured, multi-session courses ("Foundations of Jyotish," "The 22 Paths," "The Major Arcana as initiation").
- Memory across sessions (the sage remembers your chart and your questions).
- The seven traditions, each with its own sage, as the framework expands.

## Deeper chart exploration
What a member can explore beyond the free reading:
- **Degrees & dignities** — exact positions and the dignity logic behind the dominant resonance. (In the POC now.)
- **Aspects** — the conversations between your planets (conjunction, sextile, square, trine, opposition), which also become consonance and dissonance in the sound layer. (In the POC now; sonic mapping is a future sound pass.)
- **Houses** — the life-domains. Needs birthplace resolved to lat/long plus exact time (for the Ascendant + house cusps via sidereal time and a chosen house system). The current birthplace field is free text, so houses are the next data sub-project — they require geocoding and a more precise ephemeris than the POC's mean-longitude approximation.
- **The convergence view** — eventually, seeing how all seven traditions read the same placement differently. The project's cultural thesis made personal and explorable.

## Membership ladder (rough)
- **Portal** — free. The reading, the geometry, the frequency. The hook.
- **Initiate** — full chart (degrees, aspects, houses), all seven traditions, save and revisit charts.
- **Adept** — the conversational sages, guided courses (the wisdom school proper), and your personalized planetary frequency rendered as a downloadable meditation track — a direct DR product the sound engine already half-builds.
- **Temple / live** — access to the physical installation and live events.

The free Portal feeds subscriptions; the personalized audio is a standalone DR revenue line; the whole thing is exactly the "replicable model" the grant asks funded work to demonstrate.

## Return engagement — the daily loop (the retention engine)
**The hard truth:** a natal birth chart is a one-time reveal. Once someone has their birth song, the natal reading gives them no reason to return. The habit-forming mechanic is the **transit loop** — today's sky read against the person:

- **"Today's Sky"** — read the current sky (no birth time needed; today is today for everyone). A daily cosmic-weather reading plus a frequency to attune to today. This is the reason to open the app each morning. (Seeded in the POC as Pass 5.)
- **The Sage as ongoing companion / coach** — not just a chart interpreter but a contemplative guide that, keyed to your chart and the current sky, walks you through a breathwork practice, a visualization, a sound meditation. The premium depth and the recurring value.
- **Practices & programs** — a growing library of guided series (breathwork, visualization journeys, sound rituals tied to lunar phases), keyed to chart and moment. A natural DR product line, and dead-on-brand with the wellness / men's-work practice.
- **Lunar & seasonal rituals** — personalized new-moon / full-moon practices as recurring touchpoints.

**Shape:** the daily transit + frequency loop is the free/low-tier habit, and the coaching Sage + guided practices are the premium layer. Both reuse what's already built — the ephemeris on today's date, the sound engine for the daily frequency, the Sage as interpreter-turned-coach.

## No-birth-time path
Many people don't know their birth time, and that shouldn't block them. Without time, the Sun and most planets are solid and the Moon is usually right (only at risk near a sign cusp); what's genuinely lost is the rising sign and the houses. UX reassures rather than apologizes: a simple "Do you know your birth time?" choice — reveal the field if yes; if no, proceed with a calm note on what's covered and what time later unlocks. Lowers the entry barrier and creates a return reason ("come back when you find it"). (In the POC as Pass 5.)

## Model strategy
Both readings and the Sage run on Claude Sonnet 4.6 today. Model choice is one string in the API call, so it can become part of the tiering: lower tiers on Haiku (fast, cheap), standard on Sonnet, a premium "deep counsel" mode on Opus. The model itself becomes part of what a membership buys.

Abuse/cost control is an infrastructure matter for the app phase: accounts, a server-side proxy (so the API key is never exposed), and per-user rate limits and quotas by tier. The Sage's prompt already keeps it on-topic, but **prompts shape the experience while infra controls the bill.**

## Imagery strategy
Two different needs, two different tools.
- **Contemplative art** (an evocative Magician, original symbol imagery) → a diffusion generator (Midjourney, or Ideogram for its text handling).
- **Educational diagrams** with accurate, labeled symbolism → **NOT diffusion models**, which hallucinate symbols and mangle text/Hebrew letters. These should be designed SVG/vector (precise, labelable, code-generatable in the project's existing algorithmic-art idiom) or commissioned.

Whichever path: **build a curated, vetted library rather than generate esoteric imagery on-demand**, because a single hallucinated sigil undermines the credibility a wisdom school rests on.

## LACMA alignment
This roadmap strengthens three of the four grant criteria:
- **Replicable models** — a scalable digital companion that any institution could license or adapt.
- **Public engagement** — the app extends the dome's reach far past the room and past the run.
- **Emerging technology** — AI sages grounded in real chart data, conversational and tradition-specific, are a genuinely new form of guided contemplative learning.

The wisdom-school framing in the proposal and this product are the same organism.

## Phasing — and a discipline note
The honest sequence, holding completion over novelty:
1. **Now:** finish and land the POC and the LACMA demo. The Sage is seeded; that's enough to show the vision without building the business yet.
2. **Next (post-grant decision):** decide whether the app is a near-term build. If yes, the first real milestones are accounts, the houses/geocoding data layer, and the sage's course structure.
3. **Later:** payments, content library, the seven-tradition build-out, cross-session memory, the audio-product pipeline.

**The risk to name out loud:** the app is a big new horizon, and it's tempting to start building it before the dome POC and the grant are landed. The recommendation is to keep this as a captured north star — it informs the demo and the grant narrative — without letting it pull focus from the deliverable in front of you. **Bank the vision; finish the current thing.**

## Open questions
- Is the app a near-term build, or strictly post-LACMA-decision?
- Houses now (with the geocoding + sidereal-time work) or staged?
- Which tradition's course gets written first as the wisdom-school pilot?
- Does the personalized-frequency audio download become an early standalone DR product, ahead of the full app?

## Cross-references
- `memory/projects/cosmic-sonification-system.md` — the parent CSS project (active work)
- `memory/context/wisdom-school-frame.md` — the larger structural frame this expresses
- `memory/projects/dominant-resonance.md` — the offerings ladder this slots into
- `memory/projects/the-talk.md` — the ascension-path model this parallels
- `memory/projects/youtube.md` — the Entry-tier surface that funnels into this
