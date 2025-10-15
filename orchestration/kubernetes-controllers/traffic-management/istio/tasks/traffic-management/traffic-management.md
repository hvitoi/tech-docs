# Traffic management

- Traffic routing is created by means of `virtual services` and `destination rules`

- **VirtualService**
  - Allow custom routing rules to the service mesh
  - Virtual services are act in the istio-daemon. It updates all the DNS from the proxies inside all the pods
  - Virtual Services reconfigure the proxies dynamically. VS is applied upon conventional services!

- **DestinationRule**
  - A configuration for the `Istio Load Balancing` policy
  - Define subsets of pods
  - Define which pods should be part of which subset!

- Request matching
  - By header
  - By URI
  - By scheme
  - By method
  - By authority

## Canary releases

- Deploy a new version a version of a software (new image)
- If the deploy is risky, make the new image "live" for only a percentage of the time (E.g., small percentage of requests)
- Deployment alongside the old version. The old version will still be used the most part of the times
- Useful for really busy systems! Many requests and the system can't go down.
- Reduce the risk of deploying a possibly faulty component
- `Canary release` or `Staged release`
- `Bodge canary`: Not elegant way of implementing canary

## Canary release (bad implementation)

- A service pointing to two pods (a `new unknown version` and `old stable version`)
- Two pods with labels `app:staff-service`
- The old version will have more replicas! More traffic will be redirected to the old stable version

## Canary release (good implementation)

- Create weighted routing!
- The weighted routing is created by virtual services and destination rules
- `k get vs vs-name -o yaml` to generate the yaml
- `k get dr dr-name -o yaml` to generate the yaml
- On the service in istio/VirtualService (View YAML)
- On the service in istio/DestinationRules (View YAML)
- YAML with extra labels for traffic management not generated from Kiali do not allow the graphical interaction! No edit the weight for example. Deleting the rule is possible

## Sticky sessions

- Stick a session to the same version of the service (Same POD!)

  - Stick a user either to canary version or old version. And do not alternate between them

- A way to implement sticky sessions is with `Consistent Hashing`
- `Consistent Hashing`: User ID (E.g., sourceIp, httpheader, httpcookie) is used to stick the session to a Pod
  - This IP is hashed and passed to the `load balancer`
  - The load balancer use the hash to decide which target to forward to
  - `Hash` ending with `pair` goes to a pod, and ending with `odd` goes to another pod. 50% 50%
  - `Consistent Hashing` DOES NOT apply to weighted subsets - Envoy doesn't support it
- Consistent Hashing based on header properties will only work if the header is propagated across different microservices.
- Usually the property in the header is propagated starts with `x`
- A good use for consistence hashing: you do a heavy processing for a user, you want to cache that result in the pod's memory so the next time the same client requests, they get a cache hit.

## Dark release

- It's achieved by created a matching routing
- Release software before testing it first
- Staging cluster are considered to be a good practice, but it has down sides! A complete duplicate of the system!
- Dark releases are tests in live production environment
- `Dark releases` are new risky versions like canaries. The difference is that the dark releases are not accessible by a lower rate. Instead they can only be accessed by specifying a `header`
- Therefore it's only accessible to the developers using that header
- With Istio staging cluster is no longer necessary. It allows us to test in the production!
- The header propagation IS necessary

### Matching Routing

- Redirect different pods based on the header based on `Matching Routing`

- Matching can be `header`, `uri` `scheme`, `method`, `authority`
- Options are `is present`, `exact`, `prefix`, `regex`

- E.g, Only show a Dark Release Pod if the header "my-header" is exact "canary"
