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
