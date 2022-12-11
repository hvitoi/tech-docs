# nix-channel

- `nixos`: <https://nixos.org/channels/nixos-22.11>
- `nixos-unstable`: <https://nixos.org/channels/nixpkgs-unstable>

```shell
# List all channels (repos)
nix-channel --list

# Switch to another nix channel
nix-channel --add "https://nixos.org/channels/nixos-unstable" nixos

# Uses name "nixpkgs" by default
nix-channel --add "https://nixos.org/channels/nixpkgs-unstable"

# update channel
nix-channel --update
```
