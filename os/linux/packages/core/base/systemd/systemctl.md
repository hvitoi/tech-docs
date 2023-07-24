# systemctl

- `systemctl` is the interaction with `systemd`
- New version of the legacy `service` command

## Unit File Commands

- **Unit locations**
  - `/usr/lib/systemd/system/`: units provided by installed packages
  - `/etc/systemd/system/`: units installed by the system administrator
- **Unit types**
  - `.service`
    - How to start or stop a service
    - When it should actually start
    - Dependencies
  - `.socket`
    - Network, IPC socket, or FIFO buffer
    - Always have a .service associated that is started when activity is noticed on the socket
  - `.device`
    - Depends on udev rules or sysfs
  - `.mount`
    - Mount point to be managed
    - Entries at /etc/fstab have units created automatically
  - `.automount`
    - Associated with a .mount
  - `.swap`
    - Swap space on the system
  - `.target`
    - Provide synchronization points for other units when booting up or changing states
  - `.path`
    - A path to be used for activation
    - Uses inotify to monitor path changes
  - `.timer`
    - Similar to a cronjob
  - `.snapshot`
    - Allows to reconstruct the a state of the system
    - Do not survive across sessions
    - Used to roll back temporary states
  - `.slice`
    - Associated with Linux Control Group nodes
    - Restricts access of resources by processes
  - `.scope`
    - Created automatically based on information received from bus interfaces

### enable

```shell
sudo systemctl enable "unit" # system unit (--system implied)
systemctl enable "unit" --user # user unit (local config)
systemctl enable "unit" --user --global # user unit (global config)
```

### disable

```shell
systemctl disable "unit"
```

### mask

- Symlinks to /dev/null

```shell
systemctl mask "systemd-rfkill.service"
```

### list-unit-files

```shell
systemctl list-unit-files --state=masked
systemctl list-unit-files | grep masked
```

## Unit Commands

### status

```shell
# Analyzing the system state
systemctl status
systemctl status "unit" # status of a specific unit
```

### list-units

```shell
# Checking the unit status
systemctl
systemctl list-units # same output

# filters
systemctl list-units --type=automount # auto mounted partitions
systemctl list-units --type=service
systemctl list-units --user --type=target
systemctl list-units --failed
systemctl list-units --all # loaded but inactive
```

### start

```shell
systemctl start "unit"
systemctl start sway.service --wait --user
```

### stop

```shell
systemctl stop "unit"
```

### restart

```shell
systemctl restart "unit"
systemctl restart pipewire.service --user
```

## Job Commands

### list-jobs

```shell
systemctl list-jobs --user
```

## Environment Commands

### show-environment

```shell
systemctl --user show-environment
```

### set-environment

```shell
# import import-environment variables
systemctl --user import-environment DISPLAY WAYLAND_DISPLAY SWAYSOCK XDG_CURRENT_DESKTOP
dbus-update-activation-environment --systemd DISPLAY WAYLAND_DISPLAY SWAYSOCK XDG_CURRENT_DESKTOP

# set environment variables for a service
systemctl set-environment \
  MYSQLD_OPTS="--skip-grant-tables --skip-networking"
```

## Manager State Commands

### daemon-reload

```shell
systemctl daemon-reload
```
