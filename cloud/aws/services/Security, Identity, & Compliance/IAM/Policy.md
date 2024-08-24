# AWS::IAM::Policy

- An `inline policy` can be created on the fly, so that the policy is created only for that entity and cannot be reused

- **Policy types**
  - `AWS Managed Policy`
  - `Customer Managed Policy`
  - `Inline Policy`
  - `Resource Based Policy`

```yaml
Type: AWS::IAM::Policy
Properties:
  Groups:
    - String
  PolicyDocument: Json
  PolicyName: String
  Roles:
    - String
  Users:
    - String
```

- IAM is a global service
- `Root account` is created by default (though it's not good to use it directly)
- An account alias can be created in order to access the account (with any IAM user) from custom URI. <https://hvitoi.signin.aws.amazon.com/console>
- Access to Billing Information is not granted, even with administrator policy. For that, special config must be set up
- `Password policies` can be set for all users under `Account Settings`

![Policy Evaluation Logic](.images/iam-policy-evalation-logic.png)

## PolicyDocument

- Most of the policies are `AWS managed`
- But you can also create your own policy
- Always use the `grant least privilege` principle

- <https://awspolicygen.s3.amazonaws.com/policygen.html>
- <https://policysim.aws.amazon.com/>

- A policy is a JSON document with the following elements
  - **Effect**
  - **Resource**
  - **Conditions**
    - StringEquals, StringNotEquals, StringLike
    - NumericEquals, NumericNotEquals, NumericLessThan
    - DateEquals, DateNotEquals, DateLessThan
    - Bool
    - IpAddress, NotIpAddress
    - ArnEquals, ArnLike
    - Null
  - **Variables**
    - ${aws:username}
      - `"Resource": "arn:aws:s3:::mybucket/${aws:username}/*"`
    - **Tags**
      - AWS Specific
        - aws:CurrentTime
        - aws:TokenIssueTime
        - aws:principaltype
        - aws:SecureTransport
        - aws:SourceIp
        - aws:userid
        - ec2:SourceInstanceARN
      - Service Specific
        - s3:prefix
        - s3:max-keys
        - s3:x-amz-acl
        - sns:Endpoint
        - sns:Protocol

- Explicit `DENY` effects have precedence over any `ALLOW`

```json
// Alllow GET and LIST to S3 "my-bucket" when the user is root
{
  "Version": "2012-10-17",
  "Id": "S3-Read-Access", // optional
  "Statement": [
    {
      "Sid": "MyCustomStatement", // identifier (optional)
      "Effect": "Allow",
      "Action": ["s3:Get*", "s3:List*"],
      "Resource": "arn:aws:s3:::my-bucket/*", // S3 Object Level Permission (all files)
      "Principal": {
        "AWS": ["arn:aws:iam::123456789012:root"] // account/user/role this policies applies to
      },
      "Condition":
        // when this policy is in effect
        {
          "StringEquals": {
            "aws:RequestedRegion": ["eu-central-1", "eu-west-1"],
            "ec2:ResourceTag/Project": "DataAnalytics",
            "aws:PrincipalTag/Department": "Data"
          },
          "BoolIfExists": {
            "aws:MultiFactorAuthPresent": false
          },
          "NotIpAddress": {
            "aws:SourceIp": ["192.0.2.0/24", "203.0.113.0/24"]
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
      "Action": [
        "cloudformation:Describe*",
        "cloudformation:List*",
        "cloudformation:Get*"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "ec2:AttachVolume",
        "ec2:DetachVolume",
      ],
      "Resource": "arm:aws:ec2:*:*:instance/*",
      "Condition": {
        "StringEquals": {"ec2:ResourceType/Department": "Development"}
      }
    },
    {
      "Effect": "Allow",
      "Action": [
        "ec2:AttachVolume",
        "ec2:DetachVolume",
      ],
      "Resource": "arm:aws:ec2:*:*:volume/*",
      "Condition": {
        "StringEquals": {"ec2:ResourceTag/VolumeUser": "${aws:username}"}
      }
    }
  ]
}
```
