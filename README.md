# dupeguru

This is a modernized, Arch Linux-tailored fork of [arsenetar/dupeguru](https://github.com/arsenetar/dupeguru/). All credit to the original authors.

## Features
- Native C extensions (_block, _cache, _block_qt) compiled at build time for any Python version
- Pure CMake build system (no setuptools hacks)
- Full PyQt5-based duplicate finder (pictures, music, standard files)

## Building from Source (Recommended)

### Prerequisites (Arch Linux)
```bash
sudo pacman -S python python-pip python-pyqt5 cmake python-distro python-mutagen python-polib python-send2trash python-xxhash
```

### Build & Install
```bash
git clone https://github.com/4ndr0666/dupeguru.git
cd dupeguru

rm -rf build/
mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
cmake --build . --verbose
sudo cmake --install .
```

Run:
```bash
dupeguru
```

## Development

- Edit Python files in `core/` and `qt/`
- C extensions live in `core/pe/modules/` and `qt/pe/modules/`
- Re-run the CMake build after any C changes

## Packaging (Arch Linux PKGBUILD example)

See the `pkg/` directory for a ready-to-use PKGBUILD template.

## License
GPL-3.0 (same as upstream)

---

**Maintained by 4ndr0666** — issues and PRs welcome!
