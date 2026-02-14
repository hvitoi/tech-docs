# Python

- Designed by `Guido van Rossum` in 1991

## Installation

```shell
# MacOS comes with an old python version preinstalled, you can installed the newest one with brew
brew install python
brew ls python -v
which -a python3
python3 --version
```

## Interpreter

- `CPython` runs a Python code. To do that:
  - The code is **compiled** to `bytecode` by `CPython`
  - The compiled code is then **interpreted** by the `Python Virtual Machine (PVM)`.
- That means that python is both compiled and interpreted

- You can configure your IDE to use a python interpreter (the python binary) with a specific version
  - The python binary can also be picked from your chosen virtual environment
- On vscode, `Python: Select Interpreter`

### CPython compiler step

- When you run a Python code, CPython first compiles your source code (`.py`) into bytecode (`.pyc`)
- This bytecode is stored at `__pycache__/`
- The bytecode is not machine code. It's a lower-level, platform-independent representation of your code
- Example:`def add(a,b): return a+b` becomes a handful of bytecode instructions like `LOAD_FAST, BINARY_ADD, etc.`

### Python Virtual Machine (PVM) execution step

- CPython then executes that bytecode using the Python Virtual Machine, which is part of the CPython runtime.
- The PVM reads the bytecode instructions one by one and performs the corresponding machine-level operations.

## Virtual Environment

- Each virtual environment is created based on a python interpreter (a python version)
- A virtual environment contains all libraries and binaries isolated from the operating system
  - Even the python binary is isolated (although symlinked to the system python binary)
- Options
  - `venv`: the native virtual environment solution
  - `virtualenv`: 3rd party
  - `pipenv`: 3rd party
  - `poetry`: 3rd party
  - `uv`: 3rd party

```shell
python -m venv ".venv"
source ./.venv/bin/activate
echo $VIRTUAL_ENV
echo $PATH
```

- On vscode, to select the venv `Python: Select Interpreter` and select the venv or "Enter interpreter path..." and insert the absolute path of venv

## Language Server

- `Jedi`: Community-driven
- `Pyright`
  - Microsoft created the "Pylance" VS Code extension, which is powered by Pyright
  - With homebrew, source files are installed at `/opt/homebrew/Cellar/python@3.12/3.12.1_1/Frameworks/Python.framework/Versions/3.12/lib/python3.12`
- `PyLSP`

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
