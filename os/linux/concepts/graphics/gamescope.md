# gamescope

```shell
killall -9 gamescope-wl
```

```shell
# Real resolution (-H, -W). If -W is not specified, 16:9 is assumed
gamescope -H 1440 -- %command%

# Game resolution
gamescope -h 720 -- %command%

# Upscaling a 720p game to 1440p
gamescope -h 720 -H 1440  -- %command%

# Upscaling technique
gamescope -h 720 -H 1440 -U -- %command% # AMD FidelityFX™ Super Resolution 1.0
gamescope -h 720 -H 1440 -Y -- %command% # NVIDIA Image Scaling v1.0.3

# Limit a vsynced game to 30 FPS
gamescope -r 30 -- %command%

# Window type
gamescope -b -- %command% # borderless
gamescope -f -- %command% # fullscreen
```

```shell
# Launch steam with gamescope
gamescope -e -- steam -gamepadui
```

```shell
# 16:9
gamescope -H 1440 -W 2560 -h 1080 -w 1920 --prefer-vk-device 1002:73ff --rt -e -U -f -- %command%
gamescope -H 1440 -W 2560 -h 720 -w 1280 --prefer-vk-device 1002:73ff --rt -e -U -f -- %command%

# 16:10 (8:5)
gamescope -H 1200 -W 1920 -h 800 -w 1280 --prefer-vk-device 1002:73ff --rt -e -U -f -- %command%

# 21:9 (7:3)
gamescope -H 1080 -W 2560 -h 720 -w 1680 --prefer-vk-device 1002:73ff --rt -e -U -f -- %command%
```
