# config

## view

- Default context is stored at `~/.kube/config` and it must have `600` permission

```shell
# Show kubeconfig
kubectl config view
kubectl config view -o jsonpath='{.users[?(@.name == "admin")].user.password}' # get user + password of the admin user
```

## get-contexts

```shell
# List all contexts (clusters)
kubectl config get-contexts
```

## current-context

```shell
# View current context
kubectl config current-context
```

## use-context

```shell
# Select a context
kubectl config use-context "context-name"
```

## set-cluster

- Set cluster

```shell
kubectl config set-cluster <cluster-name> \
  --server <url> \
  --insecure-skip-tls-verify true
```

## set-credentials

- Set user

```shell
kubectl config set-credentials "user-name" --token="token"
```

## set-context

- Set context, set a default namespace, make it currently in use

```shell
kubectl config set-context "context-name" --cluster="cluster" --user="user" --namespace="namespace" --current
```

## ~/.kube/config

```shell
# Linux/Mac (bash)
export KUBECONFIG="/home/hvitoi/Documents/kubeconfig.yaml"
```

```cmd
rem Windows (cmd)
export KUBECONFIG="C:\Users\A0000000\Documents\kubeconfig.yaml"
```

```powershell
# Windows (powershell)
$env:KUBECONFIG="C:\Users\A0000000\Documents\kubeconfig.yaml"
```
