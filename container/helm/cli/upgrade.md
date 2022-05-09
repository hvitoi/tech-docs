# upgrade

- Upgrade a release

```shell
# Upgrade config files
helm upgrade "release" "repo/chart" --set "image.tag=1.16.1-alpine"
helm upgrade "release" "/path/to/chart-folder/" --set "image.tag=1.16.1-alpine"
helm upgrade "release" "/path/to/chart-folder/" --install # Install release if it doesn't exist
helm upgrade "release" "/path/to/chart-folder/" -f "/path/to/values.yaml" # Specify values file

helm upgrade "orders" "./infra-helm-microservices/" \
  --install \
  --namespace "producao" \
  --values "values.yaml" \
  --set "image.tag=1.0.0"

## Reuse old values file
helm upgrade "my-release" "myrepo/mychart" \
  --version "3.8.0" \
  --namespace "mynamespace" \
  --debug \
  --reuse-values \
  --set "key=value"
```
