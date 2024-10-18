# sts

## get-caller-identity

- Returns the ARN of the IAM entity that's configured for the AWS CLI
- Examples

```txt
arn:aws:sts::01234567890:assumed-role/my-role/my-role
arn:aws:iam::01234567890:user/ClusterAdmin
```

```shell
# get the identity of the configured user making the request
aws sts get-caller-identity

# The AWS Account Id
aws sts get-caller-identity | jq -r '.Account'
```

## get-session-token

- Get a new security token
- Returns temporary security credentials for an AWS CLI session

```shell
aws sts get-session-token --duration-seconds 3600
```
