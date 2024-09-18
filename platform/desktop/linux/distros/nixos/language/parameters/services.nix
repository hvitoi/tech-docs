{ config, lib, pkgs, ... }:

{
  services = {

    xserver = {
      # Enable the X11 windowing system
      enable = true;

      # Configure keymap in X11
      xkb.layout = "us";
      xkb.options = "eurosign:e,caps:escape";

      displayManager = {
        # KDE
        sddm.enable = true;

        autoLogin.enable = true;
        autoLogin.user = "john";

      };

      desktopManager = {
        # KDE
        plasma5.enable = true;
      };

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
