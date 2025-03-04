# AWS CLI

- AWS CLI is based on the Python SDK (boto3)

- The following prompts will pop up
  - **AWS Access Key ID** (saved into `~/aws/credentials`)
  - **AWS Secret Access Key** (saved into `~/aws/credentials`)
  - **Default region name** (saved into `~/aws/config`) E.g. sa-east-1
  - **Default output format** (saved into `~/aws/config`) E.g, json

- To get the `security credentials`, go to IAM -> Users -> User -> Security credentials
  - If it's an assumed role via SAML, check `aws sts assume-role-with-saml` command

```shell
aws configure # configure the [default] profile
aws configure --profile "my-profile" # configure another profile other than [default]

# Testing the connection
aws sts get-caller-identity
```

- Autocomplete: <https://docs.aws.amazon.com/cli/v1/userguide/cli-configure-completion.html>

```fish
# Autocomplete on fish
complete \
    --command aws \
    --arguments '(begin; set -lx COMP_SHELL fish; set -lx COMP_LINE (commandline); aws_completer | sed \'s/ $//\'; end)' \
    --no-files
```

## list

- Shows the current active profile

```shell
aws configure list
aws configure list --profile staging
```

## list-profiles

```shell
aws configure list-profiles
```

## set

```shell
# set the proper signature version in order not to get issues when generating URLs for encrypted files
aws configure set "default.s3.signature_version" "s3v4"

# set default region
aws configure set "region" "us-east-2"
```

## Configuration files

- Credentials & configs are placed at `~/.aws/`
- If `--profile` is not specified, uses the `[default]` profile
- For using a profile, all further aws commands must be run with the `--profile` flag or setting the `AWS_PROFILE` environment variable

### ~/.aws/config

- The default location can be overwritten with `$AWS_CONFIG_FILE`

```conf
# ~/.aws/config
[default]
region = us-east-1

[profile staging]
region = us-east-2
```

### ~/.aws/credentials

- The default location can be overwritten with `$AWS_SHARED_CREDENTIALS_FILE`

```conf
# ~/.aws/credentials
[default]
aws_access_key_id = <key-id>
aws_secret_access_key = <access-key>
aws_security_token = <security-token-base64>
aws_session_token = <session-token-base64>
x_security_token_expires = 2024-10-15T00:55:49+00:00

[profile staging]
aws_access_key_id = <key-id>
aws_secret_access_key = <access-key>
aws_security_token = <security-token-base64>
aws_session_token = <session-token-base64>
x_security_token_expires = 2024-10-15T00:55:49+00:00
```

## Configuration precedence

- <https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html#configure-precedence>

```shell
# Command line flags
aws iam list-users \
  --profile "nu-dev" \
  --region "ap-southeast-2" \
  --output "yaml"
```

```shell
# Environment variables
export AWS_PROFILE=staging # bash
set -x AWS_PROFILE staging # fish
eksctl create cluster -f spot-cluster.yaml
```

## Global flags

- `--profile`
- `--region`: us-east-1 by default if not specified anywhere
- `--output`
- `--query`

### query

```shell
aws logs get-log-events \
    --log-group-name "foo" \
    --log-stream-name "/aws/fis/$id" \
    --no-paginate \
    --query 'events[].message' \ # returns all elements in the array
    --query 'events[*].message' \ # returns all elements in the array using a wildcard notation
    --output text
```
