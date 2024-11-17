# docker registry login

```shell
# Login to docker.io
docker registry login

# Login to a custom registry
docker registry login "000000000000.dkr.ecr.us-east-1.amazonaws.com"

# Login with password
docker registry login -u "<user>" -p "<password>"
echo "password" | docker registry login -u "user" --password-stdin # legacy
```

```shell
# Logout
docker logout
```

## Add insecure registry

- Add unsecure registries to `/etc/docker/daemon.json`
- Passwords are stored unencrypted at `~/.docker/config.json`

```json
{
  "insecure-registries": ["myregistrydomain.com:5000"]
}
```

```shell
docker registry login "myregistrydomain.com:5000"
docker image build -t "myregistrydomain.com:5000/myimage:latest" .
docker image push "myregistrydomain.com:5000/myimage:latest"
```
