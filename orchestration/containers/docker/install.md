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

### Colima

```shell
# client + open source daemon
brew install docker # client only (cli)
brew install docker-compose # plugin
brew install docker-buildx # plugin
brew install colima # an open-source daemon for MacOS (in case you installed the cli only)

colima start
docker container ls
```

```json
// ~/.docker/config.json
{
  "auths": {},
  "currentContext": "colima",
  "cliPluginsExtraDirs": [
    "/opt/homebrew/lib/docker/cli-plugins" // necessary for docker-compose, docker-buildx, etc installed via homebrew
  ]
}
```
