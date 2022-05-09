# Jenkins Installation

- Jenkins webserver runs on port `localhost:8080`
- Copy the initial password from `/var/lib/jenkins/secrets/initialAdminPassword` (also displayed in the logs)

## Docker

- Create a "jenkins-docker" folder with a "jenkins_home" subfolder

```shell
docker container run --detach \
  --name "jenkins" \
  --publish "8080:8080" \
  --mount "type=bind,source=$HOME/jenkins_home,target=/var/jenkins_home" \
  "jenkins/jenkins"
```

```yaml
version: "3"
services:
  jenkins:
    container_name: jenkins
    image: jenkins/jenkins
    ports:
      - "8080:8080"
    volumes:
      - "$PWD/jenkins_home:/var/jenkins_home" # The jenkins_home folder must have user owner id 1000! (not root!)
    networks:
      - net
networks:
  net: {}
```

## Debian

- Needs JRE!

```shell
# install the gpg key
wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -

# Add repository to sources.list
sudo sh -c 'echo deb https://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'

# Download and install jenkins
sudo apt-get update
sudo apt-get install jenkins
```

- Setup Jenkins as a `daemon` to launch at startup. See `/etc/init.d/jenkins` for more details.
- Create a `jenkins` user to run this service.
- Console log output to the file `/var/log/jenkins/jenkins.log`
- Populate `/etc/default/jenkins` with configuration parameters. E.g., JENKINS_HOME

## Kubernetes

```shell
# Helm install
helm repo add "jenkins" "https://charts.jenkins.io"
helm repo update
helm upgrade --install \
  jenkins "jenkins/jenkins" \
  --namespace "jenkins" \
  --create-namespace \
  --set "controller.ingress.enabled=true" \
  --set "controller.apiVersion=networking.k8s.io/v1" \
  --set "controller.ingress.hostName=jenkins.hvitoi.com" \
  --set "controller.adminUser=admin" \
  --set "controller.adminPassword=admin" \
  --wait
xdg-open "http://jenkins.hvitoi.com"
kubectl -n "jenkins" get secret "jenkins" --output jsonpath="{.data.jenkins-admin-password}" | base64 -d # Get password



#########################
# Exploring PodTemplate #
#########################

cat jenkins-pod.yaml

kubectl --namespace jenkins \
    create secret \
    docker-registry regcred \
    --docker-server $REGISTRY_SERVER \
    --docker-username $REGISTRY_USER \
    --docker-password $REGISTRY_PASS \
    --docker-email $REGISTRY_EMAIL

##################################
# Defining roles and permissions #
##################################

cat roles.yaml

kubectl apply --filename roles.yaml

############################
# Creating GitHub webhooks #
############################

gh repo view --web

echo http://jenkins.$INGRESS_HOST.nip.io/github-webhook/

# Copy and paste the address into the webhook *Payload URL* field

###########################
# Creating a pull request #
###########################

git checkout -b my-feature

# Open config.toml and change something

git add .

git commit -m "Is this a new feature?"

git push --set-upstream origin my-feature

gh pr create \
    --title "My feature" \
    --body "I'm too lazy to write descriptions"

#####################
# Building mainline #
#####################

gh repo view --web

# Navigate to the PR and merge it.

git checkout master

git pull

echo http://jenkins-demo.$INGRESS_HOST.nip.io

# Open it
```
