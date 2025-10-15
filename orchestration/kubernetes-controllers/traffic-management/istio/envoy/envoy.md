# Envoy

- Vanilla envoy implementation. Simple Hello world example
- /google goes to google.com
- /vdd goes to virtualpairprogramming.com

- `Reverse proxy`: The client knows it's calling a proxy (and not the final target)
- `Traditional proxy`: The client thinks it's calling the target directly! (google.com)

- Envoy provides the source code (C++) to be built
- Envoy provides docker docker images to run automatically (pre-built image) - envoyproxy/envoy

## Proxies

- **Conventional Proxy**
  - A connection middleware between the client and the server component (target)
  - A proxy (procuração): The authority to represent someone else, especially in voting
  - The proxy redirects requests to the appropriate service

- **Istio Proxy**
  - The proxies implemented in Istio comes from an open source project called `Envoy`
    - Proxy for cluster-based apps (with k8s in mind)
    - The circuit breaker logic (in the yaml file) is actually managed by Envoy
    - Envoy by itself is a low level tool, it's not easy to use. It must be used in addition to other tools for an easy management
  - Envoy is the base for Istio, so why don't use it vanilla?
    - Envoy is generic! Istio sets up the app specifically for k8s
    - Istio simplifies envoy for k8s

## Envoy vs Nginx/Apache

- Envoy is a lot more than nginx
- It offers additional functionalities
- Sometimes it's overkill and a simple nginx does the job
