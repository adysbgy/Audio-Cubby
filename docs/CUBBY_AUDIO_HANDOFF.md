# Cubby Audio Research - Updated Handoff Context

## Repo Status
```text
Working directory: /Users/aj/Downloads/Audio-Cubby-cubby-audio-research
Remote: https://github.com/adysbgy/Audio-Cubby.git
Branch: cubby-audio-research
Latest commit: b0699ed
```

## Asset Status
| Status | Count |
|---|---|
| accepted | 0 |
| needs_review | 34 |
| missing | 0 |

## Completed Work
- ✅ Contextual rebuild applied to storybook, emotion, sand/sandbox
- ✅ Technical QC: 34 OK, 0 bad flags, max peak 87.9%
- ✅ Source policy cleaned (Pixabay removed)
- ✅ Reproducible script saved at `tools/rebuild_contextual.py`
- ✅ Detailed listening checklist at `docs/manual_listening_detailed.md`

## Current Sources

| Group | Source | License | Notes |
|---|---|---|---|
| Storybook | 10 Book Page Flips + Book Flip Sounds | CC0 | Real book/page sounds |
| Sandbox | Water Splash and sand footsteps by Peludo | CC0 | Sand texture, highpass loop |
| Emotion/Negative/Neutral | Local procedural soft musical cues | Project-owned | Non-UI, gentle tones |
| BGM | Children's Game Music (heartade) + Emotional piano | CC0 | Storybook BGM softened |
| UI/Dialogue | GUI Sound Effects (Lokif) + RPG Sound Pack (artisticdude) | CC0 | Interface sounds |
| Grass footstep | Different Steps (TinyWorlds) | CC0 | Leaves step for grass |

## Manual Listening Requirements

**Priority 1**: Storybook (6), Emotion/Negative/Neutral (8), Sandbox ambiance (2)  
**Priority 2**: BGM (3), UI/Dialogue/Choice (remaining)  
**Priority 3**: Gameplay interaction (6)

All assets must be:
- soft
- warm/calm/gentle
- child-friendly
- non-scary
- non-aggressive
- NOT arcade-like
- NOT wrong-answer buzzer
- NOT voice/crowd wrong context
- NOT intense crying
- NOT cartoon slapstick

## Next Steps
1. Manual listening audit pakai `docs/manual_listening_detailed.md`
2. Update status di `audio_manifest.json` ke `accepted`/`rejected`
3. Jika ada yang rejected, cari replacement CC0/non-login
4. Final docs cleanup (remove redundant, update handoff)
5. Integration copy ke project Cubby game

## Files Structure
```
raw/
  ambience/  (amb_playground_day_loop, amb_sandbox_soft_loop)
  bgm/       (3 BGM files)
  sfx/       (29 SFX files)
backup/
  raw/       (original audio archives)
docs/
  manual_listening_detailed.md  (detailed checklist)
  technical_audio_audit.md     (QC metrics)
  contextual_rebuild_audit.md  (rebuild summary)
tools/
  rebuild_contextual.py       (reproducible script)
```