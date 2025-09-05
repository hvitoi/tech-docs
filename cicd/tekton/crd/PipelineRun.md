# Pipeline

```yaml
apiVersion: tekton.dev/v1beta1
kind: PipelineRun
metadata:
  generateName: toolkit-run-
  namespace: test
spec:
  pipelineRef:
    name: toolkit # reference to the pipeline to be executed
  workspaces:
    - name: pipeline-ws
      volumeClaimTemplate:
        spec:
          resources:
            requests:
              storage: 100Mi
          accessModes:
            - ReadWriteOnce
```
