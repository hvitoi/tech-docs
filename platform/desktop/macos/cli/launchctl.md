# launchctl

- **LaunchDaemons**
  - Stored at
    - `/System/Library/LaunchDaemons/*.plist` (system)
    - `~/Library/LaunchDaemons/*.plist` (user)
- **LaunchAgents**
  - Stored at
    - `/System/Library/LaunchAgents/*.plist` (system)
    - `~/Library/LaunchAgents/*.plist` (user)
  - These services appear under "Login Items" > "Allow in the Background"

## print

```shell
launchctl print system
launchctl print system | grep enabled # enabled services
```

## disable

```shell
launchctl disable system/com.apple.ManagedClientAgent.enrollagent
launchctl disable system/com.apple.mdmclient.daemon
launchctl disable system/com.apple.devicemanagementclient.teslad
```

## unload

- Disable a daemon

```shell
launchctl unload "/Library/LaunchDaemons/org.nixos.nix-daemon.plist"
launchctl unload "~/Library/LaunchAgents/com.koekeishiya.yabai.plist."
```
