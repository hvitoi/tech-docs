# aws ssm

## get-parameters

```shell
# Get parameters
aws ssm get-parameters \
  --names "/my-app/dev/db-url" "/my-app/dev/db-password"

# Get parameters with decryption
aws ssm get-parameters \
  --names "/my-app/dev/db-url" "/my-app/dev/db-password" \
  --with-decryption # checks if you have kms permissions to decrypt it

# Get the AMI for Kubernetes Nodes
aws ssm get-parameter \
  --name /aws/service/eks/optimized-ami/1.31/amazon-linux-2/recommended/image_id \
  --query Parameter.Value \
  --output text
```

## get-parameters-by-path

```shell
# Get parameters by path
aws ssm get-parameters-by-path \
  --path "/my-app/dev/"

# Get parameters by path recursive
aws ssm get-parameters-by-path \
  --path "/my-app/" \
  --recursive

# Get parameters by path with decryption
aws ssm get-parameters-by-path \
  --path "/my-app/" \
  --recursive \
  --with-decryption
```

## Python

```python
import json
import boto3
import os

ssm = boto3.client('ssm', region_name="eu-west-3")
environment = os.environ['ENVIRONMENT'] # dev or prd

def lambda_handler(event, context):
    db_url = ssm.get_parameters(Names=["/my-app/" + environment + "/db-url"])
    print(db_url)

    db_password = ssm.get_parameters(
        Names=["/my-app/" + environment + "/db-password"], WithDecryption=True)
    print(db_password)

    return "worked!"
```
