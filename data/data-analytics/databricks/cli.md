# Databricks CLI

```shell
brew install databricks/tap/databricks
```

## configure

```shell
databricks configure --host https://mycompany.cloud.databricks.com/
databricks auth login --host https://mycompany.cloud.databricks.com/ # saves to ~/.databricks

```

## secrets

- Manage secrets
- `READ`: Can read secrets from the scope (recommended for most users)
- `WRITE`: Can add/update/delete secrets in the scope
- `MANAGE`: Full control (read, write, and manage permissions)

```shell
databricks secrets put-acl <scope> <principal/group/user> MANAGE
databricks secrets list-acls <scope>
```

```shell
databricks secrets list-secrets <scope>
databricks secrets put-secret <scope> <key> --string-value "<SECRET_VALUE>"

```

```python
SLACK_TOKEN = dbutils.secrets.get(scope='resilience', key='marinator-slack-api-key')
```
