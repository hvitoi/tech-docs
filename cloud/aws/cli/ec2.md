# aws ec2

## describe-instances

```shell
# list ec2 instances
aws ec2 describe-instances

# concise output
aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId, State.Name]' --output table
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
