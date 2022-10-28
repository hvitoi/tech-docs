# vgcreate

- Create volume group and assign it to a physical volume
- Group of PVs that serves as a container for LVs. PEs are allocated from a VG for a LV.

```sh
vgcreate "volume-group" "/dev/sdx1"
vgcreate "volume-group" "/dev/sdx1" "/dev/sdy1" # with multiple PVs
```
