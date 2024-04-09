# launchctl

- **LaunchDaemons**
  - Stored at
    - `/System/Library/LaunchDaemons/*.plist` (system)
    - `~/Library/LaunchDaemons/*.plist` (user) ?
- **LaunchAgents**
  - Stored at
    - `/System/Library/LaunchAgents/*.plist` (system)
    - `~/Library/LaunchAgents/*.plist` (user)
  - These services appear under "Login Items" > "Allow in the Background"

## unload

- Disable a daemon

```shell
launchctl unload "/Library/LaunchDaemons/org.nixos.nix-daemon.plist"
launchctl unload "~/Library/LaunchAgents/com.koekeishiya.yabai.plist."
```

## Services

- Daemons
  - `/System/Library/LaunchDaemons/com.apple.ManagedClient*`
  - `/System/Library/LaunchDaemons/com.apple.mdmclient*`
- Agents
  - `/System/Library/LaunchAgents/com.apple.ManagedClient*`
  - `/System/Library/LaunchAgents/com.apple.mdmclient*`
