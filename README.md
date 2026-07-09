# Audio Cubby - Team Delivery

**Latest commit**: 2026-07-09  
**Status**: 34 audio files, all `needs_review`

---

## Overview

This repository contains copyright-safe audio research for the **Cubby** game. All assets are either CC0, Public Domain, or Project-owned.

---

## Quick Start

1. **Play audio**: Open `audio_player.html` in your browser
2. **Review**: Follow guide in `docs/TEAM_REVIEW_GUIDE.md`
3. **Status**: See full table in `docs/AUDIO_VISUALIZATION.md`
4. **Sources**: See CC0 sources in `docs/SOURCE_LIST.md`

---

## Current Status

| Type | Count |
|---|---:|
| BGM | 3 |
| Ambience | 2 |
| SFX | 29 |
| **Total** | **34** |

**Manual listening required**: All assets remain `needs_review`

---

## Folder Structure

```
raw/
  bgm/        3 background music files
  ambience/   2 ambient sound files
  sfx/        29 sound effect files
docs/
  AUDIO_VISUALIZATION.md   Full audio table with technical specs
  TEAM_REVIEW_GUIDE.md     Manual listening checklist
  SOURCE_LIST.md           CC0 source credits and policies
audio_manifest.json        Full metadata (JSON)
audio_player.html          HTML audio player for review
```

---

## Audio Specifications

- **Format**: 44.1kHz, 16-bit PCM WAV
- **Peak normalized**: Max 87%
- **Fades**: 10ms in/out
- **No clipping**: Verified max peak 87.90%

---

## Next Steps

1. Open `audio_player.html` to listen to all files
2. Follow `docs/TEAM_REVIEW_GUIDE.md` for checklist
3. Update `audio_manifest.json` status per asset
4. When all `accepted`, integrate into Cubby game

---

## Source Policy

✅ **Allowed**: CC0, Public Domain. 8 procedural emotion/choice cues are CC0 derivatives of Lokif `positive.wav`.  
❌ **Prohibited**: Pixabay, Freesound, voice/crowd recordings

See `docs/SOURCE_LIST.md` for full source credits.

---

## Recent Updates

**2026-07-09**:
- Replaced 9 SFX from verified CC0 sources
- All audio files peak normalized, no clipping
- Added HTML audio player for team review
- Documented 8 emotion/choice cues as CC0 derivatives of Lokif positive.wav (raw files unchanged)
