# Gcloud account

1. Create a new project in google cloud
2. Create a cluster in Kubernetes Engine
3. Create a new service account in IAM
4. Download service account keys as json file
5. Rename the json file to service-account.json and move it to the app folder

## Travis CI

1. Link git repo to travis
2. Install travis CLI (to encrypt the json file and tie to travis)
   1. Run ruby in a container: `docker container run -it -v $(pwd):/app ruby:2 sh`
   2. Install travis in the container with gem (gem is a package manager for ruby): `gem install travis`
   3. Test travis installation: `travis`
3. Get into the app folder in the ruby container
4. Login to travis with github credentials: `travis login`
5. Encrypt the service-account.json `travis encrypt-file service-account.json -r hvitoi/fibo-k8s`
6. Add the service-account.json.enc to the git repo
7. Delete the origin service-account.json permanently
8. Copy the line code for decryption to the .travis.yml file
9. Configure the rest of the .travis.yml file

## Deploy . sh

1. Build the images with latest and sha tag
2. Push images to dockerhub
3. Explicitly define the SHA to the image for each deployment object

## Secret

1. Create the secret object at the gcloud
2. With cloud shell or in the travis.yml file
3. `kubectl create secret generic pgpassword --from-literal PG_PASSWORD=mypass123`

## Helm

- Outside program to administer 3rd party software inside of the cluster
- Must be installed in the local host or cloud provider
- Helm Client (CLI tool)
- https://helm.sh/docs/intro/quickstart/
- Install in gcloud shell from script v3

```bash
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3
chmod 700 get_helm.sh
./get_helm.sh
```

## Ingress Nginx

- Install Ingress Nginx via Helm

```bash
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm install my-release ingress-nginx/ingress-nginx
```

- Ingress Nginx has:
  - 1 Deployment: Runs the controller that reads the config file
  - 1 ClusterIP: Reaches the deployment object
  - 1 GoogleCloud LoadBalancer: Provide the ip addresses to reach the nodes in the cluster
  - Ingress Service: It's the config file. It has the routes in the config file

## Scaffold

- Scaffold for local development

```bash
curl -Lo skaffold https://storage.googleapis.com/skaffold/releases/latest/skaffold-linux-amd64
sudo install skaffold /usr/local/bin/
```

- Check version`skaffold version`
- Make the configuration file skaffold.yml
- Start `skaffold dev`
