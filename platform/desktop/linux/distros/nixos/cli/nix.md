# nix

## repl

- Launch repl to evaluate nix expressions

```shell
nix repl
```

- `:q`: quit
- `:p`: force evaluation

## build

```shell
nix build --extra-experimental-features 'nix-command flakes' .#m1n1 -o m1n1
nix build --extra-experimental-features 'nix-command flakes' .#uboot-asahi -o u-boot
nix build --extra-experimental-features 'nix-command flakes' .#installer-bootstrap -o installer -j4 -L
```

## search

```shell
nix search wget
```
