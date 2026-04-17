# SAML 2.0 (Security Assertion Markup Language)

XML-based protocol for authentication and authorization between an identity provider (IdP) and a service provider (SP)

Actors

- `Principal` — the user
- `Service Provider (SP)` — the app the user wants to access (e.g. AWS, Salesforce)
- `Identity Provider (IdP)` — authenticates the user and issues assertions (e.g. Okta, Azure AD)

## Flow

### SP is accessed by User

- User hits the SP and it has no session
- SP builds a `AuthnRequest` and redirects the browser to the IdP (HTTP-Redirect binding, request in URL query param)

### IdP authenticates the user

- E.g., via password, MFA, existing SSO session

### IdP generates a SAML Assertion

- IdP generates a `SAML Assertion`
- This is POST'ed to the SP's ACS (Assertion Consumer Service) URL : `https://signin.aws.amazon.com/saml` via an auto-submitting form (HTTP-POST binding)
- You can inspect the SAML Assert sent in the `SAMLResponse` from the request body. this is the base64 encoded saml assertion.

- It's also possible to start the flow from this step by going to the IdP dashboard (e.g., Okta) and click on the SP app.

### SP exchange SAML Assertion for a Token

- SP validates the signature against the IdP's cert, checks Conditions and creates a local session
- The token from the saml assertion must be redeemed within 5 minutes of issuance
- On the console login, this is done on the request to `https://signin.aws.amazon.com/saml`, but here we are doing the manual process via cli, so we extracted the assertion and will manually exchange it for a token

```shell
# Get AWS token
aws sts assume-role-with-saml \
  --role-arn "arn:aws:iam::123456789012:role/YourRoleName" \
  --principal-arn "arn:aws:iam::123456789012:saml-provider/YourOktaProviderName" \
  --saml-assertion "$(cat saml-assertion.txt)" \
  --duration-seconds 43200 > temp-credentials.json
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
