# fastboot

```shell
brew install android-platform-tools
```

## devices

```shell
fastboot devices
```

## oem

- Unlock bootloader

```shell
fastboot oem unlock
```

## flash

```shell
fastboot flash bootloader "bootloader.img"
fastboot flash radio "radio.img"
fastboot flash cache "cache.img"
fastboot flash boot "boot.img"
fastboot flash recovery "recovery.img"
fastboot flash system "system.img"
fastboot flash recovery "twrp.img"
```

## update

- Just like a flash, but pick all the imgs to be flashed from a zip

```shell
fastboot update "image-hammerhead-mra58k.zip"
```

## reboot-bootloader

```shell
fastboot reboot-bootloader
```
