{ config, lib, pkgs, ... }:

{
  console = {
    # Select internationalisation properties.
    font = "Lat2-Terminus16";
    keyMap = "us";
    useXkbConfig = true; # use xkb.options in tty.
  };
}
