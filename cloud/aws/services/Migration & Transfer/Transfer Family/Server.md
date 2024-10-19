# AWS::Transfer::Server

- `AWS Transfer Family`
- File transfer from/to `S3` or `EFS` using FTP-family protocol
- Pay per `provisioned endpoint`/ hour + data transfer in GB

![Transfer Family](.images/transfer-family.png)

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html>

```yaml
Type: AWS::Transfer::Server
Properties:
  Certificate: String
  Domain: String
  EndpointDetails:
    EndpointDetails
  EndpointType: String
  IdentityProviderDetails:
    IdentityProviderDetails
  IdentityProviderType: String
  LoggingRole: String
  PostAuthenticationLoginBanner: String
  PreAuthenticationLoginBanner: String
  ProtocolDetails:
    ProtocolDetails
  Protocols:
    - String
  S3StorageOptions:
    S3StorageOptions
  SecurityPolicyName: String
  StructuredLogDestinations:
    - String
  Tags:
    - Tag
  WorkflowDetails:
    WorkflowDetails
```

### IdentityProviderType

- Integrate with authentication systems: `AD`, `LDAP`, `Okta`, `Amazon Cognito`, etc

### Protocols

- `FTP` (File Transfer Protocol)
- `FTPS` (File Transfer Protocol over SSL)
- `SFTP` (Secure File Transfer Protocol)
