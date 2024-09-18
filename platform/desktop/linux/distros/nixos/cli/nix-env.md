# nix-env

- A package manager! Packages installed via nix-env are installed for the current user only
- Not particularly useful on NixOS systems in which you will either install via config file or launch a nix-shell
- `User environment`: is a view of a set of installed nix applications

## install

- Packages are stored at `/nix/store/<hash>-<package>-<version>`
- To install a package, the `attr-path` id must be specified. Get it with `nix-env -qaP`

```shell
# Install a package by its id
nix-env --install --attr nixpkgs.neovim
nix-env -iA nixpkgs.neovim

# Specify channel
nix-env -iA nixpkgs.neovim -f '<nixpkgs>'
```

## upgrade

```shell
# Upgrade all packages
nix-env --upgrade

# Upgrade a specific package
nix-env --upgrade --attr nixpkgs.neovim
```

## uninstall

- To uninstall a package, the `package name` must be specified. Get it with `nix-env -q`

```shell
nix-env --uninstall "neovim"
nix-env -e "neovim"
```

## query

```shell
# list all installed packages
nix-env --query
nix-env -q

# query from a channel manually (e.g., cloned from github)
nix-env -q --file "/path/to/nixpkgs"
nix-env -qf "/path/to/nixpkgs"

# list all available (installable) packages and it's id (first column)
nix-env -q --available --attr-path
nix-env -qaP
nix-env -qaP "firefox" # filter by name
nix-env -qaP "firefox.*" # filter with regex

# get the status of the package (I: installed, P: present on system, S: binary available)
nix-env -q --status
nix-env -qs
```

## list-generations

```shell
nix-env --list-generations
```
