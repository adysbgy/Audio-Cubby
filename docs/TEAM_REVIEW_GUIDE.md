# Team Review Guide - Cubby Audio

**Date**: 2026-07-09  
**Goal**: Manual listening audit to mark assets as `accepted` or `rejected`

---

## Listening Criteria

All assets must pass **ALL** criteria to be marked `accepted`:

- ✅ **Soft**: No clipping, no harsh transients
- ✅ **Warm/Calm/Gentle**: Not aggressive, not intense
- ✅ **Child-friendly**: No scary, no disturbing elements
- ✅ **Non-scary**: No horror elements
- ✅ **Non-aggressive**: No loud strikes or angry sounds
- ✅ **Not arcade-like**: No 8-bit, no synth-heavy, no gamey
- ✅ **Not wrong-answer buzzer**: Choice feedback should not feel punitive
- ✅ **No voice/crowd/realistic crying**: Emotions should be musical, not vocal
- ✅ **No cartoon slapstick**: No exaggerated comedy sounds

---

## Priority Review Order

### Priority 1 - Critical
- Storybook assets (6): book/page feel critical
- Emotion cues (8): avoid UI/error context
- Sandbox ambience (2): sand texture only

### Priority 2 - Important
- BGM (3): warm/gentle feel for children
- UI/Dialogue (8): soft interaction cues
- Choice system (5): non-punitive feedback

### Priority 3 - Gameplay
- Footsteps (2): natural texture
- Gameplay interaction (6): subtle feedback

---

## Decision Format

For each asset, provide:

```
[Asset name]:
  - Playable: YES/NO
  - Volume: OK/LOUD/QUIET
  - Mood fit: YES/NO
  - Child-safe: YES/NO
  - Notes: [detailed observation]
  - Decision: ACCEPTED / REJECTED / NEEDS_REPLACE
```

---

## How to Mark

1. Listen to each asset in `raw/`
2. Check against criteria above
3. If ALL pass → `ACCEPTED`
4. If ANY fail → `REJECTED`
5. If rejected but want alternative → `NEEDS_REPLACE`

Update `audio_manifest.json`:
```json
{
  "asset_name": "...",
  "candidate_files": [
    {
      "status": "accepted"  // or "rejected", "needs_replace"
    }
  ]
}
```

---

## Notes

- Status starts as `needs_review` for all 34 assets
- After manual listening, move to `accepted` or `rejected`
- `rejected` assets can be replaced if `needs_replace` is chosen
- Only `accepted` assets should be integrated into Cubby game

---

## Quick Reference: Replaced SFX (Check these first)

| Asset | Key Check |
|---|---|
| Storybook (6) | Real book/page feel, not cloth/door |
| Emotion (8) | Musical, not UI/error/buzzer |
| Sandbox (2) | Sand texture, no water splash |
| Choice (5) | Soft, not arcade or punishing |
| UI (8) | Subtle, not loud or gamey |
