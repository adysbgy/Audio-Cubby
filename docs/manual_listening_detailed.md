# Manual Listening Audit - Detailed Checklist

**Date**: 2026-07-08  
**Status**: accepted 0, needs_review 34, missing 0

---

## PRIORITY 1 - Critical Semantic Fixes

### Storybook Assets (REAL BOOK/PAGE SOURCE VERIFIED)
| Asset | Duration | Peak | RMS | Fit | Notes |
|---|---|---:|---:|---:|---|
| sfx_storybook_open | 1.10s | 55.0% | 3.90% | ⬜/⬛ | Real book flip open; cek book-open feel |
| sfx_storybook_page_appear | 0.55s | 42.0% | 3.59% | ⬜/⬛ | Real page flip; cek page-appear feel |
| sfx_storybook_page_next | 0.55s | 45.0% | 3.59% | ⬜/⬛ | Real page flip; cek next-page feel |
| sfx_storybook_page_previous | 0.60s | 43.0% | 4.21% | ⬜/⬛ | Real page flip; cek previous-page feel |
| sfx_storybook_close | 0.85s | 50.0% | 3.70% | ⬜/⬛ | Real book close; cek close feel (bukan door) |
| sfx_lets_talk_card_appear | 0.45s | 38.0% | 3.87% | ⬜/⬛ | Real page flip as card; cek paper/card feel |

**Storybook Checklist**:
- [ ] Terdengar seperti buku/buku hal, bukan cloth/door
- [ ] Tidak harsh/clipping
- [ ] Durasi pas untuk action
- [ ] Soft/gentle, bukan loud

### Emotion + Soft Negative/Neutral (LOCAL PROCEDURAL)
| Asset | Duration | Peak | RMS | Fit | Notes |
|---|---|---:|---:|---:|---|
| sfx_emotion_happy_soft | 0.85s | 33.8% | 6.90% | ⬜/⬛ | Procedural happy tone; cek sparkle/chime, bukan UI/menu |
| sfx_emotion_relieved_breath | 0.95s | 24.3% | 6.07% | ⬜/⬛ | Procedural relief tone; cek descending, bukan UI/error |
| sfx_emotion_uncomfortable_soft | 0.70s | 18.0% | 4.68% | ⬜/⬛ | Procedural low-tension; cek subtle, bukan scary |
| sfx_emotion_annoyed_soft | 0.55s | 18.5% | 5.08% | ⬜/⬛ | Procedural muted; cek annoyance, bukan cartoon/anger |
| sfx_emotion_cry_soft | 0.80s | 17.2% | 4.17% | ⬜/⬛ | Procedural sad tone; cek gentle, bukan crying/voice |
| sfx_emotion_upset_soft | 0.85s | 17.9% | 4.68% | ⬜/⬛ | Procedural upset tone; cek low tension, bukan horror |
| sfx_choice_neutral_soft | 0.35s | 15.2% | 6.34% | ⬜/⬛ | Procedural neutral; cek muted, bukan UI/error |
| sfx_choice_negative_soft | 0.50s | 15.4% | 4.54% | ⬜/⬛ | Procedural negative; cek soft, bukan wrong-answer buzzer |

**Emotion Checklist**:
- [ ] Terdengar seperti emosi, bukan UI/generic error
- [ ] Soft/sparkle/chime, bukan loud/aggressive
- [ ] Tidak ada voice/crowd/crying
- [ ] Tidak arcade-like
- [ ] Child-friendly, non-scary

### Sand/Texture Assets
| Asset | Duration | Peak | RMS | Fit | Notes |
|---|---|---:|---:|---:|---|
| sfx_footstep_sand_soft | 0.45s | 30.0% | 3.39% | ⬜/⬛ | Source: Peludo sand footsteps; cek sand, bukan mud |
| amb_sandbox_soft_loop | 4.00s | 18.0% | 0.75% | ⬜/⬛ | Source: Peludo sand + highpass; cek texture ambience, bukan footstep loop |

**Sand Checklist**:
- [ ] Terdengar seperti sand, bukan mud/gravel
- [ ] Loop seamless tanpa click/pops
- [ ] Tidak ada water splash audible

---

## PRIORITY 2 - Mood Fit

