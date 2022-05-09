# Mutual TLS

- K8S clusters with multiple nodes
- PCI certification for credit card is NOT appropriate mTLS

- **HTTPS** / **SSL** / **TLS**: terms interchangeably

- HTTPS
  - Client request certificate from the server (that containers the service public key)
  - Client uses the pbulic keys to say if the server is trusted or not
  - Then the TLS comes in: encrypt the data to be to the server and the response return

## Security of a cluster

- The traffic between the user browser and the load balancer is simple. But what about the communication between the service sin the cluster?
- HTTS inside the cluster how have to deal with certificates for EVERY SIMPLE POD. Without istio it would be so much trouble!

## Citadel

- `istio-citadel`: Responsible for ensuring that the proxies are all configured with the correct certificate needed to allow secure traffic between them
- The connection between container and proxy remains with the same protocol (HTTP, TCP, gRPC...) .

- `mTLS`: The proxies from client and server verify the identity of each other

## What Istio can do

1. Enforce a policy that blocks all non TLS traffic between proxies
1. AUTOMATICALLY upgrade all proxy-proxy communication to use mTLS!
1. It's already enabled by default in Istio 1.5 onwards...

- Check the security by looking at the graph in kiali/Display/Security
- It does say HTTP but it has a lock which means it's secure mTLS

## Strict vs. Permissive mTLS

- `Permissive mTLS` (default): Accept connections from a microservice without a istio proxy and that doesn't implement mTLS. For example a outside request into a NodePort
- `Strict mTLS`: Never accept the connection when the client microservice does not implement mTLS. Enforce HTTPS!
