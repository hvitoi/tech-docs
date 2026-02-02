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
├── .venv/
├── .python-version
├── pyproject.toml
├── uv.lock
├── main.py
└── README.md
```

## pyproject.toml

```toml
[project]
name = "demo"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.13"
dependencies = [
    "langchain>=1.0.5",
    "langchain-openai>=1.0.2",
]
```
