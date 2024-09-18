{ config, lib, pkgs, ... }:

{
  nixpkgs = {
    # vscode, spotify, etc
    config.allowUnfree = true;

    hostPlatform = lib.mkDefault "aarch64-linux";
  };
}
