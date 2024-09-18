{ config, lib, pkgs, ... }:

{
  hardware.bluetooth.enable = true;
  hardware.bluetooth.powerOnBoot = true;
  hardware.pulseaudio.enable = true;

  # Asahi Linux
  hardware = {
    asahi = {
      enable = true;
      peripheralFirmwareDirectory = ./firmware;
      useExperimentalGPUDriver = true;
      experimentalGPUInstallMode = "replace";
      setupAsahiSound = true;
    };
  };

}
