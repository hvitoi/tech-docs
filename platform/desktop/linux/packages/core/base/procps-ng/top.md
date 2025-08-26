# top

- Similar to ps but shows more information and workload
- List all processes running in the Linux system

- `Threading`: single PID, many threads (TH increases)
- `Multiprocessing`: multiple PIDs, few threads each

```shell
# live refresh
top # every 5 seconds by default, order by CPU
top -s # every 2 seconds

# snapshot
top -l 1       # Show snapshot once (no refresh loop)
top -l 5       # Show 5 updates then exit

# sort
top -o cpu
top -o mem
top -o pid

# limit
top -n 10      # Show only top 10 processes

# specific PID
top -pid 12345     # Show only that process

# columns
top -stats pid,ppid,command,mem,cpu,th,time,state,user

# user
top -user hv

# Combined
top -l 1 -user hv -o mem -stats pid,ppid,command,mem,cpu,th,time,state,user
```
