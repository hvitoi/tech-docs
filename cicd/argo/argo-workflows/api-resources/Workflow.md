# Workflow

## spec.templates[].container

- Create a task based on a container

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
    - name: silly # name of the in-line template
      container: # A task
        image: alpine:latest
        command: [ls]
        args: ["-l"]
        resources: # limit the resources
          limits:
            memory: 32Mi
            cpu: 100m
```

## spec.templates[].steps

- Instead of just running a container, this template has a sequence of steps
- Allow executing tasks in parallel

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
  generateName: steps-
spec:
  entrypoint: hello-hello-hello
  templates:
    - name: hello-hello-hello
      steps:
        - - name: hello1 # hello1 is run before the following steps
            template: print-message
            arguments:
              parameters:
                - name: message
                  value: "hello1"
        - - name: hello2a # double dash => run after previous step
            template: print-message
            arguments:
              parameters:
                - name: message
                  value: "hello2a"
          - name: hello2b # single dash => run in parallel with previous step
            template: print-message
            arguments:
              parameters:
                - name: message
                  value: "hello2b"
    - name: print-message
      inputs:
        parameters:
          - name: message
      container:
        image: busybox
        command: [echo]
        args: ["{{inputs.parameters.message}}"]
```

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
  generateName: parallel-
  labels:
    workflows.argoproj.io/archive-strategy: "false"
spec:
  serviceAccountName: workflow
  entrypoint: hello
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

## spec.templates[].dag

- Directed Acyclic Graph (DAG)
- Executed in parallel unless there is a dependency
- <https://argo-workflows.readthedocs.io/en/latest/walk-through/dag/>

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
  generateName: dag-
spec:
  serviceAccountName: workflow
  entrypoint: full
  templates:
    - name: full
      dag:
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

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
  generateName: dag-diamond-
spec:
  entrypoint: diamond
  templates:
    - name: echo
      inputs:
        parameters:
          - name: message
      container:
        image: alpine:3.23
        command: [echo, "{{inputs.parameters.message}}"]
    - name: diamond
      dag:
        tasks:
          - name: A
            template: echo
            arguments:
              parameters: [{ name: message, value: A }]
          - name: B
            dependencies: [A]
            template: echo
            arguments:
              parameters: [{ name: message, value: B }]
          - name: C
            dependencies: [A]
            template: echo
            arguments:
              parameters: [{ name: message, value: C }]
          - name: D
            dependencies: [B, C]
            template: echo
            arguments:
              parameters: [{ name: message, value: D }]
```

## spec.arguments

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
  generateName: hello-world-parameters-
spec:
  # invoke the print-message template with "hello world" as the argument to the message parameter
  entrypoint: print-message
  arguments:
    parameters:
      - name: message # name of the parameter
        value: hello world # value of the parameter
      # You can override parameters with: argo submit workflow.yaml -p message="goodbye world"

  templates:
    - name: print-message
      inputs:
        parameters:
          - name: message # parameter declaration
      container:
        image: busybox
        command: [echo]
        args: ["{{inputs.parameters.message}}"] # access the parameter

```

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
  generateName: global-parameters-
spec:
  entrypoint: A
  arguments:
    parameters:
      - name: log-level
        value: INFO

  templates:
    - name: A
      container:
        image: containerA
        env:
          - name: LOG_LEVEL
            value: "{{workflow.parameters.log-level}}"
        command: [runA]

    - name: B
      container:
        image: containerB
        env:
          - name: LOG_LEVEL
            value: "{{workflow.parameters.log-level}}"
        command: [runB]
```

## spec.volumes

```yaml
# Build container image
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
