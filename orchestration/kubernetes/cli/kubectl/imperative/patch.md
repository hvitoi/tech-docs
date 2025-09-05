# kubectl patch

```shell
# partially update node
kubectl patch "no" "my-node" \
  -p '{"spec":{"unschedulable":true}}'

# update container's image
kubectl patch "po" "my-pod" \
  -p '{"spec":{"containers":[{"name":"kubernetes-serve-hostname","image":"new image"}]}}'

# update container's image using a json patch with positional arrays
kubectl patch "po" "my-pod" \
  --type='json' \
  -p='[{"op": "replace", "path": "/spec/containers/0/image", "value":"new image"}]'

kubectl patch deployment <deployment-name> \ # increase memory
  --type='json' \
  -p='[{"op": "replace", "path": "/spec/template/spec/containers/0/resources/limits/memory", "value":"1Gi"}]' # or /requests

# disable a deployment livenessProbe using a json patch with positional arrays
kubectl patch "deploy" "my-deployment" \
  --type json \
  -p='[{"op": "remove", "path": "/spec/template/spec/containers/0/livenessProbe"}]'

# add a new element to a positional array
kubectl patch "sa" "default" \
  --type='json' \
  -p='[{"op": "add", "path": "/secrets/1", "value": {"name": "whatever" } }]'

#
kubectl patch \
  --local=true \
  --filename "topics/test.yaml" \
  --patch-file "../deploy-kafka-topics/environments/desenvolvimento.yaml" \
  --type "merge" \
  --output "yaml" \
  | kubectl apply -f -
```
