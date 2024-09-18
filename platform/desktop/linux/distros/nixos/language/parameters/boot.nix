{ config, lib, pkgs, ... }:

{
  boot = {
    loader = {
      systemd-boot.enable = true;

      grub = {
        enable = true;
        device = "/dev/vda";
        useOSProber = true;
      };
      efi.canTouchEfiVariables = false;
    };

    initrd = {
      luks.devices."aesthetic".device = "/dev/disk/by-label/AESTHETIC_CRYPT";
      availableKernelModules = [ "usb_storage" "sdhci_pci" ];
      kernelModules = [ ];
    };

    kernelModules = [
      "kvm-intel"
    ];

    extraModulePackages = [ ];

    extraModprobeConfig = ''
      options hid_apple swap_opt_cmd=1 fnmode=2
    '';
  };
}
