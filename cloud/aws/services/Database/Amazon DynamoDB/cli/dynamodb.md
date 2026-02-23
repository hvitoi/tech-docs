# aws dynamodb

- Follow [this](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html) to run dynamo locally

## Management

### list-tables

```shell
aws dynamodb list-tables \
  --endpoint-url "http://localhost:8000"
```

### create-table

- Key schema
  - HASH (partition key)
- Capacity
  - Table read capacity units (RCUs) = 5
  - Table write capacity units (WCUs) = 5
- Global secondary index (GSI):
  - GSI_1 (5 RCUs, 5 WCUs) - Allows for querying by host IP address.

```shell
aws dynamodb create-table \
  --table-name MyLogFile \
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

### update-table

```shell
aws dynamodb update-table \
  --table-name "MyLogFile" \
  --provisioned-throughput "ReadCapacityUnits=100,WriteCapacityUnits=100"

aws dynamodb update-table \
  --table-name "Employees" \
  --attribute-definitions "AttributeName=GSI_2_PK,AttributeType=S" \
                          "AttributeName=GSI_2_SK,AttributeType=S" \
  --global-secondary-index-updates file://gsi_manager.json # this file defines what will be created and the GSI name

# Enable streams API (let you implement event-driven systems by reacting to changes in the table - event sourcing)
aws dynamodb update-table \
  --table-name Users \
  --stream-specification StreamEnabled=true,StreamViewType=NEW_IMAGE
```

### delete-table

```shell
aws dynamodb delete-table \
  --endpoint-url "http://localhost:8000" \
  --table-name "local-insurance-social-policies-docstore"
```

### describe-table

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

### wait

- Waits for a table to become active
- Useful after updates to table

```shell
aws dynamodb wait table-exists \
  --table-name "logfile"
```

## Read

### scan

- Scan the whole table to find an item
- Consumes lots of RCU
- **filter expressions** are applicable only for `scan` and `query` operations

```shell
aws dynamodb scan \
  --endpoint-url "http://localhost:8000" \
  --table-name "local-insurance-social-policies-docstore"
```

```python
import boto3
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
  client = boto3.resource('dynamodb')
  table = client.Table('MyTable')

  # filter expression can be any attribute (not only hash or sort key)
  response = table.scan(
    FilterExpression = Attr('MyKey').eq('USA')
  )

  response = table.scan(
    FilterExpression =
      Attr('MyKey').eq('USA') &
      Attr('MyKey').begins_with('2019')
  )
```

### query

- Query operations require at least a `hash key`
- It's much more efficient than a scan, because it searches only in that partition (scan reads the entire table)

- Additionally you can use `filter expressions` to query based on other fields that are not hash/range keys

```shell
aws dynamodb query \
  --table-name "Users" \
  --key-condition-expression "UserId = :id" \
  --expression-attribute-values '{":id":{"S":"123"}}'
```

```python
import boto3
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
  client = boto3.resource('dynamodb')
  table = client.Table('MyTable')

  response = table.query(
    KeyConditionExpression =
      Key('MyPartitionKey').eq('Lala') &
      Key('MySortKey ').gt('2019-01-01')
  )
```

```shell
# Query in a different index (GSI), not the main table
# querying by non-primary key, alternate access patterns
aws dynamodb query \
  --table-name Users \
  --index-name EmailIndex \
  --key-condition-expression "Email = :e" \
  --expression-attribute-values '{":e":{"S":"a@b.com"}}'
```

### get-item

- Returns ONE specific item
- Requires the `hash key` and the `range key` (if any)

```shell
aws dynamodb get-item \
  --table-name Users \
  --key '{"UserId":{"S":"123"}}'
```

```python
import boto3
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
  client = boto3.resource('dynamodb')
  table = client.Table('MyTable')

  response = table.get_item(
    Key = {
      'MyPartitionKey': 'Lala',
      'MySortKey': '2019-11-17'
    }
  )
```

## Write

### put-item

- Insert or replace an item
- Accepts **condition-expression**

```shell
aws dynamodb put-item \
  --table-name "Users" \
  --item '{
    "UserId": {"S":"123"},
    "Name": {"S":"Alice"},
    "Age": {"N":"30"}
  }'
