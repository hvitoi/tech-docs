# AWS CLI

- AWS CLI is based on the Python SDK (boto3)
- When a region is not specified in the cli, `us-east-1` is used by default
- AWS CLI is based on the python SDK

- Other SDKs
  - Java
  - .NET
  - Node.js
  - PHP
  - Python (boto3/botocore)
  - Go
  - Ruby
  - C++

## Profiles

- Credentials & configs are placed at `~/.aws/`

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
