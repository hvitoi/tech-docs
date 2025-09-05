# kubectl delete

```shell
# Delete object by manifest
kubectl delete -f "manifest.yaml"

# Delete by the object type and name
kubectl delete "object-kind" "object-name"
kubectl delete "pod" "mypod"

# Delete all pods/deployments
kubectl delete "pod" --all
kubectl delete "deploy" --all

# Delete all forcing
kubectl delete "pod" --all --force

# Grace period
kubectl delete "pod" --force --grace-period 0

# delete based on label
kubectl delete "all" -l "app=myapp" # same as --selector
```

## Multiple delete

```shell
export K8S_OBJECT=serviceaccount;
export K8S_PARAMETER=prometheus;
for i in $(kubectl get $K8S_OBJECT | grep -i $K8S_PARAMETER | awk '{print$1}'); do kubectl delete $K8S_OBJECT/$i; done;
```
