# service

```shell
# Create Deployment Object
kubectl create deployment hello-minikube --image=kicbase/echo-server:1.0

# Create Service Object
kubectl expose deployment hello-minikube --type=NodePort --port=8080

# Port-forward the port on the service to the local host
minikube service hello-minikube

# ... same
kubectl port-forward service/hello-minikube 7080:8080
```
