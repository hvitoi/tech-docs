# sysfs

- Mounted at `/sys`
- It's a filesystem that allows `kernel subsystems` to report kernel objects, object attributes, and object relationships to user space
- It's always mounted to `/sys` at the system startup (before fstab is read)

```shell
mount | grep sysfs
```

## block

- Devices that are storage
- Usually link files that point to `devices`

## devices

- Every hardware attached to the computer
