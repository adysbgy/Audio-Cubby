# Audio Cubby

Repository ini berisi riset kandidat audio untuk **Cubby**.

## Status Saat Ini

| Status | Jumlah |
|---|---:|
| Accepted | 0 |
| Needs review | 34 |
| Missing | 0 |
| Total asset | 34 |

Semua 34 asset diproses dengan **advanced LUFS normalization** (EBU R128): BGM -18 LUFS, Ambience -24 LUFS, SFX -15/-19 LUFS. Semua file lolos technical QC dengan 0 failures. Fitur tambahan: lowpass filter (upset sound), 10ms fades, loop crossfade. Semua masih `needs_review` sampai lolos manual listening.

## Folder

```text
archive/        Arsip lama
raw/            File audio kandidat
raw/bgm/        Musik latar kandidat
raw/ambience/   Suasana/ambience kandidat
raw/sfx/        Efek suara UI, gameplay, emosi, dan storybook kandidat
docs/           Semua dokumentasi, source, audit, prompt, dan handoff
```

## Dokumen Penting

- `docs/CUBBY_AUDIO_HANDOFF.md` — konteks utama untuk chat baru
- `docs/CHAT_PROMPT.md` — prompt singkat untuk chat baru
- `docs/audio_index.md` — daftar file dan status tiap asset
- `docs/source_links.md` — tabel source valid dan link lisensi
- `docs/final_audit.md` — hasil audit kecocokan suara
- `docs/manual_listening_audit.md` — checklist audit dengar manual untuk kandidat review
- `docs/candidate_audit_report.md` — ringkasan kandidat baru dan risiko audit
- `docs/technical_audio_audit.md` — audit teknis audio
- `docs/license_notes.md` — ringkasan sumber dan lisensi
- `audio_manifest.json` — data lengkap semua asset

## Catatan Integrasi

Jangan pindahkan ke project Cubby utama sebelum semua `missing` dan `needs_review` selesai dicek.
