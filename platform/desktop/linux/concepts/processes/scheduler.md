# Kernel Scheduler

- Specifies in which thread/cpu a process should run
- A process can alternate between threads during its execution
- It's possible to restrict which threads (all by default) the processes in the system can run

```shell
# /etc/libvirt/hooks/qemu
if [ "$command" = "$started" ]; then
  # limit the CPU in which processes can run
  systemctl set-property --runtime -- system.slice AllowedCPUs=0-15
  systemctl set-property --runtime -- user.slice AllowedCPUs=0-15
  systemctl set-property --runtime -- init.scope AllowedCPUs=0-15
elif [ "$command" = "$release" ]; then
  # restore back initial config
  systemctl set-property --runtime -- system.slice AllowedCPUs=0-31
  systemctl set-property --runtime -- user.slice AllowedCPUs=0-31
  systemctl set-property --runtime -- init.scope AllowedCPUs=0-31
fi
```
