# <nixpkgs> points to the local filesystem path that containg some revisions of nixpkgs (as a tarball)
{ pkgs ? import <nixpkgs> { } }:

# equivalent to the other form
{ pkgs ? import (fetchTarball "https://github.com/NixOS/nixpkgs/archive/06278c77b5d162e62df170fec307e83f1812d94b.tar.gz") { } }:
{ pkgs ? import (fetchTarball "https://github.com/NixOS/nixpkgs/tarball/nixos-24.05") { } }:
