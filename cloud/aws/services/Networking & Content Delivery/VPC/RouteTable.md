# AWS::EC2::RouteTable

- A `route table` defines how subnets get access to other `ip ranges` (outbound traffic)
  - Example: In a **public subnet** the `default route (0.0.0.0/0 dest)` should pass through an `Internet Gateway (igw)` (AWS::EC2::InternetGateway) so that it has access to the internet
  - Example: In a **private subnet** the `default route (0.0.0.0/0 dest)` should pass through an `NAT Gateway` (AWS::EC2::NatGateway) so that it has access to other subnets
- N `route tables` can be associated to N `subnets` (a subnet can have multiple route tables)

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-routetable.html>

```yaml
Type: AWS::EC2::RouteTable
Properties:
  Tags:
    - Tag
  VpcId: String
```
