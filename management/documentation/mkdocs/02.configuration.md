# mkdocs

```yaml
site_name: Tech Docs
docs_dir: .

# MkDocs uses the Python Markdown library to translate Markdown files into HTML
markdown_extensions:
  - pymdownx.highlight
  - pymdownx.inlinehilite
  - pymdownx.superfences
  - pymdownx.tasklist
  - pymdownx.details

theme:
  name: material # pip install mkdocs-material
  # navigation_depth: 0
  # titles_only: true

plugins:
  - same-dir # pip install mkdocs-same-dir
  # - offline
  # - search
  # - social
  # - tags
```
