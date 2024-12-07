# Sign In

Sign in to AWS account can be done by `user type`

## Root user email + Root user password

- Account owner & unrestricted access
- The "root user" created at the account creation is not actually an IAM user, but rather an different entity that have unrestricted access to the account
- With the sign-in method the menu shows only the account ID

## Account ID + IAM username + IAM password

- Within an account & restricted access
- Shows the account ID + the `user @ group`
- The `Account ID` (or alias) can be auto-populated by using the url <https://myaccountalias.signin.aws.amazon.com/console>

## Federated user via IdP

- User that is defined in an external IdP (e.g., okta) and logs in into AWS with an `assumed role`
