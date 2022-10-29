# leaves

- List installed formulae that are not dependencies of another installed formula.

```sh
# all
brew leaves

# only manually installed
brew leaves --installed-on-request

# with description
brew leaves --installed-on-request | xargs -n1 brew desc
```
