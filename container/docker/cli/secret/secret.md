# Secrets

- Secrets are stored at `/run/secrets/`

```sh
# Create a secret
docker secret create "secret-name" "file"
docker secret create "psql_user" "psql_user.txt"

## Create a secret from standard input
echo "info" | docker secret create "secret-name" -
echo "mypass" | docker secret create "psql_pass" -


## List all secrets
docker secret ls

## Inspect
docker secret inspect "secret"

## Services with secrets
docker service create \
    --name psql \
    --secret psql_user \
    --secret psql_pass \
    -e POSTGRES_PASSWORD_FILE=/run/secrets/psql_pass \
    -e POSTGRES_USER_FILE=/run/secrets/psql_user \
    "postgres"
```
