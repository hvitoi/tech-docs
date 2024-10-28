# docker volume

- Volumes are stored in the host OS at `/var/lib/docker/volumes`

## Storage drivers

- Attributions
  - Maintain layered architecture
  - Create container layer (writable)
  - Copy files across layers
- Common storage drivers
  - `AUFS`
  - `ZFS`
  - `BTRFS`
  - `Device Mapper`
  - `Overlay`
  - `Overlay2`
- Docker will choose the best storage driver available based on the host OS

## Manage volumes

```shell
# List volumes
docker volume ls

# Create volume
docker volume create "volume-name"
```

## Mount volumes

```shell
# Volume mount - Unnamed volume (placeholder for the folder, so that the bind mount do not overwrite this file)
docker container run \
    -v "/var/lib/mysql" \
    "mysql"

# Volume mount - Named volume
docker container run \
    -v "mysql-db:/var/lib/mysql" \
    "mysql"

# Bind Mount (replaces all the files inside of the container folder). Can't be used in Dockerfile
docker container run \
    -v "$(pwd):/usr/share/nginx/html" \
    "nginx" # $HOME

# New mount syntax
docker container run \
    --mount "type=bind,source=/data/mysql,target=/varlib/mysql"
    "mysql"
```

## Volume drivers

- Volumes are managed by `volume driver plugins`
- Volume drivers
  - `Local`: creates a volume on the host machine (/var/lib/docker/volumes)
  - `Azure File Storage`
  - `Convoy`
  - `DigitalOcean Block Storage`
  - `Flocker`
  - `gce-dock`
  - `GlusterFs`
  - `NetApp`
  - `RexRay`
  - `PortWorx`
  - `VMware vSphere Storage`

```shell
docker container run \
  --volume-driver "rexray/ebs"
  --mount "type=bind,source=/data/mysql,target=/varlib/mysql"
  "mysql"
```
