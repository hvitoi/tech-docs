# dynamodb

- Follow [this](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html) to run dynamo locally

## list-tables

```shell
aws dynamodb list-tables \
  --endpoint-url "http://localhost:8000"
```

## create-table

- Key schema
  - HASH (partition key)
- Capacity
  - Table read capacity units (RCUs) = 5
  - Table write capacity units (WCUs) = 5
- Global secondary index (GSI):
  - GSI_1 (5 RCUs, 5 WCUs) - Allows for querying by host IP address.

```shell
aws dynamodb create-table \
  --table-name logfile \
  --attribute-definitions "AttributeName=PK,AttributeType=S" \
                          "AttributeName=GSI_1_PK,AttributeType=S" \
  --key-schema "AttributeName=PK,KeyType=HASH" \
  --provisioned-throughput "ReadCapacityUnits=5,WriteCapacityUnits=5" \
  --tags "Key=workshop-design-patterns,Value=targeted-for-cleanup" \
  --global-secondary-indexes "IndexName=GSI_1,\
      KeySchema=[{AttributeName=GSI_1_PK,KeyType=HASH}],\
      Projection={ProjectionType=INCLUDE,NonKeyAttributes=['bytessent']},\
      ProvisionedThroughput={ReadCapacityUnits=5,WriteCapacityUnits=5}"
```

## update-table

```shell
aws dynamodb update-table \
  --table-name "logfile" \
  --provisioned-throughput "ReadCapacityUnits=100,WriteCapacityUnits=100"

aws dynamodb update-table \
  --table-name "employees" \
  --attribute-definitions "AttributeName=GSI_2_PK,AttributeType=S" \
                          "AttributeName=GSI_2_SK,AttributeType=S" \
  --global-secondary-index-updates file://gsi_manager.json # this file defines what will be created and the GSI name
```

## delete-table

```shell
aws dynamodb delete-table \
  --endpoint-url "http://localhost:8000" \
  --table-name "local-insurance-social-policies-docstore"
```

## describe-table

```shell
# Returns "ACTIVE" if so
aws dynamodb describe-table \
  --table-name "logfile" \
  --query "Table.TableStatus"

# Returns a list of GSIs and its configuration
aws dynamodb describe-table \
  --table-name "logfile" \
  --query "Table.GlobalSecondaryIndexes"

# Status of all GSIs
aws dynamodb describe-table \
  --table-name employees \
  --query "Table.GlobalSecondaryIndexes[].IndexStatus"

```

## wait

- Waits for a table to become active
- Useful after updates to table

```shell
aws dynamodb wait table-exists \
  --table-name "logfile"
```

## scan

```shell
aws dynamodb scan \
  --endpoint-url "http://localhost:8000" \
  --table-name "local-insurance-social-policies-docstore"
```

## query

```shell
aws dynamodb query \
  --table-name Foo \
  --key-condition-expression ""
```
