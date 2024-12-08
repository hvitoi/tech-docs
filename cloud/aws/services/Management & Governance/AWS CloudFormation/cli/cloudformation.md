# aws cloudformation

- With CloudFormation, you declare all your resources and dependencies in a template file.
- The template defines a collection of resources as a single unit called a `stack`.
- CloudFormation creates and deletes all member resources of the stack together and manages all dependencies between the resources for you.

```yaml
# ec2-template.yaml
# Simple EC2 instance
Resources:
  MyInstance:
    Type: AWS::EC2::Instance
    Properties:
      AvailabilityZone: us-east-1a
      ImageId: ami-a4c7edb2
      InstanceType: t2.micro
```

## create-stack

```shell
aws cloudformation create-stack \
  --stack-name my-stack \
  --template-body file://~/Documents/ec2-template.yaml

aws ec2 describe-instances \
  --filters "Name=tag:aws:cloudformation:stack-name,Values=my-stack"
```

## update-stack

- It's not possible to update stack in "ROLLBACK_COMPLETE" status

```shell
aws cloudformation update-stack \
  --stack-name my-stack \
  --template-body file://~/Documents/ec2-template-updated.yaml
```

## delete-stack

- Delete a stack and all its resources
- Deleted stacks are still there, just at with a `Deleted` status

```shell
aws cloudformation delete-stack --stack-name my-stack
```

## list-stacks

```shell
aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE UPDATE_COMPLETE
```

## describe-stacks

```shell
aws cloudformation describe-stacks \
  --stack-name my-stack
```

## get-template

- Get the template content for a stack

```shell
aws cloudformation get-template --stack-name my-stack
```

## list-stack-resources

- List the resources created by a stack

```shell
aws cloudformation list-stack-resources --stack-name my-stack
```
