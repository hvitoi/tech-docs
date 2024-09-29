{ config, lib, pkgs, modulesPath, ... }:

{
  # mount filesystems
  # the device must be already unlocked
  # check boot.initrd.luks options for unlocking
  fileSystems = {
    "/" = {
      device = "/dev/disk/by-label/AESTHETIC";
      fsType = "ext4";
    };
    "/boot" = {
      device = "/dev/disk/by-label/ESP";
      fsType = "vfat";
      options = [ "fmask=0022" "dmask=0022" ];
    };
  };
}
