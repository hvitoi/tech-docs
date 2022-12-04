# at

- Schedule jobs

```shell
# same day
at "15:32" -f "./myscript.sh"

# another day
at "15:32 081622" -f "./myscript.sh"
```

## atq

- Queue of scheduled jobs ahead

```shell
atq
```

## atrm

- Delete scheduled job by its id

```shell
atrm "3"
```
