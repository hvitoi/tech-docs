# list

- List all installed `Formulae` and `Casks`
- **Formula**: package definition built from upstream sources
- **Cask**: install macOS native applications

```shell
brew list
brew ls

# One entry per line
brew list -1

# specific package info
brew list "k9s"
brew list "k9s" --versions
```
