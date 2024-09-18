# nix-channel

- Nixpkgs channels (repo)
  - `nixos`: <https://nixos.org/channels/nixos-22.11>
  - `nixos-unstable`: <https://nixos.org/channels/nixpkgs-unstable>

## list

```shell
# List all channels for the current user
nix-channel --list

# List all channels for the root user
sudo nix-channel --list
```

## add

- Add a new channel

```shell
# uses name "nixpkgs" by default
nix-channel --add "https://nixos.org/channels/nixpkgs-unstable"

# specify name manually
nix-channel --add "https://nixos.org/channels/nixos-unstable" nixos
```

## update

- Update channels

```shell
nix-channel --update
```

## remove

- Remove channel

```shell
nix-channel --remove nixpkgs
```
