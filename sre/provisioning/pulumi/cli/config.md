# pulumi config

- Manages stack's config
- It's necessary to select the stack first with `pulumi stack select`

## get

```shell
pulumi config get "foo"

# get namespaced config key
pulumi config get "my-project:my-field"
pulumi config get "aws:region"
```

## set

- Modifies the `Pulumi.*.yaml` stack config file

```shell
pulumi config set aws:region us-west-2
pulumi config set instanceCount 5

# secrets
pulumi config set dbPassword asdf --secret

# from stdin
cat pass.txt | pulumi config set dbPassword --secret

# specify the stack
pulumi config set a 1 -s dev
```
