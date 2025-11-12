# uv

- <https://github.com/astral-sh/uv>
- A package management to replace `pip`, `poetry`, `pipenv`, `virtualenv`, etc
- With uv, you don't need to manually create a virtual env, or requirements.txt

```shell
# Brew
brew install uv

# Pip (global)
pip3 install uv
```

## Project structure

```shell
# Create a project skeleton
uv init
```

```txt
.
├── .python-version
├── .venv
├── README.md
├── main.py
├── pyproject.toml
└── uv.lock
```
