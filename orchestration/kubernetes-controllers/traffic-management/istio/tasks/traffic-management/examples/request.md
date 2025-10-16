# Request

```shell
export POD=$(kubectl get pods -l app.kubernetes.io/name=kenos -o 'jsonpath={.items[0].metadata.name}')
kubectl exec "$POD" -c nu-kenos -- /usr/bin/env curl -s https://postman-echo.com/delay/1
```
