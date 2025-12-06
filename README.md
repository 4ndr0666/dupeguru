# Dupeguru

>This is the work of [Arsentar](https://github.com/arsenetar/dupeguru/) so all credit to them. This is just a modernized and Arch Linux tailored build.

## How to build dupeGuru from source

### Prerequisites
*   Python 3.8+
*   pip
*   setuptools
*   PyQt5

### System Setup (Arch Linux)
On Arch Linux, install the necessary packages using `pacman`:

```bash
sudo pacman -S python python-pip python-setuptools python-wheel pyqt5
```

### Building and Installing with Pip

1.  Clone the repository:
    ```bash
    git clone https://github.com/4ndr0666/dupeguru.git
    cd dupeguru
    ```

2.  Create and activate a Python virtual environment:
    ```bash
    python3 -m venv .env
    source .env/bin/activate
    ```

3.  Install dupeGuru:
    ```bash
    pip install .
    ```

4.  Run the application:
    ```bash
    dupeguru
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
[documentation]: http://dupeguru.voltaicideas.net/help/en/
