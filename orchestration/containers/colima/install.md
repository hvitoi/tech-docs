# Installation

## MacOS

```shell
# client + open source daemon
brew install docker # client only (cli)
brew install docker-compose
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
    "/opt/homebrew/lib/docker/cli-plugins" // necessary for docker-compose
  ]
}
```
