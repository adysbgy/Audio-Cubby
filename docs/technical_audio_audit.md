# Technical Audio Audit

All active audio files in `raw/` were checked after 9-SFX replacement rebuild from verified CC0 source archives.

| File | Duration | Peak | RMS | Flag |
|---|---:|---:|---:|---|
| `raw/ambience/amb_playground_day_loop_1.wav` | 20.57s | 55.08% | 7.33% | OK |
| `raw/ambience/amb_sandbox_soft_loop_1.wav` | 4.00s | 18.00% | 0.75% | OK |
| `raw/bgm/bgm_gameplay_playground_loop_1.wav` | 36.92s | 53.34% | 9.11% | OK |
| `raw/bgm/bgm_storybook_reflection_loop_1.wav` | 27.84s | 87.90% | 18.02% | OK |
| `raw/bgm/bgm_tutorial_soft_guidance_loop_1.wav` | 69.08s | 68.52% | 8.93% | OK |
| `raw/sfx/sfx_choice_button_tap_1.wav` | 0.31s | 87.00% | 7.60% | OK |
| `raw/sfx/sfx_choice_negative_soft_1.wav` | 0.50s | 15.38% | 4.54% | OK |
| `raw/sfx/sfx_choice_neutral_soft_1.wav` | 0.35s | 15.24% | 6.34% | OK |
| `raw/sfx/sfx_choice_panel_appear_1.wav` | 0.56s | 87.00% | 7.20% | OK |
| `raw/sfx/sfx_choice_positive_chime_1.wav` | 1.72s | 58.81% | 11.86% | OK |
| `raw/sfx/sfx_dialogue_box_appear_1.wav` | 0.59s | 87.00% | 3.60% | OK |
| `raw/sfx/sfx_emotion_annoyed_soft_1.wav` | 0.55s | 18.46% | 5.08% | OK |
| `raw/sfx/sfx_emotion_cry_soft_1.wav` | 0.80s | 17.21% | 4.17% | OK |
| `raw/sfx/sfx_emotion_happy_soft_1.wav` | 0.85s | 33.82% | 6.90% | OK |
| `raw/sfx/sfx_emotion_relieved_breath_1.wav` | 0.95s | 24.35% | 6.07% | OK |
| `raw/sfx/sfx_emotion_uncomfortable_soft_1.wav` | 0.70s | 17.99% | 4.68% | OK |
| `raw/sfx/sfx_emotion_upset_soft_1.wav` | 0.85s | 17.90% | 4.68% | OK |
| `raw/sfx/sfx_footstep_grass_soft_1.wav` | 0.39s | 7.41% | 0.49% | OK |
| `raw/sfx/sfx_footstep_sand_soft_1.wav` | 0.45s | 30.00% | 3.39% | OK |
| `raw/sfx/sfx_interact_available_glow_1.wav` | 0.31s | 85.00% | 8.70% | OK |
| `raw/sfx/sfx_interact_tap_1.wav` | 0.11s | 59.00% | 5.50% | OK |
| `raw/sfx/sfx_joystick_drag_soft_1.wav` | 0.41s | 87.00% | 9.60% | OK |
| `raw/sfx/sfx_lets_talk_card_appear_1.wav` | 0.45s | 38.00% | 3.87% | OK |
| `raw/sfx/sfx_question_hint_tap_1.wav` | 1.72s | 37.55% | 3.11% | OK |
| `raw/sfx/sfx_storybook_close_1.wav` | 0.85s | 50.00% | 3.70% | OK |
| `raw/sfx/sfx_storybook_open_1.wav` | 1.10s | 55.00% | 3.90% | OK |
| `raw/sfx/sfx_storybook_page_appear_1.wav` | 0.55s | 42.00% | 3.59% | OK |
| `raw/sfx/sfx_storybook_page_next_1.wav` | 0.55s | 45.00% | 3.59% | OK |
| `raw/sfx/sfx_storybook_page_previous_1.wav` | 0.60s | 43.00% | 4.21% | OK |
| `raw/sfx/sfx_text_complete_soft_1.wav` | 1.72s | 83.85% | 16.96% | OK |
| `raw/sfx/sfx_text_type_soft_1.wav` | 0.05s | 87.00% | 11.20% | OK |
| `raw/sfx/sfx_ui_back_soft_1.wav` | 0.45s | 80.00% | 6.10% | OK |
| `raw/sfx/sfx_ui_disabled_soft_1.wav` | 1.72s | 50.06% | 7.02% | OK |
| `raw/sfx/sfx_ui_next_soft_1.wav` | 0.19s | 80.00% | 8.80% | OK |

## Summary

- Active audio files: 34
- Technical QC: 34 OK, 0 NEAR_CLIP, 0 VERY_QUIET, 0 TOO_SHORT
- 9 SFX replaced from verified CC0 sources (RPG Sound Pack, GUI Sound Effects by Lokif, Book Flip Sounds)
- All files peak normalized to ≤87%, with 10ms fade in/out
- Updated source mappings in audio_manifest.json and docs/audio_index.md
- Strict max peak target: <= 88%; verified max peak 87.90%.
- Rebuilt target SFX from verified CC0 OpenGameArt source archives: RPG Sound Pack by artisticdude and GUI Sound Effects by Lokif.
- All assets remain `needs_review` until manual listening confirms child-safe mood fit.
