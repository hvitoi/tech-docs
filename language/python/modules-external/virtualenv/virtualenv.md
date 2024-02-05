# virtualenv

- `virtualenv` (external module) and `venv` (internal module) are old-fashioned ways of creating python virtual environments, prefer using `pipenv` instead
- A virtual environment contains all libraries and binaries isolated from the operating system
  - Even the python binary is isolated from the system python binary
- If you are using `pipenv`, the virtual environment is actually created at the home directory and referenced by the Pipfile

```shell
# creates a new virtual environment (in the current directory)
virtualenv my-awesome-environment
virtualenv my-awesome-environment -p "python3.9" # specify the version

# sources the virtual environment
source my-awesome-environment/bin/activate

# now you are in the virtual environment
echo $VIRTUAL_ENV
echo $PATH # path with more binaries

# install dependencies inside of the environment only (inside of `lib/python*/site-packages`)
pip install numpy
```
