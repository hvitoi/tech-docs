# AWS::CodeBuild::Project

- Testing/Build Server
- `Continuous Integration`
- Similar to Jenkins

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
