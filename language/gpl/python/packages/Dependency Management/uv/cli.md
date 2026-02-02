# uv

## init

```shell
# Create project in a new dir
cd ~ # parent folder
uv init demo

# Create project in the current dir
mkdir demo
cd demo
uv init
```

## add

- Adds a dependency into `pyproject.toml` and installs it in the virtual environment `.venv/`

```shell
uv add "langchain"
```

```shell
# Add a dependency for a single file
# Dependency are added as comments to the file
echo 'import requests; print(requests.get("http://example.com"))' > demo.py
uv add requests --script demo.py

# Run it
uv run demo.py
```

## run

- Run a script of a dependency

```shell
# Run python code
uv run python - <<'EOF'
  import sys
  sys.exit(1)
EOF

# Run python code interactively (and specify the version)
uv run --python pypy@3.8 -- python
uv run --python 3.12.0 -- python

#
uv run ruff check
```

## uv lock

```shell
uv lock
```

## uv sync

```shell
uv sync
```

## uv python

- Install a python version for the current project

```shell
uv python install 3.10 3.11 3.12

uv python pin 3.11 # pin a version for the cwd
```

## uv tool (uvx)

- Run tools in an ephemeral environment (similar to pipx, npx, etc)

```shell
# run
uvx pycowsay 'hello world!'
uv tool run pycowsay 'hello world!' # same

# install
uv tool install ruff # just install without running
```
