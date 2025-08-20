# gimme-aws-creds

- Obtain AWS temporary credentials using Okta IdP via SAML
- <https://github.com/Nike-Inc/gimme-aws-creds>
- It's an alternative to the official java CLI tool
- It modifies the file `~/.aws/credentials`

## Config

- The okta configuration has the following shape
- To set-up the configuration run `gimme-aws-creds --action-configure`

```conf
# ~/.okta_aws_login_config
[DEFAULT]
okta_org_url = <org-url>
gimme_creds_server = appurl
app_url = <app-url>
okta_username = henrique.vitoi
preferred_mfa_type = token:software:totp
aws_appname = AWS
aws_rolename = all
aws_default_duration = 43200
write_aws_creds = True
resolve_aws_alias = True
cred_profile = acc

[credential-fetcher]
inherits = DEFAULT
app_url = <app-url>
```
