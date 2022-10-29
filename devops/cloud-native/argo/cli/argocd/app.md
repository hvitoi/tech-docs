# app

```sh
# create
argocd app create "app-name" \
  --repo "https://github.com/hvitoi/my-app.git" \
  --path "charts/example-chart" \
  --dest-server "https://kubernetes.default.svc" \
  --dest-namespace "default"

# change application project
argocd app set "app-name" --project "myproject"

# get
argocd app get "app-name"

# manual sync
argocd app sync "app-name" # retrieve the manifests from git and apply in the cluster
```
