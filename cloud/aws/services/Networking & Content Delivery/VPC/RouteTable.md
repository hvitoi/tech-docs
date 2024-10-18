# AWS::EC2::RouteTable

- Defines how subnets get access to other `ip ranges`
- The `route table` is associated with `subnets`
- A subnet can have `multiple route tables`

- E.g., access to internet (0.0.0.0/0 dest) passes through a `gateway`

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-routetable.html>

```yaml
Type: AWS::EC2::RouteTable
Properties:
  Tags:
    - Tag
  VpcId: String
```
