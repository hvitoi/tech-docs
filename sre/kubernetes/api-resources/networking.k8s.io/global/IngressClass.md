# IngressClass (ingressclasses)

- There may be more than one ingress controller installed in the cluster. The ingress class defines multiple controllers (classes)

## Properties

### metadata.annotations."ingressclass.kubernetes.io/is-default-class"

- Whether this ingress class is the default one for the cluster
- If no default ingress class is defined, you need to specify the `ing/spec.ingressClassName`

```yaml
apiVersion: networking.k8s.io/v1
kind: IngressClass
metadata:
  name: my-ingress-class
  annotations:
    ingressclass.kubernetes.io/is-default-class: "true"
spec:
  controller: ingress.k8s.aws/alb
```

### spec.controller

```yaml
apiVersion: networking.k8s.io/v1
kind: IngressClass
metadata:
  name: my-ingress-class
spec:
  controller: ingress.k8s.aws/alb
```
