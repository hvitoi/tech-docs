# pkgutil

## pkgs

```shell
# List installed packages
pkgutil --pkgs
```

## files

- List files of a given package

```shell
pkgutil --files com.apple.pkg.BaseSystemBinaries
```

## file-info

- Discover what package a file belongs to
- Does not work for MacOS Sonoma or higher

```shell
pkgutil --file-info /usr/bin/less
```

## pkg-info

```shell
# Package information
pkgutil --pkg-info the-package-name.pkg
```

## forget

```shell
# Forget a package from the list
pkgutil --forget com.example.package
```
