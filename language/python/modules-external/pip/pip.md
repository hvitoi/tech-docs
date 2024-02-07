# pip

- Installed modules directory
  - Non-root:`~/.local/lib/python3.11/site-packages/` and `~/.local/bin/`
  - Root: `/usr/lib/pythonX.X/site-packages/` and `/usr/bin/`
- It's not advisable to install system-wide packages via pip (its other packaging system's responsability, e.g., brew, pacman, apt)
  - pip is not a OS packaging system, but rather meant to be used on `python virtual environments`
- Python packages: <https://pypi.org/>

## list

```shell
pip list
```

## install

```shell
# install a package globally
pip install numpy

# upgrade package to the newest version
pip install numpy --upgrade # -U
pip install pip --upgrade # upgrade pip itself

# install from a directory
git clone https://github.com/squidfunk/mkdocs-material.git
pip install -e mkdocs-material

# install from requirements file
pip install -r requirements.txt
```

## freeze

- Lists all the dependencies and creates a `requirements.txt` file
- This file contains the direct dependencies required
- To install them all run `pip install -r requirements.txt`
- Requirements file does not store the hash of the dependencies, so it might potentially be unsafe

```shell
pip freeze
```

```txt
mkdocs==1.5.2
mkdocs-material==9.1.21
mkdocs-redirects==1.2.1
```
