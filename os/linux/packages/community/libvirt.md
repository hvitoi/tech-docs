# libvirt

## virsh

- Setting up a new network interface is optional given that a `default` open is already created (requires `dnsmaq` package)

```xml
<network>
  <name>br10</name>
  <forward mode='nat'>
    <nat>
      <port start='1024' end='65535' />
    </nat>
  </forward>
  <bridge name='br10' stp='on' delay='0' />
  <ip address='192.168.30.1' netmask='255.255.255.0'>
    <dhcp>
      <range start='192.168.30.50' end='192.168.30.200' />
    </dhcp>
  </ip>
</network>
```

```sh
# Define the bridge network
virsh net-define "br10.xml"

# Start the bridge network
virsh net-start "br10" # br10 is the name of the interface
```
