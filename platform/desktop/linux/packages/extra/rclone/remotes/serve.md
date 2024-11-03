# serve

```shell
rclone serve webdav "remote:"
```

## --addr

- IP or socket to bind server to (127.0.0.1:8080 by default)
- Specify where to listen to incoming connections

```shell
# localhost
rclone serve webdav "remote:" --addr "127.0.0.12:8080"

# unix socket
rclone serve webdav "remote:" --addr "unix:///tmp/my.socket"
```
