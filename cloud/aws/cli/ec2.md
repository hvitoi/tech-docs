# ec2

## describe-instances

```shell
# list ec2 instances
aws ec2 describe-instances

# concise output
aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId, State.Name]' --output table
```
