# uv

- <https://github.com/astral-sh/uv>
- A package management to replace `pip`, `poetry`, `pipenv`, `virtualenv`, etc
- With uv, you don't need to manually create a virtual env, or requirements.txt

```shell
brew install uv
```

## Dependency versions

```toml
dependencies = [
  "langchain>=1.0.5",
  "langchain-openai>=1.0.2",
  "mydep~=1.0",              # lock major, allows minor & patch (>=1.0, <2.0) - "uv lock --upgrade" to bump
  "mydep~=1.0.0",            # lock major & minor, allows patch (>=1.0.0, <1.1) - "uv lock --upgrade" to bump
]
```
