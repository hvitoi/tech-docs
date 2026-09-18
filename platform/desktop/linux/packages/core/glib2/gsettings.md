# gsettings

- Write changes to `dconf` database
- It's a wrapper over `dconf`

## org.gnome.shell

```shell
gsettings set \
  org.gnome.shell \
  disable-user-extensions false

gsettings get \
  org.gnome.shell enabled-extensions
```

## org.gnome.desktop.interface

```shell
gsettings set \
  org.gnome.desktop.interface \
  clock-show-date true

gsettings set \
  org.gnome.desktop.interface \
  gtk-theme theme-name

gsettings set \
  org.gnome.desktop.interface \
  icon-theme theme-name

gsettings set \
  org.gnome.desktop.interface \
  color-scheme prefer-dark # dark mode
```

## org.gnome.desktop.calendar

```shell
gsettings set \
  org.gnome.desktop.calendar \
  show-weekdate true
```

## org.gnome.desktop.peripherals.touchpad

```shell
gsettings range \
  org.gnome.desktop.peripherals.touchpad \
  click-method

gsettings set \
  org.gnome.desktop.peripherals.touchpad \
  click-method fingers
```

## org.gnome.desktop.input-sources

```shell
gsettings set org.gnome.desktop.input-sources sources "[('xkb', 'us'), ('xkb', 'us+intl')]"
```

## org.gnome.settings-daemon.plugins.color

```shell
gsettings set \
  org.gnome.settings-daemon.plugins.color \
  night-light-temperature 5000
```
