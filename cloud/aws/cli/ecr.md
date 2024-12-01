# aws ecr

## create-repository

```shell
aws ecr create-repository \
  --repository-name alpine-linux
```

## get-login-password

- Generates an authentication token to be used to login in docker cli
- The token is your credential and it is tied to the account/role that generated the token
- It can be used to login in any ECR registry (as long as the registry allows the account/role that generated this token)

```shell
# get ECR token
aws ecr get-login-password --region us-east-1

# complete flow
set ecr_registry 123456789012.dkr.ecr.us-east-1.amazonaws.com
aws ecr get-login-password | docker login "$ecr_registry" --username AWS --password-stdin
docker build -t "$ecr_registry/my-app:1.0.0" .
docker push "$ecr_registry/my-app:1.0.0"
```
