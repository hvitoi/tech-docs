# loginctl

## Session Commands

```shell
loginctl list-sessions
loginctl session-status $XDG_SESSION_ID
loginctl show-session $XDG_SESSION_ID
```

## User Commands

```shell
loginctl list-users
loginctl show-user $USER
```

## Configuration

```conf
# /etc/systemd/logind.conf.d/logind.conf
[Login]
HandleLidSwitch=ignore
HandleLidSwitchExternalPower=ignore
HandleLidSwitchDocked=ignore
HandlePowerKey=lock
IdleAction=lock
#IdleActionSec=1min
```
