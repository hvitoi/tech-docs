# QT

- QT is a `widget toolkit` for building GUI applications

- `QT6`: qt6-base
- `QT5`: qt5-base
- `QT4`: qt4 (aur)
- `QT3`: qt3 (aur)

## Configuration

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

## Decoration plugin

- Decoration plugin

- `QGtkStyle`
- `QGnomePlatform` (deprecated)
- `QAdwaitaDecorations` (under development)
