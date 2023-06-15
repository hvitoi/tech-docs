# texlive-most

- Install the group `texlive-most` with all the texlive dependencies
- Install the AUR meta package`texlive-latexindent-meta` to use latexindent
- `texstudio` is the IDE to edit tex documents

## git-latexdiff

- It's a dependency of `texlive-core`
- Show diff between two versions of latex files
- `git-latexdiff` is a wrapper around latexdiff and diff

```shell
# Diff between the last commit and the workspace
git latexdiff "HEAD" "--" \
  --main "main.tex" \
  --lualatex \
  --run-bibtex \
  --ignore-latex-errors \
  --type "UNDERLINE" \
  --output "/home/hvitoi/Downloads/diff.pdf"
```

- Markup styles
  1. UNDERLINE (default)
  1. CTRADITIONAL
  1. TRADITIONAL
  1. CFONT
  1. FONTSTRIKE
  1. INVISIBLE
  1. CHANGEBAR
  1. CCHANGEBAR
  1. CULINECHBAR
  1. CFONTCHBAR
  1. BOLD
  1. PDFCOMMENT
