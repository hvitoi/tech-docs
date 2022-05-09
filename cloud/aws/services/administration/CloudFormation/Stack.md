# AWS::CloudFormation::Stack

- `Infrastructure as Code` (IaC)
- Similar to `ARM` templates in Azure, and `Terraform`
- Separation of concern
  - VPC stack
  - Network stack
  - App stack
- Template has to be uploaded to `S3` and referenced in CloudFormation
- Deployment
  - `Manual`: edit templates in CloudFormation Designer
  - `Automatic`: edit templates in yaml and deploy with CLI

```yaml
Type: AWS::CloudFormation::Stack
Properties:
  NotificationARNs:
    - String
  Parameters:
    Key: Value
  Tags:
    - Tag
  TemplateURL: String
  TimeoutInMinutes: Integer
```

## TemplateURL

- **Template Components**

  - `Resources`: AWS resources to be created
  - `Parameters`: dynamic input variables
  - `Mappings`: static input variables
  - `Outputs`: reference to what has been created
  - `Conditionals`: list of conditions to performe resource creation
  - `Metadata`

- **Template Helpers**
  - References
  - Functions

```yaml
# Single EC2 instance
Resources:
  MyInstance:
    Type: AWS::EC2::Instance
    Properties:
      AvailabilityZone: us-east-1a
      ImageId: ami-a4c7edb2
      InstanceType: t2.micro
```

```yaml
# EC2 with Security Group and Elastic IP
Parameters:
  SecurityGroupDescription:
    Description: Security Group Description
    Type: String
Resources:
  MyInstance:
    Type: AWS::EC2::Instance
    Properties:
      AvailabilityZone: us-east-1a
      ImageId: ami-a4c7edb2
      InstanceType: t2.micro
      SecurityGroups:
        - !Ref SSHSecurityGroup
        - !Ref ServerSecurityGroup
  # an elastic IP for our instance
  MyEIP:
    Type: AWS::EC2::EIP
    Properties:
      InstanceId: !Ref MyInstance
  # EC2 security group
  SSHSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Enable SSH access via port 22
      SecurityGroupIngress:
        - CidrIp: 0.0.0.0/0
          FromPort: 22
          IpProtocol: tcp
          ToPort: 22
  # Second EC2 security group
  ServerSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: !Ref SecurityGroupDescription
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 80
          ToPort: 80
          CidrIp: 0.0.0.0/0
        - IpProtocol: tcp
          FromPort: 22
          ToPort: 22
          CidrIp: 192.168.1.1/32
Outputs:
  ElasticIP:
    Description: Elastic IP Value
    Value: !Ref MyEIP
```
