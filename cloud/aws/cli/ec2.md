# aws ec2

## describe-instances

```shell
# list ec2 instances
aws ec2 describe-instances

# concise output
aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId, State.Name]' --output table
```

## describe-spot-instance-requests

```shell
aws ec2 describe-spot-instance-requests \
  --filters Name=launched-availability-zone,Values=us-west-1c
```

## describe-availability-zones

```shell
# get AZs in a region
aws ec2 describe-availability-zones \
    --query "AvailabilityZones[*].[ZoneId]"

# get zoneId of a given AZ
aws ec2 describe-availability-zones \
    --filters "Name=zone-name,Values=us-east-1a" \
    --query "AvailabilityZones[*].[ZoneId]" \
    --output text
```

## create-key-pair

- Creates a `ssh key pair` to access the ec2 instances
- By default creates an `rsa` key-pair (public + private)
- It returns only the private key in the response (`BEGIN RSA PRIVATE KEY`)

```shell
aws ec2 create-key-pair \
  --key-name "my-key-pair" \
  --query 'KeyMaterial' \
  --output text > private-key.pem
```

## Security Group

### create-security-group

- Newly created security group has `no inbound rules` and a default `outbound rule allowing all traffic`
- Use `authorize-security-group-ingress` and `authorize-security-group-egress` commands to customize the rules

```shell
aws ec2 create-security-group \
    --group-name MySecurityGroup \
    --description "My security group description" \
    --vpc-id vpc-123abc456def789gh
```

### authorize-security-group-ingress

```shell
aws ec2 authorize-security-group-ingress \
    --group-id sg-123abc456def789gh \
    --protocol tcp \
    --port 22 \
    --cidr 0.0.0.0/0
```

### authorize-security-group-egress

```shell
aws ec2 authorize-security-group-egress \
    --group-id sg-123abc456def789gh \
    --protocol tcp \
    --port 80 \
    --cidr 0.0.0.0/0
```

### describe-security-groups

```shell
aws ec2 describe-security-groups --group-ids sg-123abc456def789gh
```
