# cli

## shell

- Equivalent to `uv init` or `python -m venv .venv`

```shell
# sources the virtual environment (creates it empty if not yet existent)
pipenv shell

# prints the path of the venv
pipenv --venv
```

## install

- Install dependencies as specified in Pipfile[.lock]
  - If Pipfile is not found but a requirements.txt file is present, it will convert it into a Pipfile
- Dependencies are installed in home directory

```shell
pipenv install # packages
pipenv install -d # dev-packages

# Add dependency to Pipfile
pipenv install "numpy"
```

## run

- Run a command inside of the virtual environment (without sourcing it)

```shell
pipenv run
```
