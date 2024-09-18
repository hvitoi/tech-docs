{ config, lib, pkgs, ... }:

{
  networking.hostName = "nixos";

  # Pick only one of the below networking options.
  networking.wireless.enable = true; # Enables wireless support via wpa_supplicant
  networking.wireless.iwd = {
    enable = true; # Enables wireless support via iwd
    settings.General.EnableNetworkConfiguration = true;
  };
  networking.networkmanager.enable = true; # Easiest to use and most distros use this by default

  # Configure network proxy if necessary
  networking.proxy.default = "http://user:password@proxy:port/";
  networking.proxy.noProxy = "127.0.0.1,localhost,internal.domain";

  # Open ports in the firewall.
  networking.firewall.allowedTCPPorts = [ "..." ];
  networking.firewall.allowedUDPPorts = [ "..." ];
  networking.firewall.enable = false; # Or disable the firewall altogether



  # Enables DHCP on each ethernet and wireless interface. In case of scripted networking
  # (the default) this is the recommended approach. When using systemd-networkd it's
  # still possible to use this option, but it's recommended to use it in conjunction
  # with explicit per-interface declarations with `networking.interfaces.<interface>.useDHCP`.
  networking.useDHCP = lib.mkDefault true;
  networking.interfaces.wlan0.useDHCP = lib.mkDefault true;
}
