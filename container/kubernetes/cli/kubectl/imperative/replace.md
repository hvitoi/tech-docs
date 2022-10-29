# replace

- Replace completely an object
- The selection of the object to be replaced is by its "name"

```sh
kubectl replace -f "manifest.yaml"
kubectl replace -f "manifest.yaml" --force # completely recreate the object
```

```sh
# Force delete namespace in "terminating" state
kubectl get ns "desenvolvimento" -o json > "ns.json"
kubectl replace --raw "/api/v1/namespaces/desenvolvimento/finalize" -f "./ns.json" # remove 'kubernetes' from spec.finalizers
```
