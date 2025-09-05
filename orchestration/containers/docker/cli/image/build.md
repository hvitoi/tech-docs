# docker image build

## --tag (-t)

- Define the image name and optionally a tag

```shell
docker image build -t "my-image" . # . is the context to dockerfile
docker image build -t "myregistry.com:5000/myuser/myimage:latest" .
```

## --file (-f)

- Build from custom docker file (default is `Dockerfile`)

```shell
docker image build -f "MyDockerfile" .
```
