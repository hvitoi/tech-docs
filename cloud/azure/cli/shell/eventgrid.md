# eventgrid

```shell
# Create topic
az eventgrid topic create \
  --name "my-topic" \
  -l "East US" \
  -g "demo-rg"

# Subscribe to a topic
az eventgrid event-subscription create \
  --name "demoViewerSub" \
  --source-resource-id "/subscriptions/subscription-id/resourceGroups/demo-rg/providers/Microsoft.EventGrid/topics/my-topic" \
  --endpoint-type "servicebusqueue" \ # subscribe to a service bus queue
  --endpoint "www.my-website/api/updates"

# Create messages
endpoint=$(az eventgrid topic show --name $myTopicName -g az204-egdemo-rg --query "endpoint" --output tsv)

key=$(az eventgrid topic key list --name $myTopicName -g az204-egdemo-rg --query "key1" --output tsv)

event='[
  {
    "id": "1234",
    "eventType": "recordInserted",
    "subject": "myapp/vehicles/motorcycles",
    "eventTime": "'`date +%Y-%m-%dT%H:%M:%S%z`'",
    "data":{
      "make": "Contoso",
      "model": "Northwind"
    },
    "dataVersion": "1.0"
  }
]'

curl -X POST -H "aeg-sas-key:$key" -d "$event" $endpoint
```
