# webapp

## List / Show

```sh
# List all apps
az webapp list \
  --resource-group "demo-rg"

# Show app
az webapp show \
  --resource-group "demo-rg" \
  --name "hvitoi" \
  --query "outboundIpAddresses"
```

## Create

```sh
# Create webapp. The app is tied to an service plan
az webapp create \
  --resource-group "demo-rg" \
  --name "hvitoi" \
  --plan "hvitoi-appserviceplan" \
  --runtime "NODE|14-lts"

# App URL
echo "http://hvitoi.azurewebsites.net"
```

## Up

```sh
# Deploy or reload webapp app
az webapp up \
  --location "region" \
  --name "hvitoi" \
  --html
```

## Deployment

- Configure the source code to be deployed
- Pick the code from a local folder or from git repository

```sh
# Deploy code from remote git repository
az webapp deployment source config \
  --resource-group "demo-rg" \
  --name "hvitoi" \
  --repo-url "repo-url" \
  --branch "master" \
  --manual-integration # have to manually trigger the sync button

# Deploy code from zip file
az webapp deployment source config-zip \
  --resource-group "demo-rg" \
  --name "hvitoi"
  --src "api.zip"

# Deploy code from ARM template
az group deployment create \
  --resource-group "demo-rg" \
  --template-uri "https://raw.githubusercontent.com/Azure-Samples/azure-event-grid-viewer/master/azuredeploy.json" \
  --parameters "siteName=$mySiteName" "hostingPlanName=viewerhost"
```

```sh
# Setup credentials to deploy webapp from azure git repository
az webapp deployment user set \
  --user-name "azure-webapp-username" \
  --password "azure-webapp-password"

# Deploy code from local azure git repository (this will create azure git repo)
az webapp deployment source config-local-git \
  --resource-group "demo-rg" \
  --name "hvitoi"

# Add remote and push code to azure git repo
git remote add azure "https://$USERNAME@$SITENAME.scm.azurewebsites.net/$SITENAME.git"
git push azure master
```

## CORS

```sh
az webapp cors add
  --resource-group "demog-rg" \
  --name "hvitoi" \
  --allowed-origins "https://consumer.azurewebsites.net"
```

## Logs

```sh
# Configuration for docker container
az webapp log config \
  --name "hvitoi" \
  --resource-group "demog-rg" \
  --docker-container-logging

# Configuration for application
az webapp log config \
  --name "hvitoi" \
  --resource-group "demog-rg" \
  --application-logging

# Configuration for web server
az webapp log config \
  --name "hvitoi" \
  --resource-group "demog-rg" \
  --web-server-logging

# Show logs!
az webapp log tail \
  --name "hvitoi" \
  --resource-group "demog-rg"
```

## Containers

```sh
# Configure the access to the container repository
az webapp config container set \
  --name "my-app" \
  --resource-group "demo-rg" \
  --docker-registry-server-url "https://images.azurecr.io" \
  -u "admin" \
  -p "admin" \
  --docker-custom-image-name "repo/image:1.0.0"

# Create webapp from image
az webapp create \
  --plan "hvitoi-plan" \
  --deployment-container-image-name "images.azurecr.io/website:v1.0.0"
```

## Custom DNS

```sh
az webapp config hostname add \
  --webapp-name "my-app" \
  --resource-group "demo-rgs" \
  –-hostname "www.my-site.com"
```