### BGM (Check child-safe warm/gentle)
| Asset | Duration | Peak | RMS | Fit | Notes |
|---|---|---:|---:|---:|---|
| bgm_gameplay_playground_loop | 36.92s | 53.3% | 9.11% | ⬜/⬛ | Children's Game Music 1; cek warm/playful, bukan busy |
| bgm_storybook_reflection_loop | 27.84s | 54.6% | 10.20% | ⬜/⬛ | Emotional piano; **WASPADA SAD/SCARY**; cek gentle enough |
| bgm_tutorial_soft_guidance_loop | 69.08s | 68.5% | 8.93% | ⬜/⬛ | Children's Game Music 2 Adventure; cek tidak over-adventurous |

### UI/Interaction Assets
| Asset | Duration | Peak | RMS | Fit | Notes |
|---|---|---:|---:|---:|---|
| sfx_ui_next_soft | 0.19s | 87.9% | 9.67% | ⬜/⬛ | interface1; cek soft, bukan arcade |
| sfx_ui_back_soft | 0.45s | 87.9% | 6.74% | ⬜/⬛ | interface2; cek soft, bukan arcade |
| sfx_ui_disabled_soft | 1.72s | 50.1% | 7.02% | ⬜/⬛ | negative_2; cek muted, bukan error buzzer |
| sfx_dialogue_box_appear | 0.46s | 87.9% | 8.38% | ⬜/⬛ | cloth.wav; cek paper/card feel |
| sfx_text_type_soft | 0.06s | 7.8% | 1.04% | ⬜/⬛ | click.wav 0.06s; cek terlalu pelan di loop typing |
| sfx_text_complete_soft | 1.72s | 83.9% | 16.96% | ⬜/⬛ | positive.wav; cek terlalu arcade UI |

### Choice Assets
| Asset | Duration | Peak | RMS | Fit | Notes |
|---|---|---:|---:|---:|---|
| sfx_choice_button_tap | 0.19s | 87.9% | 9.67% | ⬜/⬛ | interface1; cek soft tap |
| sfx_choice_panel_appear | 0.46s | 87.9% | 8.38% | ⬜/⬛ | cloth.wav; cek soft paper/card pop |
| sfx_choice_positive_chime | 1.72s | 58.8% | 11.86% | ⬜/⬛ | positive.wav; cek warm chime, bukan arcade |

---

## PRIORITY 3 - Gameplay

| Asset | Duration | Peak | RMS | Fit | Notes |
|---|---|---:|---:|---:|---|
| sfx_footstep_grass_soft | 0.39s | 7.4% | 0.49% | ⬜/⬛ | leaves01; cek gentle grass, bukan crunchy |
| sfx_joystick_drag_soft | 0.41s | 87.9% | 9.72% | ⬜/⬛ | cloth-heavy; cek subtle drag |
| sfx_interact_available_glow | 0.88s | 87.9% | 14.69% | ⬜/⬛ | magic1; cek soft glow, bukan intense fantasy |
| sfx_interact_tap | 1.72s | 87.9% | 5.58% | ⬜/⬛ | click_2; cek volume balance |
| sfx_question_hint_tap | 1.72s | 37.6% | 3.11% | ⬜/⬛ | misc_menu; cek tidak UI/generic |

---

## Ambience

| Asset | Duration | Peak | RMS | Fit | Notes |
|---|---|---:|---:|---:|---|
| amb_playground_day_loop | 20.57s | 55.1% | 7.33% | ⬜/⬛ | Sunny Day; cek tidak mengganggu dialogue |

---

## Final Decision

Setelah manual listening, update status di `audio_manifest.json`:

- `needs_review` → `accepted` jika lolos semua kriteria
- `needs_review` → `rejected` jika tidak cocok
- `needs_review` → `needs_replace` jika mau cari alternatif

---

## Listening Notes Format

Untuk tiap asset, gunakan format:

```
[Asset name]:
  - Playable: YES/NO
  - Volume: OK/LOUD/QUIET
  - Mood fit: YES/NO
  - Child-safe: YES/NO
  - Notes: [catatan detail]
  - Final: ACCEPTED / REJECTED / NEEDS_REPLACE
```