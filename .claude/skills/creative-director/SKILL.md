---
name: creative-director
description: Come up with, structure and critique launch films, product videos, teasers and social ads before and after they are built. Use whenever someone asks for a video idea, concept, script, storyboard, hook, ad or launch film, wants a video "better", "more creative" or "less generic", or before /hyperframes or /stageshow builds something new. Holds the eight concept devices and the measured flow rules learned from the Cero, Predictstreet, Motoswap and Plasma films, plus a scoring rubric.
---

# Creative director

Work in this order: **truth, idea, flow, threads, shots, build, measure, critique.** Never start at shots. A film that starts as a shot list ends as a feature list.

Evidence and examples for everything here: `docs/creative-thinking.md` (why), `docs/visual-grammar.md` (shot by shot, how it moves) and `docs/creative-playbook.md` (production). Read both before the first concept in a session.

## 1. Find the product truth

Ask for, or dig out of the brief, the answers to these:

- What did people put up with before this product? Be concrete: "FX fees on every coffee abroad", not "friction".
- What does it feel like once that's gone? One word.
- What is the one number we can prove?
- Who is it for, and do they want **loud** (crypto-native, rewards, games) or **quiet** (salary, savings, trust)?

Write the truth as: **"[Product] turns [specific annoying thing] into [feeling]."**

## 2. Three concepts, three devices

Write three concepts, each from a **different** device. Each concept is one sentence a friend could repeat after hearing it once.

| Device | Shape | Reference | Use when | Fails when |
|---|---|---|---|---|
| Make it a game | Dull action becomes play: packs, jackpots, wheels, scores | Cero | Rewards, points, loyalty | No real reward to show |
| Before and after in one move | One transition carries the promise | Predictstreet couch-to-stadium zoom | The product changes your role | The "after" is abstract |
| The world reacts | Future shown as fact: news, boardrooms, podcasts, family dinners | Motoswap | Challengers and disruptors | No humour, or characters resemble real people |
| Proof before claim | Show it until it's obvious, say it once at the end | Plasma Zero FX, four countries | Fees, speed, coverage | The proof isn't visible on camera |
| One sentence, many shots | One line holds while footage cuts underneath | Plasma × Deel | "Anywhere / anytime" benefits | The sentence is long |
| Subtract | Remove sound, color or motion right before the reveal | Plasma "Now open." on black | Launches, announcements | Used more than once |
| Receipts | Numbers are the plot; growth is the climax | Plasma Year One, $100M chart | Milestones, anniversaries | Numbers are small or vague |
| The product is the story | One continuous move through the real UI, numbers ticking | Plasma Android | Features with a clear loop | Cluttered UI or a slow payoff |

For each concept give: the one sentence, the hook (first 2 seconds, what we **see**), the last line, and the device. Then recommend one and say why the other two lose. Kill a concept if a competitor's logo could replace ours and it would still make sense.

## 3. Design the flow before the shots

Choose the **energy shape** and say it out loud:

- **Plateau**: loud and flat throughout (Cero). Short, punchy, game-like spots.
- **Drop**: quiet setup, then the music lands (Plasma "Now open"). Launches.
- **Crescendo**: every third louder than the last (Motoswap). Stories and trailers.
- **Fade**: energy pulls back in the last third (Plasma Year One). Reflective, milestone pieces.

Measured rules from the reference films. Treat them as defaults, and break one only on purpose:

- Hook is a human moment in 0 to 2s. The product appears by 3s.
- Median shot 1.1 to 1.5s, or 2 to 4 beats of the chosen track.
- **The last third cuts slower than the busiest third** (all 7 measured films).
- **At most one silence**, right before the most important line (3 of 7 films).
- Quiet school: cut on the beat grid, about a quarter beat early (Plasma lands at 0.77 of the beat). Loud school: cut on action in the picture.
- End card holds 4 to 6s.
- Master to -14 LUFS unless the brand is deliberately quiet.

Then write the beat sheet: `time | beat | what we see | text on screen | sound | energy (1-5)`. The energy column should trace the chosen shape.

## 4. Threads: what holds the film together

Read `docs/visual-grammar.md` (the twelve principles, frame-level evidence, and a worked example). Before listing shots, decide:

- **Hero object:** the product's core action made into a thing you can hold (Cero's coin = flip for cashback). It opens the film and closes it.
- **Shape:** usually the hero object's outline or the logo. Every mask, gauge, button and transition uses it.
- **Anchor:** the one thing that stays locked on screen while the world swaps, for the "everywhere / every currency" section.
- **Milestone:** the one moment the whole frame inverts (palette flip, sunburst), not just the number.
- **Void:** where the single black or silent beat goes.

Then write the **transition chain**: for every cut in the key sequence, name what carries the eye. Options: object carry, object as wipe, anchor swap, shape match, color wipe, word per beat, hard cut on beat (montages only), void (once). A cut with no carrier is a dead cut. Fix it or move it into a montage.

Borrow the thinking, never the look. Translate each principle into the product's own world: ask "if our product's core action were an object, what is it?", and "why *this* place?" for every background.

`examples/thread-demo/` is a working HyperFrames build of these threads (coin hero object, card anchor swap, ring shape match, $1,000 inversion, void, bookend).

## 5. Shots

For every shot, answer: **what does the viewer learn or feel here?** Cut any shot that only looks good. Prefer verbs you can film: tap, rip open, zoom, count up. Avoid adjectives.

Useful moves (examples in the playbook):
- A line of text held while 3 to 5 shots cut underneath
- A cycling word slot ("Add USD" → "Add MXN" → "Add money")
- "+$130.23 from Brand" toasts on real-world shots, as testimonials
- A stat slam: big number, punch-in, a one-frame flash on the cut
- A number and a chart in sync (`examples/milestone-chart`)
- A cold open on the payoff, then "Six months earlier."
- The reward as a physical object (pack, card, ticket)

## 6. Build

- Choose the music first and note its BPM. Plan durations in beats.
- Kinetic type, stats, charts and assembly: `/hyperframes`. Product UI, phones, dashboards: `/stageshow`. Check `/hyperframes-registry` before hand-building an effect.
- One accent color (loud) or none (quiet). One display font.

## 7. Measure

Run the draft, and the reference it's meant to rival, through the flow tool:

```bash
.venv/bin/python tools/flow_report.py renders/draft.mp4 --chart renders/draft-flow.png
```

Setup, once: `python3 -m venv .venv && .venv/bin/pip install librosa matplotlib`. Look at the chart. Does the curve match the chosen shape?

## 8. Critique

Score the draft pass/fail and show the evidence for each line:

1. The idea fits in one sentence, and a competitor couldn't run it.
2. A human moment in the first 2 seconds. No logo, no black.
3. The product is on screen by 3 seconds.
4. Every number on screen is real.
5. One accent color, or none, held throughout.
6. The energy curve matches the chosen shape.
7. The last third slows down.
8. Silence used at most once, and on the key line.
9. Read with the sound off, from one frame per second, the story still lands.
10. The end card holds 4 to 6 seconds with one clear action.
11. Every cut in the key sequence has a carrier (object, anchor, shape, color, beat).
12. The film opens and closes on the same hero object or shape.

Fix the failures, re-render, measure again. Two passes, then ship.

## Guardrails

- Borrow the device, never the execution. Use our own color, type, world and characters. Never recreate a specific brand's ad.
- No real person's likeness without written permission. No lookalikes.
- Money, odds or rewards products need a legal line, in the video or in the reply post.
