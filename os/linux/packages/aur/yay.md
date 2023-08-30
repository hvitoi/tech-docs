# yay

```shell
yay -Syu # All options are forwarded to pacman and additionally includes aur
yay # same as above
```

## Operation: yay

- `--yay`/`-Y`

```shell
yay -Y "proton-ge" # search for packages given a keyword (includes aur packages)
yay "proton-ge" # same as above

# Auto update -git packages
yay -Y --gendb #
yay --devel
```

## Operation: build

- `--build`/`-B`

```shell
# Build and install a PKGBUILD in a folder
yay -Bi .
```

## Operation: show

- `--show`/`-P`

```shell
# display all packages and respective repo
yay -Pc
```

## Operation: getpkgbuild

- `--getpkgbuild`/`-G`

```shell
# Print pkgbuild
yay -Gp
```

## Operation: web

- `--web`/`-w`

```shell
# vote for a package
yay -Wv "package"
```

## Permanent options

```shell
# Also updates -git packages
yay -Y --gendb
yay --devel

# Saves this behavior to the config file
yay -save --devel
```
