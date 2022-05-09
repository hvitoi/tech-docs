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
