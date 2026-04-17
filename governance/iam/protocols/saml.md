# SAML v2

- `Security Assertion Markup Language`
- XML-based protocol for authentication and authorization between an identity provider (IdP) and a service provider (SP)
- Alternative to [OAuth 2.0 / OpenID Connect](./oauth/oauth2.md)

## Characteristics

- XML
- More mature
- More complex

## When to use

- Monoliths
- Apps with SAML support
- If you have fancy requirements

## AWS Flow Example

### Get SAML Assertion

- Obtain `temporary credentials` based on an **assumed role**
- Exchange a `SAML Assertion` for a `token`
- In order to get the `Saml Assertion`, go to the IdP dashboard (e.g., Okta) and click on the AWS app. This will perform a POST request to `https://signin.aws.amazon.com/saml` with the saml assertion. Pick the `SAMLResponse` from the request body. this is the base64 encoded saml assertion.

### Exchange SAML Assertion for Credentials

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

### Use Credentials

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
