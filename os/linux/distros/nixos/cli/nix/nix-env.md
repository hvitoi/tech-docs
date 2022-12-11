# nix-env

- `-A` searches by the exact match

## install

```shell
nix-env -f '<nixpkgs>' -iA emacs

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
```

## list-generations

```shell
nix-env --list-generations
```
