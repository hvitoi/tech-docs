# networksetup

```shell
networksetup -listallhardwareports

# Shows the MAC address of a given network interface
sudo ifconfig en0 | grep ether

# Spoof the MAC address (it's reset on restart)
sudo ifconfig en0 ether "00:00:00:00:00:00"
sudo ifconfig en0 down
sudo ifconfig en0 up
```
