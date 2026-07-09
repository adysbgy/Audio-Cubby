# Audio Cubby - New Conversation Prompt

## Working Directory
`/Users/aj/Downloads/Audio-Cubby-cubby-audio-research`

## Git Remote
`https://github.com/adysbgy/Audio-Cubby.git`  
Branch: `cubby-audio-research`

## Asset Status
| Status | Count |
|---|---|
| accepted | 0 |
| needs_review | 34 |
| missing | 0 |

## Completed Phases
- ✅ Pre-validation (all sources CC0/PD/no-login)
- ✅ Advanced processing (LUFS, fades, lowpass)
- ✅ Contextual rebuild (storybook, emotion, sandbox)
- ✅ Peak normalization (strict 88% ceiling)
- ✅ Documentation cleanup

## What To Do Next

### Option A: Manual Listening Audit
**Task**: Audit semua 34 asset di `raw/`
**How**: 
1. Buka `docs/manual_listening_detailed.md`
2. Dengar tiap file pakai player WAV
3. Tandai cocok/tidak cocok di tabel
4. Update `audio_manifest.json` status

### Option B: External Source Integration
**Task**: Ganti asset yang mungkin tidak cocok
**How**:
1. Review listening audit hasil
2. Cari replacement di OpenGameArt/SoundBible CC0/PD
3. Download ke `source_downloads/`
4. Rebuild pakai skrip `tools/rebuild_contextual.py`

### Option C: Final Docs Cleanup
**Task**: Rapikan dokumentasi
**How**:
1. Hapus redundant docs
2. Update status final di semua tabel
3. Buat ringkasan akhir

### Option D: Integration Preparation
**Task**: Siapkan file untuk game engine
**How**:
1. Copy accepted files ke folder game project
2. Buat manifest final dengan path absolut
3. Dokumentasi integrasi

## License Policy
- Preferred: CC0, Public Domain
- Avoid: Pixabay, freesound_community, NonCommercial, NoDerivatives

## Source Mapping (Contextual Rebuild)
| Asset Group | Source | License |
|---|---|---|
| Storybook | 10 Book Page Flips, Book Flip Sounds | CC0 |
| Sandbox/Sand | Water Splash and sand footsteps (Peludo) | CC0 |
| Emotion/Negative/Neutral | Local procedural soft tones | Project-owned |
| BGM | Children's Game Music (heartade) | CC0 |
| UI/Dialogue | GUI Sound Effects (Lokif), RPG Sound Pack (artisticdude) | CC0 |
| Grass footstep | Different Steps (TinyWorlds) | CC0 |

## Technical Specs Achieved
- Format: WAV, 44.1kHz, 16-bit
- Peak ceiling: ≤87.9%
- Duration: 0.06–69s (acceptable)
- All assets: needs_review