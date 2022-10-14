# brcmfmac

- Wifi

```shell
mkdir -p "/lib/firmware/brcm"
cp "./firmware/*" "/lib/firmware/brcm"
modprobe -r "brcmfmac" && modprobe "brcmfmac"
```

## MacOS

- Get driver information on Macos

```shell
# get the loaded wifi drivers
ioreg -l | grep RequestedFiles

({"Firmware"="C-4364__s-B3/bali.trx",
  "TxCap"="C-4364__s-B3/bali-X0.txcb",
  "Regulatory"="C-4364__s-B3/bali-X0.clmb",
  "NVRAM"="C-4364__s-B3/P-bali-X0_M-HRPN_V-u__m-7.7.txt"})
```

```shell
# get the loaded wifi drivers (alternative)
/usr/libexec/wifiFirmwareLoader -f

> Resolved to Firmware file path: "/usr/share/firmware/wifi/C-4364__s-B3/bali.trx"
> Resolved to NVRAM file path: "/usr/share/firmware/wifi/C-4364__s-B3/P-bali-X0_M-HRPN_V-u__m-7.7.txt"
> Resolved to Regulatory file path: "/usr/share/firmware/wifi/C-4364__s-B3/bali-X0.clmb"
> Resolved to TxCap file path: "/usr/share/firmware/wifi/C-4364__s-B3/bali-X0.txcb"
```

## Linux

```txt
brcmfmac4364b3-pcie.apple,bali.bin
brcmfmac4364b3-pcie.apple,bali.clm_blob
brcmfmac4364b3-pcie.apple,bali-HRPN-m-7.9.txt
brcmfmac4364b3-pcie.apple,bali-HRPN-u-7.7.txt
brcmfmac4364b3-pcie.apple,bali.txcap_blob
```

```shell
ln -s -f "/lib/firmware/brcm/brcmfmac4364b3-pcie.apple,bali.bin" "/lib/firmware/brcm/brcmfmac4364-pcie.bin"
ln -s -f "/lib/firmware/brcm/brcmfmac4364b3-pcie.apple,bali.clm_blob" "/lib/firmware/brcm/brcmfmac4364-pcie.clm_blob"
ln -s -f "/lib/firmware/brcm/brcmfmac4364b3-pcie.apple,bali-HRPN-u-7.7.txt" "/lib/firmware/brcm/brcmfmac4364-pcie.Apple Inc.-iMac19,2.txt"
```
