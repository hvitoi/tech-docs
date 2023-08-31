# GTK

- GKT is a `widget toolkit` for building GUI applications

## Configuration

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
