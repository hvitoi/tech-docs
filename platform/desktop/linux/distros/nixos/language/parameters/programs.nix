{ config, lib, pkgs, ... }:
{
  programs = {
    hyprland.enable = true;
    firefox.enable = true;
    git.enable = true;
    fish.enable = true;
    gnupg.agent = {
      enable = true;
      enableSSHSupport = true;
    };
  };
}
