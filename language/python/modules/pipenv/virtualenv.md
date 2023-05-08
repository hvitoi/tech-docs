# virtualenv

- A virtual environment contains all libraries and binaries isolated from the operating system
  - Even the python binary is isolated from the system python binary
- If you are using `pipenv`, the virtual environment is actually created at the home directory and referenced by the Pipfile

```shell
# creates a new virtual environment
virtualenv "myenv"
virtualenv "myenv" -p "python3.9" # specify the version

# sources the virtual environment
source "myenv/bin/activate"

# now you are in the virtual environment
echo $VIRTUAL_ENV
echo $PATH # path with more binaries
```
