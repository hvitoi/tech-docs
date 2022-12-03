# label

```shell
# Set up a label for a namespace
kubectl label "obj-kind" "obj-name" "label"
kubectl label "ns" "default" "istio-injection=enabled"
kubectl label "po" "myapp" "color=blue" --override

# Delete label
kubectl label "ns" "default" "istio-injection"- # labelname-
```
