# steam

## Flatpak

```shell
# Add permissions to external drive
# Select the path that holds the SteamLibrary folder
flatpak override \
  --user \
  --filesystem "/media/hv/moon/game" \
  "com.valvesoftware.Steam"

# Add environment variables
flatpak override \
  --user \
  --env=DXVK_FILTER_DEVICE_NAME=NAVI23 \
  "com.valvesoftware.Steam"
```
