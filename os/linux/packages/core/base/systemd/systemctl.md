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

### status

```shell
# Analyzing the system state
systemctl status
systemctl status "unit" # status of a specific unit
```

### list-units

### start

```shell
systemctl start "unit"
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
systemctl enable "unit"
```

### disable

```shell
systemctl disable "unit"
```

## Environment Commands

### set-environment

```shell
# set environment variables for a service
systemctl set-environment \
  MYSQLD_OPTS="--skip-grant-tables --skip-networking"
```

## Manager State Commands

### daemon-reload

```shell
systemctl daemon-reload
```
