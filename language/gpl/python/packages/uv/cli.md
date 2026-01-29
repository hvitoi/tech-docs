# uv

## init

```shell
mkdir demo
cd demo
uv init
```

## add

- Adds a dependency into `pyproject.toml` and installs it in the virtual environment `.venv/`

```shell
uv add "langchain"
```

## run

- Run python code

```shell
uv run python - <<'EOF'
  import sys
  sys.exit(1)
EOF
```
