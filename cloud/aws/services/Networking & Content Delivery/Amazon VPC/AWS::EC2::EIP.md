# AWS::EC2::EIP

- Specifies an `Elastic IP` (EIP) address and can, optionally, associate it with an Amazon EC2 instance.

## Allocating a Static IP

- Use the command `aws ec2 allocate-address` to allocate (create) Elastic IP addresses
- This will return an `AllocationId` and a `PublicIp`

## Associate EIP with an ENI

- The EIP needs then to be associated with a Network Interface (ENI). The ENI is used by EC2 instances, Load Balancers, etc
- In case of LBs, each AZ of the LB has a different ENI

```shell
# Get ENIs from a LB
aws ec2 describe-network-interfaces \
  --filters Name=description,Values="ELB net/*"

# Associate
aws ec2 associate-address \
  --allocation-id <AllocationId> \
  --network-interface-id <NetworkInterfaceId>
```

## Deleting an EIP

- To remove an EIP you first need to `disassociate` it and then `release` it
- If you release an Elastic IP address, you might be able to recover it. You cannot recover an Elastic IP address that you released after it is allocated to another AWS account

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-eip.html>

```yaml
Type: AWS::EC2::EIP
Properties:
  Address: String
  Domain: String
  InstanceId: String
  IpamPoolId: String
  NetworkBorderGroup: String
  PublicIpv4Pool: String
  Tags:
    - Tag
  TransferAddress: String
```
