{ pkgs ? import <nixpkgs> { system = "x86_64-linux"; } }:

pkgs.dockerTools.buildLayeredImage {
  # image name (to be built)
  name = "nix-redis";

  # image tag (to be built)
  tag = "latest";

  # packages in the docker image
  contents = [ pkgs.redis ];
}
