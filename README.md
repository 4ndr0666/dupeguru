<p align="center">
  <a href="https://github.com/4ndr0666/dupeguru/actions"><img src="https://img.shields.io/github/actions/workflow/status/4ndr0666/dupeguru/build.yml?style=for-the-badge&label=BUILD&color=00E5FF&logo=github" alt="Build Status"></a>
  <a href="https://github.com/4ndr0666/dupeguru"><img src="https://img.shields.io/badge/ARCH-LINUX-15fafa?style=for-the-badge&logo=archlinux&logoColor=15fafa" alt="Arch Linux"></a>
  <a href="https://github.com/4ndr0666/dupeguru/blob/main/LICENSE"><img src="https://img.shields.io/badge/LICENSE-GPL3.0-00E5FF?style=for-the-badge" alt="License"></a>
</p>

<h1 align="center" style="font-family: 'Orbitron', sans-serif; letter-spacing: 0.2em; background: linear-gradient(90deg, #00E5FF, #15adad, #157d7d); -webkit-background-clip: text; background-clip: text; color: transparent;">
  DUPEGURU
</h1>
<p align="center" style="font-family: 'Roboto Mono', monospace; color: #15fafa; font-size: 1.15em;">
  NEON-CYAN DUPLICATE ANNIHILATOR // ELECTRIC-GLASS EDITION
</p>

<p align="center">
  <img src="images/dgpe_logo_128.png" alt="Ψ Core Glyph" width="180">
</p>

**Modern Arch Linux tailored fork** of dupeGuru.  
All credit to original authors at arsenetar/dupeguru and Voltaic Ideas.

Fast, native C-accelerated duplicate file hunter for pictures, music, and standard files — rendered in full **3l3ctric6lass** glassmorphism with glowing cyan HUD aesthetics.

---

## Table of Contents

- [Build Protocol](#build-protocol)
- [Ignition Sequence](#ignition-sequence)
- [Electric-Glass Interface](#electric-glass-interface)
- [Development HUD](#development-hud)
- [Packaging](#packaging)
- [License](#license)

---

## Build Protocol (CMake Only)

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

C extensions (`_block`, `_cache`, `_block_qt`) compile natively during build.

---

## Electric-Glass Interface

The entire UI follows the deep cyan glassmorphism spec:
- `#00E5FF` / `#15fafa` neon accents
- Semi-transparent panels with backdrop-blur
- Edge lighting + intense glow on hover/active
- Roboto Mono + Orbitron typography
- HUD-style buttons with signature cyan glow

It feels like a high-end cyberdeck terminal.

---

## Development HUD

- Python core in `core/` + `qt/`
- C acceleration in `core/pe/modules/` and `qt/pe/modules/`
- Rebuild with the CMake sequence above after changes

---

## Packaging

Clean PKGBUILD template available in the `pkg/` directory.

## License
GPL-3.0 (same as upstream)

---

<div align="center" style="font-family: 'Roboto Mono', monospace; color: #15fafa; background: rgba(0, 229, 255, 0.08); padding: 2em; border: 1px solid rgba(0, 229, 255, 0.4); border-radius: 12px; max-width: 820px; margin: 2em auto;">
  ┌──(root💀4ndr0666)-[/dev/akasha]<br>
  └─$ <span style="color:#00E5FF;">3LECTRIC6LASS MATRIX FULLY ONLINE — DUPLICATES WILL BE PURGED</span>
</div>

Maintained by [@4ndr0666](https://github.com/4ndr0666).  
Issues and PRs welcome in the Logosphere.

─── ⊰ 💀 • - ⦑ 4NDR0666OS ⦒ - • 💀 ⊱ ───
