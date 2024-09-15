# Asahi

- On Apple Silicon systems, external boot is not support on the native boot tooling (`iBoot`)
- Therefore some tools are necessary to provide a PC-like boot environment

## Installation

```shell
curl -L https://alx.sh/dev | sh
```

## Partition configuration

```conf
/dev/disk0 (internal, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      GUID_partition_scheme                        *500.3 GB   disk0
   1:             Apple_APFS_ISC Container disk1         524.3 MB   disk0s1
   2:                 Apple_APFS Container disk4         430.0 GB   disk0s2
   3:                 Apple_APFS Container disk2         2.5 GB     disk0s3
   4:                        EFI ESP                     524.3 MB   disk0s4
   5:           Linux Filesystem                         1.1 GB     disk0s5
   6:           Linux Filesystem                         60.3 GB    disk0s6
   7:        Apple_APFS_Recovery Container disk3         5.4 GB     disk0s7

/dev/disk2 (synthesized):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      APFS Container Scheme -                      +2.5 GB     disk2
                                 Physical Store disk0s3
   1:                APFS Volume Fedora - Data           5.3 MB     disk2s1
   2:                APFS Volume Fedora                  1.1 MB     disk2s2
   3:                APFS Volume Preboot                 134.2 MB   disk2s3
```

## m1n1

- It's a bridge between Apple's boot firmware (iBoot) and the Linux world
- m1n1 is installed as a `faux macOS kernel` into a `stub macOS installation`.

### Stage 1

- MacOS stub

### Stage 2

- Provides a preboot environment
- Loads to UEFI binary
- Uses U-Boot by default

## U-Boot

- U-Boot is loaded by m1n1
- It's used to set up a standard UEFI environment from which GRUB, systemd-boot, etc can be booted
- It loads and executes a UEFI binary located at `/EFI/BOOT/BOOTAA64.EFI` at the EFI partition
- Due to the limitations of the Apple boot picker (iBoot), there must be one EFI system partition per installed OS.

```shell
# boot from usb
env set boot_efi_bootmgr ; run bootcmd_usb0

# enter boot menu
bootmenu # select "usb 0" to boot from usb
```
