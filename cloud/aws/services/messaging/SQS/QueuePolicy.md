# AWS::SQS::QueuePolicy

- `SQS Access policies`: for Cross Account Access

```yaml
Type: AWS::SQS::QueuePolicy
Properties:
  PolicyDocument: Json
  Queues:
    - String
```

## PolicyDocument

```json
// S3 - SQS integration
{
  "Version": "2012-10-17",
  "Id": "example-ID",
  "Statement": [
    {
      "Sid": "example-statement-ID",
      "Effect": "Allow",
      "Principal": {
        "Service": "s3.amazonaws.com"
      },
      "Action": ["SNS:Publish"],
      "Resource": "arn:aws:sns:Region:account-id:topic-name",
      "Condition": {
        "ArnLike": { "aws:SourceArn": "arn:aws:s3:::awsexamplebucket1" },
        "StringEquals": { "aws:SourceAccount": "bucket-owner-account-id" }
      }
    }
  ]
}
```
