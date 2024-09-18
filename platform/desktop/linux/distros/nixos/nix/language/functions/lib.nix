{ config, lib, pkgs, ... }:

{
  # mkDefault
  networking.useDHCP = lib.mkDefault true;
  networking.interfaces.wlan0.useDHCP = lib.mkDefault true;
}
