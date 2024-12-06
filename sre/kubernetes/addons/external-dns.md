# External DNS

- <https://github.com/kubernetes-sigs/external-dns>
- ExternalDNS allows you to manage `DNS records` dynamically via Kubernetes Resources (DNS-provider-agnostic).
- When an `Ingress` or a `Service` object with a DNS annotation (`external-dns.alpha.kubernetes.io/hostname`) is created, DNS records are automatically registered in the `Zone File` of the name server managing that domain in the cloud provider
- The `External DNS Controller` sync your Ingress/Service resource with the cloud provider

## External DNS Service Account (SA)

- The External DNS controller pods need an SA that grants permissions to manage the DNS records in the cloud

- **Azure**
  - New DNS hosts are added to `DNS Zone`
  - External DNS controller needs permissions by means of a `User-assigned Managed Identity` to manage DNS records in Azure

- **AWS**
  - The SA associated with an IAM role (IRSA)
  - The role grants access to `Route 53` service
