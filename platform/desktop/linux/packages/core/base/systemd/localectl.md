# localectl

## status

- Show system config at `/etc/locale.conf`

```shell
localectl status
```

## set-locale

```shell
# same as editing /etc/locale.conf
localectl set-locale "LANG=en_US.UTF-8"
```

## list-keymaps

```shell
# List all options for keyboard keymaps
localectl list-keymaps
localectl list-keymaps | grep "br-abnt2"
```
