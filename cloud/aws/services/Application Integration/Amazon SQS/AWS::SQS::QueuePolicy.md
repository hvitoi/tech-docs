# AWS::SQS::QueuePolicy

- It's a resource-based policy
- Policy generator: <https://awspolicygen.s3.amazonaws.com/policygen.html>

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sqs-queuepolicy.html>

```yaml
Type: AWS::SQS::QueuePolicy
Properties:
  PolicyDocument: Json
  Queues:
    - String
```

### PolicyDocument

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
