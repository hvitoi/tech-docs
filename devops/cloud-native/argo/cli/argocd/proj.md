# proj

- The `default` project is available by default
- Permits deployments from any source repo, to any cluster, and all resource Kinds

```sh
argocd proj create "myproject" \
  -d "https://kubernetes.default.svc.mynamespace" \
  -s "https://github.com/argoproj/argocd-example-apps.git"
```
