# iam

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
aws iam get-policy --policy-arn arn:aws:iam::000000000000:policy/casual-dev

# With aws account
set AWS_ACCOUNT $(aws sts get-caller-identity --query 'Account' --output text)
aws iam get-policy --policy-arn arn:aws:iam::$AWS_ACCOUNT:policy/my-policy
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
