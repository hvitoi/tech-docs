# Operator Lifecycle Manager (OLM)

- OLM is a tool to help manage the Operators running on your cluster.

## Installation

```shell
## OLM Installation
$ curl -sL https://github.com/operator-framework/operator-lifecycle-manager/releases/download/0.16.1/install.sh | bash -s 0.16.1
```

## Deploy operators

```shell
# Strimzi
kubectl create -f https://operatorhub.io/install/strimzi-kafka-operator.yaml

# Keycloak
kubectl create -f https://operatorhub.io/install/keycloak-operator.yaml
```

## List all operators deployed

```shell
# List ClusterServiceVersion (CSV)
kubectl get csv --all-namespaces

# List Subscription
kubectl get subscription --all-namespaces
```

## Uninstall operators

```shell
CSV=kubectl delete subscription `subscription-name` -n `namespace` -o json | jq '.status.installedCSV'
kubectl delete subscription `subscription-name` -n `namespace`
kubectl delete csv $CSV -n `namespace`
```
