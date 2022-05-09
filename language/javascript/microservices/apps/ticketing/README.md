# Ticketing App

## Environment variables

```bash
# JWT_KEY
kubectl create secret generic jwt-secret --from-literal JWT_KEY=any-secret

# STRIPE_KEY
kubectl create secret generic stripe-secret --from-literal STRIPE_KEY=stripe-key

# GitHub Secrets
- DOCKER_USERNAME
- DOCKER_PASSWORD
```

## Ingress Nginx

```bash
# Localhost
kubectl expose deployment ingress-nginx-controller --target-port=80 --type=ClusterIP -n kube-system

# Digital Ocean
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v0.34.1/deploy/static/provider/baremetal/deploy.yaml
```
