# dbus-run-session

```shell
# manually run a wayland session
XDG_SESSION_TYPE=wayland dbus-run-session gnome-session

# same
if [[ -z $DISPLAY && $(tty) == /dev/tty1 && $XDG_SESSION_TYPE == tty ]]; then
  MOZ_ENABLE_WAYLAND=1 QT_QPA_PLATFORM=wayland XDG_SESSION_TYPE=wayland exec dbus-run-session gnome-session
fi
```
