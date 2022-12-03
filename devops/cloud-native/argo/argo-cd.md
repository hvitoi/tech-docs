# Argo CD

- It's a `deploy mechanism` based on `GitOps principles` and designed for `Kubernetes`
- Argo CD uses the `Declarative` deploy approach (do something until you achieve the desired state)
- Manually applying via kubectl is the `Imperative` deploy approach
- Git repository contains the manifests with the desired state, which is now the source of truth
- Argo CD uses the `pull model`

## Install

```shell
# Install with Helm Chart
helm repo add "argo" "https://argoproj.github.io/argo-helm"
helm upgrade "argocd" "argo/argo-cd" \
  --namespace "argocd" --create-namespace \
  --version "3.6.10" \
  --set "global.image.repository=my-registry:5011/quay.io/argoproj/argocd" \
  --set "global.image.tag=v2.0.3" \
  --set "dex.image.repository=my-registry:5011/ghcr.io/dexidp/dex" \
  --set "dex.image.tag=v2.27.0" \
  --set "server.ingress.enabled=true" \
  --set "server.ingress.annotations.kubernetes\.io/ingress\.class=nginx" \
  --set "server.ingress.annotations.nginx\.ingress\.kubernetes\.io/force-ssl-redirect=true" \
  --set "server.ingress.annotations.nginx\.ingress\.kubernetes\.io/ssl-passthrough=true" \
  --set "server.ingress.hosts[0]=my.dns.com.br" \
  --set "server.ingress.tls[0].secretName=argocd-tls" \
  --set "server.ingress.tls[0].hosts[0]=my.dns.com.br"
```

- Initial pass can be obtained from `argocd-initial-admin-secret`
