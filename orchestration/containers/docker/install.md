# Installation

- **Docker Daemon**
  - `dockerd` listens for docker api requests and manages docker objects (images, containers, networks, etc)

- **Docker Client**
  - Submit commands to the docker daemon (locally or remotely)

## MacOS

- Docker daemon is exposed as a socket at `unix:///var/run/docker.sock`

```shell
# client + daemon
brew install docker --cask # Docker Desktop - the full blown solution
brew install docker-compose

# you can install only the cli and install the daemon apart (e.g., colima)
brew install docker # client only (cli)

# verify
docker container ls
```
