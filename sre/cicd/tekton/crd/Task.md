# Task

```yaml
apiVersion: tekton.dev/v1beta1
kind: Task
metadata:
  name: silly
spec:
  steps: # a task is a collection of steps
    - name: silly # each task will run in a separate container
      image: alpine:latest
      command: ["ls"]
      args: ["-l", "/"]
```
