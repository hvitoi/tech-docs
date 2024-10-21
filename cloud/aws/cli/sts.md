# sts

## get-caller-identity

- Returns the ARN of the `IAM entity` that's configured for the AWS CLI (an assumed role, a user, a role, etc)

```txt
arn:aws:sts::123456789012:assumed-role/my-role/<sub>
arn:aws:iam::123456789012:user/ClusterAdmin
```

```shell
# get the identity of the configured user making the request
aws sts get-caller-identity

# The AWS Account Id
aws sts get-caller-identity --query 'Account' --output text
```

## get-session-token

- Get a new security token
- Returns temporary security credentials for an AWS CLI session

```shell
aws sts get-session-token --duration-seconds 3600
```
