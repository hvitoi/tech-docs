# pipenv

- `Pipfile`: A file that specifies the dependencies to be available in the virtual environment
- Dependencies are installed to your home directory per virtual environment
  - `~/.local/share/virtualenvs/<myenv-xyz>`
- This is mostly deprecated and not used for new projects

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

## shell

```shell
# sources the virtual environment (creates it empty if not yet existent)
pipenv shell

# prints the path of the venv
pipenv --venv
```

## run

- Run a command inside of the virtual environment (without sourcing it)

```shell
pipenv run
```

## Pipfile

```toml
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
django = "*"

[dev-packages]

[requires]
python_version = "3.11"
```
