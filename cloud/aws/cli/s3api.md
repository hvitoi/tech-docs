# aws s3

## put-bucket-versioning

```shell
# enable MFA delete (must be logged with root account)
aws s3api put-bucket-versioning \
  --bucket "my-bucket" \
  --versioning-configuration "Status=Enabled,MFADelete=Enabled"

# disable MFA delete (must be logged with root account)
aws s3api put-bucket-versioning \
  --bucket "my-bucket" \
  --versioning-configuration "Status=Enabled,MFADelete=Disabled"
```
