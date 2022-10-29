# Android Debug Bridge (ADB)

## Connect

```sh
adb devices
fastboot devices

# connect
adb -s "device-name" reverse "tcp:8081" "tcp:8081"
```

## Unlock Bootloader

```sh
fastboot oem unlock
adb reboot bootloader
```

## flash

```sh
fastboot flash bootloader "bootloader.img"
fastboot reboot-bootloader

fastboot flash radio "radio.img"
fastboot reboot-bootloader

fastboot flash cache "cache.img"
fastboot flash boot "boot.img"
fastboot flash recovery "recovery.img"
fastboot flash system "system.img"
fastboot update "image-hammerhead-mra58k.zip" # all the previous 4 commands at once
fastboot reboot-bootloader

fastboot flash recovery "twrp.img"
fastboot reboot-bootloader
```

## push

```sh
adb push "elementalx.zip" "/sdcard/"
adb push "supersu.zip" "/sdcard/"
```
