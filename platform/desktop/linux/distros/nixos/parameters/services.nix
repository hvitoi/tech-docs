{ config, lib, pkgs, ... }:

{
  services = {

    xserver = {
      # Enable the X11 windowing system
      enable = true;

      # Configure keymap in X11
      # Get all available parameters with cat $(nix-build --no-out-link '<nixpkgs>' -A xkeyboard_config)/etc/X11/xkb/rules/base.lst
      xkb = {
        layout = "us,br";
        variant = "intl";
        options = "grp:win_space_toggle";
      };

      displayManager = {
        sddm.enable = true;
      };

      desktopManager = {
        plasma5.enable = true;
      };

    };

    displayManager = {
      autoLogin.enable = true;
      autoLogin.user = "hv";
    };

    # Enable CUPS to print documents
    printing.enable = true;

    # Enable sound
    pipewire = {
      enable = true;
      pulse.enable = true;
    };

    # Enable touchpad support (enabled default in most desktopManager)
    libinput.enable = true;

    # Enable the OpenSSH daemon
    openssh.enable = true;

    # Flatpak
    flatpak.enable = true;

    # Plex
    plex.enable = true;
  };
}
