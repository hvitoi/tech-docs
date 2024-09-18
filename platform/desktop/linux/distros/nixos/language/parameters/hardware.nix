{ config, lib, pkgs, ... }:

{
  hardware = {
    bluetooth = {
      bluetooth.enable = true;
      bluetooth.powerOnBoot = true;
    };

    pulseaudio.enable = true;

    # Asahi Linux
    asahi = {
      enable = true;
      peripheralFirmwareDirectory = ./firmware;
      useExperimentalGPUDriver = true;
      experimentalGPUInstallMode = "replace";
      setupAsahiSound = true;
    };
  };
}
