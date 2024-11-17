# Ingress (ing)

- It's a `Layer 7 Load Balancer` for HTTP(S) traffic
- Defines `rules for routing traffic` to different services and pods
- A `default backend` must be deployed to handle rules that did not match (default-http-backend:80)

## Ingress Features

1. `Contextpath-based routing`: hvitoi.com/app1, hvitoi.com/app2
1. `Hostname-based routing`: app1.hvitoi.com, app2.hvitoi.com
1. `TLS/SSL termination`

## Ingress Components

- **Ingress Controller**
  - Ingress solution (NGINX, GCE, Istio, HAProxy, Traefik, etc)
  - Take care of the actual routing rule
  - Configures the HTTP LB according to the ingress resources
  - The LBs can be software (internal), hardware (physical) or cloud (external)
- **Ingress Resource**
  - Set of rules to configure ingress
  - SSL/TLS terminations

## External DNS

- Cloud Providers are integrated with Kubernetes so that when an Ingress with a new DNS is created, it is automatically registered in the `Cloud DNS Server` (E.g., DNS Zone in Azure)
- `ExternalDNS` synchronizes exposed Kubernetes Services and Ingresses with DNS providers.
- [ExternalDNS](https://github.com/kubernetes-sigs/external-dns) allows you to control DNS records dynamically via Kubernetes Resources (DNS-provider-agnostic).
- In order to manage `DNS records` automatically, permissions to the external dns pods must be given (by means of a `User-assigned Managed Identity`)

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: external-dns
spec:
  strategy:
    type: Recreate
  selector:
    matchLabels:
      app: external-dns
  template:
    metadata:
      labels:
        app: external-dns
    spec:
      serviceAccountName: external-dns
      containers:
        - name: external-dns
          image: registry.opensource.zalan.do/teapot/external-dns:latest
          args:
            - --source=service
            - --source=ingress
            #- --domain-filter=example.com # (optional) limit to only example.com domains; change to match the zone created above.
            - --provider=azure
          #- --azure-resource-group=externaldns # (optional) use the DNS zones from the specific resource group
          volumeMounts:
            - name: azure-config-file
              mountPath: /etc/kubernetes
              readOnly: true
      volumes:
        - name: azure-config-file
          secret:
            secretName: azure-config-file # Azure config file with the service identity
```

## SSL

## Ingress Controller

- The Ingress Controller Pods are exposed as a single `LoadBalancer` (or NodePort)
- The Ingress Controller Pods have a single `Public IP` (must be created beforehand) - `az network public-ip create ...`
- All the external traffic now passed through one of the ingress controller replicas

```shell
# create public IP for the ingress controller pods
az network public-ip create \
  --resource-group "MC_aks-rg_aks-cluster_southcentralus" \ # must be the "nodeResourceGroup"
  --name "aks-ingress-ip" \
  --sku "Standard" \
  --allocation-method "static" \ # static IP!
  --query "publicIp.ipAddress" \
  -o "tsv"
```

```shell
helm install "ingress-controller" "ingress-nginx/ingress-nginx" \
  --namespace "ingress" --create-namespace \
  --version "3.30.0" \
  --set controller.replicaCount=3 \
  --set controller.service.externalTrafficPolicy=Local \
  --set controller.service.loadBalancerIP=000.000.000.000 \ # public IP created beforehand
  --set controller.nodeSelector."beta\.kubernetes\.io/os"=linux \ # controller must run on a linux worker
  --set defaultBackend.nodeSelector."beta\.kubernetes\.io/os"=linux # defaultbackend must run on a linux worker

# ... for nodeport (not recommended)
  --set "controller.service.type=NodePort" \
  --set "controller.service.nodePorts.https=31000" \

# .. for ssl
  --set "controller.extraArgs.enable-ssl-passthrough=""" \
  --set "controller.extraArgs.default-ssl-certificate=ingress/ingress-tls"
```

## Ingress Resource

### rewrite-target

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: ingress-service
  annotations:
    kubernetes.io/ingress.class: nginx
    nginx.ingress.kubernetes.io/rewrite-target: /$1 # Everything that gets routed is written in the form /$1 - $1 is to be specified as ?(.*)
spec:
  rules:
    - host: wear.mystore.com # domain name (if not specified, accept all the incoming traffic for all routes without matching the hostname)
      http:
        paths:
          - path: /?(.*) # Requests coming to /
            pathType: Prefix
            backend: # Go to ...
              service:
                name: web-service-clusterip
                port:
                  number: 3000
          - path: /api/?(.*) # Requests coming to /api
            pathType: Prefix
            backend: # Go to ...
              service:
                name: api-service-clusterip
                port:
                  number: 5000
    - host: watch.mystore.com # domain name
      http:
        paths:
          - backend: # all the traffic for that domain goes here
              service:
                name: web-service-clusterip
                port:
                  number: 3000
```

### use-regex

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: ingress
  annotations:
    kubernetes.io/ingress.class: nginx
    nginx.ingress.kubernetes.io/use-regex: "true"
spec:
  rules:
    - host: posts.com # Only consider requests to posts.com.'localhost' must be tricked into 'posts.com'
      http:
        paths:
          - path: /posts/create
            backend:
              service:
                name: posts-clusterip
                port:
                  number: 3000
          - path: /posts
            backend:
              service:
                name: query-clusterip
                port:
                  number: 3000
          - path: /posts/?(.*)/comments # ?(.*) means anything
            backend:
              service:
                name: comments-clusterip
                port:
                  number: 3000
          - path: /?(.*) # It has to be at the very end!
            backend:
              service:
                name: client-clusterip
                port:
                  number: 3000
```

### TLS

```yaml
apiVersion: networking.k8s.io/v1beta1
kind: Ingress
metadata:
  name: ingress-ssl
  annotations:
    kubernetes.io/ingress.class: "nginx"
    cert-manager.io/cluster-issuer: letsencrypt
spec:
  rules:
    - host: app1.hvitoi.com
      http:
        paths:
          - path: /
            backend:
              serviceName: app1-nginx-clusterip-service
              servicePort: 80
    - host: app2.hvitoi.com
      http:
        paths:
          - path: /
            backend:
              serviceName: app2-nginx-clusterip-service
              servicePort: 80
  tls:
    - hosts:
        - app1.hvitoi.com
      secretName: app1-hvitoi-secret
    - hosts:
        - app2.hvitoi.com
      secretName: app2-hvitoi-secret
```
