# nix-shell

- Chroot into a virtual environment with the packages your wish
- Next shells can be nested adding more packages

```shell
nix-shell
```

```nix
{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell { # mkShell is a helper function
  name="dev-environment";

  # list of pakcages to be installed in the virtual shell
  buildInputs = [
    pkgs.nodejs
  ];
  # Command to run when entering the environment
  shellHook = ''
    echo "Starting the development environment"
  '';
}
```

## packages

```shell
# single package
nix-shell --packages "nodejs"
nix-shell -p "nodejs"

# multiple packages
nix-shell -p cowsay lolcat
```

## path

- Determine what to use as source for the packages

```shell
# Uses a specific git revision of nixpkgs
nix-shell -I nixpkgs=https://github.com/NixOS/nixpkgs/archive/2a601aafdc5605a5133a2ca506a34a3a73377247.tar.gz
```

## run

- Runs a command in the shell environment and exit

```shell
nix-shell -p cowsay lolcat --run "cowsay Hey! | lolcat"
```

## pure

- Discard system environment variables
- This way, only the provided packages are available inside of the shell

```shell
nixshell -p git --pure
```

## Nix Shell Scripts

- Assure a reproducible script run
- Leverages `shebang`

```shell
#!/usr/bin/env nix-shell
#! nix-shell -i bash --pure
#! nix-shell -p bash cacert curl jq python3Packages.xmljson
#! nix-shell -I nixpkgs=https://github.com/NixOS/nixpkgs/archive/2a601aafdc5605a5133a2ca506a34a3a73377247.tar.gz

curl https://github.com/NixOS/nixpkgs/releases.atom | xml2json | jq .
```
