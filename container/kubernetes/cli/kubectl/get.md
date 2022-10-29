# get

```sh
# Options
kubectl get "po"
kubectl get "po" -o "wide" # additional info
kubectl get "po" -o "yaml" # output as yaml
kubectl get "po" -w # watch mode
watch -n2 kubectl get "po" # watch every 2s
kubectl get "po" -n "namespace" # specific namespace
kubectl get "po" -A # --all-namespaces
kubectl get "po" --context "context" # use a context
kubectl get "po" --no-headers | wc -l # count number of pods
kubectl get "po" --show-labels # show labels

# Filter by label
kubectl get "po" -l "app=myapp" # same as --selector
kubectl get "po" -l "app=myapp,component=web" # multiple labels

# sorte
kubectl get "event" --sort-by ".metadata.creationTimestamp"

# Other objects
kubectl get "all" # all resources
kubectl get "po,svc" # pod + service
kubectl get "no"
kubectl get "svc"
kubectl get "deploy"
kubectl get "ing"
kubectl get "pvc"
kubectl get "pv"
kubectl get "secret"
kubectl get "cm"
kubectl get "ns"
kubectl get "crd"

# Store a backup of all resources
kubectl get "all" \
  --all-namespaces \
  -o "yaml" \
  > "all-resources.yaml"
```

## jsonpath

```sh
kubectl get "po" \
  -o=jsonpath='{​range .items[*]}​{​"\n"}​{​.metadata.name}​{​":\t"}​{​range .spec.containers[*]}​{​.image}​{​", "}​{​end}​{​end}​'

kubectl get "vs" \
  -o jsonpath='{​​​​​​​​range .items[*]}​​​​​​​​{​​​​​​​​"\n"}​​​​​​​​{​​​​​​​​"service: "}​​​​​​​​{​​​​​​​​.spec.http[0].route[0].destination.host}​​​​​​​​{​​​​​​​​", Prefix: "}​​​​​​​​{​​​​​​​​range .spec.http[0].match[*]}​​​​​​​​{​​​​​​​​", "}​​​​​​​​{​​​​​​​​.uri.prefix}​​​​​'

kubectl get "po" "my-pod" \
  --output jsonpath="{.spec.containers[0].image}" | awk -F "/" '{print $2}' | awk -F ":" '{print $2}'
```

## Authentication

```sh
kubectl get po \
  --server "my-kube-playground:6443" \
  --client-certiticate "admin.key" \
  --client-key "admin.key" \
  --certificate-authority "ca.crt"
```

- Instead of passing these parameters manually you might want to set them in a kubeconfig file

```sh
kubectl get po \
  --kubeconfig "kubeconfig.yaml"
```
