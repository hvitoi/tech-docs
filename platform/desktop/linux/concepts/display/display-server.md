# Display Server

## Wayland

- Wayland is a `display server protocol`
- Display servers using the Wayland are called **compositors**, which are the graphical environments
- `XWayland` is used to provide a `X Server` in Wayland for backwards compatibility

### Weston

- Reference implementation for Wayland compositors

### Sway

- Sway is an i3-compatible Wayland compositor based on wlroots

### Mutter

- Gnome's native compositor

### Kwin

- KDE's native compositor

## Xorg / X11 / X Window System

- The graphical environment in Xorg is called **window manager** (WM)
- Packages
  - `xorg-server`
  - `xorg-xrandr`

### Configuration

- Configuration is stored at `/etc/X11/xorg.conf.d/` and `/usr/share/X11/xorg.conf.d/`

```conf
# /etc/X11/xorg.conf.d/10-nvidia-drm-outputclass.conf
Section "OutputClass"
    Identifier "intel"
    MatchDriver "i915"
    Driver "modesetting"
EndSection

Section "OutputClass"
    Identifier "nvidia"
    MatchDriver "nvidia-drm"
    Driver "nvidia"
    Option "AllowEmptyInitialConfiguration"
    Option "PrimaryGPU" "yes"
    ModulePath "/usr/lib/nvidia/xorg"
    ModulePath "/usr/lib/xorg/modules"
EndSection
```

### Bootstrap

- `~/.xinitrc`: stores initial script to be run (not used if a display manager is set up, e.g., gdm)

```shell
xrandr --setprovideroutputsource modesetting NVIDIA-0
xrandr --auto
```

### i3

- Most famous Xorg WM
