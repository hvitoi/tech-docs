# servicebus

```sh
# Create service bus namespace
az servicebus namespace create \
  --resource-group "demo-rg" \
  --name "hvitoi" \
  --location "Central US" \
  --sku "Standard"

# Create a queue
az servicebus queue create \
  --resource-group "demo-rg" \
  --namespace-name "hvitoi" \
  --name "appqueue" \
  --max-size "1024"

# Create a topic
az servicebus topic create \
  --resource-group "demo-rg" \
  --namespace-name "hvitoi" \
  --name "apptopic" \
  --max-size "1024"

# Create a topic subscription
az servicebus topic subscription create \
  --resource-group "demo-rg" \
  --namespace-name "hvitoi" \
  --topic-name "apptopic" \
  --name "SubscriptionA"
```
