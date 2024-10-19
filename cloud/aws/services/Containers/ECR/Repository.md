# AWS::ECR::Repository

- Private `container registry`
- Pay only for what you use
- Integrated with `ECS` & `IAM`
- All container images are backed by `S3`

![ECR](.images/ecr.png)

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-repository.html>

```yaml
Type: AWS::ECR::Repository
Properties:
  EmptyOnDelete: Boolean
  EncryptionConfiguration:
    EncryptionConfiguration
  ImageScanningConfiguration:
    ImageScanningConfiguration
  ImageTagMutability: String
  LifecyclePolicy:
    LifecyclePolicy
  RepositoryName: String
  RepositoryPolicyText: Json
  Tags:
    - Tag
```
