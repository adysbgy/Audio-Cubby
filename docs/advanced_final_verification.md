# Advanced Final Verification

**Date**: 2026-07-08
**Project**: Cubby Audio Rebuild
**Build**: v2_advanced_final

## Result

Advanced processing is complete and final verification passed.

| Check | Result |
|---|---:|
| WAV files checked | 34 |
| Technical failures | 0 |
| Peak failures | 0 |
| Too-short ambience loops | 0 |
| Missing files | 0 |

## Processing Applied

- Installed Python audio tooling: `numpy`, `scipy`, `soundfile`, `pyloudnorm`.
- Applied LUFS normalization using EBU R128-style measurement.
- Targets:
  - BGM: `-18 LUFS`
  - Ambience: `-24 LUFS`
  - SFX: `-15 LUFS` where measurable
- Applied peak limiting at approximately `-1 dB` ceiling.
- Applied 10ms fade in/out.
- Applied 2500Hz lowpass to `raw/sfx/sfx_emotion_upset_soft_1.wav`.
- Rebuilt `raw/ambience/amb_sandbox_soft_loop_1.wav` as a 4.00s loop.
- Preserved CC0/Public Domain source policy.

## Notes

- Very short SFX may not produce meaningful integrated LUFS values; they were verified by peak/duration instead.
- No Pixabay or freesound_community sources used.
- All assets remain `needs_review` until manual listening approval.

## Next Required Step

Manual listening audit for child-safe mood, softness, loop seams, and in-game balance.
