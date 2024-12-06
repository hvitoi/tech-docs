# External DNS

- <https://github.com/kubernetes-sigs/external-dns>
- ExternalDNS allows you to manage `DNS records` dynamically via Kubernetes Resources (DNS-provider-agnostic).
- When an `Ingress` or a `Service` object with a DNS annotation (`external-dns.alpha.kubernetes.io/hostname`) is created, DNS records are automatically registered in the `Zone File` of the name server managing that domain in the cloud provider
- The `External DNS Controller` sync your Ingress/Service resource with the cloud provider

## Service Account

- The External DNS controller pods need an SA that grants permissions to manage the DNS records in the cloud provider

- **Azure**
  - New DNS hosts are added to `DNS Zone`
  - External DNS controller needs permissions by means of a `User-assigned Managed Identity` to manage DNS records in Azure

- **AWS**
  - The SA associated with an IAM role (IRSA)
  - The role grants access to `Route 53` service

## Annotations

- Annotations for Ingress and Service objects are exactly the same

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-ing
  annotations:
    # The "A" Records are added to the HostedZone
    # The "A" Records will point to the LoadBalancer's IP
    # TXT records are also added
    external-dns.alpha.kubernetes.io/hostname: foo.hvitoi.com, bar.hvitoi.com
    external-dns.alpha.kubernetes.io/ttl: 10
spec:
  ingressClassName: my-ingress-class
  defaultBackend:
    service:
      name: my-svc-nodeport
      port:
        number: 80
```
