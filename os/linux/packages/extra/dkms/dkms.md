# dkms

- Install a dkms
- A `dkms` is installed at `/usr/src`

## status

- Show installed dkms

```shell
dkms status
```

## install

```shell
dkms install "."
dkms install \
  --no-depmod "rtl8188gu/r14.23b04ff" \
  -k "5.18.14-arch1-1"
```

## uninstall

```shell
dkms uninstall -m "rtl8188gu/1.0"
```
