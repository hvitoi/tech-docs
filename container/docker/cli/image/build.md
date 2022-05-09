# build

```shell
# Build image
docker image build -t "image-name" . # . is the context to dockerfile

# Build from custom file
docker image build -f "dockerfile" .

# Example
docker image build -t "myregistrydomain.com:5000/myimage:latest" .
```
