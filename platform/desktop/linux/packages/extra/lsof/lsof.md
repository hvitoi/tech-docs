# lsof

```shell
# Show the PIDs currently using this port
lsof -i :35000

#
lsof -iTCP -sTCP:LISTEN -P -n
```
