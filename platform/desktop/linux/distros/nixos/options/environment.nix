{ config, lib, pkgs, ... }:

{
  environment = {
    # packages installed on the system
    systemPackages = with pkgs; [
      ranger
      neovim
      kitty
    ];

    # environment variables
    FOO = "BAR";
    PATH = [ "path/hi/mom" "$HOME/bin" ];

    # session variables
    sessionVariables.NIXOS_OZONE_WL = "1";
  };

}
