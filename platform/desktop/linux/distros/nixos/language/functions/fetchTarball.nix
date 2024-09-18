let
  # pin nixpkgs to a specific release
  nixpkgs = fetchTarball "https://github.com/NixOS/nixpkgs/tarball/nixos-24.05";

  # import nixpkgs and explicitly set "config" and "overlays" to avoid overrides by global config
  pkgs = import nixpkgs { config = { }; overlays = [ ]; };
in
