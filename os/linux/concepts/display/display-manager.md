# Display Manager

## GDM

- Runs on wayland and launches wayland compositors

- `/usr/share/gdm/greeter/autostart/`: contains starter files (bootstrap)
- `/etc/xdg/autostart/`: contains starter files (bootstrap)

```conf
# /usr/share/gdm/greeter/autostart/optimus.desktop
[Desktop Entry]
Type=Application
Name=Optimus
Exec=sh -c "xrandr --setprovideroutputsource modesetting NVIDIA-0; xrandr --auto"
NoDisplay=true
X-GNOME-Autostart-Phase=DisplayServer
```

## LightDM

- Support launching Wayland compositors, but the display manager itself runs on Xorg

```sh
pacman -S lightdm lightdm-gtk-greeter lightdm-gtk-greeter-settings
```

```sh
systemctl enable lightdm
```
