# paccache

- Cache packages are stored at `/var/cache/pacman/pkg`
- Requires the `pacman-contrib` package in order to clean pacman cache

```shell
paccache -r
pacman -Sc # more aggressive (doesn't keep old versions)
```
