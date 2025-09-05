# Installation

- **Docker Daemon**
  - `dockerd` listens for docker api requests and manages docker objects (images, containers, networks, etc)

- **Docker Client**
  - Submit commands to the docker daemon (locally or remotely)

## MacOS

- Docker daemon is exposed as a socket at `unix:///var/run/docker.sock`

```shell
brew install docker --cask # client + daemon
brew install docker # client only (cli)
```
