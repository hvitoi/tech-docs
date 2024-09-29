{ config, lib, pkgs, ... }:

{
  users = {

    # Define a user account. Don't forget to set a password with "passwd"
    users.john = {
      isNormalUser = true;
      home = "/home/john";
      extraGroups = [ "wheel" ]; # Enable ‘sudo’ for the user
      shell = pkgs.fish; # default shell
      packages = with pkgs; [
        firefox # user packages
      ];
      openssh.authorizedKeys.keys = [
        "ssh-rsa AAAAbbb...."
      ];
    };

    extraGroups = {
      vboxusers.members = [ "john" ];
    };

  };
}
