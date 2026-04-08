# aws route53

## list-hosted-zones

```shell
aws route53 list-hosted-zones \
  --query "HostedZones[?contains(Name, 'awesome.hvitoi.com')]"
```

## list-resource-record-sets

- On the record set you can find the targets (e.g., Load Balancers)

```shell
HOSTED_ZONE_ID=/hostedzone/Z034210386YZ1ETJ4D2Z
aws route53 list-resource-record-sets \
  --hosted-zone-id $HOSTED_ZONE_ID \
  --query "ResourceRecordSets[?contains(Name, 'staging-global-grafana-mcp')]"
```
