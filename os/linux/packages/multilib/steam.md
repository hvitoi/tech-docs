# steam

## Flatpak

```shell
# Add permissions to external drive
# Select the path that holds the SteamLibrary folder
flatpak override \
  --user \
  --filesystem "/media/hv/moon/game" \
  "com.valvesoftware.Steam"
```
