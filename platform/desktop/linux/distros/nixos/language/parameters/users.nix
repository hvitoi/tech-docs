{ config, lib, pkgs, ... }:

{
  # Define a user account. Don't forget to set a password with "passwd"
  users.users.john = {
    isNormalUser = true;
    extraGroups = [ "wheel" ]; # Enable ‘sudo’ for the user
    shell = pkgs.fish; # default shell
    packages = with pkgs; [
      firefox # user packages
    ];
  };
}

