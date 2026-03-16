# EC2NodeClass (ec2nc)

- AWS's implementation of the VMs that Karpenter is provisioning (EC2 VM)
- Specifies AWS-specific information about the EC2 instance
- If the conditions specified in the NodeClass are not met, no EC2 will be provisioned

## Properties

### spec.amiFamily

- AMIFamily dictates the `UserData` format and default `BlockDeviceMappings`
- When the field `spec.amiSelectorTerms` is set is its only responsibility to select the AMI. `spec.amiFamily` in this case will only dictate the UserData

```yaml
apiVersion: karpenter.k8s.aws/v1
kind: EC2NodeClass
metadata:
  name: default
spec:
  amiFamily: AL2 # Amazon Linux 2
  subnetSelectorTerms:
    - tags:
        karpenter.sh/discovery: my-cluster
  securityGroupSelectorTerms:
    - tags:
        karpenter.sh/discovery: my-cluster
```

### spec.role

- IAM role of the EC2 instance

```yaml
apiVersion: karpenter.k8s.aws/v1
kind: EC2NodeClass
metadata:
  name: default
spec:
  role: KarpenterNodeRole-my-cluster
  amiSelectorTerms:
    - alias: al2@latest
  subnetSelectorTerms:
    - tags:
        karpenter.sh/discovery: my-cluster
  securityGroupSelectorTerms:
    - tags:
        karpenter.sh/discovery: my-cluster
```

### spec.blockDeviceMappings

```yaml
apiVersion: karpenter.k8s.aws/v1
kind: EC2NodeClass
metadata:
  name: default
spec:
  blockDeviceMappings:
    - deviceName: /dev/xvda
      ebs:
        volumeSize: 100Gi
        volumeType: gp3
        iops: 10000
        encrypted: true
        kmsKeyID: "1234abcd-12ab-34cd-56ef-1234567890ab"
        deleteOnTermination: true
        throughput: 125
        snapshotID: snap-0123456789
  amiSelectorTerms:
    - alias: al2@latest
  subnetSelectorTerms:
    - tags:
        karpenter.sh/discovery: my-cluster
  securityGroupSelectorTerms:
    - tags:
        karpenter.sh/discovery: my-cluster
        environment: test
```

### spec.userData

```yaml
apiVersion: karpenter.k8s.aws/v1
kind: EC2NodeClass
metadata:
  name: default
spec:
  userData: |
    echo "Hello world"
  amiSelectorTerms:
    - alias: al2@latest
  subnetSelectorTerms:
    - tags:
        karpenter.sh/discovery: my-cluster
  securityGroupSelectorTerms:
    - tags:
        karpenter.sh/discovery: my-cluster
        environment: test
```

### spec.tags

- Set tags to the EC2 instance

```yaml
apiVersion: karpenter.k8s.aws/v1
kind: EC2NodeClass
metadata:
  name: default
spec:
  tags:
    app: payment
  amiSelectorTerms:
    - alias: al2@latest
  subnetSelectorTerms:
    - tags:
        karpenter.sh/discovery: my-cluster
  securityGroupSelectorTerms:
    - tags:
        karpenter.sh/discovery: my-cluster
        environment: test
```

### Selector Terms

- Terms within the same item are treated as `OR`
- Different items are treated as `AND`

#### spec.amiSelectorTerms

- Pick a specific AMI with a seletor. In this case the `amiFamily` can be omitted
- If multiple AMIs are found, Karpenter picks only the latest one
- <https://github.com/awslabs/amazon-eks-ami>

- **AMI Families**
  - al2
  - al2023
  - bottlerocket
  - windows2019
  - windows2022

- **AMI Updates**
  - AWS publishes newest recommended AMIs for each k8s version in SSM
  - If a new AMI is released and the selector specifies the `latest` version there will be a drift and Karpenter will reconcile all the nodes
  - Similarly if you update your cluster, new AMIs will be available and there will be a drift

```yaml
apiVersion: karpenter.k8s.aws/v1
kind: EC2NodeClass
metadata:
  name: default
spec:
  amiSelectorTerms:
    - alias: al2@latest # same as setting amiFamily: AL2 (family@version)
    - alias: al2@v20240729 # pin a version
    - name: "amazon-eks-node-1.30-*" # more flexible
    - id: ami-05615bc865ff8a182
  subnetSelectorTerms:
    - tags:
        karpenter.sh/discovery: my-cluster
  securityGroupSelectorTerms:
    - tags:
        karpenter.sh/discovery: my-cluster
```

```shell
# You can use the following query to fetch the exact AMI ID
set K8S_VERSION "1.31"
aws ssm get-parameter \
  --name /aws/service/eks/optimized-ami/${K8S_VERSION}/amazon-linux-2/recommended/image_id \
  --query Parameter.Value \
  --output text
```

#### spec.subnetSelectorTerms

```yaml
apiVersion: karpenter.k8s.aws/v1
kind: EC2NodeClass
metadata:
  name: default
spec:
  amiSelectorTerms:
    - alias: al2@latest
  subnetSelectorTerms:
    # select subnets based on resource tags
    - tags:
        karpenter.sh/discovery: my-cluster
    # select subnets based on resource id
    - id: subnet-09fa4a0a8f233a921
  securityGroupSelectorTerms:
    - tags:
        karpenter.sh/discovery: my-cluster
```

#### spec.securityGroupSelectorTerms

```yaml
apiVersion: karpenter.k8s.aws/v1
kind: EC2NodeClass
metadata:
  name: default
spec:
  amiSelectorTerms:
    - alias: al2@latest
  subnetSelectorTerms:
    - tags:
        karpenter.sh/discovery: my-cluster
  securityGroupSelectorTerms:
    - tags:
        karpenter.sh/discovery: my-cluster
        environment: test
```
