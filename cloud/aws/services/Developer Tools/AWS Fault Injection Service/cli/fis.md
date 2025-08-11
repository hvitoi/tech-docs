# aws fis

## list-experiment-templates

```shell
aws fis list-experiment-templates
```

## get-experiment-template

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
        "clusterIdentifier": "arn:aws:eks:us-east-1:000000000000:cluster/foo",
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

## create-target-account-configuration

```shell
aws fis create-target-account-configuration \
  --experiment-template-id "abc" \
  --account-id "<aws-account>" \
  --role-arn "<role-arn-on-target-account>"
```

## update-experiment-template

- Updating an experiment template do not affect any running experiments that use the template

## start-experiment

```shell
aws fis start-experiment \
    --experiment-options "actionsMode=skip-all" \
    --experiment-template-id "EXTxxxxxxxxx"
```
