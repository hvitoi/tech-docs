# State Management

- Constantly compare the `actual state` to the `desired state`
- Detect `drifts` and `reconcile` as needed

## Gitops

- The desired state is defined in a `git repository`
- Tools like ArgoCD and Flux ensure that the desired state in the repo is applied to the environment

## Kubernetes

- The desired state (yaml files) are saved in `etcd`
