# AWS::CloudFormation::StackSet

- Create, update or delete stacks across `multiple accounts and regions`
- When a `stackset` is updated, all stack instances are updated throughout all accounts and regions

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html>

```yaml
Type: AWS::CloudFormation::StackSet
Properties:
  AdministrationRoleARN: String
  AutoDeployment:
    AutoDeployment
  CallAs: String
  Capabilities:
    - String
  Description: String
  ExecutionRoleName: String
  ManagedExecution:
    ManagedExecution
  OperationPreferences:
    OperationPreferences
  Parameters:
    - Parameter
  PermissionModel: String
  StackInstancesGroup:
    - StackInstances
  StackSetName: String
  Tags:
    - Tag
  TemplateBody: String
  TemplateURL: String
```
