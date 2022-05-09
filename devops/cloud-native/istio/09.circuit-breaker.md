# Circuit breaker

- `Cascading failure`: One pod failure causes the whole system failure
- `Hystrix` is library
  - Implementation of a circuit breaker.
  - Netflix project (now abandoned). Netflix is an early adopter of the microservice architecture
  - Monitors the success rating.
  - Configurable to immediately returns an error if it's the case
  - The problem is that it must be built in every microservice! And it relies on a particular programming language
- The `Proxy` is Istio has the circuit breaker!
  - If there are consecutive failures coming from a particular pod, this proxy will stop load balancing to it! From time to time it will check the pod's health and eventually reestablish the connection
  - If there's only one replica (one pod), then the microservice itself will return error immediately (`backpressure`)

## Reasons of cascading failure

- False iamge
- Bad code
- Environment variables
- Node out of memory
- Network stack

## The application

- The are two pods for the same clusterIP. One is faulty and delays the response (and responds with 503) and the other is ok
- The circuit breaker in Istio is a `destination rule` for `outlier detection`
- To create a circuit breaker in istio we need to create a destination rule

## The Circuit breaker

- Add a timeout for a API request

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: fleetman-driver-monitoring
spec:
  hosts:
    - 2oujlno5e4.execute-api.us-east-1.amazonaws.com
  http:
    - match:
        - port: 80
      timeout: 1s
      route:
        - destination:
            host: 2oujlno5e4.execute-api.us-east-1.amazonaws.com
            port:
              number: 443
```
