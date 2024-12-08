# AWS::WorkSpaces::Workspace

- Managed `Cloud Desktop`
- Great to eliminate management of on-premise `VDI` (Virtual Desktop Infrastructure)
- Integrated with AD

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html>

```yaml
Type: AWS::WorkSpaces::Workspace
Properties:
  BundleId: String
  DirectoryId: String
  RootVolumeEncryptionEnabled: Boolean
  Tags:
    - Tag
  UserName: String
  UserVolumeEncryptionEnabled: Boolean
  VolumeEncryptionKey: String
  WorkspaceProperties:
    WorkspaceProperties
```
