# AWS::IAM::OIDCProvider

- **Web identity**
- Allows users federated by the specified external web identity provider to assume this role to perform actions in this account

## Examples

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "sts:AssumeRoleWithWebIdentity",
      "Principal": {
        "Federated": "arn:aws:iam::123456789012:oidc-provider/oidc.eks.us-east-1.amazonaws.com/id/0123456789ABCDEF0123456789ABCDEF"
      },
      "Condition": {
        "StringEquals": {
          "oidc.eks.us-east-1.amazonaws.com/id/7B4887CC1B7841B1BAEB98263BC64B9C:aud": "sts.amazonaws.com",
          "oidc.eks.us-east-1.amazonaws.com/id/7B4887CC1B7841B1BAEB98263BC64B9C:sub": "system:serviceaccount:kube-system:aws-load-balancer-controller"
        }
      }
    }
  ]
}
```

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "sts:AssumeRoleWithWebIdentity",
      "Principal": {
        "Federated": "accounts.google.com"
      },
      "Condition": {
        "StringEquals": {
          "accounts.google.com:sub": "111296964555974010651"
        }
      }
    }
  ]
}
```

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-oidcprovider.html>

```yaml
Type: AWS::IAM::OIDCProvider
Properties:
  ClientIdList:
    - String
  Tags:
    - Tag
  ThumbprintList:
    - String
  Url: String
```
