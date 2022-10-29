# login

```sh
# Login
docker login

# Login with password
docker login -u "user" -p "password"
echo "password" | docker login -u "user" --password-stdin # legacy
```

```sh
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

```sh
docker login "myregistrydomain.com:5000"
docker image build -t "myregistrydomain.com:5000/myimage:latest" .
docker image push "myregistrydomain.com:5000/myimage:latest"
```
