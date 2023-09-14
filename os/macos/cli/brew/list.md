# list

- List all installed `Formulae` and `Casks`
- **Formula**: package definition built from upstream sources
- **Cask**: install macOS native applications

```shell
brew list
brew ls

brew list -l # long format
brew list -1 # one line per package

# List files of a given package
brew list "fish"
brew list "fish" -v # verbose expands the directories and show the nested files
brew list "fish" --versions
```

## Brew catalog

- Creates a catalog of files per installed package

```bash
brew list --formula |
  while read formula; do
    brew list $formula |
      while read file; do
        echo -e "$formula\t$file"
      done
  done
```
