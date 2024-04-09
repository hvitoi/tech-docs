# unshare

- Executes a command in a new `namespace`
- It's like a sandboxed process

## pid namespace

- Hides all the other processes (`/proc`) (creates a new own /proc)
- Executes a command as PID 1

```shell
# root privilege
unshare \
  --fork \ # f
  --pid \ # p
  --mount-proc \ # mount proc fs first
  /bin/bash

# user (nobody) privilege
unshare \
  --user \
  --fork \
  --pid \
  --mount-proc \
  /bin/bash

# user (uid+gid) privilege
unshare \
  --user \
  --setuid 1000 \
  --setgid 1000 \
  --fork \
  --pid \
  --mount-proc
  /bin/bash
```

```shell
# 1. Create a new namespace (with a new proc fs)
# 2. Mount this proc fs into a custom linux filesystem
# 3. Chroot into this Linux Filesystem
unshare \
  --fork \
  --pid \
  --mount-proc=/tmp/myrootfs/proc \
  chroot /tmp/myrootfs /bin/bash
```

## network namespace

- Isolate virtual networks

## ipc namespace

- Inter-process communication

## uts namespace

- Change internal hostname

## mount namespace

- Create different mounts than the host system

## cgroup namespace

- New cgroups
