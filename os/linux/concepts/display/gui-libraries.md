# GUI libraries

## GTK

- GTK will default to the Wayland backend
- Override it to Xwayland by modifying the environment variable: `GDK_BACKEND=x11`

## Qt

- To enable Wayland support in Qt 5 or 6, install the `qt5-wayland` or `qt6-wayland` package

## Electron

- To use electron-based applications natively under Wayland, create or edit the file `${XDG_CONFIG_HOME}/electron-flags.conf` to add the following options.

```conf
# ~/.config/electron-flags.conf
--enable-features=UseOzonePlatform
--ozone-platform=wayland
```
