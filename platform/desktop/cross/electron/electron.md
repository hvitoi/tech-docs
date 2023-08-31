# Electron

- To use electron-based applications natively under Wayland, create or edit the file `${XDG_CONFIG_HOME}/electron-flags.conf` to add the following options.

```conf
# ~/.config/electron-flags.conf
--enable-features=UseOzonePlatform
--ozone-platform=wayland
```
