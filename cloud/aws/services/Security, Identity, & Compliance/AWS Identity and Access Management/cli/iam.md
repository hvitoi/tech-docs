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

### create-user

```shell
aws iam create-user \
  --user-name ses-smtp-user
```

### attach-user-policy

- Attach a policy to a user

```shell
aws iam attach-user-policy \
    --user-name ses-smtp-user \
    --policy-arn arn:aws:iam::aws:policy/AmazonSESFullAccess
```

### create-access-key

- Create access keys for a given user

```shell
aws iam create-access-key \
  --user-name ses-smtp-user
```

```json
{
  "AccessKey": {
    "UserName": "ses-smtp-user",
    "AccessKeyId": "...",
    "SecretAccessKey": "...",
    "Status": "Active",
    "CreateDate": "2024-12-05T12:00:00Z"
  }
}
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

## Service Roles

### create-service-linked-role

- Creates an IAM role that is linked to a specific AWS service
- The service itself will manage the role (including attaching new policies)

```shell
aws iam create-service-linked-role \
  --aws-service-name spot.amazonaws.com
```
