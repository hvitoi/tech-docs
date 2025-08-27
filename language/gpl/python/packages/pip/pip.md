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

## requirements.txt

- Defines exact versions for your environment needs
- Pinning exact versions ensures reproducibility

```shell
pip install -r requirements.txt
```

## pyproject.toml

- Package metadata and lists dependencies that will be installed when other users use your package (when they install it via pip)
- Does not include dev dependencies (e.g., pytest)

```shell
pip install .
```
