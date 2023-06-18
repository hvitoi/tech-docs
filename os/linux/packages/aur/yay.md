# yay

```shell
yay -Syu # All options are forwarded to pacman and additionally includes aur
yay # same as above
```

## Operation: yay

- `--yay`/`-Y` operation

```shell
yay -Y "proton-ge" # search the keyword including in aur
yay "proton-ge" # same as above
```

## Operation: show

- `--show`/`-P`

```shell
# display all packages and respective repo
yay -Pc
```

## Operation: build

- `--build`/`-B`

```shell
# Build and install a PKGBUILD in a folder
yay -Bi .
```

## Operation: getpkgbuild

- `--getpkgbuild`/`-G`

```shell
# Print pkgbuild
yay -Gp
```
