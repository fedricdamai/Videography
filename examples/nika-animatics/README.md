# Nika copytrading ripomatics

Three pitch videos for the Nika copytrading launch, one per flow in the script docs (Flow A: Mirror or Inverse, Flow B: Life Is Busy, Flow C: Someone Is Always Wrong).

- `kit/` holds the Nika UI rebuilt in HTML from the app screen recording: Strategies, trader detail, Mirror and Inverse sheet, portfolio, notifications, Nika AI chat. Handles are fictional and all numbers are placeholders.
- Flows A and B cut free Mixkit stock footage under the app overlays to show pace and story. The final film replaces them with shot or generated footage of the actual characters.
- Flow C is pure motion design and close to the final look. `flow-c2/` is the Group Chat version of Flow C, built entirely in code with Mixkit sound effects.

Rebuild:

```bash
bash examples/nika-animatics/fetch-assets.sh
```

```bash
cd examples/nika-animatics/flow-a && npx hyperframes render --output flow-a.mp4
```

Footage and music come from [Mixkit](https://mixkit.co) under the Mixkit License (free for commercial and personal use). Clip IDs and trims are listed in `fetch-assets.sh`.
