# External DNS

- <https://github.com/kubernetes-sigs/external-dns>
- ExternalDNS allows you to control DNS records dynamically via Kubernetes Resources (DNS-provider-agnostic).
- Cloud Providers are integrated with Kubernetes so that when an Ingress with a new DNS is created, it is automatically registered in the `Cloud DNS Server` (E.g., DNS Zone in Azure)
- `ExternalDNS` synchronizes exposed Kubernetes Services and Ingresses with DNS providers.
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
