# dynamodb

- Follow [this](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html) to run dynamo locally

## list-tables

```shell
aws dynamodb list-tables \
  --endpoint-url "http://localhost:8000"
```

## scan

```shell
aws dynamodb scan \
  --endpoint-url "http://localhost:8000" \
  --table-name "local-insurance-social-policies-docstore"
```

## delete-table

```shell
aws dynamodb delete-table \
  --endpoint-url "http://localhost:8000" \
  --table-name "local-insurance-social-policies-docstore"
```
