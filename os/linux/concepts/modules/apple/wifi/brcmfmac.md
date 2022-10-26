# brcmfmac

- Wifi

```sh
mkdir -p "/lib/firmware/brcm"
cp "./firmware/*" "/lib/firmware/brcm"
modprobe -r "brcmfmac" && modprobe "brcmfmac"
```

## MacOS

- Get driver information on Macos

```sh
# get the loaded wifi drivers
ioreg -l | grep RequestedFiles

> ({"Firmware"="C-4364__s-B3/bali.trx",
>   "TxCap"="C-4364__s-B3/bali-X0.txcb",
>   "Regulatory"="C-4364__s-B3/bali-X0.clmb",
>   "NVRAM"="C-4364__s-B3/P-bali-X0_M-HRPN_V-u__m-7.7.txt"})
```

```sh
# get the loaded wifi drivers (alternative)
/usr/libexec/wifiFirmwareLoader -f

> Resolved to Firmware file path: "/usr/share/firmware/wifi/C-4364__s-B3/bali.trx"
> Resolved to NVRAM file path: "/usr/share/firmware/wifi/C-4364__s-B3/P-bali-X0_M-HRPN_V-u__m-7.7.txt"
> Resolved to Regulatory file path: "/usr/share/firmware/wifi/C-4364__s-B3/bali-X0.clmb"
> Resolved to TxCap file path: "/usr/share/firmware/wifi/C-4364__s-B3/bali-X0.txcb"
```

```sh
# Copy mac firmware folder
(cd "/usr/share" && tar -czvf "./apple-firmware.tar.gz" "firmware")
```

## Linux

```sh
# get module error logs
journalctl -k --grep=brcmfmac
```

```sh
# copy mac firmware into linux
cp "bali.trx" "/lib/firmware/brcm/brcmfmac4364-pcie.bin"
cp "P-bali-X0_M-HRPN_V-u__m-7.7.txt" "/lib/firmware/brcm/brcmfmac4364-pcie.Apple Inc.-MacBookPro16,1.txt"
cp "bali-X0.clmb" "/lib/firmware/brcm/brcmfmac4364-pcie.clm_blob"
cp "bali-X0.txcb" "/lib/firmware/brcm/brcmfmac4364-pcie.txcb"
```

```txt
brcmfmac4364b3-pcie.apple,bali.bin
brcmfmac4364b3-pcie.apple,bali.clm_blob
brcmfmac4364b3-pcie.apple,bali-HRPN-m-7.9.txt
brcmfmac4364b3-pcie.apple,bali-HRPN-u-7.7.txt
brcmfmac4364b3-pcie.apple,bali.txcap_blob
```

```sh
ln -s -f "/lib/firmware/brcm/brcmfmac4364b3-pcie.apple,bali.bin" "/lib/firmware/brcm/brcmfmac4364-pcie.bin"
ln -s -f "/lib/firmware/brcm/brcmfmac4364b3-pcie.apple,bali.clm_blob" "/lib/firmware/brcm/brcmfmac4364-pcie.clm_blob"
ln -s -f "/lib/firmware/brcm/brcmfmac4364b3-pcie.apple,bali-HRPN-u-7.7.txt" "/lib/firmware/brcm/brcmfmac4364-pcie.Apple Inc.-iMac19,2.txt"
```
