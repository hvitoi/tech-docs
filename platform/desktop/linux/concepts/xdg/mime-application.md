# MIME Application

- `/etc/xdg/mimeapps.list` (system wide)
- `~/.config/mimeapps.list` (user overrides)

```toml
# /etc/xdg/mimeapps.list
[Default Applications]

# browser
text/html=firefox.desktop
x-scheme-handler/http=firefox.desktop
x-scheme-handler/https=firefox.desktop
x-scheme-handler/about=firefox.desktop
x-scheme-handler/unknown=firefox.desktop

# video
video/mp4=vlc.desktop
video/mpeg=vlc.desktop
video/webm=vlc.desktop
video/x-matroska=vlc.desktop
video/x-ms-wmv=vlc.desktop

# image
image/bmp=org.gnome.eog.desktop
image/gif=org.gnome.eog.desktop
image/jpeg=org.gnome.eog.desktop
image/jpg=org.gnome.eog.desktop
image/png=org.gnome.eog.desktop
image/webp=org.gnome.eog.desktop

# files
inode/directory=org.gnome.Nautilus.desktop

# pdf
application/pdf=org.gnome.Evince.desktop

# txt
text/plain=org.gnome.TextEditor.desktop

# torrent
x-scheme-handler/magnet=org.qbittorrent.qBittorrent.desktop
application/x-bittorrent=org.qbittorrent.qBittorrent.desktop
```
