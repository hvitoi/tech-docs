# airmon-ng

## Set Interface Mode as "Monitor"

```sh
# get wireless interface info
airmon-ng

# find any process that can interfere with using the adapter in Monitor Mode
airmon-ng check

# kill any process that can interfere with using the adapter in Monitor Mode
airmon-ng kill

# check an interface into monitor mode
airmon-ng start "wlp3s0" # wlp3s0 is replaced with wlp3s0mon

# stop monitor interface
airmon-ng stop "wlp3s0mon"
```

```sh
# restart nm
systemctl start "NetworkManager"
```
