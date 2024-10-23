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

## init

- Create a new empty stack

```shell
pulumi stack init "prod"
```

## output

- Get an output property of the execution of a stack

```shell
pulumi stack output "url"
```
