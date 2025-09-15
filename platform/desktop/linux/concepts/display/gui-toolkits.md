# GUI toolkits

## GTK

- GKT is a `widget toolkit` for building GUI applications
- GTK will default to the Wayland backend
  - Override it to Xwayland by modifying the environment variable: `GDK_BACKEND=x11`

### Configuration

#### GTK3

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

## QT

- QT is a `widget toolkit` for building GUI applications
- To enable Wayland support in Qt 5 or 6, install the `qt5-wayland` or `qt6-wayland` package

- `QT6`: qt6-base
- `QT5`: qt5-base
- `QT4`: qt4 (aur)
- `QT3`: qt3 (aur)

### Configuration-

```conf
# Set default style/theme
QT_STYLE_OVERRIDE=adwaita-dark
QT_STYLE_OVERRIDE=kvantum
```

```conf
# Set default platform theme
QT_QPA_PLATFORMTHEME=gtk2 # QGtkStyle
QT_QPA_PLATFORMTHEME=gnome # QGnomePlatform
QT_QPA_PLATFORMTHEME=qt5ct
```

```conf
QT_WAYLAND_DECORATION=adwaita # QAdwaitaDecorations
```

### Decoration plugin

- Decoration plugin

- `QGtkStyle`
- `QGnomePlatform` (deprecated)
- `QAdwaitaDecorations` (under development)
