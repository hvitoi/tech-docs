# AWS::IAM::Policy

- IAM is a global service
- Defines an `identity-based inline policy`
- Always use the `grant least privilege principle` when creating policies.
  - Use IAM Access Analyzer(AWS::AccessAnalyzer::Analyzer) to help with that

## Policy Evaluation

![Policy Evaluation Logic](.images/iam-policy-evalation-logic.png)

## Policy types

- **Identity-Based Policies**
  - These policies are attached to IAM identities (user, group, or role)
  - `Managed Policy`: AWS Managed or Customer Managed (AWS::IAM::ManagedPolicy)
  - `Inline Policy`: can be created on the fly, so that the policy is created only for that entity and cannot be reused (AWS::IAM::Policy)

- **Resource-Based Policies**
  - These policies are attached to AWS resources (e.g., s3)
  - This not what AWS::IAM::Policy creates
  - `S3 Bucket Policies`
  - `SQS Queue Policies`
  - `IAM Role Trust Policies`
  - `AWS KMS Key Policies`

## Properties

- <https://docs.aws.amazon.com/pt_br/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html>

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

### PolicyDocument

- <https://awspolicygen.s3.amazonaws.com/policygen.html>
- <https://policysim.aws.amazon.com/>
- All the available actions can be found at <https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsfaultinjectionservice.html>

```json
{
  "Version": "2012-10-17",
  "Id": "S3-Read-Access", // optional
  "Statement": [
    {
      // Identifier (optional)
      "Sid": "MyStatement",

      // Effect (allow or deny)
      "Effect": "Allow",

      // Actions
      "Action": [
        "s3:Get*",
        "s3:List*"
      ],

      // Resource
      "Resource": "arn:aws:s3:::my-bucket/*", // S3 Object Level Permission (all files)

      // Principal
      "Principal": {
        "AWS": [
          "arn:aws:iam::123456789012:root" // account/user/role this policies applies to
        ]
      },

      // Condition (when this policy is in effect)
      "Condition": {
        "StringEquals": {
          "aws:RequestedRegion": [
            "eu-central-1",
            "eu-west-1"
          ],
          "ec2:ResourceTag/Project": "DataAnalytics",
          "aws:PrincipalTag/Department": "Data"
        },
        "BoolIfExists": {
          "aws:MultiFactorAuthPresent": false
        },
        "NotIpAddress": {
          "aws:SourceIp": [
            "192.0.2.0/24",
            "203.0.113.0/24"
          ]
        }
      }
    }
  ]
}

```

#### Statements

##### Effect

- **ALLOW** or **DENY**
- Explicit `DENY` effects have precedence over any `ALLOW`

##### Action

##### Resource

##### Conditions

- StringEquals, StringNotEquals, StringLike
- NumericEquals, NumericNotEquals, NumericLessThan
- DateEquals, DateNotEquals, DateLessThan
- Bool
- IpAddress, NotIpAddress
- ArnEquals, ArnLike
- Null

##### Variables

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
