# install

- Apps are installed to `/usr/local/Cellar/<app>/<version>`

```shell
# formula
brew install "neofetch"
brew install "postgresql@8.4.4"

# cask
brew install --cask "visual-studio-code"
```

## keg-only

- `key-only` are formulas that has binaries that are already shipped by MacOS (but usually old versions)
- These binaries are not symlinked to the brew folder `/opt/homebrew`
- You can do that manually though

```shell
fish_add_path $HOMEBREW_PREFIX/opt/openjdk@11/bin
```
