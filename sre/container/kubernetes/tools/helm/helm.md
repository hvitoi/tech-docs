# Helm

- Helm is a package manager for Kubernetes
- The packaging format is called `charts`: Related set of K8S resources
- Helm creates `charts` which are instructions to deploy config files
- `values.yaml` is a `configuration file` which stores the information instead of hard coding them into the config files

## Installation

```shell
# Download and install
curl -fsSL "https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3" -o "get_helm.sh"
chmod 700 "get_helm.sh"
./get_helm.sh

# Version
helm version
```

## Helm goals

- Define a common blueprint for all the microservices
- Dynamic values are replaced by placeholders (template file)

```yaml
# Template files
apiVersion: v1
kind: Pod
metadata:
  name: { { .Values.name } }
spec:
  containers:
    - name: { { .Values.container.name } }
      image: { { .Values.container.image } }
      port: { { .Values.container.port } }
```

```yaml
# Configuration file (values.yaml) - Default settings for the chart
name: my-app
container:
  name: my-app-container
  image: my-app-image
  port: 9001
```

- Template + values = Valid k8s yaml
