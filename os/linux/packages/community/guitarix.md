# guitarix

## Groups

```sh
# Add the necessary groups to your user
sudo usermod -aG "audio" $USER
sudo usermod -aG "realtime" $USER # create it if it doesn't exist
```

## Limits

- Check `max locked memory` (should be unlimited)
- Check `real-time priority` (should be over 90)

```sh
ulimit -a
```

- If not, change it in `/etc/security/limits.conf`

```conf
@audio soft memlock unlimited
```
