# Theming

## Widget Toolkits

### GTK

#### Configuration GTK

- **Dark Mode**

- For GTK3 apps

```conf
# Force GTK3 dark mode (not recommended)
GTK_THEME=Adwaita:dark
```

```ini
# /etc/gtk-3.0/settings.ini
[Settings]
gtk-application-prefer-dark-theme = true
```

- For GTK4 apps

```shell
gsettings set \
  org.gnome.desktop.interface \
  color-scheme prefer-dark # dark mode
```

### QT

- `QT6`: qt6-base
- `QT5`: qt5-base
- `QT4`: qt4 (aur)
- `QT3`: qt3 (aur)

#### Configuration QT

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

## Styles

### Breeze

- Default QT style on KDE

- Ports

  - `GTK3`, `GTK2`: breeze-gtk

  - `QT6`, `QT5`: breeze
  - `QT4`: breeze-kde4 (aur)

### Adwaita

- Default GTK style on gnome

- Ports
  - `GTK3`: gtk3
  - `GTK2`: gnome-themes-extra
  - `QT6`: adwaita-qt6-git (aur)
  - `QT5`: adwaita-qt5-git (aur)
  - `QT4`: adwaita-qt4 (aur)

## Fusion

- Default QT style

## Decorations

- Decoration plugin

- `QGtkStyle`
- `QGnomePlatform` (deprecated)
- `QAdwaitaDecorations` (under development)
