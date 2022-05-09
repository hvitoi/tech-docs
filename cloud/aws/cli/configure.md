# configure

- Prompts:
  - Access key ID
  - Secret access key
  - Default region. E.g. sa-east-1
  - Default output format. E.g, json

```shell
aws configure
```

- Optionally you can set the environment variables
  - `AWS_ACCESS_KEY_ID`
  - `AWS_SECRET_ACCESS_KEY`

## Profiles

- Allow multiple logged-in profiles
- All further commands must be run with `--profile` flag

```shell
aws configure --profile "my-root-account"
```

## MFA

- If MFA is activated under IAM, all commands must have the `--mfa` flag

```shell
# example
aws s3 ls --mfa "arn-of-mfa-device mfa-code"
```

## Set

```shell
# set the proper signature version in order not to get issues when generating URLs for encrypted files
aws configure set "default.s3.signature_version" "s3v4"
```
