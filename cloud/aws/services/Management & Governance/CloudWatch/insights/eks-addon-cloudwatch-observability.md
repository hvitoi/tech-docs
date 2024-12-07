
# EKS Addon: CloudWatch Observability

## Components

The addon install the following components in the cluster:

- **cloudwatch-agent**
  - It exports metrics
  - It's a `DaemonSet` that runs on the EKS cluster and collects metrics from the Pods and send it to CloudWatch
  - The agent needs to be installed on the cluster otherwise it won't appear in Container Insights
  - It requires the permission `CloudWatchAgentServerPolicy` attached to the worker nodes

- **fluent-bit**
  - It exports logs

- **neuron-monitor**

- **cloudwatch-controller**

## Permissions

```shell
eksctl create iamserviceaccount \
  --name cloudwatch-agent \
  --cluster my-cluster \
  --namespace amazon-cloudwatch \
  --attach-policy-arn arn:aws:iam::aws:policy/CloudWatchAgentServerPolicy \
  --role-only \
  --approve
```

## Install Addon

- After creating the required IRSA, you can then install the EKS Addon `amazon-cloudwatch-observability`

```shell
aws eks create-addon \
  --addon-name amazon-cloudwatch-observability \
  --cluster-name my-cluster-name \
  --service-account-role-arn arn:aws:iam::123456789012:role/<role>
```

- If you use Fargate profiles, install the EKS Addon `AWS Distro for OpenTelemetry`
