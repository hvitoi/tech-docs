# ps (Process Status)

- `Application`: It's a service. E.g., firefox, gimp
- `Process`: A small portion of the application. Application is composed of processes
- `Threads`: Instances of the process. Usually multiple

- `Daemon`: It's a process that continuously run in the background until it's stopped
- `Job`: It's a service or process that is scheduled (workorder)
- `Script`: List of instructions. pwd, useradd

```shell
# List processes running in terminal emulators, can be in another terminal window, even if it's another emulator (e.g., iterm2 + alacritty)
ps

# Display information about other users' processes, including those without controlling terminals.
ps -e

# Columns
ps -f # uid (UID), pid (PID), parent pid (PPID), recent CPU usage (C), process start time (STIME), controlling tty (TTY), elapsed CPU usage (TIME), associated command (CMD)
ps -l # uid (UID), pid (PID), parent pid (PPID), flags (F), cpu (CPU), pri (PRI), nice (NI), vsz (SZ), rss (RSS), wchan (WCHAN), state (S), paddr (ADDR), controlling tty (TTY), elapsed CPU usage (TIME), associated command (CMD)
ps -o pid,ppid,%mem,%cpu,user,command # comm for sort command

# user
ps --user hv
ps -u hv # macos

# sort (linux only)
ps --sort=%mem
ps --sort=%cpu
ps --sort=-%cpu # descent order
ps --sort=ppid,-%cpu # two columns

# Combined
ps -eo pid,ppid,%mem,%cpu,user,command
```

- `ps` always show the ps command itself in the list. Because when the processes are listed ps is currently running
