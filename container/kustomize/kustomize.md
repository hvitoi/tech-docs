# kustomize

- Different environment require slightly different field (E.g., namespace)
- `Kustomize` prevents recreating kubernetes manifest with small differences
- `Helm` also solves this problem, but it's an overkill!
- Kustomize works directly with kubectl, therefore it's natively supported

```sh
# Build manifests from a base folder
kustomize build "base/" # contains the kustomization.yaml
kustomize build "base/" | kubectl apply --filename -

# Edit kustomize.yaml
kustomize edit set image "argoproj/argocli=argoproj/argocli:v2.12.4"
```
