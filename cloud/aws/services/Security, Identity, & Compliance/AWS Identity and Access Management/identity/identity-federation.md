# Identity federation

- `Federated users` are not "real users" (AWS::IAM::User), but entities that have signed-in assuming a role (via an Identity Provider, e.g., Okta)
- Federated users can log in aws console normally (if the role permits it)
- On the console it appears as follows

```txt
Account ID: 0000-0000-0000
Federated user: my-role/my-sub

my-role/my-sub @ my-aws-account-alias
```
