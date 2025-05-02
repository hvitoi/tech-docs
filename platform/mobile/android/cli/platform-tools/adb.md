# Android Debug Bridge (ADB)

```shell
brew install android-platform-tools
```

## devices

```shell
adb devices
```

## -s (connect)

```shell
adb -s "device-name" reverse "tcp:8081" "tcp:8081"
```

## reboot

```shell
adb reboot bootloader
```

## shell

```shell
# Uninstall an app
adb shell pm uninstall -k com.whatsapp

# Get phone properties (e.g., the architecture - ABI)
adb shell getprop ro.product.cpu.abi
```

## install

```shell
# Install app from apk
adb install -r -d myapp.apk
```

## push

```shell
adb push "elementalx.zip" "/sdcard/"
adb push "supersu.zip" "/sdcard/"
```
