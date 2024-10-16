# sts

## get-caller-identity

```shell
# get the identity of the configured user making the request
aws sts get-caller-identity

# The AWS Account Id
aws sts get-caller-identity | jq -r '.Account'
```
