# configure

- The following prompts will pop up
  - **AWS Access Key ID** (saved into `~/aws/credentials`)
  - **AWS Secret Access Key** (saved into `~/aws/credentials`)
  - **Default region name** (saved into `~/aws/config`) E.g. sa-east-1
  - **Default output format** (saved into `~/aws/config`) E.g, json

```shell
aws configure
aws configure --profile "my-profile" # configure another profile other than [default]
```

```shell
# Testing the connection
aws iam list-users
```

## Profiles

- Credentials & configs are placed at `~/.aws/`
- If `--profile` is not specified, uses the `[default]` profile
- For using a profile, all further aws commands must be run with the `--profile` flag or setting the `AWS_PROFILE` environment variable

### Config

```conf
# ~/.aws/config
[default]
region = us-east-1

[profile staging]
region = us-east-1
```

### Credentials

- Okta IdP via SAML
  - [aws-gimme-creds](https://github.com/Nike-Inc/gimme-aws-creds) can be used to obtain AWS temporary credentials

```conf
# ~/.aws/credentials
[default]
aws_access_key_id = <key-id>
aws_secret_access_key = <access-key>
aws_security_token = <security-token-base64>
aws_session_token = <session-token-base64>
x_security_token_expires = 2024-10-15T00:55:49+00:00
```

### Usage

```shell
export AWS_PROFILE=staging
export AWS_DEFAULT_PROFILE=staging
eksctl create cluster -f spot-cluster.yaml
```

## set

```shell
# set the proper signature version in order not to get issues when generating URLs for encrypted files
aws configure set "default.s3.signature_version" "s3v4"

# set default region
aws configure set "region" "us-east-2"
```
