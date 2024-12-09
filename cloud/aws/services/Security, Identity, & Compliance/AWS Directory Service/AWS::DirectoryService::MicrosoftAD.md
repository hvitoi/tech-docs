# AWS::DirectoryService::MicrosoftAD

- Fully managed `Microsft Active Directory` service and integrated with AWS services
- The AD users can access out of the box the AWS Management Console with their existing credentials

- **AWS Managed Microsoft AD**
  - Create your own AD in AWS
  - Manage users locally
  - Support to MFA

## Integration with on-premises AD

- It's necessary to establish a `trust connection` between the AWS Managed AD and the on-premises AD

## AD Connector

- A Gateway (proxy) to connect the Cloud AD to the on-premises AD
- Users are managed in the on-premises AD

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html>

```yaml
Type: AWS::DirectoryService::MicrosoftAD
Properties:
  CreateAlias: Boolean
  Edition: String
  EnableSso: Boolean
  Name: String
  Password: String
  ShortName: String
  VpcSettings:
    VpcSettings
```
