# xdg-mime

## query

```shell
# get the file mime type for a file
xdg-mime query filetype "photo.jpeg"

# get default app
xdg-mime query default "image/jpeg"
```

## default

- Mime applications are saved at `/etc/xdg/mimeapps.list` (or `~/.config/mimeapps.list`)
- Desktop entries (eligible for default apps are stored at `/usr/share/applications`)

```shell
# set default app
xdg-mime default "feh.desktop" "image/jpeg"
xdg-mime default "thunar.desktop" "inode/directory"
xdg-mime default "firefox.desktop" "x-scheme-handler/https"
```
