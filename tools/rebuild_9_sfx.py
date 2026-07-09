#!/usr/bin/env python3
import os
import numpy as np
import soundfile as sf
from scipy.signal import butter, filtfilt

ROOT = os.path.abspath(os.path.dirname(__file__) + '/..')
SR = 44100

def read(path):
    data, sr = sf.read(path, always_2d=True)
    if sr != SR:
        data = resample_to_44100(data, sr)
    return data

def resample_to_44100(data, orig_sr):
    from scipy.signal import resample
    new_len = int(len(data) * SR / orig_sr)
    return resample(data, new_len)

def peak_limit(data, peak=0.65):
    m = np.max(np.abs(data)) if data.size else 0
    if m > 0:
        data = data * (peak / m)
    return data

def fade(data, ms=10):
    n = min(int(SR * ms / 1000), len(data) // 2)
    if n > 0:
        fi = np.linspace(0, 1, n)[:, None]
        fo = np.linspace(1, 0, n)[:, None]
        data[:n] *= fi
        data[-n:] *= fo
    return data

def lowpass(data, hz=3500):
    b, a = butter(3, hz / (SR / 2), btype='low')
    return filtfilt(b, a, data, axis=0)

def write(rel, data, peak=0.65, lp=None, trim_ms=None):
    data = np.asarray(data, dtype=np.float32)
    if trim_ms:
        n = int(SR * trim_ms / 1000)
        data = data[:n]
    if lp:
        data = lowpass(data, lp)
    data = fade(peak_limit(data, peak))
    sf.write(os.path.join(ROOT, rel), data, SR, subtype='PCM_16')

# Source paths
rpg = os.path.join(ROOT, 'source_downloads/rpg_sound_pack/extracted/RPG Sound Pack')
lokif = os.path.join(ROOT, 'source_downloads/gui_sound_effects_lokif/extracted/GUI_Sound_Effects_by_Lokif')

# Rebuild 9 SFX with child-safe soft targets
# 1. sfx_interact_available_glow - magic1.wav, soft gentle glow
write('raw/sfx/sfx_interact_available_glow_1.wav', read(f'{rpg}/battle/magic1.wav'), peak=0.55, lp=6200)

# 2. sfx_choice_button_tap - interface1.wav, clean soft tap  
write('raw/sfx/sfx_choice_button_tap_1.wav', read(f'{rpg}/interface/interface1.wav'), peak=0.58, lp=6500)

# 3. sfx_choice_panel_appear - cloth.wav, soft card/paper pop
write('raw/sfx/sfx_choice_panel_appear_1.wav', read(f'{rpg}/inventory/cloth.wav'), peak=0.42, lp=5200)

# 4. sfx_dialogue_box_appear - cloth.wav, soft paper appear
write('raw/sfx/sfx_dialogue_box_appear_1.wav', read(f'{rpg}/inventory/cloth.wav'), peak=0.42, lp=5200)

# 5. sfx_interact_tap - click_2.wav, short soft tap
write('raw/sfx/sfx_interact_tap_1.wav', read(f'{lokif}/click_2.wav'), peak=0.35, lp=5800, trim_ms=220)

# 6. sfx_joystick_drag_soft - cloth-heavy.wav, very subtle
write('raw/sfx/sfx_joystick_drag_soft_1.wav', read(f'{rpg}/inventory/cloth-heavy.wav'), peak=0.35, lp=4200)

# 7. sfx_ui_next_soft - interface1.wav, short clean
write('raw/sfx/sfx_ui_next_soft_1.wav', read(f'{rpg}/interface/interface1.wav'), peak=0.58, lp=6500)

# 8. sfx_ui_back_soft - interface2.wav, soft back
write('raw/sfx/sfx_ui_back_soft_1.wav', read(f'{rpg}/interface/interface2.wav'), peak=0.42, lp=5200)

# 9. sfx_text_type_soft - click.wav, very short 0.06s
write('raw/sfx/sfx_text_type_soft_1.wav', read(f'{lokif}/click.wav'), peak=0.08, trim_ms=60)