# hyprland

- **Configuration**

  - `~/.config/hypr/hyprland.conf`
  - `Variables`: configuration variables. e.g., general, animations
  - `Keywords`: commands that define special behaviors. e.g., monitor, exec-once

## hyprctl

## devices

- Show peripheral devices connected
  - `mice`
  - `keyboards`
  - `tablets`
  - `touch`
  - `switches`

```shell
hyprctl devices
```

### clients

- Clients describe the **windows**
- It's every tiled window
- Check which apps are running in xwayland or wayland

```shell
hyprctl clients
```

### layers

- **LayerSurfaces**
  - Wallpapers
  - Notifications
  - Overlays
  - Bars
  - Etc.

```shell
hyprctl layers
```

### workspaces

```shell
hyprctl workspaces
```

### monitors

```shell
hyprctl monitors
```

## keyword

- Submit a keyword command

```shell
hyprctl keyword monitor ',preferred,auto,1'
```

## dispatch

- Issue a dispatch to call a keybind dispatcher with an arg

```shell
hyprctl dispatch exec kitty

hyprctl dispatch -- exec kitty --single-instance
```

## switchxkblayout

```shell
hyprctl switchxkblayout <keyboard> next
```

## notify

```shell
hyprctl notify -1 10000 "rgb(ff1ea3)" "Hello everyone!"
```
