# list

- List all installed `Formulae` and `Casks`
- **Formula**: package definition built from upstream sources
- **Cask**: install macOS native applications

```shell
brew list
brew ls

# One entry per line
brew list -1

# List files of a given package
brew list "fish"
brew list "fish" -v # verbose expands the directories and show the nested files
brew list "fish" --versions
```
