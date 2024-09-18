{ config, lib, pkgs, ... }:
{
  programs = {
    hyprland.enable = true;
    firefox.enable = true;
    git.enable = true;
    fish.enable = true;
    programs.gnupg.agent = {
      enable = true;
      enableSSHSupport = true;
    };
  };
}
