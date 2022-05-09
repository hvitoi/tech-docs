# Application

## Plain yaml

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: example-app
  namespace: argocd
  finalizers:
    - resources-finalizer.argocd.argoproj.io
spec:
  project: default
  source:
    repoURL: https://github.com/hvitoi/my-app.git # repo where the plain yamls live
    targetRevision: master
    path: argo/example-app
    directory:
      recursive: true
  destination:
    server: https://kubernetes.default.svc
    namespace: test-ns
  syncPolicy:
    automated:
      prune: false
      selfHeal: false
```

## Helm chart

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: example-app
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/hvitoi/my-app.git # repo where the plain yamls live
    targetRevision: master
    helm:
      version: 3
      values: |
        image:
          tag: latest
        ingress:
          host: myhost.com
  destination:
    server: https://kubernetes.default.svc
    namespace: test-ns
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
```
