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

## Infrastructure Composer

- Previously known as CloudFormation Designer
- Allows you to edit/create cloudformation templates
- It's a cloud-based editor with visualization (low-code) features

## Resources

- The resources created by a cloudformation template acquire some tags
  - `aws:cloudformation:logical-id`: value is the resource name defined in the template (E.g., MyResource)
  - `aws:cloudformation:stack-id`: arn of the cloudformation (E.g., arn:aws:cloudformation:us-east1:123456789012:stack/mystack/uuid)
  - `aws:cloudformation:stack-name`: name of the cloudformation (E.g., mystack)

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stack.html>

```yaml
Type: AWS::CloudFormation::Stack
Properties:
  Capabilities:
    - String
  ChangeSetId: String
  CreationTime: String
  Description: String
  DisableRollback: Boolean
  EnableTerminationProtection: Boolean
  LastUpdateTime: String
  NotificationARNs:
    - String
  Outputs:
    - Output
  Parameters:
    Key: Value
  ParentId: String
  RoleARN: String
  RootId: String
  StackId: String
  StackName: String
  StackPolicyBody: Json
  StackPolicyURL: String
  StackStatus: String
  StackStatusReason: String
  Tags:
    - Tag
  TemplateBody: Json
  TemplateURL: String
  TimeoutInMinutes: Integer
```

### TemplateURL

- A template is a yaml/json file declaring all the configuration for the desired resources

- **Template Components**
  - `Resources`: AWS resources to be created. It's the only mandatory field
  - `Parameters`: dynamic input variables
  - `Mappings`: static input variables
  - `Outputs`: reference to what has been created
  - `Conditionals`: list of conditions to performe resource creation
  - `Metadata`
  - `AWSTemplateFormatVersion`
  - `Description`

- **Template Helpers**
  - References
  - Functions

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: EC2 with Security Group and Elastic IP

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
        - !Ref MySSHSecurityGroup
        - !Ref ServerSecurityGroup

  # Elastic IP for our instance
  MyEIP:
    Type: AWS::EC2::EIP
    Properties:
      InstanceId: !Ref MyInstance

  # EC2 security group
  MySSHSecurityGroup:
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
