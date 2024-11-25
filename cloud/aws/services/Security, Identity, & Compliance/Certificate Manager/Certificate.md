# AWS::CertificateManager::Certificate

- An `AWS Certificate Manager (ACM)` certificate that you can use to enable secure connections. For example, you can deploy an ACM certificate to an `Elastic Load Balancer` to enable HTTPS support

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html>

```yaml
Type: AWS::CertificateManager::Certificate
Properties:
  CertificateAuthorityArn: String
  CertificateTransparencyLoggingPreference: String
  DomainName: String
  DomainValidationOptions:
    - DomainValidationOption
  KeyAlgorithm: String
  SubjectAlternativeNames:
    - String
  Tags:
    - Tag
  ValidationMethod: String
```
