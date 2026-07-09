#!/usr/bin/env python3
import os
import numpy as np
import soundfile as sf
from scipy.signal import butter, filtfilt

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
SR = 44100


def read(path):
    data, sr = sf.read(os.path.join(ROOT, path), always_2d=True)
    if sr != SR:
        raise ValueError(f'{path}: expected {SR}, got {sr}')
    return data


def peak_limit(data, peak=0.65):
    m = np.max(np.abs(data)) if data.size else 0
    if m > 0:
        data = data * (peak / m)
    return data


def fade(data, ms=12):
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


def highpass(data, hz=120):
    b, a = butter(2, hz / (SR / 2), btype='high')
    return filtfilt(b, a, data, axis=0)


def write(rel, data, peak=0.65, lp=None):
    data = np.asarray(data, dtype=np.float32)
    if lp:
        data = lowpass(data, lp)
    data = fade(peak_limit(data, peak))
    sf.write(os.path.join(ROOT, rel), data, SR, subtype='PCM_16')


def env_tone(freqs, dur, amp=0.25, decay=3.0):
    t = np.linspace(0, dur, int(SR * dur), endpoint=False)
    y = sum(np.sin(2 * np.pi * f * t) for f in freqs) / len(freqs)
    e = np.exp(-decay * t)
    y = (y * e * amp).astype(np.float32)
    return np.column_stack([y, y])


def main():
    book_base = 'source_downloads/book_page_flips/starninjas'
    volt = 'source_downloads/book_page_flips/voltiment'

    write('raw/sfx/sfx_storybook_open_1.wav', read(f'{volt}/BookFlip3.wav')[:int(1.10 * SR)], peak=0.55, lp=5200)
    write('raw/sfx/sfx_storybook_page_appear_1.wav', read(f'{book_base}/book_flip.4.ogg')[:int(0.55 * SR)], peak=0.42, lp=5500)
    write('raw/sfx/sfx_storybook_page_next_1.wav', read(f'{book_base}/book_flip.8.ogg')[:int(0.55 * SR)], peak=0.45, lp=5500)
    write('raw/sfx/sfx_storybook_page_previous_1.wav', read(f'{book_base}/book_flip.6.ogg')[:int(0.60 * SR)], peak=0.43, lp=5200)
    write('raw/sfx/sfx_storybook_close_1.wav', read(f'{volt}/BookFlip13.wav')[:int(0.85 * SR)], peak=0.50, lp=4800)
    write('raw/sfx/sfx_lets_talk_card_appear_1.wav', read(f'{book_base}/book_flip.1.ogg')[:int(0.45 * SR)], peak=0.38, lp=6000)

    sand = read('source_downloads/sand_footsteps/sand_footsteps_peludo.wav')
    write('raw/sfx/sfx_footstep_sand_soft_1.wav', sand[int(0.35 * SR):int(0.80 * SR)], peak=0.30, lp=4200)
    amb = np.concatenate([sand, sand[::-1], sand, sand[::-1]], axis=0)[:int(4.0 * SR)]
    write('raw/ambience/amb_sandbox_soft_loop_1.wav', highpass(amb, 90), peak=0.18, lp=3600)

    write('raw/sfx/sfx_emotion_happy_soft_1.wav', env_tone([523.25, 659.25, 783.99], 0.85, 0.23, 2.7), peak=0.36, lp=4200)
    write('raw/sfx/sfx_emotion_relieved_breath_1.wav', env_tone([392.00, 493.88], 0.95, 0.16, 2.2), peak=0.25, lp=2600)
    write('raw/sfx/sfx_emotion_uncomfortable_soft_1.wav', env_tone([220.00, 246.94], 0.70, 0.13, 3.0), peak=0.20, lp=2200)
    write('raw/sfx/sfx_emotion_annoyed_soft_1.wav', env_tone([196.00, 207.65], 0.55, 0.14, 3.8), peak=0.22, lp=1800)
    write('raw/sfx/sfx_emotion_cry_soft_1.wav', env_tone([261.63, 311.13], 0.80, 0.12, 2.8), peak=0.18, lp=2000)
    write('raw/sfx/sfx_emotion_upset_soft_1.wav', env_tone([174.61, 196.00], 0.85, 0.13, 2.5), peak=0.20, lp=1600)
    write('raw/sfx/sfx_choice_negative_soft_1.wav', env_tone([196.00, 174.61], 0.50, 0.11, 3.5), peak=0.18, lp=1700)
    write('raw/sfx/sfx_choice_neutral_soft_1.wav', env_tone([329.63], 0.35, 0.10, 4.0), peak=0.16, lp=2500)


if __name__ == '__main__':
    main()
