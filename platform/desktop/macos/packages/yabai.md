# Yabai

```shell
yabai --start-service
yabai --stop-service
yabai --restart-service
```

## Config

```shell
yabai -m config layout bsp

# Padding
yabai -m config top_padding 5
yabai -m config bottom_padding 5
yabai -m config left_padding 5
yabai -m config right_padding 5
yabai -m config window_gap 5

# Mouse
yabai -m config mouse_modifier alt

# Focus
yabai -m config focus_follows_mouse autofocus
yabai -m config mouse_follows_focus on
yabai -m config window_origin_display focused
```

## Display

```shell
# Focus display 1
yabai -m display --focus 1
```

## Space

```shell
# Focus space 1
yabai -m space --focus 1

# Rebalance windows in a space
yabai -m space --balance

# Toggle mission control
yabai -m space --toggle mission-control
```

## Window

```shell
# Focus to a direction
yabai -m window --focus south

# Toggle feature
yabai -m window --toggle float

# Resize grid
yabai -m window --grid 4:4:1:1:2:2
```

## Query

```shell
yabai -m query --displays
yabai -m query --spaces
yabai -m query --windows
```

## Rule

```shell
# list rules
yabai -m rule --list

# add a new rule
yabai -m rule --add app="^System Settings$" manage=off
```

## Signal

```shell
# List registered events
yabai -m signal --list
```
