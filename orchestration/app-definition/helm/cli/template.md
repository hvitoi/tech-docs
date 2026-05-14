# template

```shell
# save the manifest files from a repo
helm template "consul" "hashicorp/consul" \
  --namespace "vault" \
  --version "0.39.0" \
  -f "consul-values.yaml" \
  > "consul.yaml"

helm template mychart \
  oci://registry-1.docker.io/<org>/<chart> \
  --version v0.5.0 \
  -f your-values.yaml > a.yaml
```
