# brcmfmac

- Wifi

```shell
sudo mkdir -p "/lib/firmware/brcm"
sudo cp "./firmware/*" "/lib/firmware/brcm"
sudo modprobe -r "brcmfmac" && sudo modprobe "brcmfmac"
```
