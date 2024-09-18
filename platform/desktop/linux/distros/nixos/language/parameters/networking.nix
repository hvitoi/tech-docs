{ config, lib, pkgs, ... }:

{

  networking = {
    hostName = "nixos";

    # Pick only one of the below networking options.
    networkmanager.enable = true; # Easiest to use and most distros use this by default
    wireless.enable = true; # Enables wireless support via wpa_supplicant
    wireless.iwd = {
      enable = true; # Enables wireless support via iwd
      settings.General.EnableNetworkConfiguration = true;
    };

    # Configure network proxy if necessary
    proxy.default = "http://user:password@proxy:port/";
    proxy.noProxy = "127.0.0.1,localhost,internal.domain";

    # Open ports in the firewall.
    firewall = {
      allowedTCPPorts = [ "..." ];
      allowedUDPPorts = [ "..." ];
      enable = false; # Or disable the firewall altogether
    };


    # Enables DHCP on each ethernet and wireless interface. In case of scripted networking
    # (the default) this is the recommended approach. When using systemd-networkd it's
    # still possible to use this option, but it's recommended to use it in conjunction
    # with explicit per-interface declarations with `networking.interfaces.<interface>.useDHCP`.
    useDHCP = lib.mkDefault true;
    interfaces.wlan0.useDHCP = lib.mkDefault true;
  };
}
