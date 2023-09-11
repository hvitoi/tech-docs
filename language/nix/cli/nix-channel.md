# nix-channel

- Nixpkgs channels (repo)
  - `nixos`: <https://nixos.org/channels/nixos-22.11>
  - `nixos-unstable`: <https://nixos.org/channels/nixpkgs-unstable>

```shell
# List all channels
nix-channel --list
sudo nix-channel --list # channels defined by the root user

# Add a new channel
nix-channel --add "https://nixos.org/channels/nixpkgs-unstable" # uses name "nixpkgs" by default
nix-channel --add "https://nixos.org/channels/nixos-unstable" nixos # specify name manually

# update channel
nix-channel --update

# remove channel
nix-channel --remove nixpkgs
```
