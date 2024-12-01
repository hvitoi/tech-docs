# AWS::CodeBuild::Project

- Testing/Build Server
- `Continuous Integration`
- Similar to Jenkins

## Permissions

- Give CodeBuild permission to interact with EKS

```json
// trust-policy.json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "eks:Describe*",
      "Resource": "*"
    }
  ]
}

```

```json
// policy.json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:root"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

```shell
set AWS_ACCOUNT (aws sts get-caller-identity --query 'Account' --output text)

# Create role to be assumed by CodeCommit
aws iam create-role \
  --role-name EksCodeBuildKubectlRole \
  --assume-role-policy-document (cat trust-policy.json)

# Add inline policy to the role
aws iam put-role-policy \
  --role-name EksCodeBuildKubectlRole \
  --policy-name eks-describe \
  --policy-document file://policy.json
```

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html>

```yaml
Type: AWS::CodeBuild::Project
Properties:
  Artifacts:
    Artifacts
  BadgeEnabled: Boolean
  BuildBatchConfig:
    ProjectBuildBatchConfig
  Cache:
    ProjectCache
  ConcurrentBuildLimit: Integer
  Description: String
  EncryptionKey: String
  Environment:
    Environment
  FileSystemLocations:
    - ProjectFileSystemLocation
  LogsConfig:
    LogsConfig
  Name: String
  QueuedTimeoutInMinutes: Integer
  ResourceAccessRole: String
  SecondaryArtifacts:
    - Artifacts
  SecondarySources:
    - Source
  SecondarySourceVersions:
    - ProjectSourceVersion
  ServiceRole: String
  Source:
    Source
  SourceVersion: String
  Tags:
    - Tag
  TimeoutInMinutes: Integer
  Triggers:
    ProjectTriggers
  Visibility: String
  VpcConfig:
    VpcConfig
```
