---
name: kinetic-type
description: Animate on-screen text the way top app launch films do - block-cursor type-on with scrambled glyphs, two cursors typing at once, right-to-left reveals, slammed loud words, time-stamp chips, rolling stats, and an end line that assembles from earlier beats. Use whenever a video needs text that moves (titles, captions, taglines, end cards, stat callouts, "text graphic animation"), or when someone asks for type like Base, Apple or a launch film. Includes a seek-safe HyperFrames engine.
---

# Kinetic type

Text in a launch film is a performer, not a label. It enters with a move, it lands on a beat, and it says one thing.

Learned frame by frame from the Base App launch film (57s, 60fps, 640K views on X), then generalized. Borrow the moves, never Base's look: use the brand's own cursor shape and color.

## 1. The moves

### Block-cursor type-on (the signature)
- A solid colored block (the brand mark) runs at the front of the text like a cursor.
- Inside the block, a scrambled glyph flickers (block characters, symbols), so the reveal feels computed, not typed.
- Letters not yet revealed keep their space. The layout never jumps.
- A full line lands in 0.6 to 1.0 s (about 0.05 s per letter), then holds clean with no cursor.
- Base specifics measured: "See what's happening" fully revealed by 0.9 s; "Send money globally for free" in 0.6 s with two cursors.

### Two cursors at once
Split the line at the middle space and type both halves at the same time ("See wh█ ha█"). Use it for longer lines and for lines that should feel fast.

### Right-to-left reveal
Type backwards from the end. Reserve it for a line whose meaning is a reversal (Inverse, undo, opposite). A move that means something beats a move that only decorates.

### Typed input with caret
Text typed into a real UI field (chat box, search bar) with a thin caret, the field scrolling as it grows. Base uses this for chat. Makes the UI feel live.

### Slammed loud words
For a loud character's line: heavy caps, one word per beat, each word scaling down from 2x with a slight random rotation, the line shaking afterward. Pair each word with a hard pop sound. Contrast: quiet lines type on, loud lines slam.

### Time-stamp chips
A bold time plus a short label ("09:00 · Lecture"), bottom left, typed on in under 0.5 s at the start of each shot. Turns a montage into one day passing and gives every shot a reason.

### Rolling stats
Big numbers never just appear. They count up (power2.out, 1.2 to 1.6 s) with a small label above ("quietkoi · 30 days").

### Underline sweep
A thick bar in the line's color sweeps under a landed line (0.5 s, power3.out). For right-to-left lines, sweep right to left.

### Logo build (Base)
The mark cycles colors on consecutive beats (yellow, red, blue squares, about 0.25 s each), then pixelates into the wordmark, then resolves clean. Adapt with the brand's own colors and mark.

## 2. Composition rules

- One line at a time on screen. If two lines must coexist, they are two halves of one idea.
- Over footage: white, heavy (700-800), bottom left or top left, a soft shadow and a bottom gradient for legibility. Keep faces clear.
- On type cards: dark text on a light neutral, medium weight (500-600), centered, no full stop on Base-style taglines; keep the full stop when the line is a statement.
- Type cards are short (1 to 1.6 s each) and cut hard between footage.
- Cursor color carries meaning. One color per idea, reused every time that idea appears (Nika: green for Mirror, purple for Inverse, blue for everything else).

## 3. Make the end line shine

The end line is the payoff, so the film should build it before it is said in full:

1. Plant each half on its own beat earlier in the film, each with its own color and move.
2. At the end, assemble the halves on a clean card using the same moves, so the viewer recognizes them.
3. Color the halves in their idea colors as the line completes, with the single strongest sound hit of the film.
4. Hold 4 to 6 s with only the logo and the CTA added.

Example (Nika Flow B v5): "Mirror the best." types left to right in green over the Mirror beat; "Inverse the rest." types right to left in purple over the Inverse beat; the end card types both again in the same colors and directions, then tints them, on a metal-hit sound.

## 4. The engine (HyperFrames)

`examples/nika-animatics/kit/kit.js` contains `NK.typeOn` and `NK.slamWords`, plus `kit.css` classes `.tc`, `.tcur`, `.sw`.

```js
// reveal the text already inside #line, starting at 12.0 s
NK.typeOn(tl, "#line", 12.0, { color: "#22c55e", dur: 0.9 });
NK.typeOn(tl, "#line2", 13.0, { color: "#8b5cf6", dir: "rtl" });   // types backwards
NK.typeOn(tl, "#card", 9.1, { color: "#3b49f0", cursors: 2 });      // two fronts
NK.slamWords(tl, "#loud", 19.75, 0.18);                              // one word per 0.18 s
```

Both are driven by a progress tween with `onUpdate`, so they are seek-safe: HyperFrames can render any frame in any order. Don't drive type with `tl.call` or timers.

Rules when using it:
- Set the element's opacity to 1 at the same time the type-on starts (the engine hides unrevealed letters, not the element).
- Avoid a page-level CSS variable named `--card`; the kit uses it for its dark card color.
- After `lint`, snapshot the frames mid-reveal (about a third of the way through) and at the end to check the cursor and the final line.
