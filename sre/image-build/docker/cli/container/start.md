# start

```shell
# Start container
docker container start <container> # start does not replace the CMD!
docker container start -a <container> # attach container's STDOUT and STDERR
docker container start -i <container> # keep STDIN open even if not attached
```
