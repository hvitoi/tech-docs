# AWS::EC2::EIP

- Specifies an `Elastic IP` (EIP) address and can, optionally, associate it with an Amazon EC2 instance.
- If you release an Elastic IP address, you might be able to recover it. You cannot recover an Elastic IP address that you released after it is allocated to another AWS account

```yaml
Type: AWS::EC2::EIP
Properties:
  Domain: String
  InstanceId: String
  PublicIpv4Pool: String
  Tags:
    - Tag
```
