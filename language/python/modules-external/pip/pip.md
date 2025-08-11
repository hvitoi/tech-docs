# pip

- Installed modules directory
  - Root: `/usr/lib/python3.13/site-packages/` and `/usr/bin/`
  - Non-root:`~/.local/lib/python3.13/site-packages/` and `~/.local/bin/`
  - Venv: `<venv>/lib/python3.13/site-packages/` and `<venv>/bin`
- It's not advisable to install system-wide packages via pip (its other packaging system's responsibility, e.g., brew, pacman, apt)
  - pip is not a OS packaging system, but rather meant to be used on `python virtual environments`
- Python packages: <https://pypi.org/>

```shell
# Python comes with an ensurepip module, which can install pip in a Python environment.
python -m ensurepip --upgrade
```

## list

- The packages shown are coupled to the pip binary ran
- If you ran the pip binary from your venv you will probably have several project dependencies
- If you the the pip binary from the system-wide installed you will have few dependencies, usually the packages "pip", "wheel" and "packaging"

```shell
pip list
```

## show

- Show information about a package, including where it is installed and its dependencies

```shell
pip show "pip"
```

## install

```shell
# install a package globally
pip install numpy
pip install "numpy[standard]" # specify version

# upgrade package to the newest version
pip install --upgrade pip # upgrade pip itself

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
