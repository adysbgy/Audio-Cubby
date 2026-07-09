#!/usr/bin/env python3
import wave
import struct
import os
import subprocess
import tempfile
import shutil

WORKSPACE = "/Users/aj/Downloads/Audio-Cubby-cubby-audio-research"
SOURCE_DIR = os.path.join(WORKSPACE, "source_downloads")
RAW_SFX_DIR = os.path.join(WORKSPACE, "raw", "sfx")

def resample_to_wav16(source_file, out_file=None):
    if out_file is None:
        with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as tmp:
            out_file = tmp.name
    cmd = ['afconvert', '-f', 'WAVE', '-d', 'LEI16@44100', source_file, out_file]
    subprocess.run(cmd, check=True, capture_output=True)
    return out_file

def get_duration(filepath):
    result = subprocess.run(['afinfo', filepath], capture_output=True, text=True)
    for line in result.stdout.split('\n'):
        if 'estimated duration' in line:
            return float(line.split(':')[1].strip().split()[0])
    return 0

def read_wav(filepath):
    with wave.open(filepath, 'rb') as wf:
        frames = wf.readframes(wf.getnframes())
        params = wf.getparams()
        n_channels = wf.getnchannels()
    samples = list(struct.unpack(f'<{len(frames)//2}h', frames))
    return params, samples, n_channels

def write_wav(filepath, params, samples, n_channels):
    frames = struct.pack(f'<{len(samples)}h', *samples)
    with wave.open(filepath, 'wb') as wf:
        wf.setparams(params)
        wf.writeframes(frames)

def normalize_peak(samples, target_peak=0.87):
    if not samples:
        return samples
    max_amp = max(abs(s) for s in samples)
    if max_amp > 0:
        scale = (target_peak * 32767) / max_amp
        samples = [int(s * scale) for s in samples]
    return samples

def fade_in_out(samples, fade_sec=0.01, rate=44100):
    n = len(samples)
    fade_samples = int(fade_sec * rate)
    if n > fade_samples * 2:
        for i in range(fade_samples):
            factor = i / fade_samples
            samples[i] = int(samples[i] * factor)
        for i in range(fade_samples):
            factor = (fade_samples - i) / fade_samples
            samples[-(i+1)] = int(samples[-(i+1)] * factor)
    return samples

def trim_samples(samples, target_sec, n_channels, rate=44100):
    target_n = int(target_sec * rate) * n_channels
    if len(samples) > target_n:
        samples = samples[:target_n]
    return samples

MAPPING = [
    (
        "sfx_interact_available_glow",
        "/Users/aj/Downloads/Audio-Cubby-cubby-audio-research/source_downloads/rpg_sound_pack/extracted/RPG Sound Pack/inventory/coin3.wav",
        os.path.join(RAW_SFX_DIR, "sfx_interact_available_glow_1.wav"),
        None, 0.85
    ),
    (
        "sfx_choice_button_tap",
        "/Users/aj/Downloads/Audio-Cubby-cubby-audio-research/source_downloads/rpg_sound_pack/extracted/RPG Sound Pack/inventory/wood-small.wav",
        os.path.join(RAW_SFX_DIR, "sfx_choice_button_tap_1.wav"),
        None, 0.87
    ),
    (
        "sfx_choice_panel_appear",
        "/Users/aj/Downloads/Audio-Cubby-cubby-audio-research/source_downloads/book_page_flips/voltiment/BookFlip2.wav",
        os.path.join(RAW_SFX_DIR, "sfx_choice_panel_appear_1.wav"),
        None, 0.87
    ),
    (
        "sfx_dialogue_box_appear",
        "/Users/aj/Downloads/Audio-Cubby-cubby-audio-research/source_downloads/book_page_flips/voltiment/BookFlip4.wav",
        os.path.join(RAW_SFX_DIR, "sfx_dialogue_box_appear_1.wav"),
        None, 0.87
    ),
    (
        "sfx_interact_tap",
        "/Users/aj/Downloads/Audio-Cubby-cubby-audio-research/source_downloads/gui_sound_effects_lokif/extracted/GUI_Sound_Effects_by_Lokif/click_2.wav",
        os.path.join(RAW_SFX_DIR, "sfx_interact_tap_1.wav"),
        0.22, 0.87
    ),
    (
        "sfx_joystick_drag_soft",
        "/Users/aj/Downloads/Audio-Cubby-cubby-audio-research/source_downloads/rpg_sound_pack/extracted/RPG Sound Pack/inventory/cloth-heavy.wav",
        os.path.join(RAW_SFX_DIR, "sfx_joystick_drag_soft_1.wav"),
        None, 0.87
    ),
    (
        "sfx_ui_next_soft",
        "/Users/aj/Downloads/Audio-Cubby-cubby-audio-research/source_downloads/rpg_sound_pack/extracted/RPG Sound Pack/interface/interface1.wav",
        os.path.join(RAW_SFX_DIR, "sfx_ui_next_soft_1.wav"),
        None, 0.80
    ),
    (
        "sfx_ui_back_soft",
        "/Users/aj/Downloads/Audio-Cubby-cubby-audio-research/source_downloads/rpg_sound_pack/extracted/RPG Sound Pack/interface/interface2.wav",
        os.path.join(RAW_SFX_DIR, "sfx_ui_back_soft_1.wav"),
        None, 0.80
    ),
    (
        "sfx_text_type_soft",
        "/Users/aj/Downloads/Audio-Cubby-cubby-audio-research/source_downloads/rpg_sound_pack/extracted/RPG Sound Pack/inventory/wood-small.wav",
        os.path.join(RAW_SFX_DIR, "sfx_text_type_soft_1.wav"),
        0.05, 0.87
    ),
]

print("=" * 60)
print("PROCESSING 9 SFX FILES")
print("=" * 60)

for asset_name, source, target, trim_sec, target_peak in MAPPING:
    print(f"\nProcessing: {asset_name}")
    print(f"  Source: {os.path.basename(source)}")
    
    tmp_wav = resample_to_wav16(source)
    params, samples, n_channels = read_wav(tmp_wav)
    
    samples = normalize_peak(samples, target_peak)
    samples = fade_in_out(samples, fade_sec=0.01)
    
    if trim_sec:
        samples = trim_samples(samples, trim_sec, n_channels)
        print(f"  Trimmed to {trim_sec}s")
    
    write_wav(target, params, samples, n_channels)
    os.remove(tmp_wav)
    
    final_dur = get_duration(target)
    print(f"  Final duration: {final_dur:.3f}s")
    print(f"  Target: {target}")

print("\n" + "=" * 60)
print("PROCESSING COMPLETE")
print("=" * 60)
