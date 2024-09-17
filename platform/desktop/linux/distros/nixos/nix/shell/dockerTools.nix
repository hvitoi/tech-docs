{ pkgs ? import <nixpkgs> { system = "x86_64-linux"; } 
}:

# docker helper function
pkgs.dockerTools.buildLayeredImage {
  name="nix-redis"; # image name (to be built)
  tag = "latest"; # image tag (to be built)
  contents = [ pkgs.redis ]; # packages in the docker image
}
