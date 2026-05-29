# aws lambda

## create-function

```shell
aws lambda create-function \
  --function-name "ddbreplica_lambda" \
  --zip-file "fileb://ddbreplica_lambda.zip" \
  --handler "ddbreplica_lambda.lambda_handler" \
  --timeout "60" \
  --runtime "python3.7" \
  --description "Sample lambda function for dynamodb streams" \
  --role $(cat ~/workshop/ddb-replication-role-arn.txt)
```

## update-event-source-mapping

- For **poll-based** sources like `SQS`, `Kinesis`, or `DynamoDB streams`  you can disable the lambda by disabling the mapping so Lambda stops pulling messages

```shell
# find the UUID
aws lambda list-event-source-mappings --function-name my-function

# disable it - Disable the trigger (event source mapping)
aws lambda update-event-source-mapping \
  --uuid <uuid> \
  --enabled false
```

- For **push-based** sources, like `EventBridge/CloudWatch Schedule` or `API Gateway` triggers, disable the rule rather than the Lambda

```shell
aws events disable-rule --name my-rule
```
