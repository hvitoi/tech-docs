# disown

- Disown a running `job` job so that it is not tied to a terminal session
- Useful if you want to continue running a process even after closing the terminal session
- Works similar to `nohup`
- The logs keep appearing at the terminal (use nohup if you don't want it)

```shell
sleep 9999 &
jobs # job is there
disown $! # or simply disown for the last job
jobs # job is not there anymore
ps aux | grep sleep # but still running
```
