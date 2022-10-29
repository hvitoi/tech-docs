# Operator Lifecycle Manager (OLM)

- OLM is a tool to help manage the Operators running on your cluster.

## Installation

```sh
## OLM Installation
$ curl -sL https://github.com/operator-framework/operator-lifecycle-manager/releases/download/0.16.1/install.sh | bash -s 0.16.1
```

## Deploy operators

```sh
# Strimzi
kubectl create -f https://operatorhub.io/install/strimzi-kafka-operator.yaml

# Keycloak
kubectl create -f https://operatorhub.io/install/keycloak-operator.yaml
```

## List all operators deployed

```sh
# List ClusterServiceVersion (CSV)
kubectl get csv --all-namespaces

# List Subscription
kubectl get subscription --all-namespaces
```

## Uninstall operators

```sh
CSV=kubectl delete subscription `subscription-name` -n `namespace` -o json | jq '.status.installedCSV'
kubectl delete subscription `subscription-name` -n `namespace`
kubectl delete csv $CSV -n `namespace`
```
