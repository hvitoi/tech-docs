# kubectl create

- Create a **Kubernetes Resource** from a file or from stdin

## Generic

```shell
kubectl create -f "manifest.yaml"
kubectl create -f "manifest.yaml" --save-config # save last applied config to metadata
```

## Deployment

```shell
kubectl create deployment "nginx" \
  --image "nginx" \
  --replicas "5" \
  --dry-run="client" \
  -o "yaml" \
  > "deployment.yaml"
```

## Service

```shell
kubectl create service clusterip "my-svc" \
  --tcp "6379:6379" \
  --dry-run="client" \
  -o "yaml" \
  > "service.yaml"
```

## ConfigMap

```shell
# From literal
kubectl create configmap "simpleconfig" \
  --from-literal "foo_env=bar" \
  --from-literal "hello_env=world"

# From file
kubectl create configmap "simpleconfig" \
  --from-file "config.properties=/config/app-config.properties"

# From folder
kubectl create configmap "simpleconfig" \
  --from-file "/config/" # a key will be added for each file inside of the folder

# From env file
kubectl create configmap "simpleconfig" \
  --from-env-file "local.env" # each key-value pair will be added as a keyvalue pair in the config map

# Dry run and replace
kubectl create configmap "app-envs" \
  --from-env-file "env/dev.env" \
  --dry-run="client" \
  -o "yaml" \
  | kubectl replace -f -
```

## Secret

```shell
# generic
kubectl create secret generic "secret-name" \
  --from-literal "key1=value1" \
  --from-literal "key2=value2"

kubectl create secret generic "secret-name" \
  --from-file "mycert.crt=ca.crt"

# tls
kubectl create secret tls "tls-cert" \
  --cert "admin.crt" \
  --key "admin.key"

# docker-registry
kubectl create secret docker-registry "regcred" \
  --docker-server "private-registry.io" \
  --docker-username "registry-user" \
  --docker-password "registry-password" \
  --docker-email "mail@mail.com"
```
