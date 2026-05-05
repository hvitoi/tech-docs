# pytest

- It's a Python testing framework

## Test Discovery

- Searches recursively for all files named `test_*.py` and `*_test.py`
- On those files, run the functions that start with `test_`

```shell
pytest
pytest -v # verbose
pytest tests/test_main.py              # single file
pytest tests/test_main.py::test_name   # single test
```
