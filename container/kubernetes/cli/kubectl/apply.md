# apply

- The declarative approach to create/update kubernetes objects
- If the config file is `new`, the object gets created
- If the config file is `modified`, the object gets updated
- If the config file is `unchanged`, the object does not alter

- The config of the last applied object is stored as json in an annotation at the live object
  - `metadata.annotations.kubectl.kubernetes.io/last-applied-configuration`

```sh
# Apply a single config file
kubectl apply -f "manifest.yaml"
kubectl apply -f "manifest1.yaml" -f "manifest2.yaml"

# Apply config files from a whole directory
kubectl apply -f "directory/"

# Apply from a directory containing kustomization.yaml
kubectl apply -k "base/"

# Apply from STDIN
kube apply -f -
```
