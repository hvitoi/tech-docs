# pipenv

- `Pipfile`: A file that specifies the dependencies to be available in the virtual environment
- Dependencies are installed to your home directory per virtual environment
  - `~/.local/share/virtualenvs/<myenv-xyz>`

## shell

```shell
# sources the virtual environment (creates it if not yet existent)
pipenv shell

# prints the path of the venv
pipenv --venv
```

## install

```shell
# Install dependencies as specified in Pipfile (installs in home directory)
pipenv install

# Add dependency to Pipfile
pipenv install "numpy"
```
