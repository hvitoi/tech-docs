# Templating

## Copier

- <https://copier.readthedocs.io/en/stable/>
- A library and CLI app for rendering project templates

```shell
# Install
brew install copier # only copier
uv tool install copier --with jinja2-strcase # copier + jinja_extensions (jinja2_strcase)

mkdir foo && cd foo
copier copy git@github.com:qonto-private/golang-modular-template.git . --trust
copier copy --trust --overwrite --skip-tasks https://github.com/myorg/mytemplate.git .
```
