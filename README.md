<p align="center">
  <a href="https://github.com/4ndr0666/dupeguru/actions"><img src="https://img.shields.io/github/actions/workflow/status/4ndr0666/dupeguru/build.yml?style=for-the-badge&label=BUILD&color=00E5FF&logo=github" alt="Build Status"></a>
  <a href="https://github.com/4ndr0666/dupeguru"><img src="https://img.shields.io/badge/ARCH-LINUX-15fafa?style=for-the-badge&logo=archlinux&logoColor=15fafa" alt="Arch Linux"></a>
  <a href="https://github.com/4ndr0666/dupeguru/blob/main/LICENSE"><img src="https://img.shields.io/badge/LICENSE-GPL3.0-00E5FF?style=for-the-badge" alt="License"></a>
</p>

<h1 align="center" style="font-family: 'Orbitron', sans-serif; letter-spacing: 0.2em; background: linear-gradient(90deg, #00E5FF, #15adad, #157d7d); -webkit-background-clip: text; background-clip: text; color: transparent;">
  DUPEGURU
</h1>
<p align="center" style="font-family: 'Roboto Mono', monospace; color: #15fafa; font-size: 1.15em;">
  DUPLICATE ANNIHILATOR // ARCH EDITION
</p>

<p align="center">
  <img src="images/dupeguru-electric-glass-glyph.png" alt="Ψ Electric-Glass Glyph" width="220">
</p>

**Arch Linux tailored fork** of dupeGuru.  
All credit to original authors at [arsenetar/dupeguru](https://github.com/arsenetar/dupeguru) and Voltaic Ideas.

Fast, native C-accelerated duplicate file hunter for pictures, music, and standard files.

---

## Table of Contents

- [Build Protocol](#build-protocol)
- [Python Ignition Sequence](#python-ignition-sequence)
- [Make Ignition Sequence](#make-ignition-sequence)
- [Packaging](#packaging)
- [Testing](#testing)
- [License](#license)

---

## Build Protocol 

### Prerequisites (Arch Linux)
```bash
sudo pacman -S python python-pyqt5 cmake python-distro python-mutagen \
               python-polib python-send2trash python-xxhash debhelper
```

### Python Ignition Sequence
```bash
git clone https://github.com/4ndr0666/dupeguru.git
cd dupeguru

python3 -m venv --system-site-packages ./env
source ./env/bin/activate
pip install -r requirements.txt
python build.py
python run.py
```

### Make Ignition Sequence
```bash
git clone https://github.com/4ndr0666/dupeguru.git
cd dupeguru

make
make run
```

**Install it:**
```bash
sudo make install
```

---

## Packaging

bash -c "python3 -m venv --system-site-packages env && source env/bin/activate && pip install -r requirements.txt -r requirements-extra.txt && python build.py --clean && python package.py"

*Clean command  for a fresh install:*
```bash
    $ python build.py --clean
```

## Testing

The complete test suite is run with [Tox 1.7+][tox]. If you have it installed system-wide, you
don't even need to set up a virtualenv. Just `cd` into the root project folder and run `tox`.

If you don't have Tox system-wide, install it in your virtualenv with `pip install tox` and then
run `tox`.

You can also run automated tests without Tox. Extra requirements for running tests are in
`requirements-extra.txt`. So, you can do `pip install -r requirements-extra.txt` inside your
virtualenv and then `py.test core hscommon`

[dupeguru]: https://dupeguru.voltaicideas.net/
[documentation]: http://dupeguru.voltaicideas.net/help/en/
[tox]: https://tox.readthedocs.org/en/latest/

## License
GPL-3.0 (same as upstream)

---

<div align="center" style="font-family: 'Roboto Mono', monospace; color: #15fafa; background: rgba(10, 24, 38, 0.9); padding: 1.8em; border: 1px solid #00E5FF; border-radius: 12px; max-width: 820px; margin: 3em auto 2em;">
  <pre style="margin: 0; color: #00E5FF; font-size: 1.05em;">
┌──(root💀4ndr0666)-[/dev/akasha]
└─$ <span style="color:#15fafa;">DUPLICATES WILL BE PURGED</span>
  </pre>
</div>

Maintained by [@4ndr0666](https://github.com/4ndr0666).  

─── ⊰ 💀 • - ⦑ 4NDR0666OS ⦒ - • 💀 ⊱ ───
