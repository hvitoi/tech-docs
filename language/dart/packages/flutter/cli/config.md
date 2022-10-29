# config

- Show current flutter config
- Modify flutter config

```sh
# show all custom configs
flutter config
```

## android studio

```sh
# android studio path
flutter config --android-studio-dir "/var/lib/flatpak/app/com.google.AndroidStudio/current/active/files/extra/android-studio" # flatpak installation
flutter config --android-studio-dir "/Applications/Android Studio.app/Contents" # brew installation
```

## android sdk

```sh
# android sdk path
flutter config --android-sdk "~/android-sdk"
```

## flutter desktop

- Enable flutter desktop support
- This will create a new device

```sh
# macos
flutter config --enable-macos-desktop

# linux
flutter config --enable-linux-desktop
```
