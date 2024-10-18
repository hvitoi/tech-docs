# fis

## list-experiment-templates

```shell
aws fis list-experiment-templates
```

## create-experiment-template

```shell
aws fis create-experiment-template --cli-input-json file://fis-template.json
```

```json
// fis-template.json
{
  "description": "network-loss",
  "roleArn": "arn:aws:iam::000000000000:role/prod-green-fis-role",
  "targets": {
    "my-target-pod": {
      "resourceType": "aws:eks:pod",
      "selectionMode": "ALL",
      "parameters": {
        "clusterIdentifier": "arn:aws:eks:us-east-1:000000000000:cluster/my-cluster",
        "namespace": "default",
        "selectorType": "deploymentName",
        "selectorValue": "my-deployment",
        "targetContainerName": "my-container"
      }
    }
  },
  "actions": {
    "network-loss": {
      "actionId": "aws:eks:pod-network-packet-loss",
      "parameters": {
        "duration": "PT5M",
        "kubernetesServiceAccount": "my-service-account",
        "lossPercent": "30",
        "sources": "google.com"
      },
      "targets": {
        "Pods": "my-target-pod"
      }
    }
  },
  "stopConditions": [
    {
      "source": "none"
    }
  ],
  "experimentOptions": {
    "accountTargeting": "single-account",
    "emptyTargetResolutionMode": "fail"
  },
  "tags": {
    "Name": "network-loss"
  }
}
```
