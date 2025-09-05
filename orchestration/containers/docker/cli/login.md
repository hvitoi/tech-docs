# docker login

```shell
# Login to docker.io
docker login

# Login to a custom registry
docker login "000000000000.dkr.ecr.us-east-1.amazonaws.com"

# Login with password
docker login -u "<user>" -p "<password>"
echo "password" | docker login -u "user" --password-stdin # legacy
```

## Add insecure registry

- Add unsecure registries to `/etc/docker/daemon.json`
- Passwords are stored unencrypted at `~/.docker/config.json`

```json
{
  "insecure-registries": [ "myregistrydomain.com:5000" ]
}
```

```shell
docker login "myregistrydomain.com:5000"
docker image build -t "myregistrydomain.com:5000/myimage:latest" .
docker image push "myregistrydomain.com:5000/myimage:latest"
```
