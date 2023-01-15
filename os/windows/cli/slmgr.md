# slmgr

- `Software Licensing Manager`
- Get the `Product Key Channel`
  - `RETAIL`: the most flexible type of key. Possible to be transferred to another machine
  - `OEM_DM`: purchased by manufacturers. Tied to the hardware/motherboard
  - `VOLUME_MAK`
  - `VOLUME_KMSCLIENT`: kms activators

```powershell
# basic licensing information
slmgr /dli

# how long the activation is valid for
slmgr /xpr
```

## vbs

```powershell
# get the key type
slmgr.vbs /dlv

# deactivate the license key on the machine
slmgr.vbs /upk

# remove key from the registry
slmgr.vbs /cpky

# activate key (on a new machine)
slmgr.vbs /ipk "product-key"
```
