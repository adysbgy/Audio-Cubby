# Manual Listening Audit

Gunakan file ini untuk audit suara manual. Jangan ubah status menjadi `accepted` kecuali semua kriteria lolos.

## Status Saat Ini

| Status | Jumlah |
|---|---:|
| accepted | 0 |
| needs_review | 34 |
| missing | 0 |

## Kriteria Wajib

Setiap kandidat harus:

- soft
- warm/calm/gentle
- child-friendly
- non-scary
- non-aggressive
- bukan arcade-like
- bukan wrong-answer buzzer
- bukan crowd/voice salah konteks
- bukan intense crying
- bukan cartoon slapstick

## Checklist Umum per Asset

Untuk setiap asset:

- [ ] File bisa diputar
- [ ] Volume nyaman, tidak clipping/menusuk
- [ ] Tidak terlalu pelan di konteks game
- [ ] Mood sesuai fungsi asset
- [ ] Aman untuk anak
- [ ] Tidak terdengar seperti UI arcade/generic jika asset emosi
- [ ] Tidak ada voice/crowd salah konteks
- [ ] Tidak ada realistic crying/moan/slapstick

## Fokus Khusus

### Non-storybook SFX Original

File original Cubby cues ada di `raw/sfx/` dan `raw/ambience/amb_sandbox_soft_loop_1.wav`.

- [ ] UI cues terasa lembut dan tidak arcade
- [ ] Choice negative tidak terasa wrong-answer buzzer
- [ ] Emotion cues terasa seperti emosi yang dimaksud, bukan UI generic
- [ ] Footsteps terasa grass/sand, bukan noise acak
- [ ] Sandbox ambience terasa texture ambience, bukan loop footstep mengganggu

### Storybook SFX

Storybook SFX tetap dari Kenney RPG Audio:

- [ ] `sfx_storybook_open`
- [ ] `sfx_storybook_page_appear`
- [ ] `sfx_storybook_page_next`
- [ ] `sfx_storybook_page_previous`
- [ ] `sfx_storybook_close`

Cek apakah book/page sounds tetap soft dan tidak harsh/clipping.

### BGM / Ambience

- [ ] BGM tidak terlalu loud/busy
- [ ] Storybook BGM tidak terlalu sad/scary
- [ ] Tutorial BGM tidak terlalu adventurous
- [ ] Playground ambience tidak mengganggu dialogue
