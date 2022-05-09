# transaction

- <https://redis.io/commands#transactions>

```shell
# Create string data
SET foos 230

# Start a transaction, enter numerous command and after call EXEC to effect all were effected
MULTI
INCRBY foos 10
DECRBY foos 5
EXEC

GET foos

# Start a transaction, enter numerous command and after call DISCARD to effect none of the commands
MULTI
INCRBY foos 10
DECRBY foos 5
DISCARD

GET foos


```
