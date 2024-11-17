# docker secret

- Secrets are stored at `/run/secrets/`

## ls

```shell
docker secret ls
```

## create

```shell
# Create a secret
docker secret create "my-secret" "pass.txt"

# Create a secret from stdin
echo "mysupersecret" | docker secret create "my-secret" -

# Services with secrets
docker service create \
    --name psql \
    --secret psql_user \
    --secret psql_pass \
    -e POSTGRES_PASSWORD_FILE=/run/secrets/psql_pass \
    -e POSTGRES_USER_FILE=/run/secrets/psql_user \
    "postgres"
```

## inspect

```shell
docker secret inspect "my-secret"
```
