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

## assume-role

```shell
aws sts assume-role \
  --role-arn arn:aws:iam::123456789012:role/MyRole \
  --role-session-name MySession \
  --duration-seconds 900

# With MFA
aws sts assume-role \
  --role-arn arn:aws:iam::ACCOUNT_ID:role/ROLE_NAME \
  --role-session-name SESSION_NAME \
  --serial-number arn-of-the-mfa-device \
  --token-code MFA_CODE \
  --external-id EXTERNAL_ID
```

## assume-role-with-saml

- Exchange a `SAML Assertion` for a `token`
- In order to get the `Saml Assertion`, go to the IdP dashboard (e.g., Okta) and click on the AWS app. This will perform a POST request to `https://signin.aws.amazon.com/saml` with the saml assertion. Pick the `SAMLResponse` from the request body. this is the base64 encoded saml assertion.
- The token from the saml assertion must be redeemed within 5 minutes of issuance
- STS then generates `Temporary Credentials`
  - Access Key ID
  - Secret Access Key
  - Session Token
- Along with these credentials, the `assumed-role ARN` is returned

```shell
aws sts assume-role-with-saml \
  --role-arn "arn:aws:iam::123456789012:role/YourRoleName" \
  --principal-arn "arn:aws:iam::123456789012:saml-provider/YourOktaProviderName" \
  --saml-assertion "$(cat saml-assertion.txt)" \
  --duration-seconds 43200 > temp-credentials.json
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

## assume-role-with-web-identity

- Obtain `temporary credentials` for users logged with IdP
- Supports any OIDC-compatible IdP (e.g., cognito, login with google, login with facebook)

## get-session-token

- Get a new security token based on a MFA
- Obtain `temporary credentials`
- You cannot call `GetSessionToken` with session credentials

```shell
aws sts get-session-token \
  --duration-seconds 3600

# With MFA
aws sts get-session-token \
  --serial-number arn-of-the-mfa-device \
  --token-code MFA_CODE
```

## get-federation-token

- Obtain `temporary credentials` for a federated user
