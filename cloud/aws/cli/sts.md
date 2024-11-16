# aws sts

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

## assume-role-with-saml

- To get the `saml-assertion`, go to the IdP dashboard (e.g., Okta) and click on the AWS app. This will perform a POST request to `https://signin.aws.amazon.com/saml` with the saml assertion. Pick the `SAMLResponse` from the request body, this is the base64 encoded saml assertion.
- The token from the saml assertion must be redeemed within 5 minutes of issuance

```shell
aws sts assume-role-with-saml \
  --role-arn "arn:aws:iam::123456789012:role/YourRoleName" \
  --principal-arn "arn:aws:iam::123456789012:saml-provider/YourOktaProviderName" \
  --saml-assertion "$(cat saml-assertion.txt)" > temp-credentials.json
```

```json
// temp-credentials.json
{
  "Credentials": {
    "AccessKeyId": "...",
    "SecretAccessKey": "...",
    "SessionToken": "...",
    "Expiration": "2024-11-16T16:57:39+00:00"
  },
  "AssumedRoleUser": {
    "AssumedRoleId": "1234:henrique.vitoi",
    "Arn": "arn:aws:sts::123456789012:assumed-role/my-role/henrique.vitoi"
  },
  "Subject": "henrique.vitoi",
  "SubjectType": "urn:oasis:names:tc:SAML:1.1:nameid-format:x509SubjectName",
  "Issuer": "http://www.okta.com/asdf",
  "Audience": "https://signin.aws.amazon.com/saml",
  "NameQualifier": "..."
}
```

```shell
export AWS_ACCESS_KEY_ID=$(jq -r '.Credentials.AccessKeyId' temp-credentials.json)
export AWS_SECRET_ACCESS_KEY=$(jq -r '.Credentials.SecretAccessKey' temp-credentials.json)
export AWS_SESSION_TOKEN=$(jq -r '.Credentials.SessionToken' temp-credentials.json)

cat >> ~/.aws/credentials <<EOL
[default]
aws_access_key_id = $AWS_ACCESS_KEY_ID
aws_secret_access_key = $AWS_SECRET_ACCESS_KEY
aws_session_token = $AWS_SESSION_TOKEN
EOL
```
