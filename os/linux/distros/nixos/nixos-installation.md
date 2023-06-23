# NixOS installation

- Installation page <https://nixos.org/manual/nixos/stable/>

```shell
# log in as root
sudo -i
```

## Wifi

```shell
sudo mkdir -p /lib/firmware
tar -xvf apple-wifi-firmware.tar -C /lib/firmware
sudo modprobe -r brcmfmac && sudo modprobe brcmfmac
```

```shell
systemctl start wpa_supplicant
wpa_cli
```

## Mounting

```shell
cryptsetup open "/dev/sdxN" "foo"
mount "/dev/mapper/foo" "/mnt" -o "compress=zstd,subvol=@"
mount -m "/dev/mapper/foo" "/mnt/home" -o "compress=zstd,subvol=@home"
mount -m "/dev/sdx1" "/mnt/boot"
```

## Nix configuration

```shell
# creates "configuration.nix" and "hardware-configuration.nix" at /etc/nixos
nixos-generate-config --root "/mnt"
```

```nix
{ config, pkgs, ... }: {
  imports = [
    "${builtins.fetchGit { url = "https://github.com/kekrby/nixos-hardware.git"; }}/apple/t2"
  ];
  hardware.firmware = [
    (pkgs.stdenvNoCC.mkDerivation {
      name = "brcm-firmware";

      buildCommand = ''
        dir="$out/lib/firmware"
        mkdir -p "$dir"
        cp -r ${./files/firmware}/* "$dir"
      '';
    })
  ];
  programs.hyprland.enable = true;
}

```

```shell
nixos-install
```
