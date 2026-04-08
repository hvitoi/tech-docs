# Finding a resource out of a hostname

```shell
# Get the ip of hostname
nslookup myservice.awesome.hvitoi.com

# Get the Hosted Zone
aws route53 list-hosted-zones --query "HostedZones[?contains(Name, 'awesome.hvitoi.com')]"

# Get the Record Set (and the DNS of the target LB)
ZONE_ID=/hostedzone/Z034210386YZ1ETJ4D2Z
aws route53 list-resource-record-sets \
  --hosted-zone-id $ZONE_ID \
  --query "ResourceRecordSets[?contains(Name, 'myservice')]"

# Get all LBs and grep by the DNS_NAME
aws elbv2 describe-load-balancers \
  --query "LoadBalancers[*].[LoadBalancerName,DNSName,Scheme,Type]" \
  --output table

# Check ingresses across all namespaces
kubectl get ingress -A -o wide | grep -i myservice

# Check LoadBalancer services
kubectl get svc -A --field-selector spec.type=LoadBalancer | grep -i myservice
```
