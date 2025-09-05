# kubectl logs

```shell
# Logs from pods
kubectl logs <pod>

# Logs from umbrella objects
kubectl logs "job/hello"
kubectl logs "deploy/mydeployment"
```

## --container (-c)

- This flag is mandatory if the pod has more than more container

```shell
# Logs from a specific container
kubectl logs <object> --container <container> # -c
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
kubectl logs -n kube-system -l app.kubernetes.io/name=karpenter -f
```

## --previous (-p)

- Prints the logs for the previous instance of the container in a pod if it exists

```shell
kubectl logs <pod> -c <container> -p
```

## --follow (-f)

- Stream logs

```shell
kubectl logs <object> -f
```

## --tail

```shell
# Last 20 lines
kubectl logs <object> --tail=20
```

## --since

```shell
kubectl logs <object> --since=1h
kubectl logs <object> --since=10m
```
