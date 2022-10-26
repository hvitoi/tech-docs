# ps

- _Application_: It's a service. E.g., firefox, gimp
- _Process_: A small portion of the application. Application is composed of processes
- _Threads_: Instances of the process. Usually multiple

- _Daemon_: It's a process that continuously run in the background until it's stopped
- _Job_: It's a service or process that is scheduled (workorder)
- _Script_: List of instructions. pwd, useradd

```sh
# List processes running in the system
ps -ef

# List processes running in the current terminal!
ps

# List all processes along with additional info
ps aux
ps aux | grep "chrome"
```

- `ps` always show the ps command itself in the list. Because when the processes are listed ps is currently running
