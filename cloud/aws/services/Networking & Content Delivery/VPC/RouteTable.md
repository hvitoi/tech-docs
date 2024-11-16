# AWS::EC2::RouteTable

- N `route tables` can be associated to N `subnets` (a subnet can have multiple route tables)

- A `route table` defines how subnets get access to other `ip ranges`
  - E.g., Default route (0.0.0.0/0 dest) representing access to the outside world (internet) should pass through an `internet gateway (igw)` (AWS::EC2::InternetGateway)

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-routetable.html>

```yaml
Type: AWS::EC2::RouteTable
Properties:
  Tags:
    - Tag
  VpcId: String
```
