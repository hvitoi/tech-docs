# Flux CLI

## Setup

- Create github repo `flux-fleet`
- Create flux manifest and push to the repo
- Installs flux manifest on `flux-system` namespace

```sh

flux bootstrap github \
  --owner "$GITHUB_ORG" \
  --repository "flux-fleet" \
  --branch "main" \
  --path "apps" \
  --personal "$GITHUB_PERSONAL"
```

## GithubRepository

- Source is just a source, it has no action
- Sources are placed inside the `flux-fleet` repo (apps folder)

```sh
# Create source (staging environment)
flux create source git "staging" \
  --url "https://github.com/$GITHUB_ORG/flux-staging" \
  --branch "master" \
  --interval "30s" \
  --export \
  | tee "apps/staging.yaml" # do not apply, just generate the manifest

# Create source (production environment)
cd flux-production
flux create source git "production" \
  --url "https://github.com/$GITHUB_ORG/flux-production" \
  --branch "master" \
  --interval "30s" \
  --export \
  | tee "apps/production.yaml"

# Create source (app)
cd my-app
flux create source git "my-app" \
  --url "https://github.com/hvitoi/my-app" \
  --branch "master" \
  --interval "30s" \
  --export \
  | tee "apps/my-app.yaml"

git add .
git commit -m "Added environments sources"
git push # push to flux-fleet repo

# watch sources
flux get sources git
```

## Kustomization

- Kustomizations are appended together to its source

```sh
# Append kustomization to its source
flux create kustomization "staging" \
    --source "staging" \ # reference to the source created earlier
    --path "./" \
    --prune "true" \ # delete from cluster if deleted manifest
    --validation "client" \ # client-side validation
    --interval "10m" \ # pooling period
    --export \
    | tee -a "apps/staging.yaml"

# Append kustomization to its source
flux create kustomization "production" \
    --source "production" \
    --path "./" \
    --prune "true" \
    --validation "client" \
    --interval "10m" \
    --export \
    | tee -a "apps/production.yaml"

git add .
git commit -m "Added environments kustomizations"
git push

# watch kustomizations
flux get kustomizations
```

## HelmRelease

- The release is created in its own environment (E.g, flux-staging)

```sh

# Create values for my-app release (staging environment)
echo "image:
  tag: 2.9.9
ingress:
  host: staging.my-app.$INGRESS_HOST.nip.io" \
| tee "values.yaml" # remove it after applied

flux create helmrelease "my-app-staging" \
  --source "GitRepository/my-app" \
  --values "values.yaml" \
  --chart "helm" \
  --target-namespace "staging" \
  --interval "30s" \
  --export \
  | tee "apps/my-app.yaml"

git add .
git commit -m "Initial commit"
git push

# modify myapp release
cat "apps/my-app.yaml" \
  | sed -e "s@tag: 2.9.9@tag: 2.9.17@g" \
  | tee "apps/my-app.yaml"

git add .
git commit -m "Upgrade to 2.9.17"
git push

# watch releases
watch flux get helmreleases
```

```sh
###########################
# Promoting to production #
###########################

cd flux-production

echo "image:
    tag: 2.9.17
ingress:
    host: my-app.$INGRESS_HOST.nip.io" \
    | tee values.yaml

flux create helmrelease "my-app-production" \
    --source "GitRepository/my-app" \
    --values "values.yaml" \
    --chart "helm" \
    --target-namespace "production" \
    --interval "30s" \
    --export \
    | tee "apps/my-app.yaml"
```
