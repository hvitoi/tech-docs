# import nixpkgs package set
{ pkgs ? import <nixpkgs> { } }:

# construct a shell environment with compiler toolchain (make, gcc, etc)
pkgs.mkShell {
  name = "dev-environment";

  # list of pakcages to be installed in the virtual shell
  buildInputs = [
    pkgs.nodejs
    pkgs.python3
  ];

  # Command to run when entering the environment
  shellHook = ''
    echo "Starting the development environment"
  '';
}
