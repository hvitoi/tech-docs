# nix-env

- `User environment`: is a view of a set of installed nix applications

## install

```shell
# Install a package by its id
nix-env --install --attr nixpkgs.neovim
nix-env -iA nixpkgs.neovim

# Specify channel
nix-env -iA nixpkgs.neovim -f '<nixpkgs>'

# install vim
nix-env -iAv nixos.vim

#$ install "hello"
# stores it at "/nix/store/[hash]-hello-[version]/bin/hello"
nix-env -iA nixpkgs.hello
```

## uninstall

```shell
nix-env --uninstall "hello"
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
