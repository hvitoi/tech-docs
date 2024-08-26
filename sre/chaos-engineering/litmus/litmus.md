# Litmus

## Installation

```shell
helm repo add litmuschaos https://litmuschaos.github.io/litmus-helm/
helm repo list
kubectl create ns litmus
helm upgrade --install chaos litmuschaos/litmus \
  --namespace "litmus" \
  --set "portal.frontend.service.type=NodePort" \
  --set "mongodb.image.registry=ghcr.io/zcube" \
  --set "mongodb.image.repository=bitnami-compat/mongodb" \
  --set "mongodb.image.tag=6.0.5"
kubectl port-forward svc/chaos-litmus-frontend-service -n litmus 9091:9091
```

## Concepts

- **Experiment**
  - Set of chaos faults defined in a definitive sequence to achieve desired chaos impact

## Architecture

- **Control Plane**
  - Create and schedule experiments
  - Components
    - `Authentication Server`: authentication and authorization
    - `Backend server`: serves requests received from the ChaosCenter (either query the db or the execution plane)
    - `Database`: NoSQL db to store users, experiments execution, experiment templates, projects
    - `ChaosCenter`
      - WebUI
      - Litmusctl
      - Litmus API

- **Execution Plane**
  - Where the experiment configuration is stored
  - Interprets the experiment
  - Can be running in a different infrastructure/cluster
