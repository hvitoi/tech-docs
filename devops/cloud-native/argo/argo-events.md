# Argo Events

## Event Source

- It's where the information that is comming from
- An `Event Source` is "populated" with `Events` trigged, for example, via webhook
- E.g., git when a new code is pushed

```yaml
apiVersion: argoproj.io/v1alpha1
kind: EventSource
metadata:
  name: webhook
spec:
  service:
    ports:
      - port: 12000
        targetPort: 12000
  webhook:
    # List of events
    my-webhook:
      endpoint: /my-webhook
      method: POST
      port: "12000"
```

```sh
# Manually trigger the webhook
curl -X POST \
    -H "Content-Type: application/json" \
    -d '{"message":"My first webhook"}' \
    http://localhost:12000/my-webhook
```

## Event Bus

- `Event Bus`: bridge between event `sources` and `sensors`
- It monitors events from event source and make it available
- Sensors, on the other hand, monitors the EventBus and take an action when an event arrives

## Sensor

- An action to perform when an `Event` is triggered

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Sensor
metadata:
  name: webhook
spec:
  template:
    serviceAccountName: argo-events-sa
  dependencies:
    - name: payload # takes the payload from the event request
      eventSourceName: webhook
      eventName: my-webhook
  triggers:
    - template:
        name: payload
        k8s:
          group: ""
          version: v1
          resource: pods
          operation: create
          source:
            resource:
              apiVersion: v1
              kind: Pod
              metadata:
                generateName: payload- # names get auto filled
                labels:
                  app: payload
              spec:
                containers:
                  - name: hello
                    image: alpine
                    command: ["echo"]
                    args: ["This is the message you sent me:\n", ""] # argument of index 1 is filled with parameter
                restartPolicy: Never
          parameters:
            - src:
                dependencyName: payload
                dataKey: body.message
              dest: spec.containers.0.args.1
```
