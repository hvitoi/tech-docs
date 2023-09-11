# nix-build

```shell
# Booting from “netboot” media (PXE)
nix-build -A netboot.x86_64-linux '<nixpkgs/nixos/release.nix>'
```

## Built from nix file

```nix
{ pkgs ? import <nixpkgs> { system = "x86_64-linux"; }
}:

# docker helper function
pkgs.dockerTools.buildLayeredImage {
  name="nix-redis"; # image name (to be built)
  tag = "latest"; # image tag (to be built)
  contents = [ pkgs.redis ]; # packages in the docker image
}
```

```shell
# build docker image into a file
nix-build "docker-environment.nix" -o "./my-image"

# ...
docker load -i "./my-image"
docker images
```
