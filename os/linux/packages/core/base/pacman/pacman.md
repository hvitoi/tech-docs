# pacman

- Pacman settings: `/etc/pacman.conf`
- Pacman logs: `/var/log/pacman.log`

- **Mirrors**
  - Mirrorlist stored at `/etc/pacman.d/mirrorlist`
  - Official list is available from the package `pacman-mirrorlist`
- **Last Modified packages**
  - `grep -iE 'installed|upgraded|removed' /var/log/pacman.log`

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

# remove cache
pacman -Sc # doesn't keep old versions
```

## Remove

```shell
# Remove package
pacman --remove "package"
pacman -R "package"

# Remove configuration files
pacman -Rn "package"

# Remove unnecessary dependencies
pacman -Rs "package"

# Cascade (remove all packages that depend on them)
pacman -Rc "package"
```

## Upgrade

```shell
# Downgrade a kernel
pacman --upgrade "linux-4.15.8-1-x86_64.pkg.tar.xz"
pacman -U "linux-4.15.8-1-x86_64.pkg.tar.xz"
```

## Files

```shell
# refresh package databases from the server
pacman -Fy

# search for a package by file
pacman --files "file"
pacman -F "file"

# list all files by a package
pacman -Fl "package"
```

## makepkg

- Build user package in Archlinux
- Requires package `base-devel`

```shell
git clone "https://aur.archlinux.org/google-chrome.git"
cd "./google-chrome/"
makepkg -s # Creates pacman package
pacman -U" pacote.pkg.tar.xz" # Install package

# Make and install
makepkg -si
```

```shell
makepkg --syncdeps --rmdeps --clean --install --cleanbuild
makepkg -srciC
```

## pacman.conf

- Skip package from being upgraded
- Add the packages to the at `/etc/pacman.conf`

```conf
IgnorePkg=linux
```
