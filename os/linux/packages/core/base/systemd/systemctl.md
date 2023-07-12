# systemctl

- `systemctl` is the interaction with `systemd`
- New version of the legacy `service` command

## Unit Commands

- Units types
  - `services` (.service)
  - `mount points` (.mount)
  - `devices` (.device)
  - `sockets` (.socket)
- `/usr/lib/systemd/system/`: units provided by installed packages
- `/etc/systemd/system/`: units installed by the system administrator

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

## Unit File Commands

- `/etc/systemd/system/`

```conf
# Example /etc/systemd/system/tomcat.service
[Unit]
Description=Apache Tomcat Web Application Container
After=network.target

[Service]
Type=forking

Environment=JAVA_HOME=/usr/lib/jvm/java-1.11.0-openjdk-amd64
Environment=CATALINA_PID=/opt/tomcat/temp/tomcat.pid
Environment=CATALINA_HOME=/opt/tomcat
Environment=CATALINA_BASE=/opt/tomcat
Environment='CATALINA_OPTS=-Xms512M -Xmx1024M -server -XX:+UseParallelGC'
Environment='JAVA_OPTS=-Djava.awt.headless=true -Djava.security.egd=file:/dev/./urandom'

ExecStart=/opt/tomcat/bin/startup.sh
ExecStop=/opt/tomcat/bin/shutdown.sh

User=tomcat
Group=tomcat
UMask=0007
RestartSec=10
Restart=always

[Install]
WantedBy=multi-user.target
```

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

## Environment Commands

### set-environment

```shell
# import import-environment variables
systemctl --user import-environment DISPLAY WAYLAND_DISPLAY SWAYSOCK XDG_CURRENT_DESKTOP

# set environment variables for a service
systemctl set-environment \
  MYSQLD_OPTS="--skip-grant-tables --skip-networking"
```

## Manager State Commands

### daemon-reload

```shell
systemctl daemon-reload
```
