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
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: ingress-service
  annotations:
    kubernetes.io/ingress.class: nginx # overrides the default ingress class
spec:
  rules:
    - host: api.hvitoi.com # Only consider requests to api.hvitoi.com. When developing locally, "localhost" must be tricked into this host in /etc/hosts
      http:
        paths:
          - path: /posts/create
            backend:
              service:
                name: posts-svc
                port:
                  number: 3000
          - path: /posts
            backend:
              service:
                name: query-svc
                port:
                  number: 3000
          - path: /posts/?(.*)/comments # ?(.*) means anything
            backend:
              service:
                name: comments-svc
                port:
                  number: 3000
          - path: /?(.*) # Catch-all. It has to be at the very end.
            backend:
              service:
                name: client-svc
                port:
                  number: 3000
    - host: foo.hvitoi.com # domain name (if not specified, accept all the incoming traffic for any host)
      http:
        paths:
          - path: /?(.*) # Requests coming to /
            pathType: Prefix
            backend: # Go to ...
              service:
                name: web-service-svc
                port:
                  number: 3000
          - path: /api/?(.*) # Requests coming to /api
            pathType: Prefix
            backend: # Go to ...
              service:
                name: api-service-svc
                port:
                  number: 5000
    - host: bar.hvitoi.com
      http:
        paths:
          - backend: # all the traffic for that domain goes here
              service:
                name: web-service-svc
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
    - host: foo.hvitoi.com
      http:
        paths:
          - path: /
            backend:
              serviceName: foo-svc
              servicePort: 80
    - host: bar.hvitoi.com
      http:
        paths:
          - path: /
            backend:
              serviceName: bar-svc
              servicePort: 80
  tls:
    - hosts:
        - foo.hvitoi.com
      secretName: foo-secret
    - hosts:
        - bar.hvitoi.com
      secretName: bar-secret
```
