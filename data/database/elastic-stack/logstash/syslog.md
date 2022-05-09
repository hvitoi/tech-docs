# Syslog

- Syslog is a standardized way to generate log information
- `Syslog daemon`: Collect log info and store it!
  - Can be stored locally or remotelly (port 514 UDP or 6514 TCP)
- Logstash: Opens a TCP port and listens for syslog data

```shell
sudo head -10 /var/log/syslog
```

- Rsyslog config file: `/etc/rsyslog.conf`

```conf
*.* @@127.0.0.1:10514
```

- `*.*`: Forward all messages
- `@`: transmit through UDP connections
- `@@`: transmit through TCP connections
- `127.0.0.1:10514`: where to send logs to
