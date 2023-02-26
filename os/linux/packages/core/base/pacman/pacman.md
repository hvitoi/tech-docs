# pacman

- Pacman settings: `/etc/pacman.conf`
- Pacman logs: `/var/log/pacman.log`

- **Mirrors**
  - Mirrorlist stored at `/etc/pacman.d/mirrorlist`
  - Official list is available from the package `pacman-mirrorlist`
- **Last Modified packages**
  - `grep -iE 'installed|upgraded|removed' /var/log/pacman.log`

## Query

- A package on arch is a tarball

```shell
# Query all packages
pacman --query
pacman -Q

# Explicitly installed
pacman -Qe

# Installed as dependency
pacman -Qd
pacman -Qdt  # + unrequired
pacman -Qdtt # + optional deps

# Foreign packages (installed manually, AUR packages or from libraries removed from pacman.conf)
pacman -Qm

# Info about a package
pacman -Qi "package"
pacman -Qip "package.pkg.tar.xz" # query a file directly

# List package files
pacman -Ql "package"
pacman -Qlp "package.pkg.tar.xz" # query a file directly

# List outdated packages
pacman -Qu

# Changelog
pacman -Qc "package"

# Query the package that owns a file
pacman -Qo "file"
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
pacman -Scc # clear also packages that are installed

# List packages in a repo
pacman -Sl "core"
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

## Database

```shell
# test local database
pacman -Dk

# mark a package as explicit installed
pacman -D --asexplicit "package"

# mark a package as dependency
pacman -D --asdeps "package"
```

## pacman.conf

- Skip package from being upgraded
- Add the packages to the at `/etc/pacman.conf`

```conf
IgnorePkg=linux
```
