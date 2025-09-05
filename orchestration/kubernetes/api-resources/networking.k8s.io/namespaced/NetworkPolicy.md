# NetworkPolicy (netpol)

- **Ingress** is the incoming traffic
- **Egress** is the outgoing traffic
- For example, a API receives ingress traffic on port `3000` from a front end and egress traffic on port `3306` to a mysql server

- Kubernetes by default uses `All Allow` rule, which allow `all ingress and egress ports` between services
- You can restrict ingress and egress ports by means of `Network Policies`
  - E.g., only allow ingress traffic on port 3306 from a specific pod
- The match of a `NetworkPolicy` with a `Pod` is done via labels
- If a pod has no matching NetworkPolicy, then the All Allow rule will apply

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: db-policy
  namespace: default
spec:
  podSelector:
    matchLabels:
      role: db # policy applies to this resource
  policyTypes:
    - Ingress # request originated from outside. The response is included
    - Egress # request originated from inside. The response is included
  ingress:
    - from: # 2 possibles "from" rules are defined. The resource can match one or the other (OR)
        - podSelector:
            matchLabels:
              name: api-pod
          namespaceSelector: # podSelector & namespaceSelector must match together (AND)
            matchLabels:
              name: prod
        - ipBlock:
            cidr: 192.168.5.10/32 # traffic comming from this network
      ports:
        - protocol: TCP
          port: 3306
  egress:
    - to:
        - ipBlock:
            cidr: 192.168.5.10/32
      ports:
        - protocol: TCP
          port: 80
```

- `Network Solutions` that support network policies
  - kube-router
  - calico
  - romana
  - weave-net
