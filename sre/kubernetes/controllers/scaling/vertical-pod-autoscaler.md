# Vertical Pod Autoscaler (VPA)

- <https://github.com/kubernetes/autoscaler>
- Automatically Adjusts `CPU` and `Memory` reservations to help `right sizing` the application
- VPA is not natively available in the Kubernetes Cluster like HPA is. It's necessary to install it manually
- `VPA` needs the `metrics server` installed in order to watch the metrics

## VPA Components

- **VPA Admission Controller**
  - Whenever a new pod is created it calls this webhook
  - It checks whether the Pod (or its Deployment) has a configured VPA

- **VPA Recommender**
  - Connects to the Metric Server to fetch historical and current resource usage for a given vpa-enabled application
  - It generates recommendations for scaling up/down the requests and limits for these applications

- **VPA Updater**
  - Updates the resources for an application running out of the recommendation range
  - It tells the Admission Hook to change the resource settings before the pod starts
  - Runs every 1 minute

## Installation

- Check <https://github.com/kubernetes/autoscaler>

## Manifest

```yaml
apiVersion: autoscaling.k8s.io/v1beta2
kind: VerticalPodAutoscaler
metadata:
  name: my-vpa
spec:
  targetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: my-app
  resourcePolicy:
    containerPolicies:
      - containerName: "*"
        minAllowed:
          cpu: 5m
          memory: 5Mi
        maxAllowed:
          cpu: 1
          memory: 500Mi
        controlledResources: ["cpu", "memory"]
```
