# AWS::DirectoryService::MicrosoftAD

- Amazon implementation of `Microsoft Active Directory` (AD)
- AD is a `database of objects` (users, files, printers, etc)
- Objects are organized in `trees`, a group of trees is a `forest`

- **AWS Managed Microsoft AD**
  - Create your own AD in AWS
  - Manage users locally
  - Support to MFA
  - Establish trust connections with on-premises AD (share users)
- **AD Connector**
  - AD Gateway to proxy to on-premises AD
  - Users are managed in the on-premises AD
