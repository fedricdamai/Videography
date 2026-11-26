# Videography

Launch films and product videos, built as code.

- Before planning any video, use `/creative-director`: fill the blueprint first (goal → spine, audience → world, beats → moves), then idea, flow, shots. Never combine styles. Evidence lives in `docs/decision-logic.md`, `docs/launch-video-formula.md`, `docs/creative-thinking.md`, `docs/visual-grammar.md` and `docs/creative-playbook.md`.
- Measure every draft with `tools/flow_report.py` and compare it to the references.
- Use `/hyperframes` for any video work (compose, animate, render). Use `/stageshow` for product UI, phone screens, dashboards and cursor walkthroughs.
- Run `npx hyperframes lint` and `npx hyperframes check` before every render. Watch the exported MP4, not just the preview.
- Renders and source footage stay out of git (see `.gitignore`).
- Never use a real person's likeness without written permission.
