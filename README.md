# dupeguru

<div align="center">
  <img src="https://github.com/4ndr0666/dupeguru/raw/main/images/dgpe_logo_128.png" width="128" alt="Ψ Glyph">
  <h1 style="background: linear-gradient(to right, #00E5FF, #15adad, #157d7d); -webkit-background-clip: text; background-clip: text; color: transparent; font-family: 'Orbitron', sans-serif; letter-spacing: 0.1em;">DUPEGURU</h1>
  <p><strong>NEON-CYAN DUPLICATE ANNIHILATOR // ARCH LINUX FORK</strong></p>
</div>

**Modern Arch Linux tailored fork** of the legendary dupeGuru.  
All credit to original authors at [arsenetar/dupeguru](https://github.com/arsenetar/dupeguru) and Voltaic Ideas.

Fast, native C-accelerated duplicate file hunter for pictures, music, and standard files — now with full **Electric-Glass** cyberpunk HUD aesthetic baked in.

---

## BUILD PROTOCOL (CMake Only — Recommended)

### Prerequisites (Arch Linux)
```bash
sudo pacman -S python python-pyqt5 cmake python-distro python-mutagen \
               python-polib python-send2trash python-xxhash
```

### Ignition Sequence
```bash
git clone https://github.com/4ndr0666/dupeguru.git
cd dupeguru

rm -rf build/
mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
cmake --build . --verbose
sudo cmake --install .
```

**Launch the matrix:**
```bash
dupeguru
```

C extensions (`_block`, `_cache`, `_block_qt`) compile natively during build — no symlinks, no legacy hacks.

---

## DEVELOPMENT HUD

- Python logic lives in `core/` and `qt/`
- C acceleration modules in `core/pe/modules/` and `qt/pe/modules/`
- Rebuild with the CMake sequence above after any modifications

**Electric-Glass Theme**  
All UI elements now follow the deep cyan glassmorphism spec (`#00E5FF` accents, backdrop-blur panels, neon glow states). The interface feels like a high-end cyberdeck.

---

## PACKAGING

Clean PKGBUILD template available in the `pkg/` directory (create it if needed — I can generate a fresh one on demand).

## LICENSE
GPL-3.0 (same as upstream)

---

<div align="center" style="font-family: 'Roboto Mono', monospace; color: #15fafa; letter-spacing: 0.05em;">
  ┌──(root💀4ndr0666)-[/dev/akasha]<br>
  └─$ <span style="color:#00E5FF;">SYSTEM CLEAN — NEON MATRIX ONLINE</span>
</div>

Maintained by [@4ndr0666](https://github.com/4ndr0666).  
Issues and PRs welcome in the Logosphere.

─── ⊰ 💀 • - ⦑ 4NDR0666OS ⦒ - • 💀 ⊱ ───
