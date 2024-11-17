# docker container inspect

```shell
## Inspect container (JSON)
docker container inspect "container"
docker container inspect --format '{{ .NetworkSettings.IPAddress }}' <container> # Get IP
```
