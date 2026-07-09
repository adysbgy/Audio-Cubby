# Contextual Audio Rebuild Audit

**Date**: 2026-07-08

## Reason

Manual review found several SFX mappings were technically valid but semantically wrong:

- Storybook SFX used cloth/door sounds instead of book/page sounds.
- Emotion SFX used UI/interface/negative sounds instead of emotional cues.
- Sand/sandbox used mud step sounds instead of sand texture.

## Rebuild Scope

| Group | Assets rebuilt | New approach |
|---|---:|---|
| Storybook/book/card | 6 | Real CC0 book/page flip recordings |
| Sand/sandbox | 2 | CC0 sand footsteps source |
| Emotion + soft negative/neutral | 8 | Soft non-UI procedural musical cues generated locally |

## Verified Sources

| Source | URL | License | Used for |
|---|---|---|---|
| 10 Book Page Flips by StarNinjas | https://opengameart.org/content/10-book-page-flips | CC0 | storybook page/card sounds |
| Book Flip Sounds by Voltiment555 | https://opengameart.org/content/book-flip-sounds | CC0 | storybook open/close |
| Water Splash and sand footsteps by Peludo | https://opengameart.org/content/water-splash-and-sand-footsteps | CC0 | sand footstep + sandbox texture |
| Local procedural tones | generated in project | original/project-owned | emotion and soft choice feedback |

## Technical QC

- Active WAV files: 34
- Bad technical flags: 0
- Peak clipping: 0
- Strict max peak: <= 88% target, verified max peak 87.90%
- Too-short sandbox loop: 0
- Typing SFX remains short: OK
- Rebuild script preserved at `tools/rebuild_contextual.py` for reproducibility

## Manual Review Still Needed

All assets remain `needs_review`. This rebuild improves semantic fit, but final acceptance still requires listening in game context.
