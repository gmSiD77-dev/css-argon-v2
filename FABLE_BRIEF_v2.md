# CSS v2: system audit, canon, and desktop rebuild. Brief for a Fable cloud session

*Draft v2, Oct 11, 2026. Replaces FABLE_BRIEF.md (kept for reference). Paste everything from "THE PROMPT" down. Before launch, fill the two "Outside review" sections at the bottom, or delete them if skipped.*

---

## THE PROMPT

You are working on the **Cosmic Sonification System (CSS)**, an immersive dome installation by composer and spatial-audio designer Greg Maloney (Souls in Drag / Dominant Resonance). CSS reads the real sky through several cosmological traditions and turns it into spatial audio, sacred geometry and live visuals. It is the experiential continuation of the synthesis Manly P. Hall made in *The Secret Teachings of All Ages* (1928). A pre-recorded presentation of it was accepted for HARMONICS 2026 (UC Irvine: music, medicine and science, Oct 28–29, 2026), and a LACMA Art+Technology Lab grant application is pending. Describe both exactly that way.

This repo holds:
- the working browser prototype (`poc/index.html`: one file, p5.js + Web Audio + the Claude API)
- Greg's context (`context/`)
- reference code (`reference/`)

**This session has three jobs, in this order:**
1. **Audit:** is the *system* sound, not just the code?
2. **Canon:** write the baseline rules the system runs on, each one sourced.
3. **Build v2:** build it in a new folder on top of that canon.

Commit after each part. If you run low on budget, a finished Audit and Canon matter more than a half-built v2.

