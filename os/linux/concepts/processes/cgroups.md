# Control Groups (ggroups)

- `cgroup` is a filesystem mounted into `/sys/fs/cgroup`
- All processes running on a linux machine is associated with a least one cgroup
- Group processes together and `limit memory and cpu`
- cgroups are arranged hierarchically
- a cgroup will inherit the configs of a parent cgroup

```shell
# List manually the tree of cgroups
ls /sys/fs/cgroup

# List via systemd
systemctl status

# Get the cgroup of a specific process
cat /proc/<pid>/cgroup
```

## Cgroup example

```conf
# /etc/systemd/system/foo.slice
[Slice]
CPUQuota=30% # processes can take up to 30% of the CPU/thread
AllowedCPUs=0-5 # processes can use cpus 0 to 5 only
MemoryHigh=6G
```

```shell
# Run a shell attached to a cgroup
systemd-run --slice=foo.slice --uid=foo --shell
```
