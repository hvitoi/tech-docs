# Multimedia

## Codecs

- Install Fusion (free & nonfree) repos first

```shell
# Audio & Video codecs (add RPM fusion repos first)
dnf group install --with-optional "multimedia"
dnf group install --with-optional "sound-and-video"
```

## DRM content

- Installs `Widevine Content Decryption Module` for aarch64 systems

```shell
sudo widevine-installer
```
