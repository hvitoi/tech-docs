# docker container create

- Create container without starting it
- Accepts most of the options just like `docker container run`
  - Some are not available (for instance --detach)

```shell
docker container create "image"

docker container create --name archlinux --platform linux/amd64 archlinux
```
