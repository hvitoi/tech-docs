# AWS::EC2::InternetGateway

- Traffic going to outside internet passes through an `Internet Gateway`
- An `Internet Gateway` can only be attached to one `VPC`
- In order for EC2 instances to connect to Internet Gateway:
  - An entry in the `route table` must be added to forward 0.0.0.0/0 to the Internet Gateway
  - Instances must have public IPs
  - NACL must allow traffic out
