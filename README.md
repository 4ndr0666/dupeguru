# dupeGuru

[dupeGuru][dupeguru] is a cross-platform (Linux, OS X, Windows) GUI tool to find duplicate files in
a system. It is written mostly in Python 3 and uses [qt](https://www.qt.io/) for the UI.

## Current status
Still looking for additional help especially with regards to:
* OSX maintenance: reproducing bugs, packaging verification.
* Linux maintenance: reproducing bugs, maintaining PPA repository, Debian package, rpm package.
* Translations: updating missing strings, transifex project at https://www.transifex.com/voltaicideas/dupeguru-1
* Documentation: keeping it up-to-date.

## Contents of this folder

This folder contains the source for dupeGuru. Its documentation is in `help`, but is also
[available online][documentation] in its built form. Here's how this source tree is organized:

* core: Contains the core logic code for dupeGuru. It's Python code.
* qt: UI code for the Qt toolkit. It's written in Python and uses PyQt.
* images: Images used by the different UI codebases.
* pkg: Skeleton files required to create different packages
* help: Help document, written for Sphinx.
* locale: .po files for localization.
* hscommon: A collection of helpers used across HS applications.

## How to build dupeGuru from source

### Prerequisites
*   Python 3.8+
*   pip
*   setuptools
*   PyQt5
*   CMake

### System Setup (Arch Linux)
On Arch Linux, install the necessary packages using `pacman`:

```bash
sudo pacman -S python python-pip python-setuptools python-wheel pyqt5 cmake
```

### Building with CMake

1.  Clone the repository:
    ```bash
    git clone https://github.com/arsenetar/dupeguru.git
    cd dupeguru
    ```

2.  Create and activate a Python virtual environment:
    ```bash
    python -m venv env
    source env/bin/activate
    ```

3.  Install Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4.  Build the project using CMake:
    ```bash
    mkdir build
    cd build
    cmake ..
    cmake --build . --target install --prefix ../install
    ```

5.  Run the application:
    ```bash
    # Ensure you are in the project root directory
    source env/bin/activate # If not already active
    python run.py
    ```

### Generating Arch Linux Package (PKGBUILD)
To generate an Arch Linux package, you would typically create a `PKGBUILD` file. Below is an example `PKGBUILD` for dupeGuru. Remember to replace `sha256sums=('SKIP')` with the actual checksum of the source tarball.

```PKGBUILD
# Contributor: Your Name <your_email@example.com>
pkgname=dupeguru
pkgver=4.3.1
pkgrel=1
pkgdesc="A cross-platform GUI tool to find duplicate files."
arch=('x86_64')
url="https://dupeguru.voltaicideas.net/"
license=('GPL3')
depends=('python' 'python-pyqt5')
makedepends=('cmake' 'python-setuptools' 'python-wheel' 'python-pip')
_pkgname=dupeguru # Used for source tarball naming

source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/arsenetar/dupeguru/archive/v${pkgver}.tar.gz")
sha256sums=('SKIP') # IMPORTANT: Replace 'SKIP' with the actual sha256sum of the downloaded source tarball!

build() {
  # Create a build directory
  mkdir -p build
  cd build

  # Configure CMake
  cmake ../${_pkgname}-${pkgver} \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_BUILD_TYPE=Release \
    -DPYTHON_EXECUTABLE=/usr/bin/python

  # Build the project
  cmake --build . 
}

package() {
  cd build
  # Install the built files to the fakeroot environment
  cmake --install . --prefix="${pkgdir}/usr"
  # Python specific install, if not handled by cmake --install
  # python -m pip install ../${_pkgname}-${pkgver} --root="${pkgdir}" --optimize=1 --no-deps
}
```

[dupeguru]: https://dupeguru.voltaicideas.net/
[cross-toolkit]: http://www.hardcoded.net/articles/cross-toolkit-software
[documentation]: http://dupeguru.voltaicideas.net/help/en/
[python]: http://www.python.org/
[pyqt]: http://www.riverbankcomputing.com
[tox]: https://tox.readthedocs.org/en/latest/