
# STS

- `Security Token Service` (STS) is the service used to endorse the roles and get the short term credentials (temporary credentials)
- `STS` is used to create and provide `trusted users` with `temporary security credentials` that can control access to your AWS resources.
- Generate token with limited and temporary access to AWS resources. The token is valid up to 1 hour, must be refreshed after this
- Identity Providers authenticate with AWS by means of STS. Example: Okta via SAML

- APIs
  - **AssumeRole**
    - User will use a role within your account or cross-account
    ![AssumeRole](.images/sts-assume-role.png)
  - **AssumeRoleWithSaml**: return credentials for users logged in SAML
  - **AssumeRoleWitWebIdentity**: returns credentials for users logged with IdP (fb, google, etc)
  - **GetSessionToken**: for MFA
