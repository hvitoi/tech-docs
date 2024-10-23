# pulumi login

- Pulumi offers a PaaS to manage the stacks
- Login info is stored at `~/.pulumi/credentials.json`

```shell
# Log in to pulumi cloud
pulumi login

# Log in to a self hosted server
pulumi login https://api.pulumi.acmecorp.com

# Other object storage backends
pulumi login s3://my-pulumi-state-bucket

# Locally managed server at ~/.pulumi/
pulumi login file://~
pulumi login --local # same
```
