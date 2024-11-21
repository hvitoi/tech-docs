# kubectl get

```shell
# Get summary
kubectl get "po"
kubectl get "po,svc"
kubectl get "all"

# Get the yaml manifest
kubectl get po/my-pod -o yaml
```

```shell
# Backup all resources
kubectl get "all" --all-namespaces -o yaml > "all-resources.yaml"
```

## --selector (-l)

- Filter by label

```shell
kubectl get "po" -l "app=myapp"
kubectl get "po" -l "app=myapp,component=web" # multiple labels
```

## --watch (-w)

```shell
kubectl get "po" -w
watch -n2 kubectl get "po" # gnu watch
```

## --sort-by

```shell
kubectl get "event" --sort-by ".metadata.creationTimestamp"
```

## --no-headers

```shell
kubectl get "po" --no-headers | wc -l # count number of pods
```

## --show-labels

```shell
kubectl get "po" --show-labels
```

## --all-namespaces (-A)

```shell
kubectl get "po" -A
```

## --namespace (-n)

- If not provided, use the default namespace

```shell
kubectl get "po" -n "namespace"
```

## --context

```shell
kubectl get "po" --context <context>
```

## --output (-o)

```shell
kubectl get "po" -o "wide" # additional info
kubectl get "po" -o "yaml" # output as yaml
```

```shell
# jsonpath
kubectl get "po" \
  -o=jsonpath='{​range .items[*]}​{​"\n"}​{​.metadata.name}​{​":\t"}​{​range .spec.containers[*]}​{​.image}​{​", "}​{​end}​{​end}​'

kubectl get "vs" \
  -o jsonpath='{​​​​​​​​range .items[*]}​​​​​​​​{​​​​​​​​"\n"}​​​​​​​​{​​​​​​​​"service: "}​​​​​​​​{​​​​​​​​.spec.http[0].route[0].destination.host}​​​​​​​​{​​​​​​​​", Prefix: "}​​​​​​​​{​​​​​​​​range .spec.http[0].match[*]}​​​​​​​​{​​​​​​​​", "}​​​​​​​​{​​​​​​​​.uri.prefix}​​​​​'

kubectl get "po" "my-pod" \
  --output jsonpath="{.spec.containers[0].image}" | awk -F "/" '{print $2}' | awk -F ":" '{print $2}'
```

## Authentication

```shell
kubectl get po \
  --server "my-kube-playground:6443" \
  --client-certiticate "admin.key" \
  --client-key "admin.key" \
  --certificate-authority "ca.crt"
```

- Instead of passing these parameters manually you might want to set them in a kubeconfig file

```shell
kubectl get po \
  --kubeconfig "kubeconfig.yaml"
```

## Object shortnames

```shell
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
```
