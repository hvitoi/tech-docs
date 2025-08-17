# Python Packages

- **Package** is a directory that contains a special file called `__init__.py` (can be empty).
- The presence of `__init__.py` tells Python that this directory is a package, and can contain `modules` and `subpackages`

```shell
myapp/               # package
├── __init__.py
├── models.py        # module
└── utils/           # subpackage
    ├── __init__.py
    └── helper.py    # module
```

## Native Modules (Standard Library)

- The Python Standard Library: <https://docs.python.org/3/library/index.html>
- Types: <https://docs.python.org/3/library/stdtypes.html>
- Data Structures: <https://docs.python.org/3/tutorial/datastructures.html>
- Keywords: <https://www.w3schools.com/python/python_ref_keywords.asp>
- Standard Libraries complexity: <https://www.geeksforgeeks.org/complexity-cheat-sheet-for-python-operations/>

## External Packages

- External Packages: <https://pypi.org/>
- `Pip` is the endorsed package manager for python, although it's an external module

```shell
# Pip can be installed through the built-in module "ensurepip"
python -m ensurepip --upgrade
```
