# dupeguru

Modern Arch Linux tailored fork of dupeGuru.  
All credit to the original authors at [arsenetar/dupeguru](https://github.com/arsenetar/dupeguru) and Voltaic Ideas.

Fast duplicate file finder with native C extensions for pictures, music, and standard files.

## Build from Source (CMake only — recommended)

### Prerequisites (Arch Linux)
```bash
sudo pacman -S python python-pyqt5 cmake python-distro python-mutagen \
               python-polib python-send2trash python-xxhash
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

Run the app:
```bash
dupeguru
```

C extensions (`_block`, `_cache`, `_block_qt`) are automatically compiled during the build.

## Development
- Edit Python code in `core/` and `qt/`
- Modify C sources in `core/pe/modules/` or `qt/pe/modules/`
- Rebuild with the CMake commands above after changes

## Packaging
A clean PKGBUILD template is available in the `pkg/` directory.

## License
GPL-3.0 (same as upstream)

---

Maintained by [@4ndr0666](https://github.com/4ndr0666).  
Issues and PRs welcome!
