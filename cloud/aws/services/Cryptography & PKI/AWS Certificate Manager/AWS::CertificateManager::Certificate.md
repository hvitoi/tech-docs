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

### DomainName

- Wildcard certificate: `*.hvitoi.com`
- Or a simple domain name: `foo.hvitoi.com`

### KeyAlgorithm

- RSA_1024
- RSA_2048
- RSA_3072
- RSA_4096
- EC_prime256v1
- EC_secp384r1
- EC_secp521r1

### ValidationMethod

- Before the Amazon `Certificate Authority (CA)` can issue a certificate for your site, `AWS Certificate Manager (ACM)` must prove that you own or control all of the domain names that you specify in your request
- You can choose to prove your ownership with either `Domain Name System (DNS) validation` or with `email validation` at the time you request a certificate.

- In order to validate via `DNS`, you need to add a `CNAME` record to your domain, with the with `name` and `value` provided by the certificate request. Example:
  - CNAME name: 12345abc.123acb.acm-validations.aws.
  - CNAME value: _12345abcd.test.hvitoi.com.
