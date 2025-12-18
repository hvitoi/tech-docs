# argo submit

```shell
# Create and run a Workflow
argo submit workflow.yaml

# Watch as it runs and reports whether it succeeds or not
argo submit --watch https://raw.githubusercontent.com/argoproj/argo-workflows/main/examples/hello-world.yaml

# Override parameters
argo submit workflow.yaml -p message="goodbye world"
argo submit workflow.yaml --parameter-file params.yaml # from file

# Override entrypoint template
argo submit workflow.yaml --entrypoint another-entrypoint

```

```shell
# List submitted workflows
argo list -n argo-workflows # Same as: kubectl get workflows.argoproj.io -n argo-workflows

# Get a specific workflow
argo get -n argo-workflows @latest
```
