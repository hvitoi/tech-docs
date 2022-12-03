# guitarix

## Groups

```shell
# Add the necessary groups to your user
sudo usermod -aG "audio" $USER
sudo usermod -aG "realtime" $USER # might be necessary to install the realtime-privileges package (or realtime group)
```

## Limits

- Check `max locked memory` (should be unlimited)
- Check `real-time priority` (should be over 90)

```shell
ulimit -a
```

- If not, change it in `/etc/security/limits.conf`

```conf
@audio soft memlock unlimited
```
