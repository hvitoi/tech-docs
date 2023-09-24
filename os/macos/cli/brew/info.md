# info

- Information about an app installed

```shell
brew info "aws-iam-authenticator"
```

```shell
brew info --json=v2 --installed \
    | jq -r '.formulae[]|select(any(.installed[]; .installed_on_request)).full_name'
```
