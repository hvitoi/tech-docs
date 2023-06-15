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

## net

```shell
# List all networks
sudo virsh net-list --all

# Define the bridge network
virsh net-define "br10.xml"

# Start the bridge network
virsh net-start "br10" # br10 is the name of the interface
virsh net-start "default" # run with sudo!
```

## dumpxml

- The `domain name` is the name of the VM defined at it creation

```shell
# get the whole VM configuration
virsh dumpxml "win11"
```

## domblklist

- Show block level devices (sda, sdb, ...)
- Show qcow2 paths (hda, hdb, ...)

```shell
virsh domblklist "win11"
```

## snapshot

```shell
domain="win11"
snapshot="mysnapshot"
```

```shell
# look at '<disk>' types, should be just 'file' types
virsh dumpxml "$domain" | grep '<disk' -A5

# show block level devices and qcow2 paths (hda,hdb,..etc)
virsh domblklist "$domain"

# create snapshot in default pool location
# file name is $domain.$snapshot
virsh snapshot-create-as "$domain" --name "$snapshot" --disk-only

# list snapshot
virsh snapshot-list "$domain"
```

```shell
# notice path to hda has now changed to snapshot file
virsh domblklist "$domain"

# <source> has changed to snapshot file
virsh dumpxml "$domain" | grep '<disk' -A5

# pull default pool path from xml
pooldir=$(virsh pool-dumpxml default | grep -Po "(?<=path\>)[^<]+")
echo "default pool dir: $pooldir"

# should see two files starting with $thedomain
# the one named $thedomain.$snapshotname is the snapshot
cd $pooldir
ls -latr "$domain"*

# snapshot points to backing file, which is original disk
sudo qemu-img info "$domain"."$snapshot" -U --backing-chain

# capture original backing file name so we can revert
backingfile=$(qemu-img info $domain.$snapshot -U | grep -Po 'backing file:\s\K(.*)')
echo "backing file: $backingfile"
```

```shell
# stop VM
virsh destroy "$domain"

# edit hda path back to original qcow2 disk
virt-xml "$domain" --edit target=$targetdisk --disk path=$backingfile --update

# validate that we are now pointing back at original qcow2 disk
virsh domblklist "$domain"

# delete snapshot metadata
virsh snapshot-delete --metadata "$domain" $snapshotname

# delete snapshot qcow2 file
sudo rm $pooldir/"$domain".$snapshotname

# start guest domain
virsh start "$domain"
```