### Read first
1. `context/cosmic-sonification-system.md`: the master context (three layers, mapping table, traditions, creative model, open decisions).
2. `context/Cosmic_Sonification_Parameter_Map.xlsx`: the parameter map, per-planet identity cards and tradition matrix. Most rows are marked TBD; the Canon should settle as many as it can defend.
3. `context/harmonics_2026_script.md`: the most current public statement of what CSS claims. Every claim in it should be true of v2.
4. `context/prs-research-arc.md`: Hall, PRS and the Getty (geometry provenance and the Sage's voice).
5. `context/lacma-criteria.md`: what the grant evaluators weigh, and what Phase 1 promised.
6. `poc/index.html`: the prototype.
7. `reference/harmonics_gfx.py`: visual-language reference (octave climb, Kepler Lissajous, Schumann spectrum).
8. `reference/ephemeris_check.js`: a quick comparison of the POC's planet math against astronomy-engine (see Part 1).
9. `context/css-wisdom-school.md`: the deferred phone/subscription product. Read it only so v2's architecture doesn't block it.

Hall's *Secret Teachings* (1928) is in the US public domain (1928 works entered it in 2024); full text is on archive.org. Kepler's *Harmonices Mundi* is available in the Aiton/Duncan/Field translation; cite the book and chapter.

### Decisions already made (treat as fixed)
- **Greg is the composer; the system conducts.** Every timbre, theme and harmonic language is human-authored. Data and traditions select and shape; they never generate music from nothing. No generative-AI music.
- **Frequencies are design choices, not health claims.** 432 Hz, 136.1 Hz and 7.83 Hz are never framed as healing or therapeutic.
- **Vibroacoustics go to seating or wearables first**; the floor stays an option. Access for deaf and hard-of-hearing people is a design principle.
- **Traditions are an open set.** The public list is seven (Kabbalistic, Vedic/Jyotish, Egyptian, Buddhist, Hermetic, Taoist, Tarot), with Mayan as the named example of growth. The POC runs three while the first versions are built out (**Kabbalistic, Vedic/Jyotish, Tarot**); **Hermetic is the fourth**, the next one in, and the natural home of Hall and Ficino. v2 builds full modules for those four, with stubs for the other three. Adding a tradition must be a module, not a rewrite.
- **Desktop web first, phone-ready.** v2 is the web experience designed for a laptop or large screen. A phone app is likely later, so the **engine** (ephemeris, grammar, tradition modules, Sage contract, audio and visual parameter streams) must be separate from the **interface**. It should run in a browser now and be reusable by a phone app or the dome rig. v2 should not break on a phone, but phone UX is not this session's job.
- **Hybrid sound.** Synthesis stays for the data-true tones (Cousto roots, Kepler glides, aspect intervals). Add a clear slot so Greg can drop in his own composed stems and timbres per planet and per tradition, and have the system conduct them. Ship with placeholders and a short spec of what files Greg should provide (format, length, naming, loop points).
- **"Video" means the live visuals engine:** geometry and cymatics rendered in real time, with a dome-ready path (fisheye / domemaster output) at least specified, even if not built.
- **Cousto planetary roots:** Sun 126.22 · Moon 210.42 · Mercury 141.27 · Venus 221.23 · Mars 144.72 · Jupiter 183.58 · Saturn 147.85 Hz. Earth year 136.10 Hz. **Kepler intervals:** Saturn 4:5 · Jupiter 5:6 · Mars 2:3 · Earth 15:16 · Venus 24:25 · Mercury 5:12. Verify each Cousto derivation (which period each comes from) and record it in the Canon.
- **Do not modify `poc/`. Do not deploy. Do not commit API keys.**

---

### PART 1: AUDIT (`CSS_AUDIT.md`)

Lead each finding with the conclusion. Grade each one **Fix now / Fix in v2 / Decide (Greg) / Fine**.

**1a. Astronomy. Known problem; confirm it and measure it.** `calcPlanets()` takes *heliocentric mean longitudes* for Mercury–Saturn and *geocentric mean* longitudes for Sun and Moon. A chart needs apparent geocentric positions. `reference/ephemeris_check.js` already shows the size of the errors:
- Jan 13 1977: Mercury is 152° off and Venus 83° off (Gemini instead of Pisces).
- Oct 11 2026: Venus is 154° off.
- Jul 20 1969: Mars is 44° off.

Also check:
- **Birth time is read as UTC** (`Date.UTC(...)`) and the place field is never used: no timezone, no coordinates, no Ascendant, no houses.
- **Dates before 1582** need Julian-calendar handling, and the far past (e.g. Giza, ~2560 BCE) needs ΔT. Report how uncertain the Moon and the Ascendant become in the far past.
- **No retrograde detection.**

Recommend the ephemeris, for example:
- `astronomy-engine` (MIT, small, runs in browser and phone)
- Swiss Ephemeris WASM (most complete; the two reviewers disagree on whether its free licence is AGPL or GPL, so check the actual release and the WASM wrapper against the open-source plan)
- JPL DE440/441 data

Prove the choice with a test that compares positions for 5 dates, including 2560 BCE and 1977-01-13 10:36 EST, Weymouth, Massachusetts (42.22°N, 70.94°W).

**1b. The traditions: are they rooted, or Western astrology in costume?** For each of the four v2 traditions (and quickly for the other three), check the POC's mappings against primary or standard sources and say what is wrong, missing or mixed. Known issues to confirm:
- **Jyotish:**
  - It is computed on the tropical zodiac with Western dignities. Jyotish is sidereal (name the ayanamsa; Lahiri is standard), has nine grahas (Rahu and Ketu are missing) and has its own dignity system (uccha/nicha, moolatrikona, own sign; consider a simplified Shadbala).
  - The "graha bala" claim in the master context isn't what the code does.
  - The bija mantras don't match the standard Navagraha set (Jupiter "Kleem" should be Gram/Greem; Moon and Venus share "Shreem"). Nakshatras are absent.
- **Kabbalah:**
  - Jupiter → Tzaddi / "The Star" contradicts the POC's own Tarot map (Jupiter → Wheel of Fortune = Kaph).
  - Planet → letter assignments for the seven double letters differ between Sefer Yetzirah recensions and the Golden Dawn. Pick one lineage per module and name it.
  - Add the Sephirot (Saturn–Binah … Moon–Yesod).
- **Tarot:** confirm the Golden Dawn planetary attributions, and name the lineage (Golden Dawn / Thoth / Marseille differ).
- **Dignity scoring:** `ANGULAR_SIGNS` treats the cardinal *signs* as angular. In the tradition, angularity belongs to *houses* (1/4/7/10), which need a birth time and place. Hard-coded `PLANET_HARMONIC_KEYS` contradicts the Cousto roots (Sun 126.22 Hz is B, not D). Find any other contradictions.
- **The other four:**
  - Egyptian: separate pharaonic sources (decans, Sothic/Sirius rising, the Duat journey, the native planet names) from Hellenistic syncretism (Thoth = Mercury).
  - Taoist/Chinese: the five-phase planets, the 28 lunar mansions (xiu), Jupiter's 12-year cycle.
  - Buddhist: Kalachakra and Tibetan reckoning.
  - Mayan: the Venus cycle, the 260-day count, the Long Count. Name the Dresden Codex Venus table as a source.

  For each, say what a module would need: data, sources, and a cultural consultant.

**1c. Claims vs code.** List every claim in the HARMONICS script and the master context that the code doesn't yet make true. Example: "the same frequency that makes the music also generates the geometry". Today the Chladni n/m pairs are a hand-picked lookup table, not derived from the frequency.

**1d. Code and architecture.** The data flow end to end (date → positions → dignity → drones → geometry → reading → mixer): what's solid, what's fragile, what's hard-coded. The Sage calls `claude-sonnet-4-6` from the browser with a user-supplied key. Recommend:
- the current model per job. As of Oct 2026 the IDs are `claude-opus-5-5`, `claude-sonnet-5-5` and `claude-haiku-5-5`; verify on docs.claude.com.
- a small server-side proxy, with rate limiting and no keys in the browser.

**1e. What we haven't thought of.** Your open pass. What principles, structures or sources would make this a stronger system: more coherent, more rooted, more defensible to a curator or scientist, more beautiful? Push back where Greg's framing is weak. Label guesses as guesses.

---

### PART 2: CANON (`CSS_CANON.md`, plus machine-readable `engine/canon/*.json`)

The baseline rulebook the engine runs on: versioned (v0.1), and expected to evolve. For every rule, give **the rule, its source (book/chapter or dataset), confidence (established / scholarly debate / Greg's artistic choice), and which parameter it drives.** Separate *astronomical fact*, *traditional doctrine* and *artistic decision* so nobody confuses them. That separation is what makes the work defensible.

Include at least the following. Several are candidate principles: argue for or against, then propose.

1. **Frame of reference.** Kepler's harmonies are heliocentric (angular velocity seen from the Sun); astrology is geocentric (the sky seen from Earth). Proposal: two named layers, a heliocentric **physics voice** (Kepler, Cousto) and a geocentric **sky voice** (chart, aspects, traditions), never blurred.
2. **Angle = interval = polygon.** In *Harmonices Mundi* Book IV, Kepler derives the aspects from the same division of the circle as musical consonance:
   - opposition ↔ octave
   - trine ↔ fifth
   - square ↔ fourth
   - sextile ↔ minor third
   - quintile, which Kepler added ↔ major third
   - with matching polygons (Book I/II).

   Verify the exact correspondences. If they hold, this one rule makes the aspects the music *and* the geometry. It would replace the POC's improvised `ASPECT_COLOR` beats, and it is the "compositional grammar" LACMA Phase 1 promised.
3. **Kepler's moving voices.** Each planet's pitch glides between its perihelion and aphelion values at its real angular speed on the chosen date (Book V), rather than holding a static drone.
4. **Tuning rule.** Cousto absolute frequencies vs a 432 Hz root vs Kepler ratios on a movable root. Proposal: data-true by default, composer overrides explicit and labelled in the UI. Resolve open decisions 1–3 from the master context or set them out for Greg.
5. **Each tradition reckons its own sky.** The module schema declares:
   - frame (geo/helio)
   - zodiac (tropical / sidereal + ayanamsa / none)
   - how it divides the sky (12 signs / 27 nakshatras / 28 xiu / 36 decans / 260-day count)
   - planet set (seven / nine grahas / five-phase / Venus-centred)
   - dignity system
   - correspondences (letters, mantras, cards, deities), each with its lineage
   - sonic colour (the "cultural pedalboard")
   - geometry family (Tree of Life, yantra, mandala…)
   - Sage voice and sources
   - consultant status

   This is what makes "adding Mayan is one file" true. Write modules for Kabbalah, Jyotish, Tarot and Hermetic at the level of sourced correspondences, and stubs for the rest. Depth goes into one complete example first (see the Outside review merge, item A). For Hermetic: the Chaldean order, the planetary spheres, Ficino's planetary music (*De Vita* III), and the Corpus Hermeticum.
6. **The dome is the sky.** Optional mode: each voice is placed at the planet's real azimuth and altitude above the participant's location, computed as horizon coordinates. Planets below the horizon move to the vibroacoustic channel: felt, not heard (the Egyptian Duat / the Sun's night journey). The Ascendant sets the orientation. Contrast this with the zodiac-wheel panning the POC uses, and recommend.
7. **Geometry that comes from the data.**
   - Chladni n/m chosen from frequency by physics (square plate, or circular-membrane Bessel modes, which suit a dome), not a lookup.
   - Aspect polygons drawn from the actual chart.
   - Orbital-resonance figures from real orbits (Venus–Earth 8-year pentagram, Mars/Jupiter loops).
   - A slot for ratios Greg will extract from Hall's manuscripts at the Getty, so specific geometry has named provenance.
   - The Flower of Life backdrop survives only if it can be justified.
8. **Planetary hours and days** (Chaldean order → the weekday heptagram) as a real-time-mode structure. Should the current hour's ruler lead?
9. **Silence and session arc.** Session length (5/10/20 min, or variable), with silence designed in.
10. **Sacred geometry from Greg's NotebookLM notebook.** See "Outside review" below and fold those principles in where they hold up.

---

### PART 3: BUILD v2 (`v2/`)

A new desktop-first web build on the Canon. `poc/` stays untouched as the reference.

**Architecture.** `v2/engine/` is plain modules with no DOM dependency: ephemeris, chart (houses, aspects, dignities per tradition), grammar (chart → composition spec), tradition modules (JSON + small code hooks), Sage contract. `v2/app/` is the interface. Write a one-page `ARCHITECTURE.md` that someone fluent in signal flow can follow; use a signal-flow diagram.

**The grammar output is the heart of v2.** One JSON "score" per chart:
- lead voice and why
- per-planet root, Kepler glide and position (zodiac *and* horizon)
- aspect intervals and polygons
- tradition colouring
- reverb/space character
- vibroacoustic feed
- geometry parameters
- session arc

Everything downstream reads this one object: browser audio, visuals, Sage, and later the dome (OSC / WebSocket to Max, TouchDesigner, Ableton) and a phone app. Specify that bridge, and stub it if there's time.

**Sound.** Web Audio, rebuilt on the score:
- Cousto/Kepler synthesis for the data-true layer
- the stem slot for Greg's composed material
- per-tradition colouring
- a separate vibroacoustic bus

Output binaural/headphone first, with a note on how the same scene maps to Greg's dome or Atmos 7.1.4 path, e.g. ambisonics as the intermediate format.

**Visuals.** The live visuals engine:
- data-derived Chladni / Bessel modes
- aspect polygons
- orbital-resonance figures

60 fps on a laptop. Specify the domemaster/fisheye output (4K, 60 fps), what should eventually move to TouchDesigner, and why.

**The Sage.** Rebuild the prompt architecture:
- **Voice:** Hall's grounded, mythic, educated voice; cite his public-domain prose.
- **Sources:** each tradition's module supplies its own sources and lineage.
- **Output:** structured output the grammar and the UI can use, as well as prose. Readings may *explain* the score but never change the astronomy.
- **Rules:** keep the existing ones (not fortune-telling, stays on topic, no health claims).

Include three sample exchanges: a personal birth chart (Greg's own: Jan 13 1977, 10:36 am EST, Weymouth, Massachusetts), a historical moment (Giza), and tonight's sky. Run the Sage through a mock if no API key is present, and include a proxy stub.

**Design.** Keep the POC's dark cosmic world; Greg's rule is "style over mediocrity". No generic glassmorphism dashboard or purple-gradient SaaS look. The sky, the geometry and the sound are the interface; controls stay out of the way. Accessible: keyboard, captions for the Sage, reduced-motion.

**Tests.** Ephemeris accuracy tests, a tradition-module schema test, and a golden-file test that the same chart always produces the same score.

---

### PART 4: REVIEW (`CSS_V2_REVIEW.md`, read in about an hour)
- What changed from the POC and why, in plain language.
- **The decision list for Greg:** every "Decide (Greg)" item, each framed as a this-or-that with your recommendation.
- **Gap list against LACMA Phase 1:** grammar, ephemeris, prompt architecture for the v1 traditions (three promised, four built), public deployment, open-source repo. Ranked by effort vs impact.
- **The three moves you'd make next,** each sized for one working session, with its first concrete step.
- **Every claim in the HARMONICS script:** now true / still not true.

### How to write
Plain language. Greg is a composer and audio engineer, fluent in signal flow, less so in web architecture. Lead with the conclusion. Cite sources for any claim about Hall, the traditions or astronomy, and mark guesses as guesses. Long code lives in files, with a pointer from the doc.

**Done means:**
- `CSS_AUDIT.md`, `CSS_CANON.md` (+ `engine/canon/*.json`) and `CSS_V2_REVIEW.md` exist.
- `v2/` runs locally with a one-line "how to run".
- Ephemeris tests pass.
- A chart produces a score JSON that drives the sound and visuals.
- `poc/` is unchanged.
- Everything is committed to a branch named `fable-v2`.

---

## OUTSIDE REVIEW: merged notes (Oct 24)

Two independent critical reviews (four seats: astronomer, historian of traditions, composer/psychoacoustician, curator) and Greg's sacred-geometry NotebookLM notebook (Robert J. Gilbert's course material) were run against this brief. **The full text is in `context/outside-reviews-full.md`.** Read it, but treat it the way you treat everything else: verify before adopting, cite what you adopt, and note where the reviewers disagree. Below is what changes in the brief because of them. Where an item here conflicts with an earlier part of the brief, this section wins.

### A. Scope change: one golden thread before breadth
Both reviews agree that the most valuable proof is **one complete example, traced end to end**, before filling every module. Use Greg's chart (Jan 13 1977, 10:36 EST, Weymouth MA; 15:36 UTC). Trace at least one relationship all the way through:
- the verified astronomical input
- the correctly attributed tradition rule (with its lineage)
- the compositional decision
- the sound **and** the geometry

Show the source trail, the uncertainty, and a clear label of what is fact, what is doctrine and what is Greg's authorship. v2 is "done" only when this thread works. Breadth comes second.

### B. Truth layers, all the way through
The Canon, the score JSON, the interface and the Sage must all keep three layers distinguishable: **astronomy** (computed state), **historical model / doctrine** (Kepler's published arguments, a tradition's rules, with the lineage named) and **CSS rule** (Greg's mappings, octave shifts, accelerated time). Every field in the score carries its layer and its source.

### C. Astronomy corrections
- **Moon topocentric parallax.** Use the observer's latitude, longitude and elevation (up to ~1° for the Moon; matters for horizon placement and close boundaries). Meeus, *Astronomical Algorithms*, ch. 40.
- **Time handling.** Local civil time → UTC → TT, with explicit ΔT. Astronomical year numbering, with a year 0 (2560 BCE = −2559). Calendar convention stated per input, since Gregorian adoption varies by country. The reviewers disagree on the size of ΔT uncertainty at ~2500 BCE (NASA's table vs Stephenson–Morrison–Hohenkerk 2016). Look it up, and **carry uncertainty into the score**: an ancient Ascendant must not look more precise than the evidence allows.
- **Ephemeris range.** Confirm the accurate range of astronomy-engine (VSOP87 degrades outside roughly 2000 BCE–6000 CE, per one review). DE440 covers ~1550–2650 CE; DE441 covers ~13,200 BCE–17,191 CE at lower modern precision. If you choose a hybrid, document it.
- **Tests need tolerances.** Use independent reference values (e.g. JPL Horizons). Test longitude, latitude, retrograde stations, horizon coordinates and time conversion separately.
- **Honest failure.** If something can't be computed, a source is missing, or a module is a stub, return an explicit unavailable/incomplete state. The UI must distinguish live / cached / mock / authored demo.

### D. Kepler and Cousto, stated precisely
- **Aspect → interval (Book IV).** Kepler divides the circle like a string and reads the *part-to-remainder* ratios (Book III ch. 1–2; Book IV ch. 5), so each aspect yields a *set* of consonances, not one:
  - opposition → 1:2
  - trine → 2:3 and 1:3
  - square → 3:4 and 1:4
  - sextile → 5:6
  - quintile → 4:5, biquintile → 3:5
  - octile/sesquiquadrate → 5:8 and 3:8

  Kepler added the quintile *and* other aspects, not the quintile alone. Define the conjunction (0°) too. Present the mapping as a **chosen CSS grammar built on Kepler's division**, not a law of nature.
- **Book V glides.** The ratios (Saturn 4:5 … Mercury 5:12) are the *min:max apparent heliocentric angular speed*. Record direction explicitly (4:5 as an ascending interval is 5:4). Instantaneous speed scales ~1/r²; cite ch. 3 and give the formula. Call the feature a **"Kepler-inspired angular-velocity glide"**. Over a 20-minute session the real change is close to nothing, so state the time-scaling (see F).
- **Kepler's choir (Book V ch. 7)** sets the registers: Saturn/Jupiter bass, Mars tenor, Earth/Venus alto, Mercury/Moon soprano. Verify the chapter.
- **Kepler's unresolved harmony (Book V ch. 9).** The full six-voice consonance almost never occurs. One reviewer calls this the work's emotional core: perpetual yearning and suspension. Consider making it a compositional principle, not just a footnote.
- **Cousto derivations.** Record a calculation for each root: the cycle, the period in seconds, raw Hz, octave multiplier, result, source. Earth = tropical year; Moon = *synodic* month (the sidereal month would give ~227 Hz); planets = sidereal orbital periods. **The Sun (126.22 Hz) is not an orbital period.** The two reviewers give different derivations (a gravitational-length calculation vs a solar-rotation convention). Find Cousto's own derivation, or mark it unresolved. The HARMONICS script says each planet's orbital period becomes a frequency; make sure nothing claims that for the Sun.
- **Notes need a reference.** 126.22 Hz is about 38 cents sharp of B2 at A=440. Store Hz as the data; note names and the 432 override are display/tuning decisions.

### E. The tuning collision: the biggest musical trap
Raw Cousto roots all sit in about one octave (126–221 Hz). Mars 144.72 and Saturn 147.85 are only ~37 cents apart, inside the critical band (Plomp & Levelt 1965). Played together as fundamentals they rough up instead of forming the aspect's interval, and seven voices in one octave fuse into mud (Bregman 1990), wrecking localisation in the dome. Both reviews converge on a hierarchy. Propose it in the Canon and let Greg decide:
- **Layer A, Cousto = identity.** Each planet's named root anchors its timbre, motif or drone colour.
- **Layer B, Kepler = motion and relationship.** The lead planet sets the tonic. Aspected planets are voiced by the aspect intervals relative to it, placed in their Kepler-choir register across ~4 octaves.
- **Layer C, Greg's composition.** Authored stems carry theme, timbre, phrasing and arc. The score decides when the data layers enter, recede or fall silent.

### F. Time
Define three timescales explicitly: **real sky time**, **an openly accelerated celestial time** (e.g. compress a synodic cycle into a session), and **the composed session arc**. Suggested arc: emergence → orientation → development → instability or convergence → release → silence. The interface says what is being accelerated.

### G. New traditional principles worth adopting
- **Combustion / cazimi / heliacal rising as masking states.** A planet near the Sun is swallowed by its glare (combust, within ~8–17°), "in the heart of the Sun" within 17′ (cazimi), and re-emerges at heliacal rising. These recur across Babylonian, Egyptian, Jyotish (astangata), Hellenistic/Hermetic and Maya sky-watching, which makes them a rare genuinely cross-tradition rule. Map solar elongation to masking, emergence and silence. Sources: Ptolemy, *Tetrabiblos* I.24; BPHS.
- **Ficino's planetary music is modal and behavioural, not frequency-based** (*De Vita* III.21). Saturn and Mars have no music of their own, only music that answers them. Encode this in the Hermetic module rather than imposing frequencies on it.
- **Kabbalah lineages genuinely disagree.** In the Gra recension of Sefer Yetzirah (ch. 4) the seven doubles follow Chaldean order (Beth = Saturn … Tav = Moon). The Golden Dawn attributions differ. Module per lineage; the Sephirot scheme is Hermetic-Qabalistic, so label it so.
- **Tarot's planetary and Kabbalistic correspondences are 19th-century.** Lévi (1854–56), then the Golden Dawn's *Book T* (1888). Paul Foster Case/B.O.T.A. is LA-rooted. The Marseille deck has no correspondences. Name the lineage on every card mapping.
- **Taoist/Chinese.** The five visible planets *are* the five phases by name (Jupiter = Wood/Suixing, the 12-year Year Star; Mars = Fire; Saturn = Earth; Venus = Metal; Mercury = Water), plus the 28 xiu. Sources: Huainanzi ch. 3; Shiji ch. 27.
- **Tibetan.** Choose a school. Kar-tsi (from Kalachakra) vs Nag-tsi; Henning, *Kalachakra and the Tibetan Calendar* (2007).
- **Egyptian.** The 12-sign zodiac arrives only in the Ptolemaic period (Dendera, ~50 BCE). Native astronomy uses the 36 decans and star clocks (Neugebauer & Parker), the Duat/Amduat hours (Hornung) and Sothic rising.
- **Maya.** The Dresden Codex Venus table (pp. 24, 46–50) and the 584-day Venus cycle in four stations, plus the Tzolk'in/Haab'/Long Count. Bricker & Bricker 2011; Aveni 2001.
- **A module may return something that isn't a chart.** A calendar, a cycle state or a textual correspondence must be possible without forcing a 12-sign wheel or a dignity score.

### H. Sound, space and touch
- **Spatial contract.** Use a target-independent scene: 3rd-order ambisonics (AmbiX) internally or an object stream, and document coordinates, channel order, normalisation and decoder. For the dome bridge, prefer **ADM-OSC** (the object-position standard used by SPAT Revolution, L-ISA and others) over a custom schema. Headphone playback does not validate a dome.
- **A tactile score, not a copy of the mix.** Skin responds best at roughly 28–90 Hz (peak ~40–60). Design a separate vibroacoustic score that keeps the rhythm, envelope and relationships, translated for the actual transducer. 7.83 Hz as a raw sine is not perceivable as intended; specify how it is carried (e.g. amplitude modulation of a tactile carrier). The below-horizon "Duat bus" is a named, optional mode.
- **Direction of flow.** An optional artistic mapping from the notebook (Steiner/Adams/Schwenk projective geometry): direct or waxing planets radiate centre → periphery; retrograde or waning planets stream periphery → centre. Label it CSS authorship.
- **Test perception, not just calculation.** Specify simple listening and viewing tests to check that the intended differences are actually perceivable.

### I. Geometry
- **Two honest modes.**
  - *Physics-led:* circular-membrane Bessel modes, which suit a dome (Fletcher & Rossing ch. 3), with the modelled system documented.
  - *Procedural-art:* designed patterns driven by ratios and aspects, labelled as a CSS mapping.

  Never call a procedural pattern a physical Chladni figure. Retire the square-plate equation as the default.
- **From the notebook, where it holds up.**
  - **Monochord principle:** the same ratio is a pitch *and* a figure. This aligns with Kepler.
  - **The Venus–Earth 8:5 cycle and pentagram:** data-true, and also usable as an 8-against-5 polyrhythm.
  - **5-fold as "organic/life" vs 6-fold as "mineral/creation".**
  - **Octave as helix:** an octave rises along an axis rather than closing a circle.
  - **Platonic duals and nesting:** cube ↔ octahedron, dodecahedron ↔ icosahedron, the rhombic triacontahedron, Kepler's *Mysterium Cosmographicum*.

  Label these as tradition or artistic sources with their confidence.
- **What the notebook itself flags as contested.** The "Flower of Life" name is a 1980s popularisation. The golden ratio in the pyramids and the Parthenon is disputed (Egyptologists see simple integer slopes such as 11:7). Don't use either as provenance.
- **Treat as artistic palette only, never as Canon fact.** The 432/144 "grid constants" (432 × 50 = 21,600), the BG3/16/19/64 gain-and-EQ numerology, and the companion "Sacred Geometry Music Composition Guide" in Greg's Drive. These can be offered as an optional "Gilbert palette" preset, clearly labelled. They also conflict with the data-true default (Cousto absolute Hz), so the tuning rule (Part 2 item 4) must say how the two coexist.

### J. The Sage
Keep Hall's voice, and add a **source contract**:
- Every tradition-specific factual claim links to a source the module supplies.
- Unsupported claims are omitted or marked as uncertain.
- The Sage distinguishes direct quotation, sourced paraphrase and CSS synthesis.
- It never invents a missing traditional rule.

One reviewer suggests framing the Sage as a citation-grounded guide or dramaturg to the score rather than a role-played "ancient sage". Propose how Hall's voice and that discipline coexist. Model IDs live in server-side configuration, not the Canon.

### K. Governance (write these up in the Canon; little or no code)
- **Cultural consultation as a process.** Who qualifies, credit, compensation, authority over representation, how disagreements are recorded. Use the CARE Principles for Indigenous Data Governance for the Maya work and beyond.
- **Version and licence the knowledge.** For each module record the edition, translation, data release, mapping version and rights status. A public-domain 1928 Hall does not make every modern edition, scan or translation free. The 1997 Kepler translation needs a rights check before you quote it at length.
- **Birth data is private by default.** Compute locally. Sending it to the Sage is an explicit, documented choice. The proxy keeps no sensitive logs.

### L. Curatorial framing (for the review doc and any public copy v2 produces)
- **The defensible proposition:** a composer builds an auditable instrument that lets a real sky and historically distinct systems of meaning **coexist without being forced into agreement**. Not proof of one universal ancient harmony.
- **Hall's place:** Hall is the project's point of departure and its LA lineage (PRS, the Getty), not the authority for every historical claim. Avoid perennialist flattening.
- **Specs vs demonstrations:** don't present the 4K/60 fps domemaster target as proof the work is dome-ready; separate what is specified from what is demonstrated.
