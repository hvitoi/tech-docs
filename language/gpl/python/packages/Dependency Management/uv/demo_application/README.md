# Application

- Flat layout
- No build system, you just point at files
- No `src/` and not installable
- Conventionally `main.py` is used as entrypoint

```shell
uv init "demo"
cd demo
source .venv/bin/activate
uv add "requests"
uv add "pytest" --dev
uv sync
uv run main.py
uv run pytest
```
