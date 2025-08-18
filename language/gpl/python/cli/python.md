# python

- Additionally install `python-pip` (Extra)

## -m

- Run library module as a script

```shell
python -m "pip" install pip --upgrade # run pip to upgrade itself
python -m "unittest" test_your_module.py # run tests
python -m "ensurepip" --upgrade

# Run a python file as a package (the demo dir needs to have __init__.py)
# your cwd needs to be the parent directory of the demo package
python -m demo.main
```
