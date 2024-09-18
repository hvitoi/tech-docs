{ config, lib, pkgs, modulesPath, ... }:

{
  imports =
    [
      ./hardware-configuration.nix
      <apple-silicon-support/apple-silicon-support>
      (modulesPath + "/installer/scan/not-detected.nix")
    ];
}
