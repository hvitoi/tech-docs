# config

- Show current flutter config
- Modify flutter config

```shell
# show all custom configs
flutter config
```

## android studio

```shell
# android studio path
flutter config --android-studio-dir "/var/lib/flatpak/app/com.google.AndroidStudio/current/active/files/extra/android-studio" # flatpak installation
flutter config --android-studio-dir "/Applications/Android Studio.app/Contents" # brew installation
```

## android sdk

```shell
# android sdk path
flutter config --android-sdk "~/android-sdk"
```

## flutter desktop

- Enable flutter desktop support
- This will create a new device

```shell
# macos
flutter config --enable-macos-desktop

# linux
flutter config --enable-linux-desktop
```
