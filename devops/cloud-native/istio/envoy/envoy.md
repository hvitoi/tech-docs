# Envoy

```shell
docker image build -t "my-istio-demo" .
docker container run -d -p "10000:10000" -p "9901:9901" my-istio-demo
docker container logs -f "pod-name"
```
