# import nixpkgs package set
{ pkgs ? import <nixpkgs> { } }:

pkgs.mkShell {
  # mkShell is a helper function
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
