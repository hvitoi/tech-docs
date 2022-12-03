# install

There are five different ways you can express the chart you want to install:

1. By chart reference: `helm install mymaria example/mariadb`
1. By path to a packaged chart: `helm install mynginx ./nginx-1.2.3.tgz`
1. By path to an unpacked chart directory: `helm install mynginx ./nginx`
1. By absolute URL: `helm install mynginx https://example.com/charts/nginx-1.2.3.tgz`
1. By chart reference and repo url: `helm install --repo https://example.com/charts/ mynginx nginx`

```shell
# Install chart from repo
helm install "repo/chart" --generate-name
helm install "release" "repo/chart" # specify a name for the release
helm install "release" "repo/chart" --namespace "namespace" --create-namespace # specify ns and create if not exists
helm install "release" "repo/chart" --dry-run --debug # Dry run & debug

# Install chart from local file
helm install "release" "/path/to/chart/"

# Install chart with custom values
helm install "release" "repo/chart" --set "version=2.0.0" --set "service.type=NodePort" # modify chart default values
helm install "release" "repo/chart" -f "values.yaml" # Apply values.yaml
helm install "release" "repo/chart" --values "values.yaml" # Apply values.yaml

# Specify chart version
helm install "release" "repo/chart" --version "0.22"

# Dry raun
helm install "release" "repo/chart" --debug --dry-run
```
