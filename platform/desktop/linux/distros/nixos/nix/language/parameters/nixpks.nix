{ config, lib, pkgs, ... }:

{
  # vscode, spotify, etc
  nixpkgs.config.allowUnfree = true;

  nixpkgs.hostPlatform = lib.mkDefault "aarch64-linux";
}
