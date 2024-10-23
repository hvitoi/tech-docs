# pulumi config

- Modifies the `Pulumi.*.yaml` stack config file

```shell
pulumi config set aws:region us-west-2
pulumi config set instanceCount 5

# secrets
pulumi config set dbPassword asdf --secret

# specify the stack
pulumi config set a 1 -s dev
```
