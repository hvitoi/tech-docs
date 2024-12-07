# AWS::Organizations::OrganizationalUnit

- An `Organizational Unit` (OU) is a container for accounts that enables you to organize your accounts to apply policies according to your business requirements
- It's best practice to keep the `management account` (formerly known as "master account") under the `root OU`

![Organization Units](.images/organizations-unit.png)

## Root OU

- The `Root OU` is the parent OU for `all accounts` in an organization and `all other OUs` in the organization
- When you apply a policy to the root OU, it applies to every OU and account in the organization.
- The root OU cannot be removed

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-organizationalunit.html>

```yaml
Type: AWS::Organizations::OrganizationalUnit
Properties:
  Name: String
  ParentId: String
  Tags:
    - Tag
```
