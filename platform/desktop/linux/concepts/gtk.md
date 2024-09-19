# GTK

- GKT is a `widget toolkit` for building GUI applications
- GTK will default to the Wayland backend
  - Override it to Xwayland by modifying the environment variable: `GDK_BACKEND=x11`

## Configuration

### GTK3

```shell
# Force GTK3 dark mode using environment variable (not recommended)
GTK_THEME="Adwaita:dark" nautilus
```

```ini
# /etc/gtk-3.0/settings.ini
# ~/.config/gtk-3.0/settings.ini
[Settings]
gtk-application-prefer-dark-theme = true
```

### GTK4

```shell
gsettings set \
  org.gnome.desktop.interface \
  color-scheme prefer-dark
```
