# nix-shell

- Chroot into a virtual environment with the packages your wish

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

```shell
nix-shell
```

## packages

```shell
# single package
nix-shell --packages "nodejs"
nix-shell -p "nodejs"

# multiple packages
nix-shell -p python3 nodejs go rustc
```
