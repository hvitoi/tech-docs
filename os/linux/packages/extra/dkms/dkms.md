# dkms

- Install a dkms
- A `dkms` is installed at `/usr/src`

## status

- Show installed dkms

```sh
dkms status
```

## install

```sh
dkms install "."
dkms install "rtl8188gu/r14.23b04ff" \
  --no-depmod \
  -k "5.18.14-arch1-1"
```

## uninstall

```sh
dkms uninstall -m "rtl8188gu/1.0"
```

## remove

```sh
sudo dkms remove "apple-bce/0.2" --all # remove from all kernel versions
sudo dkms remove "apple-bce/0.2" -k "6.0.1-arch1-1" # remove from a specific kernel only

# clean up folders
rm -rf "apple-bce-0.2"
```

## unbuild

```sh
dkms unbuild -m "apple-gmux/yourversion"
```
