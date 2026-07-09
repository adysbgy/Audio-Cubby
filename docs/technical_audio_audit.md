# Technical Audio Audit

All active audio files in `raw/` were checked after contextual rebuild and strict peak normalization.

| File | Duration | Peak | RMS | Flag |
|---|---:|---:|---:|---|
| `raw/ambience/amb_playground_day_loop_1.wav` | 20.57s | 55.08% | 7.33% | OK |
| `raw/ambience/amb_sandbox_soft_loop_1.wav` | 4.00s | 18.00% | 0.75% | OK |
| `raw/bgm/bgm_gameplay_playground_loop_1.wav` | 36.92s | 53.34% | 9.11% | OK |
| `raw/bgm/bgm_storybook_reflection_loop_1.wav` | 27.84s | 87.90% | 18.02% | OK |
| `raw/bgm/bgm_tutorial_soft_guidance_loop_1.wav` | 69.08s | 68.52% | 8.93% | OK |
| `raw/sfx/sfx_choice_button_tap_1.wav` | 0.19s | 87.90% | 9.67% | OK |
| `raw/sfx/sfx_choice_negative_soft_1.wav` | 0.50s | 15.38% | 4.54% | OK |
| `raw/sfx/sfx_choice_neutral_soft_1.wav` | 0.35s | 15.24% | 6.34% | OK |
| `raw/sfx/sfx_choice_panel_appear_1.wav` | 0.46s | 87.90% | 8.38% | OK |
| `raw/sfx/sfx_choice_positive_chime_1.wav` | 1.72s | 58.81% | 11.86% | OK |
| `raw/sfx/sfx_dialogue_box_appear_1.wav` | 0.46s | 87.90% | 8.38% | OK |
| `raw/sfx/sfx_emotion_annoyed_soft_1.wav` | 0.55s | 18.46% | 5.08% | OK |
| `raw/sfx/sfx_emotion_cry_soft_1.wav` | 0.80s | 17.21% | 4.17% | OK |
| `raw/sfx/sfx_emotion_happy_soft_1.wav` | 0.85s | 33.82% | 6.90% | OK |
| `raw/sfx/sfx_emotion_relieved_breath_1.wav` | 0.95s | 24.35% | 6.07% | OK |
| `raw/sfx/sfx_emotion_uncomfortable_soft_1.wav` | 0.70s | 16.65% | 4.49% | OK |
| `raw/sfx/sfx_emotion_upset_soft_1.wav` | 0.85s | 14.76% | 4.64% | OK |
| `raw/sfx/sfx_footstep_grass_soft_1.wav` | 0.39s | 7.43% | 0.49% | OK |
| `raw/sfx/sfx_footstep_sand_soft_1.wav` | 0.45s | 28.57% | 5.34% | OK |
| `raw/sfx/sfx_interact_available_glow_1.wav` | 0.88s | 87.90% | 14.67% | OK |
| `raw/sfx/sfx_interact_tap_1.wav` | 1.72s | 87.90% | 5.58% | OK |
| `raw/sfx/sfx_joystick_drag_soft_1.wav` | 0.41s | 87.90% | 9.72% | OK |
| `raw/sfx/sfx_lets_talk_card_appear_1.wav` | 0.45s | 35.07% | 4.04% | OK |
| `raw/sfx/sfx_question_hint_tap_1.wav` | 1.72s | 37.59% | 3.11% | OK |
| `raw/sfx/sfx_storybook_close_1.wav` | 0.85s | 46.18% | 6.95% | OK |
| `raw/sfx/sfx_storybook_open_1.wav` | 1.10s | 48.46% | 8.93% | OK |
| `raw/sfx/sfx_storybook_page_appear_1.wav` | 0.55s | 40.45% | 3.98% | OK |
| `raw/sfx/sfx_storybook_page_next_1.wav` | 0.55s | 41.40% | 5.37% | OK |
| `raw/sfx/sfx_storybook_page_previous_1.wav` | 0.60s | 40.46% | 5.08% | OK |
| `raw/sfx/sfx_text_complete_soft_1.wav` | 1.72s | 58.81% | 11.86% | OK |
| `raw/sfx/sfx_text_type_soft_1.wav` | 0.06s | 7.86% | 1.04% | OK |
| `raw/sfx/sfx_ui_back_soft_1.wav` | 0.45s | 87.90% | 6.74% | OK |
| `raw/sfx/sfx_ui_disabled_soft_1.wav` | 1.72s | 50.14% | 7.03% | OK |
| `raw/sfx/sfx_ui_next_soft_1.wav` | 0.19s | 87.90% | 9.67% | OK |

## Summary

- Active audio files: 34
- Technical QC: 34 OK, 0 NEAR_CLIP, 0 VERY_QUIET, 0 TOO_SHORT
- Strict max peak: <= 88% target, verified max peak 87.90%.
- Contextual rebuild fixed storybook, emotion, sand/sandbox wrong-context mappings.
- All assets remain `needs_review` until manual listening confirms child-safe mood fit.
