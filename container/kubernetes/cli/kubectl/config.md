# config

## view

- Default context is stored at `~/.kube/config` and it must have `600` permission

```sh
# Show kubeconfig
kubectl config view
kubectl config view -o jsonpath='{.users[?(@.name == "admin")].user.password}' # get user + password of the admin user
```

## set-credentials, set-cluster, set-context

```sh
# Set user
kubectl config set-credentials "user-name" --token="token"

# Set cluster
kubectl config set-cluster "cluster-name" --server="url" --insecure-skip-tls-verify=true

# Set context, set a default namespace, make it currently in use
kubectl config set-context "context-name" --cluster="cluster" --user="user" --namespace="namespace" --current

# View current context
kubectl config current-context
```

## get-context

```sh
# List all contexts (clusters)
kubectl config get-contexts

# Select a context
kubectl config use-context "context-name"
```

## kubeconfig

```sh
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
