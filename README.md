# dupeguru

Modernized Arch Linux fork of the original dupeGuru by Arsentar / Voltaic Ideas.  
All credit to the upstream authors.

Fast duplicate finder for pictures, music, and standard files with native C extensions.

## Build from Source (CMake only)

### Prerequisites (Arch Linux)
```bash
sudo pacman -S python python-pyqt5 cmake python-distro python-mutagen python-polib \
               python-send2trash python-xxhash
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
- C extensions are automatically compiled from `core/pe/modules/` and `qt/pe/modules/`
- Rebuild with the CMake commands above after any changes to `.c` files

## Packaging
A clean PKGBUILD template is available in the `pkg/` directory.

## License
GPL-3.0 (same as upstream)

---

Maintained by [@4ndr0666](https://github.com/4ndr0666).  
Issues and PRs welcome!
