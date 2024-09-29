{ config, lib, pkgs, ... }:
{
  # modules that not only install but also configure a software
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
