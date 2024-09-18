{ config, lib, pkgs, ... }:

{
  # packages installed on the system
  environment.systemPackages = with pkgs; [
    ranger
    neovim
    kitty
  ];

  # environment variables
  environment.sessionVariables.NIXOS_OZONE_WL = "1";
}
