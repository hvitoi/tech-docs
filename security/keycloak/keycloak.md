# Keycloak

- It's an `identity provider` and `token issuer` (oauth 2)

```shell
kubectl apply -f ./keycloack.yaml
kubectl apply -f ./keycloack-ingress.yaml

# Check credentials
KEYCLOAK_URL=https://keycloak.$(minikube ip).nip.io/auth &&
echo "" &&
echo "Keycloak:                 $KEYCLOAK_URL" &&
echo "Keycloak Admin Console:   $KEYCLOAK_URL/admin" &&
echo "Keycloak Account Console: $KEYCLOAK_URL/realms/myrealm/account" &&
echo ""
```
