# GitHub Action

- An action to be performed on triggering an event. E.g.,
  - Code pushed
  - Pull Request Created
  - Pull Request Closed
  - Repository is Forked
- Actions Tab are the Repository
  - Setup a new workflow
- Actions `main.yml` must be committed to master branch on the GitHub platform

- `Test Script`

```yml
name: tests # Name of the workflow

on: pull_request # Trigger on pull request (open, closed, updated)

jobs:
  build: # Build a container
    runs-on: ubuntu-latest # with ubuntu
    steps:
      - uses: actions/checkout@v2 # take all the code in the repo
      - run: cd auth && npm install && npm run test:ci # Run the tests for auth
```

- `secrets` must be added to Repo Settings/Secrets. E.g.
  - JWT keys
  - API keys
  - Docker credentials
- Secrets are encrypted and only exposed to selected actions
- Secrets are NOT passed to workflows triggered by PR

- `Deploy Script`

```yml
name: deploy-myservice

on:
  push:
    branches:
      - master
    paths:
      - 'myservice/**'

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Setup repository
        uses: actions/checkout@v2

      - name: Build docker image
        run: docker build -t hvitoi/myservice myservice

      - name: Login to DockerHub
        run: docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD
        env:
          DOCKER_USERNAME: ${{ secrets.DOCKER_USERNAME }}
          DOCKER_PASSWORD: ${{ secrets.DOCKER_PASSWORD }}

      - name: Push image to DockerHub
        run: docker push hvitoi/myservice

      - name: Setup Digital Ocean doctl
        uses: digitalocean/action-doctl@v2
        with:
          token: ${{ secrets.DIGITALOCEAN_ACCESS_TOKEN }}

      - name: Create kubectl context
        run: doctl kubernetes cluster kubeconfig save mycluster

      - name: Restart the deployment
        run: kubectl rollout restart deployment myservice-depl
```

- A script to apply all the config files must the included
- The script to apply config files is named manifest

```yml
name: deploy-manifests

on:
  push:
    branches:
      - master
    paths:
      - 'infra/**'

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Setup repository
        uses: actions/checkout@v2

      - name: Setup Digital Ocean doctl
        uses: digitalocean/action-doctl@v2
        with:
          token: ${{ secrets.DIGITALOCEAN_ACCESS_TOKEN }}

      - name: Create kubectl context
        run: doctl kubernetes cluster kubeconfig save mycluster

      - name: Apply all the config files to the Kubernetes cluster
        run: kubectl apply -f infra/k8s && kubectl apply -f infra/k8s-prod
```
