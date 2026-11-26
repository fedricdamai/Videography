# Launch Film Playbook

How Cero, Predictstreet, Motoswap and Plasma built their launch videos, and how we make our own.

Nine videos from 2026. Together they pulled 4.21M views on X. Every timing and audio number below was measured from the source files with ffmpeg, not eyeballed.

Two schools show up. Cero, Predictstreet and Motoswap are **loud**: fast cuts, one hot accent color, 3D rewards, big type. Plasma is **quiet**: white space, small type, a silver card, cinematic lifestyle. Sections 1 to 3 cover loud. Section 3b covers quiet. Pick one per brand and stay in it.

---

## 1. The three films at a glance

| | Cero | Predictstreet | Motoswap |
|---|---|---|---|
| Post | [joincero](https://x.com/joincero/status/2087953404190466515) | [predictstreet](https://x.com/predictstreet/status/2065073042729111841) | [motoswap](https://x.com/motoswap/status/2104535846724755529) |
| Views / likes | 1.35M / 1.6K | 884K / 9.2K | 849K / 1.3K |
| Length | 34.8s | 35.1s | 97.5s |
| Format | 1920x1080, 60fps | 1920x1080, 24fps | 1920x1080, 30fps |
| Hard cuts | 14 | 11 | 52 |
| Median shot | 1.25s | 1.25s | 1.10s |
| Shortest shot | 0.40s | 0.17s | 0.07s |
| Loudness | -16.1 LUFS | -14.3 LUFS | -14.0 LUFS |
| Loudness range | 1.9 LU (music bed) | 4.9 LU | 9.7 LU (dialogue) |
| Accent color | Electric lime | Royal blue into orange | Ultraviolet purple |
| Type | Editorial serif | Wide heavy caps | Heavy rounded caps |
| Genre | Lifestyle product spot | Sports hype promo | Narrative parody short |

All three are 16:9. X plays landscape full width in the timeline, so none of them shot vertical first.

---

## 2. The shared formula

Strip the brands off and the same skeleton shows up in all three.

1. **A human moment in the first 2 seconds.** A hand tossing a lime ball at the sky. A fan slumped on a couch. A coastal road under a "Breaking news" caption. Never a logo.
2. **The product on a screen by second 3.** A phone notification, a tournament screen, a news chyron. Viewers learn "this is an app" before they can scroll.
3. **One accent color owns the film.** Cero is white plus lime. Predictstreet is navy plus a blue-to-orange gradient. Motoswap is black plus purple. Every graphic, glow and UI highlight uses it.
4. **The reward becomes a physical object.** Cero rips open a lime foil pack and a Lambo, cash and a watch fly out. Predictstreet spins a foil pack, then a glowing player card, then a gold match ticket. Abstract value (points, rewards, odds) turns into something you could hold.
5. **Big numbers get their own shot.** `$1,100,000`. `$492.01B`. `8,927,021`. Full frame, nothing else, counting up.
6. **Shots last about one second.** Median shot is 1.1 to 1.25s across all three. They only hold longer on two things: the UI explainer (6 to 13s) and the logo.
7. **The logo holds 4 to 5 seconds at the end.** Cero: icon, tagline, wordmark resolve. Predictstreet: partner lockup. Motoswap: "MOTOSWAP IS COMING", URL, mark.

---

## 3. Shot-by-shot breakdowns

### Cero, "Spending with upside" (34.8s)

| Time | Shot | How it was made |
|---|---|---|
| 0.0-2.2 | POV hand tosses lime ball against blue sky between buildings | Live action, handheld, low angle |
| 2.2-4.3 | Phone macro, McDonald's transaction card slides in | UI animation inside phone mockup |
| 4.3-5.7 | Tap-to-pay at food truck, then water park counter | Live action POV, phone screen composited |
| 5.7-7.5 | "opened the packs" / "for the upside" serif type, confetti | Kinetic type, particle confetti |
| 8.0-9.0 | Phone with pack peeking out of screen | UI plus 3D object breaking the frame |
| 9.0-11.0 | Lime "cero" pack rips, Lambo, cash, watch, ball, ticket burst out on lime sunburst | 3D render (Blender/C4D) |
| 11.0-12.5 | `$1,100,000` in 3D lime chrome, MEGAPOT above | 3D extruded type |
| 12.5-13.7 | Phone: Cero Score gauge counts to 435 | UI animation |
| 13.7-15.2 | Cashier at grocery POS, then iOS notification "You've been paid your salary $3,200" | Live action, then UI on lake wallpaper |
| 16.5-19.2 | Spin wheel lands on 2x, salary doubles $3,200 to $6,400 | Motion graphic |
| 19.2-20.2 | Florist, tap to pay | Live action |
| 20.2-23.5 | Score inputs: Cash held +9, On-chain wallets +28, Socials +61, orbit into 1000 gauge | Motion graphic explainer |
| 23.5-26.7 | Phone: credit line unlocks, glass card, `$339 / $500 left` | UI animation |
| 26.7-29.5 | Coffee shop tap, then circle-masked collage of tap moments | Live action plus mask grid |
| 29.5-34.8 | App icon, "The upside of spending", wordmark resolves | Logo animation |

**Steal this:** alternate live action and UI every 1 to 2 seconds. Live action proves "real people use it". UI proves "here's what you get". The 3D pack burst is the one indulgent moment.

### Predictstreet, "World Cup '26 Sprint" (35.1s)

| Time | Shot | How it was made |
|---|---|---|
| 0.0-2.1 | Bored fan on couch in jersey, holding phone | Live action or AI video |
| 2.1-3.1 | "DON'T JUST WATCH THE GAME" over TV, "WATCH" in orange | Kinetic type over footage |
| 3.1-4.4 | Phone: "Who will win the World Cup?" market | UI in hand |
| 4.4-6.0 | Match footage, goalkeeper dive | Licensed or generated sports footage |
| 6.0-9.0 | "JOIN THE GAME" with radial zoom blur, fan teleports from couch to stadium | Speed-ramp zoom transition |
| 10.0-12.5 | Fan of player cards, then silver foil pack spinning on blue | 3D render |
| 12.5-14.6 | "GET YOUR CARD", glowing player card pops from pack | 3D plus glow |
| 14.6-17.0 | "EXPLORE" letters explode over tilted dashboard; 3 step cards: Explore markets, Take a position, Win if correct | Kinetic type over 3D-tilted UI |
| 17.0-22.0 | "TAKE YOUR POSITION", dashboard screens fly through perspective, World Cup Sprint panel | UI screens in 3D camera move |
| 22.0-23.0 | "CLIMB THE RANKS" over leaderboard | Type plus UI |
| 23.0-28.2 | Pack returns, morphs into gold "MATCH TICKET", "WIN YOUR TICKET TO THE FIFA WORLD CUP 2026" | 3D render |
| 28.2-29.6 | Ball macro with brand, whip blur | 3D or macro shot |
| 29.6-35.1 | Partner lockup | Logo animation |

A legal line runs the whole film: "18+. Prediction markets involve risk. Not available in all jurisdictions." Any money, odds or rewards product needs one.

**Steal this:** the 6 to 14.6 and 14.6 to 28.2 stretches have almost no hard cuts. Motion carries you from scene to scene (zoom blur, pack morphs into ticket). Fewer cuts, more camera.

### Motoswap, "The house pays the players" (97.5s)

| Time | Beat | Shots |
|---|---|---|
| 0-12 | Cold open, hype montage | Aerial road, news anchor "ETHEREUM SENDING SHOCKWAVE", `$492.01B`, price chart, split-screen reaction streamers, guy in car "No way", guy on laptop "ETH really made a comeback" |
| 12-20 | Proof via numbers | Purple stat slams: CATS PVE AIRDROPS 14,641 to 8,927,021, MOTO PAID OUT 623,997 to 1,810,081. Yacht, champagne toast. RGB glitch out |
| 20-23 | Time jump | Black frame, monospace "Six months earlier." |
| 23-31 | Origin | Streamer with LIVE badge: "I'm going to talk about a new app launching soon… Motoswap". Logo flash |
| 31-41 | The world reacts | News chyron "TRADERS MIGRATE BACK TO ETH", developer at laptop "I think we're back in business", finance exec "Looks like there's a new dex… taking all the volume" |
| 41-53 | Product proof | Wall of tweets, rakeback UI counting to `$1,500.00`, tweet quotes zoomed huge: "Time to earn $MOTO" |
| 53-75 | Comedy runner | Exec and analyst scene. Family dinner: "How much did you lose today?" "1 billion." Suits stride into boardroom |
| 75-80 | Feature wall | Purple kinetic stack: RAKEBACK, CREATOR FEES, PVE LAUNCHES, REVENUE TO MOTO STAKERS |
| 80-89 | Emotional turn | Podcast split-screen: "Trenches are broken… there's no hope for the little guy. Maybe now there is" |
| 89-97.5 | CTA | "MOTOSWAP IS COMING" builds word by word, MOTOSWAP.ORG, logo |

Small burned-in subtitles on every line of dialogue. Most viewers watch muted.

The live action is AI-generated cinema: shallow depth of field, warm practical lights, consistent faces across shots.

**Steal this:** the structure. Cold open on the payoff, jump back "six months earlier", tell the origin, show the world reacting, land on a line with heart. The X post copy is the hook ("BlackRock holds an emergency meeting about us"), the video pays it off.

**Don't steal this:** two characters are recognisable lookalikes of real public figures (a BlackRock CEO, an Ethereum founder). For a financial product that invites right-of-publicity claims, false-endorsement complaints and X synthetic-media labels. Use archetypes ("a Wall Street CEO", "a famous dev") who don't resemble anyone real.

---

## 3b. Plasma, the quiet school

[@plasma](https://x.com/plasma) is a stablecoin neobank (Plasma One card and app). 230K followers. Six of their top videos, measured:

| Video | Views | Format | Length | Cuts | Median shot | Loudness |
|---|---|---|---|---|---|---|
| [Year One](https://x.com/plasma/status/2103107655376269729) | 465K | 1920x1080, 23.976fps | 67.6s | 50 | 0.67s | -14.4 LUFS |
| [Zero FX fees with Platinum](https://x.com/plasma/status/2100578363521802659) | 260K | 1920x1080, 30fps | 21.9s | 5 | 4.40s | -23.6 LUFS |
| [Plasma One is now open to everyone](https://x.com/plasma/status/2102764201219596555) | 212K | 1920x1080, 23.976fps | 38.4s | 20 | 1.46s | -18.7 LUFS |
| [Aurora partnership](https://x.com/plasma/status/2102792796885197310) | 109K | 3840x2160, 25fps | 80.4s | 66 | 0.88s | -17.9 LUFS |
| [Business waitlist](https://x.com/plasma/status/2122708492150824961) | 52K | 1080x1350, 30fps | 10.1s | 1 | one shot | -25.0 LUFS |
| [$100M moved](https://x.com/plasma/status/2112923666325340182) | 32K | 1920x1920, 60fps | 18.2s | 0 | one shot | -13.0 LUFS |
| Plasma × Deel, "Get paid in stablecoins" | local file | 1920x1080, 23.976fps | 28.1s | 18 | 1.29s | -13.8 LUFS |
| Plasma One, live on Android | local file | 1920x1080, 23.976fps | 28.7s | 3 | one 25.5s UI take | -21.8 LUFS |

The last two came from our own sample folder and were analyzed locally. That analysis measured three of the same files I did (Cero, Motoswap, "Now open"), and its cut times and loudness matched mine exactly.

### The look

- **No accent color.** Off-white or black backgrounds, a brushed silver card, and green only inside charts. Restraint is the brand.
- **Small type, centered, sentence case, full stop.** "Now open." "Add money and start spending." "Do more." Never more than five words on screen.
- **Words write on one at a time.** "Wherever" holds, then becomes "Wherever you are." "Only with" becomes "Only with Platinum." The pause does the work a bold font does in the loud school.
- **Glass UI chips float in the footage.** A man checks his phone in a gym and a frosted card hangs in the air beside him: `+$130.23 from Eight Sleep`. Tracked to the scene, not slapped on top.
- **The silver card is the hero object.** It plays the role the foil pack plays for Cero and Predictstreet, but rotates slowly with a light sweep instead of exploding.

### Four films, four jobs

**Zero FX fees (21.9s).** Four overhead shots of a card tapping a terminal: a New York hot dog stand, a red Paris café table, a candlelit restaurant, a Japanese convenience store counter. Four seconds each, no words. Then white: "0% FX fees." / "Wherever you are." / "Only with Platinum." The claim is shown as geography before it is ever said.

**Now open to everyone (38.4s).** Logo, "Now open.", then lifestyle footage (street, sauna, gym, Tuscany road, sunset swim, yacht) with one short line each and a balance chip ticking up. Ends on the app icon with store badges. Shots land every 1.1 to 1.25s, the same rhythm as the loud school.

**Year One (67.6s).** A stats-and-logos year in review. Deposit numbers (`$500M`, `$1B`, `$7.00B+`) on full-bleed slides, partner logos cut every 10 frames (0.417s, which is 144 BPM at 23.976fps), product footage, real usage charts, "We're just getting started." It also uses real press footage of public officials. That's licensed news archive, not AI lookalikes, and it still needs clearance.

**$100M moved (18.2s).** One shot. A huge number counts up while a line chart draws beneath it, and both axes rescale as it grows, so the curve always fills the frame. Ends with a tooltip on the last point. **We rebuilt this as a template: `examples/milestone-chart/index.html`.** Swap `FINAL`, `DAYS`, `MONTHS` and the data and it renders a 9-second 1080x1080 video in 14 seconds.

**Plasma × Deel (28.1s).** "Work happens" holds over a home office and a sunroom. "everywhere." lands over a café and a beach camper. The sentence is unfinished for 2.7 seconds, and that wait is the hook. Then frosted toasts on four locations: `+$3,714.76 from Deel` at an airport, `+$750.00` on a mountain, `+$2,743.40` in a workshop, `+$1,250.00` on a Tokyo platform. Then "Spend in stablecoins." stays fixed on screen while five shots cut underneath it in 3.3 seconds. The first six cuts sit on a 1.33s grid, two beats at 90 BPM.

**Live on Android (28.7s).** Three live shots in 3.2 seconds, then the entire rest of the ad is one continuous take of the app: balance, an "Earn $10" card, a progress bar filling, a scrolling list of real purchases each with its cashback (`Tesla supercharger -$12.41 +$0.37`, `ChatGPT -$20.00 +$1.00`), a "You earned $10!" toast, and the balance ticking `$410.96` to `$420.96`. The reward loop is told in the UI itself. This is the exact job `/stageshow` exists for.

### Three moves to copy from Plasma

1. **Hold one line of text while the footage cuts under it.** "Spend in stablecoins." over five places reads as "everywhere" without saying it.
2. **Cycle one word slot.** "Add [USD]" becomes "Add [MXN]" becomes "Add money". You show breadth in four seconds without writing a list.
3. **Use toasts as testimonials.** `+$130.23 from Eight Sleep` over a real person in a real place gives you social proof with no quotes and no faces to clear.

### How they post

- Video post first, then a **reply** carrying the link and any legal line ("Plasma is not a bank…"). The video post stays clean.
- Every reply link has its own campaign slug: `plasma.org/TRLLNS`, `/AEDONE`, `/DUBAIP`, `/111111`. Every film is tracked separately.
- Formats match the content: 16:9 for films, 4:5 for UI demos, 1:1 for data.

### Loud or quiet?

| Use loud when | Use quiet when |
|---|---|
| The audience is crypto-native or under 30 | The product holds people's salary or savings |
| The hook is a reward, a game, a points race | The hook is trust, fees, access, status |
| You need to win the scroll against memes | You need to look like a bank that isn't boring |

Quiet spots mix low (-18 to -25 LUFS) on purpose, for an ambient mood. They also play quieter than everything around them in the feed. Our default stays -14 unless the brand is deliberately quiet.

---

## 4. The production stack

Each film is five layers. Here is what makes each one and where our tools fit.

| Layer | Examples in refs | Tool | Effort |
|---|---|---|---|
| A. Live action and lifestyle | Tap-to-pay, fans, streamers, boardroom | Shoot on phone/cinema camera, or generate (Veo, Kling, Runway, or HeyGen through `/media-use`) | High |
| B. 3D hero objects | Foil packs, player card, ticket, chrome `$1,100,000` | Blender or Cinema 4D; Spline for quick versions; image-to-video from a rendered still as a shortcut | High |
| C. Product UI | Score gauge, notifications, dashboards, credit line | **StageShow** (`/stageshow`) to rebuild the real UI as faux UI and animate it; **HyperFrames** to render it | Medium |
| D. Kinetic type and stats | "JOIN THE GAME", stat slams, feature walls, end card | **HyperFrames** (`/hyperframes`, registry blocks via `/hyperframes-registry`) | Low |
| E. Edit, sound, captions | Cuts on the beat, whooshes, burned subtitles | HyperFrames as the timeline (clips plus overlays plus audio), or Premiere/Resolve if footage-heavy | Medium |

Layers C and D are where code beats After Effects. They are 40 to 60% of the screen time in Cero and Predictstreet, they change every launch, and HTML means the real brand fonts, real numbers and real UI tokens with no rebuild.

Proof it works: `examples/stat-slam/index.html` rebuilds Motoswap's 0:13 stat slam (punch-in with blur, counter, one-frame white flash on the cut). It renders to 1080p MP4 in 43 seconds in this repo's cloud container. `examples/milestone-chart/index.html` rebuilds Plasma's number-plus-chart milestone film as a reusable template.

---

## 5. The production run, step by step

### Step 1. Brief (half a day)

Answer five lines before anything gets made:

- **Hook line** for the X post. Concrete and a little absurd. "BlackRock holds an emergency meeting about us." beats "Introducing our new DEX."
- **The one feeling.** Cero: spending is fun. Predictstreet: stop watching, start playing. Motoswap: the little guy wins.
- **The tangible reward.** What becomes the 3D object? A pack, a card, a ticket, a coin, a key.
- **Three proof numbers.** Real ones you can defend. They become the stat slams.
- **One accent color and one display font.** Pull from brand. If the brand has none, pick a color nobody in your category owns.

### Step 2. Beat sheet (half a day)

Write the film as a table before storyboarding. 35 seconds fits about 28 shots at the reference median.

| Time | Beat | Visual | On-screen text | Sound |
|---|---|---|---|---|
| 0-2 | Hook | Human moment | none | Music in, no intro |
| 2-4 | Product reveal | UI on phone | none | Swipe/tap SFX |
| 4-8 | Life proof | 2-3 live action taps | 1 short line | Beat hits on cuts |
| 8-12 | Reward | 3D object reveal | Big number | Riser into impact |
| 12-24 | How it works | 3 UI steps | Step labels | Clicks, dings |
| 24-29 | Social proof | Collage / reactions / stats | Stat slams | Build |
| 29-35 | End card | Logo lockup | Tagline, URL | Final hit, ring out |

For a 90s narrative like Motoswap, use the cold open / time jump / origin / reaction / turn / CTA structure from section 3.

### Step 3. Storyboard and style frames (1 day)

- One still per shot. AI image models are fine here; it's a plan, not the film.
- Three finished style frames: one live action, one UI, one 3D. Get sign-off on these before any animation.

### Step 4. Make the layers (3 to 7 days, in parallel)

**A. Live action.** Shoot POV handheld at 60fps (Cero) or 24fps cinematic (Predictstreet, Motoswap). Phone screens: shoot with a plain screen and track the UI on later, or keep the screen off-angle. If generating, lock one character sheet per person so faces stay consistent shot to shot.

**B. 3D objects.** Model once, render several angles. Packs and cards need: foil material with sharp speculars, a slow rotation, one "burst" moment. Render with alpha (ProRes 4444 or PNG sequence) so HyperFrames can layer type over and behind it.

**C. UI.** In Claude Code:

> Using /stageshow, build our [screen] as faux UI: a phone showing the score gauge counting from 0 to 435, then a notification sliding in. Brand color #XXXXXX.

Then render it through HyperFrames as its own clip, with transparent background if it sits over footage (`--format mov` for alpha).

**D. Type and stats.** In Claude Code:

> Using /hyperframes, make a 4-second stat slam in our purple: "USERS" counting to 1,204,330, hard cut with a one-frame flash, then "PAID OUT" counting to $3.1M.

Check `/hyperframes-registry` first for ready blocks (glitch, kinetic type, captions, zoom transitions) before hand-building.

### Step 5. Assemble (1 to 2 days)

- Cut to the music. Every hard cut lands on a beat or a hit.
- Default shot length 1 to 1.5s. Hold only the UI explainer and the end card.
- Transitions the refs use: hard cut with 1-frame white flash, radial zoom blur, RGB split glitch, object morph (pack into ticket), circle-mask collage.
- Burn in captions for any dialogue. Small, white, bottom center (Motoswap style) or big kinetic (TikTok style). `npx hyperframes transcribe` gives word timings.

### Step 6. Sound (1 day)

- Music bed under everything. Cero's 1.9 LU range means the music is compressed flat and never dips.
- One SFX per cut: whoosh into, impact on. Risers before every reveal.
- Master to **-14 LUFS integrated, -1 dBTP peak**. That's where Predictstreet and Motoswap landed and what social platforms normalise to.

### Step 7. QC and deliver

```bash
npx hyperframes lint
```

```bash
npx hyperframes check
```

```bash
npx hyperframes render --output launch-16x9.mp4
```

Checklist before posting:

- [ ] Watch the exported MP4 muted. Does it still make sense?
- [ ] First frame is a human moment, not a logo or black.
- [ ] Every number on screen is real and defensible.
- [ ] Legal line present if money, odds or rewards are involved.
- [ ] No real person's likeness unless you have their written OK.
- [ ] Loudness -14 LUFS (`ffmpeg -i out.mp4 -af ebur128 -f null -`).
- [ ] Exports: 16:9 1920x1080 for X. 9:16 1080x1920 and 1:1 cutdowns for other feeds (`npx hyperframes init --resolution portrait`).

### Step 8. The post

- First line is the hook, 10 words or fewer.
- Second line is the product in plain words. "Motoswap is live on Ethereum."
- Third line is the promise. "The house pays the players."
- Link last. Upload the video natively.
- Or Plasma's way: video post with no link, then a reply with the link, its own tracking slug, and any legal line.

---

## 6. Skills installed in this repo

All live in `.claude/skills/` and load automatically in Claude Code sessions here.

| Skill | Use it for |
|---|---|
| `/hyperframes` | Read first for any video: make, edit, animate, render |
| `/hyperframes-cli` | Scaffold, lint, check, snapshot, preview, render |
| `/hyperframes-registry` | ~450 ready blocks: transitions, captions, kinetic type, charts, 3D |
| `/media-use` | Music, SFX, voiceover, images, logos, cutouts, color grades |
| `/stageshow` | Faux product UI: phones, dashboards, notifications, cursor walkthroughs |
| `/reverse-any-video` | Rebuild an existing video as an editable HyperFrames project. **HyperFrames Pro (paid).** Only for videos we have rights to |
| `/style-sampling` | New episode in a proven explainer style. Pro |
| `/figma` | Pull Figma frames, tokens and logos into a video |
| `/remotion-to-hyperframes` | Port Remotion or other animation code |
| `/slideshow` | Live presentation decks |

Notes:

- HyperFrames skills offer to send a usage ping to HeyGen when they start. Say no to skip, or set `HYPERFRAMES_SKIP_SKILLS=1`.
- Refresh with `npx hyperframes skills update`. StageShow is pinned to commit `8020577` of `benjitaylor/skills`.
- Rendering needs Node 22+, Chrome and FFmpeg. `npx hyperframes doctor` checks all three.
