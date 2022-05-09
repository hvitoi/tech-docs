# AWS::S3::BucketPolicy

- <https://awspolicygen.s3.amazonaws.com/policygen.html>

- **User based**
  - `IAM policies`: permissions per user
- **Resource based**
  - `Bucket policies`: global rules
  - Object `Access Control List` (ACL): per object
  - Bucket `Access Control List` (ACL): less common

```yaml
Type: AWS::S3::BucketPolicy
Properties:
  Bucket: String
  PolicyDocument: Json
```

## PolicyDocument

```json
// bucket policy
{
  "Version": "2012-10-17",
  "Id": "S3-Read-Access",
  "Statement": [
    {
      "Sid": "PublicRead",
      "Effect": "Allow",
      "Action": ["s3:Get*", "s3:List*"],
      "Resource": "arn:aws:s3:::mybucket/*",
      "Principal": "*"
    }
  ]
}
```

- Example of policy: deny upload of object that are not encrypted
