# Workflow

## Simple

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
  generateName: very- # prefix + random hash. A static name can also be fixed
  labels:
    workflows.argoproj.io/archive-strategy: "false"
spec:
  serviceAccountName: workflow
  entrypoint: silly # First template to execute
  templates:
    - name: silly
      container: # A task
        image: alpine:latest
        command: [ls]
        args: ["-l"]
```

## Parallel

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
  generateName: parallel-
  labels:
    workflows.argoproj.io/archive-strategy: "false"
spec:
  serviceAccountName: workflow
  entrypoint: hello # First template to execute
  templates:
    - name: hello
      steps: # A sequencial task
        - - name: ls # 1st task
            template: template-ls
        - - name: sleep-a # 2nd task (parallel)
            template: template-sleep
          - name: sleep-b # 2nd task (parallel)
            template: template-sleep
        - - name: delay # 3rd task
            template: template-delay
        - - name: sleep # 4th task
            template: template-sleep
    - name: template-ls
      container: # Container task
        image: alpine
        command: [ls]
        args: ["-l"]
    - name: template-sleep
      script: # Script task
        image: alpine
        command: [sleep]
        args: ["10"]
    - name: template-delay
      suspend: # Suspend task
        duration: "600s"
```

## DAG

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
  generateName: dag-
  labels:
    workflows.argoproj.io/archive-strategy: "false"
spec:
  serviceAccountName: workflow
  entrypoint: full
  templates:
    - name: full
      dag: # Directed Acyclic Graph (Executed in parallel unless there is a dependency)
        tasks:
          - name: task-a
            template: my-task
            arguments:
              parameters:
                - name: message
                  value: This is task-a
          - name: task-b
            template: my-task
            arguments:
              parameters:
                - name: message
                  value: This is task-b
          - name: task-c
            template: my-task
            arguments:
              parameters:
                - name: message
                  value: This is task-c
          - name: task-d # Will not execute at beginning because it has dependency on "task-a"
            template: my-task
            arguments:
              parameters:
                - name: message
                  value: This is task-d
            dependencies:
              - task-a
          - name: task-e
            template: my-task
            arguments:
              parameters:
                - name: message
                  value: This is task-e
            dependencies:
              - task-a
          - name: task-f
            template: my-task
            arguments:
              parameters:
                - name: message
                  value: This is task-f
            dependencies:
              - task-a
              - task-e
          - name: task-g
            template: my-task
            arguments:
              parameters:
                - name: message
                  value: This is task-g
    - name: my-task
      inputs:
        parameters:
          - name: message
      container:
        image: alpine
        command: [echo]
        args:
          - "{{inputs.parameters.message}}"
```

## Build container image

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
  generateName: build-container-image-
  labels:
    workflows.argoproj.io/archive-strategy: "false"
spec:
  serviceAccountName: workflow
  entrypoint: build
  volumes:
    - name: kaniko-secret
      secret:
        secretName: regcred
        items:
          - key: .dockerconfigjson
            path: config.json
  templates:
    - name: build
      dag:
        tasks:
          - name: build
            templateRef:
              name: container-image
              template: build-kaniko-git
              clusterScope: true
            arguments:
              parameters:
                - name: app_repo
                  value: git://github.com/vfarcic/argo-workflows-demo
                - name: container_image
                  value: vfarcic/devops-toolkit
                - name: container_tag
                  value: "1.0.0"
```
