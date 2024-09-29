{ config, lib, pkgs, ... }:

{
  nixpkgs = {
    # vscode, spotify, etc
    config.allowUnfree = true;

    # architecture
    hostPlatform = lib.mkDefault "aarch64-linux";
  };
}
