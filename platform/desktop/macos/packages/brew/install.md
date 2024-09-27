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

## Package dependencies

A package that has other packages as dependencies on `brew install` will install all the required dependencies as "installed on request"
If a package is not correctly marked as a "dependency" but "explicitly installed" you can force it to be marked "installed on request" but uninstalling it and reinstalling the parent package the depends on it

```shell
brew uninstall --ignore-dependencies xy
brew reinstall ranger
```
