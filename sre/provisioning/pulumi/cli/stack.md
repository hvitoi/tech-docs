# pulumi stack

## ls

- List all stacks

```shell
pulumi stack ls
```

## select

- Switch the current workspace to the given stack

```shell
pulumi stack select "dev"
```

## output

- Get an output property of the execution of a stack

```shell
pulumi stack output "url"
```

## init

```shell
# Create a new empty stack
pulumi stack init "prod"

# Create a stack based on an existing yaml config (in this case Pulumi.foo.yaml)
pulumi stack init --copy-config-from foo --stack foo
```

## rm

```shell
pulumi stack rm "prod"
pulumi stack rm "prod" --force # remove all resources if any
```
