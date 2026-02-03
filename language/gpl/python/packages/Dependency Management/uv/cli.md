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

## sync

- What is does?
  - Read your pyproject.toml
  - Create a `.venv/` (if not there yet)
  - Install all dependencies
  - Create/update the uv.lock file
- It's similar to `npm i`

```shell
uv sync
uv sync --extra dev # also install "project.optional-dependencies.dev"
```

## run

```shell
# Run the entrypoint of the project
uv run python main.py
uv run python main.py --arg1 value1

# Run python code
uv run python - <<'EOF'
  import sys
  sys.exit(1)
EOF

# Run python code interactively (and specify the version)
uv run --python pypy@3.8 -- python
uv run --python 3.12.0 -- python

# Run an arbitrary command of a dependency
uv run ruff check

# Run a custom script
uv run start

# Run test deps
uv run pytest tests/
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

## uv lock

```shell
uv lock
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
