# logs

```sh
# Logs from pod (single container)
kubectl logs "pod-name"
kubectl logs "pod-name" -c "container-name" # specify container
kubectl logs "pod-name" --container "container-name" # specify container

# Logs with specific label
kubectl logs --selector "app=myapp"

# Logs from pod (all containers)
kubectl logs "pod-name" --all-containers=true

# Logs from the previous instance of container
kubectl logs "pod-name" -c "container-name" -p

# Stream logs
kubectl logs "pod-name" -f

# Last 20 lines
kubectl logs "pod-name" --tail=20

# Last 1 hour
kubectl logs "pod-name" --since=1h
kubectl logs "pod-name" --since=10m

# Logs from all pods in a deployment
kubectl logs job/hello
kubectl logs "deployment/deployment-name" -c "container-name"
```

```sh
kubectl logs \
  --context "admin-user@lojaonline-prd" \
  --namespace "production" \
  "deployment/webservices" \
  --container "webservices" \
  --since "1h" \
  > "logs.txt"
```
