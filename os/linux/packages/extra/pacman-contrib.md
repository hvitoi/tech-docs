# pacman-contrib

## pactree

```shell
# Dependencies of linux package
pactree "linux" -scu

# Packages that depends on linux package
pactree "linux" -scur
```

## paclist

```shell
# Find installed packages from a given repository
paclist "multilib"
```

## paccache

- Cache packages are stored at `/var/cache/pacman/pkg`
- Requires the `pacman-contrib` package in order to clean pacman cache

```shell
paccache -r
pacman -Sc # more aggressive (doesn't keep old versions)
```
