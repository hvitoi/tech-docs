# template

```shell
# save the manifest files from a repo
helm template "consul" "hashicorp/consul" \
  --namespace "vault" \
  --version "0.39.0" \
  -f "consul-values.yaml" \
  > "consul.yaml"
```
