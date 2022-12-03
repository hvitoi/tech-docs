# timedatectl

```shell
# List timezones
timedatectl list-timezones
timedatectl list-timezones | grep "America/Sao_Paulo"

# Enable ntp server for clock update
timedatectl set-ntp true

# Clock status
timedatectl status
```
