# pvcreate

- Create a physical volume
  - A hard disk
  - A partition
  - A loopback file
  - A device mapper device

```shell
pvcreate "/dev/sdx1"
```

```txt
NAME          MAJ:MIN RM   SIZE RO TYPE  MOUNTPOINTS
sda             8:0    1  28.6G  0 disk
└─lol         254:1    0  28.6G  0 crypt
  ├─haha-hehe 254:2    0     2G  0 lvm
  ├─haha-hihi 254:3    0     3G  0 lvm
  └─haha-hoho 254:4    0  23.6G  0 lvm
```
