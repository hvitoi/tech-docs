# kubectl run

- Creates a **Pod Resource**
- Set the container images via command line

```shell
# Create pod
kubectl run "pod-name" \
  --image "nginx" \ # takes image from docker store by default
  --port "8080"

# Create pod + service
kubectl run "pod-name" \
  --image "nginx" \ # takes image from docker store by default
  --port "8080" \
  --expose

# Create pod with command (entrypoint)
kubectl run "pod-name" \
  --image "busybox" \
  --command "sleep 1000" \
  --restart "Never"
```

```shell
# Just generate the yaml
kubectl run "pod-name" \
  --image "nginx" \
  --dry-run="client" \
  -o "yaml" \
  > "pod.yaml"
```
