from setuptools import setup, Extension, find_packages
from pathlib import Path
from os import path

# Read the version from core/__init__.py
about = {}
here = path.abspath(path.dirname(__file__))
with open(path.join(here, "core", "__init__.py"), "r", encoding="utf-8") as f:
    exec(f.read(), about)

exts = [
    Extension(
        "core.pe._block",
        [
            str(Path("core", "pe", "modules", "block.c")),
            str(Path("core", "pe", "modules", "common.c")),
        ],
        include_dirs=[str(Path("core", "pe", "modules"))],
    ),
    Extension(
        "core.pe._cache",
        [
            str(Path("core", "pe", "modules", "cache.c")),
            str(Path("core", "pe", "modules", "common.c")),
        ],
        include_dirs=[str(Path("core", "pe", "modules"))],
    ),
    Extension("qt.pe._block_qt", [str(Path("qt", "pe", "modules", "block.c"))]),
]

headers = [str(Path("core", "pe", "modules", "common.h"))]

# Read requirements from requirements.txt
with open(path.join(here, "requirements.txt"), encoding="utf-8") as f:
    install_requires = f.read().splitlines()

setup(
    name="dupeguru",
    version=about["__version__"],
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    package_dir={"": "."},
    ext_modules=exts,
    headers=headers,
    install_requires=install_requires,
    entry_points={
        "console_scripts": [
            "dupeguru = core.__main__:main",
        ],
    },
)