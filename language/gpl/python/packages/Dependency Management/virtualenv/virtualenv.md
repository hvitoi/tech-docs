# virtualenv

- This is an external package! The native module is `venv`

```shell
# creates a new virtual environment (in the current directory)
virtualenv ./my-awesome-environment
virtualenv ./my-awesome-environment -p "python3.9" # specify the version

# sources the virtual environment
source ./my-awesome-environment/bin/activate

# now you are in the virtual environment
echo $VIRTUAL_ENV
echo $PATH # path with more binaries

# install dependencies inside of the environment only (inside of `lib/python*/site-packages`)
pip install numpy
```
