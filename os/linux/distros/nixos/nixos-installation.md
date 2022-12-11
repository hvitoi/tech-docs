# NixOS installation

- Installation page <https://nixos.org/manual/nixos/stable/>

## Partitioning

```shell
# log in as root
sudo -i

# create boot + root partition
cfdisk
```

## Formatting

```shell
mkfs.ext4 "/dev/vda2" -L "my-nix"
mkfs.fat "/dev/vda1" -F 32 -n "my-boot"
```

## Mounting

```shell
# mount the root partition
mount "/dev/vda2" "/mnt"

# mount the boot partition
mount "/dev/vda1" "/mnt/boot" --mkdir
```

## Nix configuration

```shell
# creates "configuration.nix" and "hardware-configuration.nix" at /etc/nixos
nixos-generate-config --root "/mnt"
```

```shell
nixos-install
```
