# kubectl describe

- Information about an object

```shell
# Inspect a specific object
kubectl describe <object-kind>/<object-name>
kubectl describe po/my-pod
kubectl describe po my-pod # same

# Inspect all objects of that kind
kubectl describe <object-kind>
kubectl describe po
```
