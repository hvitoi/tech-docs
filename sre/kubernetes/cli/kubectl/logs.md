# kubectl logs

```shell
# Logs from pods
kubectl logs <pod>

# Logs from umbrella objects
kubectl logs "job/hello"
kubectl logs "deployment/mydeployment"
```

## --container (-c)

```shell
# Logs from pod (single container)
kubectl logs "pod-name" --container "container-name" # -c
```

## --all-containers

- Logs from all containers in the pod

```shell
kubectl logs <pod> --all-containers
```

## --selector (-l)

- Logs with specific label

```shell
kubectl logs --selector "app=myapp"
```

## --previous (-p)

- Prints the logs for the previous instance of the container in a pod if it exists

```shell
kubectl logs <pod> -c <container> -p
```

## --follow (-f)

- Stream logs

```shell
kubectl logs "pod-name" -f
```

## --tail

```shell
# Last 20 lines
kubectl logs "pod-name" --tail=20
```

## --since

```shell
kubectl logs "pod-name" --since=1h
kubectl logs "pod-name" --since=10m
```