```

```shell
aws dynamodb put-item \
  --table-name Users \
  --item '{"UserId":{"S":"123"}}' \
  --condition-expression "attribute_not_exists(UserId)"

```

### update-item

- Updates only selected attributes
- Avoids rewriting the entire item
- Accepts **update-expression** and **condition-expression**

#### SET

```shell
aws dynamodb update-item \
  --table-name "Users" \
  --key '{
    "UserId":{"S":"123"},
    "JoinedAt":{"S":"<date>"}
  }' \
  --update-expression "SET Name = :n, Age = :a, Profile.City = :c, Tags = list_append(Tags, :t)" \
  --expression-attribute-values '{
    ":n": {"S":"John"},
    ":a": {"N":"31"},
    ":c": {"S":"Berlin"},
    ":t": {"L":[{"S":"VIP"}]}
  }'

# Update only if value matches. This is optimistic locking
aws dynamodb update-item \
  --table-name Users \
  --key '{"UserId":{"S":"123"}}' \
  --update-expression "SET Age = :new" \
  --expression-attribute-values '{
    ":new":{"N":"31"},
    ":old":{"N":"30"}
  }' \
  --condition-expression "Age = :old"
  # --condition-expression "attribute_exists(UserId)"
```

#### REMOVE

```shell
aws dynamodb update-item \
  --table-name "Users" \
  --key '{"UserId":{"S":"123"}}' \
  --update-expression "REMOVE Age, Profile.City"
```

#### ADD

- If field doesn't exist it starts at 0 automatically

```shell
aws dynamodb update-item \
  --table-name "Users" \
  --key '{"UserId":{"S":"123"}}' \
  --update-expression "ADD LoginCount :n, Tags :t" \
  --expression-attribute-values '{
    ":n": {"N":"1"},
    ":t": {"SS":["VIP"]}
  }'
```

#### DELETE

- Remove a specific value from a set

```shell
aws dynamodb update-item \
  --table-name "Users" \
  --key '{"UserId":{"S":"123"}}' \
  --update-expression "DELETE Tags :t"
  --expression-attribute-values '{
    ":t": {"SS":["VIP"]}
  }'
```

### delete-item

```shell
aws dynamodb delete-item \
  --table-name Users \
  --key '{"UserId":{"S":"123"}}'
```

## Batch

- Used for multiple operations in the `same table`

### batch-get-item

```shell
aws dynamodb batch-get-item \
  --request-items '{
    "Users": {
      "Keys": [
        {"UserId":{"S":"1"}},
        {"UserId":{"S":"2"}}
      ]
    }
  }'
```

### batch-write-item

- Great for imports or migrations
- Limit: 25 items per request

```shell
aws dynamodb batch-write-item \
  --request-items '{
    "Users":[
      {"PutRequest":{"Item":{"UserId":{"S":"1"}}}},
      {"PutRequest":{"Item":{"UserId":{"S":"2"}}}},
      {"DeleteRequest":{"Key":{"UserId":{"S":"3"}}}}
    ]
  }'
```

## Transactions

- Used for multiple operations in `different tables`

### transact-get-items

```shell
aws dynamodb transact-get-items \
  --transact-items '[
    {"Get":{"TableName":"Users","Key":{"UserId":{"S":"1"}}}},
    {"Get":{"TableName":"Accounts","Key":{"AccountId":{"S":"A1"}}}}
  ]'
```

### transact-write-items

- Multiple writes succeed or fail together (in different tables)

```shell
aws dynamodb transact-write-items \
  --transact-items '[
    {
      "Put":{
        "TableName":"Users",
        "Item":{"UserId":{"S":"1"}}
      }
    },
    {
      "Update":{
        "TableName":"Accounts",
        "Key":{"AccountId":{"S":"A1"}},
        "UpdateExpression":"SET Balance = Balance - :x",
        "ExpressionAttributeValues":{":x":{"N":"10"}}
      }
    }
  ]'
```
