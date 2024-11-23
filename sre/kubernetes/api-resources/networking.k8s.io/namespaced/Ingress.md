# Ingress (ing)

- <https://kubernetes.io/docs/concepts/services-networking/ingress/>
- It's a `Layer 7 Load Balancer` for HTTP(S) traffic
- Defines `rules for routing traffic` to different services and pods
- A `default backend` must be deployed to handle rules that did not match (default-http-backend:80)

## Ingress Features

1. `Contextpath-based routing`: hvitoi.com/app1, hvitoi.com/app2
1. `Hostname-based routing`: app1.hvitoi.com, app2.hvitoi.com
1. `TLS/SSL termination`

## Ingress Controller

- <https://kubernetes.io/docs/concepts/services-networking/ingress-controllers>
- You must have an Ingress controller to satisfy an Ingress. Only creating an Ingress resource has no effect.
- Kubernetes as a project supports and maintains the following ingress controllers:
  - AWS: <ttps://kubernetes-sigs.github.io/aws-load-balancer-controller>
  - GCE: <https://github.com/kubernetes/ingress-gce/blob/master/README.md#readme>
  - Nginx: <https://kubernetes.github.io/ingress-nginx>
- Configures the HTTP LB according to the ingress object
- The LBs can be software (internal), hardware (physical) or cloud (external)

## Properties

### rules

```yaml
# rewrite-target
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

```yaml
# use-regex
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

### tls

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
