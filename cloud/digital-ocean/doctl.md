# Create kubernetes context

```shell
# Install management tools
sudo snap install "doctl"

# Authenticate
doctl auth init # and paste the DO token

# Create context
doctl kubernetes cluster kubeconfig save "cluster-name"
```
