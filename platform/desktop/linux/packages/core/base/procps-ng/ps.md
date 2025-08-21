# ps

- _Application_: It's a service. E.g., firefox, gimp
- _Process_: A small portion of the application. Application is composed of processes
- _Threads_: Instances of the process. Usually multiple

- _Daemon_: It's a process that continuously run in the background until it's stopped
- _Job_: It's a service or process that is scheduled (workorder)
- _Script_: List of instructions. pwd, useradd

```shell
# List processes running in the current terminal!
ps

# List all processes running in the system (not only in the current terminal)
ps -e

# full format (includes UID, PPID, C, STIME)
ps -f

# select columns and sort by cpu usage
ps -eo pid,comm,%cpu,%mem --sort=-%cpu

# List all processes along with additional info
ps aux
ps aux | grep "chrome"
```

- `ps` always show the ps command itself in the list. Because when the processes are listed ps is currently running
