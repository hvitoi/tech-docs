# jobs

```shell
# List the current jobs running
jobs

# Kill a job by its id
kill %1

# Kill by the id of the last running job
kill $!
```

- Jobs are tied to a terminal sesson. If the session is closed all the jobs are killed

```shell
sleep 99999 &
jobs # shows the sleeping job

# **closes the session**
jobs # shows no jobs
```
