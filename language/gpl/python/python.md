# Python

## Installation

```shell
# MacOS comes with an old python version preinstalled, you can installed the newest one with brew
brew install python
brew ls python -v
which -a python3
python3 --version
```

## Interpreter

- You can configure your IDE to use a python interpreter (the python binary) with a specific version
  - The python binary can also be picked from your chosen virtual environment
- On vscode, `Python: Select Interpreter`

## Virtual Environment

- Each virtual environment is created based on a python interpreter (version)
- A virtual environment contains all libraries and binaries isolated from the operating system
  - Even the python binary is isolated (although symlinked to the system python binary)
- Options
  - `venv`: the native virtual environment solution
  - `virtualenv`: 3rd party
  - `pipenv`: 3rd party, more recent

```shell
python -m venv ".venv"
source ./.venv/bin/activate
echo $VIRTUAL_ENV
echo $PATH
```

- On vscode, to select the venv `Python: Select Interpreter` and select the venv or "Enter interpreter path..." and insert the absolute path of venv

## Language Server

- `Jedi`: Community-driven
- `Pylance`: Developed by Microsoft
- With homebrew, source files are installed at `/opt/homebrew/Cellar/python@3.12/3.12.1_1/Frameworks/Python.framework/Versions/3.12/lib/python3.12`

## Linter & Formatter

- <https://code.visualstudio.com/docs/python/linting>

- `Ruff` <https://github.com/astral-sh/ruff-vscode>
- `Flake8`: By Microsoft

## IDEs

- **Vscode extensions**
  - ms-python.python
  - ms-python.debugpy
  - ms-python.vscode-pylance
  - charliermarsh.ruff
  - ms-toolsai.jupyter
