# sway

```sh
pacman -S \
  "sway" \
  "swaylock" \
  "swayidle" \
  "waybar" \
  "dmenu" \
  "alacritty" \
  "grim" \
  "xdg-desktop-portal-wlr" \
  "xorg-xwayland" \
  "ttf-font-awesome" \
  "networkmanager" \
  "bluez"
```

## Configuration file

- `~/.config/sway/config`: Default config file
- To start you can copy the default config from `/etc/sway/config`

## Basic Commands

- `Mod + Shift + C`: restart wayland session
- `Mod + Shift + E`: exit wayland session
- `Mod + Shift + Q`: quit application

- `Mod + Enter`: open new terminal
- `Mod + D`: launcher

- `Mod + Num`: move to workspace
- `Mod + Left/Right`: navigate
- `Mod + Shift + Num`: move the application to a workspace

## swaymsg

```sh
# Get monitor devices
swaymsg --type get_outputs

# Get input devices
swaymsg --type get_inputs

# Execute command
swaymsg -- output * resolution --custom 1920x1080
```

## Statusbar

- `swaybar` (default)
- `waybar`
- `i3status`
