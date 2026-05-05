# Packaged Application

- `src layout`: code inside `src/<package>/`
- Requires a build system
- Application is installed into `.venv/`

```shell
uv init "demo" --package
cd demo
source .venv/bin/activate
uv add "requests"
uv add "pytest" --dev
uv sync
uv run demo
uv run pytest
```
