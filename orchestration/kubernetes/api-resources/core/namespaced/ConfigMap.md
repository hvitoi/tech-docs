# Config Map (cm)

## Properties

### data

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-cm
data:
  FOO_KEY: foo-value
  BAR_KEY: bar-value
  config.json: |
    {
      "array": [
        1,
        2,
        3
      ],
      "boolean": true,
      "number": 123,
      "object": {
        "a": "b",
        "c": "d",
        "e": "f"
      },
      "string": "Hello World"
    }
```
