# lvcreate

- Create a logical volume (attached to a volume group)
- "Virtual/logical partition" that resides in a VG and is composed of PEs
- LVs are Unix block devices analogous to physical partitions, e.g. they can be directly formatted with a file system.

```shell
# create a logical partition (fixed size)
lvcreate "volume-group" \
  -n "logical-volume" \
  -L "50G"

# create a logical partition (the rest of the VG)
lvcreate "volume-group" \
  -n "logical-volume" \
  -l "+100%FREE"
```
