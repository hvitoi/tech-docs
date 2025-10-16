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

## Demo

```shell
# Deploy HTTP Server (httpbin)
kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.27/samples/httpbin/httpbin.yaml

# Apply DR to the App
kubectl apply -f destination-rule.yaml

# Deploy an HTTP Client (fortio) - this client will trip the circuit breaker of the server app
kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.27/samples/httpbin/sample-client/fortio-deploy.yaml
```

```shell
# Trigger requests!
# 2 concurrent connections, 20 requests
export FORTIO_POD=$(kubectl get pods -l app=fortio -o 'jsonpath={.items[0].metadata.name}')
kubectl exec "$FORTIO_POD" -c fortio -- /usr/bin/fortio load -c 2 -qps 0 -n 20 -loglevel Warning http://httpbin:8000/get
```
