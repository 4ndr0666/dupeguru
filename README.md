<div align="center">
  <img src="https://github.com/4ndr0666/dupeguru/raw/main/images/dgpe_logo_128.png" width="148" alt="Ψ Core">
  <h1 style="font-family: 'Orbitron', sans-serif; letter-spacing: 0.15em; background: linear-gradient(90deg, #00E5FF, #15adad, #157d7d); -webkit-background-clip: text; background-clip: text; color: transparent; margin: 0.2em 0;">
    DUPEGURU
  </h1>
  <p style="font-family: 'Roboto Mono', monospace; color: #15fafa; font-size: 1.1em; letter-spacing: 0.08em;">
    NEON-CYAN DUPLICATE ANNIHILATOR // ARCH LINUX FORK
  </p>
  <p><strong>Electric-Glass Cyberdeck Edition</strong></p>
</div>

**Modern Arch Linux tailored fork** of dupeGuru.  
All credit to original authors at [arsenetar/dupeguru](https://github.com/arsenetar/dupeguru) and Voltaic Ideas.

Fast, native C-accelerated duplicate file hunter for pictures, music, and standard files — now rendered in full **3l3ctric6lass** glassmorphism with glowing cyan HUD aesthetics.

---

## BUILD PROTOCOL (CMake Only)

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

C extensions (`_block`, `_cache`, `_block_qt`) compile natively — zero legacy friction.

---

## DEVELOPMENT HUD

- Python core in `core/` + `qt/`
- C acceleration in `core/pe/modules/` and `qt/pe/modules/`
- Rebuild with the CMake sequence above

**Electric-Glass Interface**  
The entire UI now follows the deep cyan glassmorphism spec (`#00E5FF` / `#15fafa` accents, semi-transparent panels with backdrop-blur, neon glow states, edge lighting, Roboto Mono + Orbitron typography). It feels like a high-end cyberdeck terminal.

---

## PACKAGING

Clean PKGBUILD template lives in the `pkg/` directory.

## LICENSE
GPL-3.0 (same as upstream)

---

<div align="center" style="font-family: 'Roboto Mono', monospace; color: #15fafa; letter-spacing: 0.05em; background: rgba(0, 229, 255, 0.05); padding: 1.5em; border: 1px solid rgba(0, 229, 255, 0.3); border-radius: 8px;">
  ┌──(root💀4ndr0666)-[/dev/akasha]<br>
  └─$ <span style="color:#00E5FF;">SYSTEM CLEAN — 3LECTRIC6LASS MATRIX FULLY ONLINE</span>
</div>

Maintained by [@4ndr0666](https://github.com/4ndr0666).  
Issues and PRs welcome in the Logosphere.

─── ⊰ 💀 • - ⦑ 4NDR0666OS ⦒ - • 💀 ⊱ ───
