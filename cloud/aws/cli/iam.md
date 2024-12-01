# aws iam

## Account

### list-account-aliases

```shell
aws iam list-account-aliases --query "AccountAliases[0]" --output text
```

## Users

### list-users

```shell
aws iam list-users
```

## Groups

### list-groups

```shell
aws iam list-groups
```

## Policies

### list-policies

```shell
aws iam list-policies
```

### get-policy

```shell
# get a managed policy
aws iam get-policy --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess

# get a customer managed policy
aws iam get-policy --policy-arn arn:aws:iam::123456789012:policy/casual-dev

# With aws account
set AWS_ACCOUNT (aws sts get-caller-identity --query 'Account' --output text)
aws iam get-policy --policy-arn arn:aws:iam::$AWS_ACCOUNT:policy/my-policy
```

### create-policy

```shell
aws iam create-policy \
  --policy-name AWSLoadBalancerControllerIAMPolicy \
  --policy-document file://iam_policy.json
```

## Roles

### list-roles

```shell
aws iam list-roles
```

### get-role

```shell
aws iam get-role --role-name henrique.vitoi-dev-role
```

### list-attached-role-policies

- List `managed policies` attached to the specified role

```shell
aws iam list-attached-role-policies --role-name henrique.vitoi-dev-role
```

### list-role-policies

- List `inline policies` attached to the specified role
- Inline policies are policies that are embedded directly in the role

```shell
aws iam list-role-policies --role-name henrique.vitoi-dev-role
```

### create-role

```shell
aws iam create-role \
  --role-name AmazonEKS_EBS_CSI_DriverRole \
  --assume-role-policy-document "file://aws-ebs-csi-driver-trust-policy.json"
```

### attach-role-policy

- Attach a `managed policy` to a role

```shell
aws iam attach-role-policy \
  --role-name "MyRole" \
  --policy-arn "arn:aws:iam::aws:policy/service-role/AmazonEBSCSIDriverPolicy"
```

### put-role-policy

- Attach an `inline policy` to a role

```shell
aws iam put-role-policy \
  --role-name MyRole \
  --policy-name MyInlinePolicy \
  --policy-document file://policy.json
```
