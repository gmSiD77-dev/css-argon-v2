# HARMONICS 2026 — VO record script (final deck: CSS Slides v2, 13 slides)

**Due to Sweta: Wed Oct 7** (she uploads to the CME portal Oct 8).
Source: "HARMONICS 2026 Video — Plan of Attack & Script" (Drive, Sep 29), remapped to the 13-slide deck.
Changed from that doc: **slide 2 now reads the Heal disclosure** (Sweta, Sep 29: use the same language everywhere), and Methods II is split across slides 6 + 7.

## Record spec
- 48 kHz / 24-bit WAV, mono, dry. ~1 s of room tone at head and tail.
- **One file per slide:** `slide_01.wav` … `slide_13.wav` → `assets/audio/vo/`
- Pace: contemplative, ~135 wpm. Total ≈ 1,550 words ≈ 12 min (hard limit 15:00).
- Pickups: re-record the whole slide file. Don't splice; it's faster for both of us.

## Also drop in
- `assets/audio/bed.wav`: one planetary drone bed, stereo, ≥ 3 min (I'll loop it and duck it under the voice). Longer is better.
- `assets/poc-capture/poc.mov`: QuickTime screen recording, 1080p, ~90 s. Enter a date → drones start → geometry → reading → mixer. Silent is fine.
- Already have: `assets/generated/CSS_chladni_planetary_morph_1080p.mp4` (cut in on slide 5, "Third, geometry").

---

### slide_01 — Title
Every planet in our solar system moves in a rhythm so precise you could set a clock by it. For thousands of years, people have asked what those rhythms would sound like, if we could hear them. I'm Greg Maloney, a composer and spatial audio designer. For twenty years I worked in film music, alongside Danny Elfman and at Hans Zimmer's Remote Control Productions. This is the Cosmic Sonification System.

### slide_02 — Disclosure
I hold an equity stake in Heal, a company that makes spatial audio meditation pods marketed as a health and wellness product. Heal has no involvement in the Cosmic Sonification System, and neither Heal nor its products appear in or are referenced by this presentation.

### slide_03 — Learning Objectives
By the end of this session, you'll be able to describe the musica universalis tradition and how planetary orbits can be mapped to pitch and interval. You'll be able to explain how an AI interpretive layer can pass the same astronomical data through multiple cultural cosmologies to create personalized contemplative spatial audio. And you'll be able to identify how vibroacoustic delivery can open immersive music experiences to deaf and hard-of-hearing participants.

### slide_04 — Background & Objective
The idea that the cosmos is musical is very old. Pythagoras noticed that strings in simple ratios, like two to one or three to two, sound harmonious together, and he wondered whether the heavens followed the same ratios. Boethius later called this musica mundana, the music of the world. Then in 1619, the astronomer Johannes Kepler published Harmonices Mundi, The Harmony of the World. In it, he gave each planet a musical interval, based on how its speed changes as it travels around the Sun. That same book also introduced one of the founding laws of modern astronomy: the exact mathematical relationship between a planet's distance from the Sun and the time it takes to complete an orbit. For Kepler, the science and the music were never separate.

Today, data sonification is an established field. Scientists turn solar wind, gravitational waves and galaxy images into sound. But most of it maps data to sound literally: a number goes in, a pitch comes out. What's usually missing is an interpretive layer, something between the data and the listener that gives it meaning a person can feel. So the objective of this work is a computational framework that translates real orbital data into personalized, contemplative spatial audio through multiple cosmological traditions.

### slide_05 — Methods I: The Physics
The system starts with physics. Three things ground it.

First, pitch. Each planet's orbital period is a frequency, just an extremely slow one. Double it enough times and it rises into the audible range. This is octave transposition, the method Hans Cousto described as the Cosmic Octave. Earth's year becomes 136.1 hertz. Saturn becomes 147.85. The frequencies come from the data. They aren't invented.

Second, harmony. The relationships between voices come from Kepler's own interval assignments: Saturn a major third, Jupiter a minor third, Mars a perfect fifth. The system is tuned to a 432 hertz root, with a 136.1 hertz Earth drone, and a 7.83 hertz layer, the Schumann resonance, which sits below hearing and is delivered as vibration.

Third, geometry. In the late 1700s, Ernst Chladni bowed metal plates dusted with sand and watched the sand settle into patterns. Each frequency makes its own shape. Hans Jenny later called this cymatics.

Long before Chladni, the builders of sacred spaces seem to have been listening too. Acoustic studies of Neolithic chambers in Britain and Ireland, including Newgrange, and of the Hypogeum in Malta, found that they resonate strongly in the range of the human voice. And at Rosslyn Chapel in Scotland, carved in the fourteen hundreds, some researchers read the patterns on its stone cubes as Chladni figures. That's still an open question. But the intuition is ancient: that sound has a shape, and that sacred space can hold it.

In this system, the same frequency that makes the music also generates the projected geometry. Sound and image aren't two layers laid over each other. They're one signal, seen and heard.

### slide_06 — Methods II: The Interpretive Layer
Physics gives us the notes. Meaning comes from the second layer. Across history, cultures separated by oceans and centuries looked at the same sky and built cosmologies around it: Kabbalistic, Vedic, Egyptian, Buddhist, Hermetic, Taoist and Tarot. Each one encoded the planets into its own architecture of meaning. These seven are a starting set, not a closed canon. The framework can hold any tradition that has read meaning in the sky.

In this framework, a large language model, Anthropic's Claude, acts as a translator. It takes the planetary positions of any moment, whether a birth, a historical event or tonight's sky, and reads them through a chosen tradition. From that reading, it produces a compositional grammar: which planet leads, the harmonic center, the character of the space, and a written narrative.

### slide_07 — The composer sets the language
An important distinction: I'm the composer. Every timbre, theme and harmonic language is written by a person. The data and the traditions act as the conductor, shaping which of those materials play and how. The composer sets the language. The system conducts.

And the framework is built to grow, for example with Mayan astronomy, as the work meets new communities.

### slide_08 — Methods III: The Experience
The full-scale form is a 360-degree dome. Participants recline at the center. Each planet becomes a voice positioned in space. Each orbital relationship becomes a harmonic interval, and the dome becomes a living orrery.

The visuals are live cinema rather than a fixed backdrop: cymatic geometry, cosmological imagery, sacred sites, the natural world. Beneath it all, low-frequency vibroacoustic resonance is felt directly in the body, through the seating or a wearable. It's designed to support contemplative practice. Part planetarium, part cathedral, part meditation chamber.

### slide_09 — Accessibility as Health Equity
The part of this work I care most about for this audience is what you feel. The composition isn't only heard. It's also rendered as physical vibration, delivered through the seating or a wearable device, so the experience doesn't depend on hearing alone. Research on vibrotactile perception shows that people, including deaf listeners, can tell musical qualities such as timbre apart through touch alone.

So the vibroacoustic layer isn't an add-on. It's a design principle. Immersive, contemplative music experiences have mostly been built for hearing audiences. This one is built to include deaf and hard-of-hearing participants from the start. That's where this project meets music, medicine and health equity most directly.

### slide_10 — Results: A Working Prototype  *(POC capture plays under this)*
I want to be clear about where this is. What I'm about to show you is an early, in-progress prototype. It's crude. It's a sketch.

You enter a moment in time. The prototype calculates real planetary positions with ephemeris math, weighs each planet's strength using rules from Vedic astrology, and assigns each a drone at its orbital frequency with Kepler-ratio harmonics, generated live in the browser. The cymatic geometry is drawn from those same frequencies. And the language model produces a written reading of that moment through the chosen tradition. Each layer can be balanced independently.

What matters here isn't polish. It's that the whole chain, from data to sound to geometry to narrative, already runs end to end in an ordinary web browser.

### slide_11 — Discussion & Next Steps
This work sits where psychoacoustics, contemplative practice and accessibility meet. And the question underneath it is still open: why did so many cultures, looking at the same sky, arrive at such similar structures? The system doesn't answer that. It lets you hear it. Same sky, different voice.

Next is moving from prototype to dome scale: building the full music system in Max, TouchDesigner and Ableton, and partnering with institutions and venues to produce it. The goal is a replicable grammar, not a finished object.

### slide_12 — References
The sources for this presentation are listed here.

### slide_13 — Close
The ancient idea was that the universe is music. I believe it always has been and always will be. We just needed the instruments to hear it. This is the portal. Thank you.
