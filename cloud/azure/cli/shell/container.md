# container

```shell
# Create container
az container create \
  --resource-group "demo-rg" \
  --name "demo-container" \
  --image "microsoft/aci-helloworld" \
  --ports "80" \
  --dns-name-label "dns_label_name" \
  --location "eastus"

# Show container
az container show \
  --resource-group "demo-rg" \
  --name "demo-container" \
  --query "{FQDN:ipAddress.fqdn,ProvisioningState:provisioningState}" \
  --out table

# Attach to the container to see error streams
az container attach
```

## Deployment yaml

```shell
# Create container (From deployment file)
az container create \
  --resource-group "demo-rg" \
  --name "demo-container" \
  --file "deployment.yaml"
```

```yaml
apiVersion: 2019-12-01
location: eastus
name: demo-container
properties:
  containers:
    - name: nginx
      properties:
        image: hvitoi.azurecr.io/nginx
        resources:
          requests:
            cpu: 1
            memoryInGb: 1.5
        ports:
          - port: 80
        volumeMounts:
          - mountPath: /mounts/secrets
            name: volumesecret
  volumes:
    - name: volumesecret
      secret:
        storage-connection: base64-encoded-connection-string # base64 encoded secrets
  osType: Linux
  imageRegistryCredentials:
    - server: hvitoi.azurecr.io
      username: hvitoi
      password: pass1234 # get the password from "access keys" menu in CR
  ipAddress:
    type: Public
    ports:
      - protocol: tcp
        port: 80
tags: null
type: Microsoft.ContainerInstance/containerGroups
```
