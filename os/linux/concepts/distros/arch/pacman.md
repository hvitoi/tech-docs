# pacman

- Pacman settings: `/etc/pacman.conf`
- Pacman logs: `/var/log/pacman.log`

- **Mirrors**
  - Mirrorlist stored at `/etc/pacman.d/mirrorlist`
  - Official list is available from the package `pacman-mirrorlist`

## Query

```shell
# Query all packages
pacman --query
pacman -Q

# Explicitly installed
pacman -Qe

# Installed as dependency
pacman -Qd

# Installed as dependency and not required anymore
pacman -Qdt
pacman -Qdtt # plus optional deps

# AUR packages (foreign)
pacman -Qm

# Info about a package
pacman -Qi "package"

# List outdated packages
pacman -Qu
```

## Sync

```shell
# Install package
pacman --sync "package"
pacman -S "package"

# Refresh package database from server
pacman -Sy
pacman -Syy # force download (even if up to date)

# Upgrade installed packages
pacman -Su
pacman -Syu # update & upgrade

# Search package on remote repo
pacman -Ss "regex-package"
```

## Remove

```shell
# Remove package
pacman -R "package"

# Remove configuration files
pacman -Rn "package"

# Remove unnecessary dependencies
pacman -Rs "package"

# Cascade (remove all packages that depend on them)
pacman -Rc "package"
```

## Modify

```shell
# Downgrade a kernel
pacman -U "linux-4.15.8-1-x86_64.pkg.tar.xz"
```

## IgnorePkg

- Skip package from being upgraded
- Add the packages to the at `/etc/pacman.conf`

```conf
IgnorePkg=linux
```

## Last Modified packages

```shell
grep -iE 'installed|upgraded|removed' /var/log/pacman.log
```

## Cache

- Cache packages are stored at `/var/cache/pacman/pkg`
- Requires the `pacman-contrib` package in order to clean pacman cache

```shell
paccache -r
pacman -Sc # more aggressive (doesn't keep old versions)
```

## Database

```shell
# update database
pacman -Fy

# search package by file
pacman -F $(which chsh)
```

## makepkg

- Build user package in Archlinux
- Requires package `base-devel`

```shell
git clone https://aur.archlinux.org/google-chrome.git
cd google-chrome/
makepkg -s # Creates pacman package
sudo pacman -U pacote.pkg.tar.xz # Install package

# Make and install
makepkg -si
```

```shell
makepkg --syncdeps --rmdeps --clean --install --cleanbuild
makepkg -srciC
```
