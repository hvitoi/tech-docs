# rpm-ostree

- Git for filesystem trees!

- Directories
  - `/var`: mutable and shared among deployments
  - `/etc`: mutable and unique for each deployment. It's copied over the next deployment
  - `/usr`: immutable and unique for each deployment

  - `/sysroot`: the actual raw root mount-point of the HDD, which contains all the deployments
  - `/sysroot/ostree`: Holds the base ostree system
  - `/sysroot/ostree/deploy`: each system version
  - `/sysroot/ostree/var`: shared files
  - `/sysroot/ostree/repo`: shared commit objects (to avoid duplicate files)
- Package install methods
  - `Package layering`: useful for drivers, libvirt, etc
  - `Flatpak`: sandboxed apps
  - `Toolbox`: primarily for CLI apps

## status

- Show all deployments

```shell
rpm-ostree status
```

## update

```shell
# check for updates in the base image
rpm-ostree update --check
```

## upgrade

- A new `etc` directory is copied over to the new system
- Brand new `usr` directories are created
- `var` directory is shared
- Upgrade is automatically done by fedora, but you can do it manually with this command
- Updates the packages in the image

```shell
rpm-ostree upgrade
```

## install

- Install a package as layered image on top of the base image
- Requires reboot

```shell
rpm-ostree install <package>
```

## rebase

- Adopt a new base image

```shell
rpm-ostree rebase <branch>
rpm-ostree rebase fedora:fedora/39/x96_64/kinoite
```

## rollback

- Rollback to a previous deployment

```shell
rpm-ostree rollback
```
