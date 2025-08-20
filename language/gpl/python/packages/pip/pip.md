# pip

- It's not advisable to install system-wide packages via pip (its other packaging system's responsibility, e.g., brew, pacman, apt)
- pip is not a OS packaging system, but rather meant to be used on `python virtual environments`
- Python packages: <https://pypi.org/>

```shell
# Python comes with an ensurepip module, which can install pip in a Python environment.
python -m ensurepip --upgrade
```

## Modules directories

- Root: `/usr/lib/python3.13/site-packages/` and `/usr/bin/`
- Non-root:`~/.local/lib/python3.13/site-packages/` and `~/.local/bin/`
- Venv: `<venv>/lib/python3.13/site-packages/` and `<venv>/bin`

## Provides-Extra

- Some packages provide sets of extra packages, examples:
  - fastapi[standard], fastapi[standard-no-fastapi-cloud-cli], etc
- If you install it this way, pip will additionally install other extra packages for you

## Requirements file

```txt
# import other requirements file, e.g., requirements.txt imported by requirement-dev.txt
-r requirements_base.txt

# import the package plus other extra packages
fastapi[standard-no-fastapi-cloud-cli]

# Pin to specific version
mkdocs==1.5.2

# Version range
fastapi>=0.45.0,<0.46.0
```
