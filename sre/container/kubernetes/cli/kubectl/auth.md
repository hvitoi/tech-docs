# auth

- Check if a user has permission to do something

```shell
# Current user
kubectl auth can-i "create" "deployments" -n "development"
kubectl auth can-i "delete" "nodes"

# Specific user
kubectl auth can-i "create" "deployments" --as "dev-user"
kubectl auth can-i "create" "deployments" --as "admin-user"
```
