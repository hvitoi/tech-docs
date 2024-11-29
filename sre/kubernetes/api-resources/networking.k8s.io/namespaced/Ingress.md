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

### spec.ingressClassName

- Overrides the default ingress class (defined by the IngressClass)
- This can be omitted if a default ingress class is defined
- It's a deference to an `IngressClass` object
- This deprecates an old annotation `kubernetes.io/ingress.class`

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-ing
spec:
  ingressClassName: my-aws-ingress-class
  defaultBackend:
    service:
      name: my-app-svc
      port:
        number: 80
```

### spec.defaultBackend

- It's a "catch-all" for traffic that has not matched any rule or that has not defined any rule

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-ing
spec:
  ingressClassName: my-aws-ingress-class
  defaultBackend:
    service: # service & resource are mutually exclusive
      name: my-default-nodeport-svc
      port:
        number: 80
    resource:
      apiGroup: k8s.example.com
      kind: StorageBucket
      name: static-assets
```

### spec.rules[]

- <https://kubernetes.io/docs/concepts/services-networking/ingress/#ingress-rules>

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-ing
spec:
  rules:
    - host: api.hvitoi.com # Only consider requests to api.hvitoi.com (if not specified, accept all the incoming traffic for any host)
      http:
        paths:
          # the order of the paths matter. The first matching path is the one to be picked
          - path: /posts/?(.*)/comments
            pathType: Prefix
            backend:
              service:
                name: comments-svc
                port:
                  number: 3000
          - path: /posts
            pathType: Prefix
            backend:
              service:
                name: posts-svc
                port:
                  number: 3000
          - path: /?(.*) # Catch-all (not recommended! Use spec.defaultBackend instead)
            pathType: Prefix
            backend:
              service:
                name: default-svc
                port:
                  number: 3000
```

### spec.tls[]

- Here you can set TLS encryption with your own managed certificates (from a a secret, usually generated with openssl)
- Another option is to use a `certificate management service` (e.g., AWS Certificate Manager), in this case the certificate is generated on their cloud and is set up via annotations depending on the ingress controller (e.g., alb.ingress.kubernetes.io/certificate-arn)

```yaml
apiVersion: networking.k8s.io/v1beta1
kind: Ingress
metadata:
  name: my-ing
  annotations:
    cert-manager.io/cluster-issuer: letsencrypt
spec:
  rules:
    - host: foo.hvitoi.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              serviceName: foo-svc
              servicePort: 80
    - host: bar.hvitoi.com
      http:
        paths:
          - path: /
            pathType: Prefix
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
