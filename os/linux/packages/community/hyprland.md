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

### monitors

```shell
hyprctl monitors
```

## keyword

- Submit a keyword command

```shell
hyprctl keyword monitor ',preferred,auto,1'
```
