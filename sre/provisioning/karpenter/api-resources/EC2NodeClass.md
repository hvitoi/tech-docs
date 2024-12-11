# EC2NodeClass (ec2nc)

- AWS's implementation of the VMs that Karpenter is provisioning (EC2 VM)
- Specifies AWS-specific information about the EC2 instance
- If the conditions specified in the NodeClass are not met, no EC2 will be provisioned

## Properties

### spec.amiFamily

- The VM image

```yaml
apiVersion: karpenter.k8s.aws/v1
kind: EC2NodeClass
metadata:
  name: default
spec:
  amiFamily: AL2 # Amazon Linux 2

  subnetSelectorTerms:
    - tags:
        karpenter.sh/discovery: "my-cluster"

  securityGroupSelectorTerms:
    - tags:
        karpenter.sh/discovery: "my-cluster"
```

### spec.role

- IAM role of the EC2 instance

```yaml
apiVersion: karpenter.k8s.aws/v1
kind: EC2NodeClass
metadata:
  name: default
spec:
  amiFamily: AL2
  role: KarpenterNodeRole-my-cluster

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
  amiFamily: AL2

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
  amiFamily: AL2

  userData: |
    echo "Hello world"

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
  amiFamily: AL2

  tags:
    app: payment

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

- Pick a specific AMI with a seletor
- In this case the `amiFamily` can be omitted
- You can use the following query to fetch the exact AMI ID

```shell
set K8S_VERSION "1.31"
aws ssm get-parameter \
  --name /aws/service/eks/optimized-ami/${K8S_VERSION}/amazon-linux-2/recommended/image_id \
  --query Parameter.Value \
  --output text
```

```yaml
apiVersion: karpenter.k8s.aws/v1
kind: EC2NodeClass
metadata:
  name: default
spec:
  amiSelectorTerms:
    # - id: "${ARM_AMI_ID}"
    # - id: "${AMD_AMI_ID}"
    # - id: "${GPU_OPTIMIZED_AMI_ID}"
    - name: "amazon-eks-node-1.30-*" # more flexible

  subnetSelectorTerms:
    - tags:
        karpenter.sh/discovery: my-cluster

  securityGroupSelectorTerms:
    - tags:
        karpenter.sh/discovery: my-cluster
```

#### spec.subnetSelectorTerms

```yaml
apiVersion: karpenter.k8s.aws/v1
kind: EC2NodeClass
metadata:
  name: default
spec:
  amiFamily: AL2

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
  amiFamily: AL2

  subnetSelectorTerms:
    - tags:
        karpenter.sh/discovery: my-cluster

  securityGroupSelectorTerms:
    - tags:
        karpenter.sh/discovery: my-cluster
        environment: test
```
