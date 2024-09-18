let
  nixpkgs = fetchTarball "https://github.com/NixOS/nixpkgs/tarball/nixos-24.05";
  pkgs = import nixpkgs { config = { }; overlays = [ ]; };
in

# construct a shell environment without a compiler toolchain
pkgs.mkShellNoCC {

  # packages available in the shell environment
  packages = with pkgs; [
    cowsay
    lolcat
  ];

  # any other attribute that is not reserved end up as a environment variable in the shell
  GREETING = "Hello!";

  # command to run before entering the shell
  shellHook = ''
    echo $GREETING | cowsay | lolcat
  '';
}
