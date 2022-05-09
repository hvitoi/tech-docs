# Pipeline

```yaml
apiVersion: tekton.dev/v1beta1
kind: Pipeline
metadata:
  name: parallel
spec:
  tasks:
    # if "runAfter" is not specified, all of the tasks will run in parallel
    - name: ls
      taskRef:
        name: task-ls # refers to tasks defined in other CRDs
    - name: sleep-a
      taskRef:
        name: task-sleep
      runAfter:
        - ls
    - name: sleep-b
      taskRef:
        name: task-sleep
      runAfter:
        - ls
    - name: echo
      taskRef:
        name: task-echo
      params:
        - name: message
          value: Finishing the pipeline
      runAfter:
        - sleep-a
        - sleep-b

---
apiVersion: tekton.dev/v1beta1
kind: Task
metadata:
  name: task-ls
spec:
  steps:
    - name: ls
      image: alpine:latest
      command: [ls]
      args: ["-l", "/"]

---
apiVersion: tekton.dev/v1beta1
kind: Task
metadata:
  name: task-sleep
spec:
  steps:
    - name: sleep
      image: alpine:latest
      script: |
        echo Starting to sleep...
        sleep 10
        echo Finished sleeping

---
apiVersion: tekton.dev/v1beta1
kind: Task
metadata:
  name: task-echo
spec:
  params:
    - name: message
      type: string
  steps:
    - name: echo
      image: alpine:latest
      command: [echo]
      args: ["$(params.message)"]
```

## Parameters

```yaml
apiVersion: tekton.dev/v1beta1
kind: Pipeline
metadata:
  name: toolkit
  namespace: tekton-builds
spec:
  params:
    - name: project
      default: tekton-demo
    - name: release
      default: "1.0.1"
  workspaces:
    - name: pipeline-ws
  tasks:
    - name: git-clone
      taskRef:
        name: task-git-clone
      workspaces:
        - name: source
          workspace: pipeline-ws
      params:
        - name: url
          value: git://github.com/vfarcic/$(params.project)
    - name: build-container-image
      taskRef:
        name: build-kaniko-git
      params:
        - name: app_repo
          value: git://github.com/vfarcic/$(params.project)
        - name: container_image
          value: vfarcic/$(params.project)
        - name: container_tag
          value: "$(params.release)"
    - name: deploy-staging
      taskRef:
        name: task-kustomize
      params:
        - name: container_image
          value: vfarcic/$(params.project)
        - name: container_tag
          value: "$(params.release)"
        - name: manifests_path
          value: $(params.project)/kustomize/overlays/staging
      workspaces:
        - name: source
          workspace: pipeline-ws
      runAfter:
        - build-container-image
        - git-clone
    - name: tests
      taskRef:
        name: task-echo
      params:
        - name: message
          value: Running integration tests (before, during, and after the deployment is finished)...
      runAfter:
        - deploy-staging
    - name: deploy-production
      taskRef:
        name: task-kustomize
      params:
        - name: container_image
          value: vfarcic/$(params.project)
        - name: container_tag
          value: "$(params.release)"
        - name: manifests_path
          value: $(params.project)/kustomize/overlays/production
      workspaces:
        - name: source
          workspace: pipeline-ws
      runAfter:
        - tests
---
apiVersion: tekton.dev/v1beta1
kind: Task
metadata:
  name: build-kaniko-git
  namespace: tekton-builds
spec:
  params:
    - name: app_repo
    - name: container_image
    - name: container_tag
  volumes:
    - name: kaniko-secret
      secret:
        secretName: regcred
        items:
          - key: .dockerconfigjson
            path: config.json
  steps:
    - name: build
      image: gcr.io/kaniko-project/executor:debug
      args:
        - --context=$(params.app_repo)
        - --destination=$(params.container_image):$(params.container_tag)
      volumeMounts:
        - name: kaniko-secret
          mountPath: /kaniko/.docker/
---
apiVersion: tekton.dev/v1beta1
kind: Task
metadata:
  name: task-echo
  namespace: tekton-builds
spec:
  params:
    - name: message
      type: string
  steps:
    - name: sleep
      image: alpine:latest
      command: [echo]
      args: ["$(params.message)"]
---
apiVersion: tekton.dev/v1beta1
kind: Task
metadata:
  name: task-kustomize
  namespace: tekton-builds
spec:
  params:
    - name: container_image
      type: string
    - name: container_tag
      type: string
    - name: manifests_path
      type: string
  workspaces:
    - name: source
  steps:
    - name: version
      image: nekottyo/kustomize-kubeval
      script: |
        cd $(workspaces.source.path)/$(params.manifests_path)
        kustomize edit set image $(params.container_image)=$(params.container_image):$(params.container_tag)
        kustomize build | kubectl apply --filename -
---
apiVersion: tekton.dev/v1beta1
kind: Task
metadata:
  name: task-git-clone
  namespace: tekton-builds
spec:
  workspaces:
    - name: source
  params:
    - name: url
      type: string
  steps:
    - name: clone
      image: bitnami/git
      script: |
        cd $(workspaces.source.path)
        git clone $(params.url)
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: pipelines
rules:
  - apiGroups:
      - "*"
    resources:
      - "*"
    verbs:
      - "*"
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: pipelines
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: pipelines
subjects:
  - kind: ServiceAccount
    name: default
    namespace: tekton-builds
```
