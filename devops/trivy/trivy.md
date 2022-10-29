# Trivy

- Scanner for `vulnerabilities` and `misconfiguration` in
  - `Container images`
  - `Filesystems`
  - `Repositories`
- Features
  - Prevent
  - Protect
  - Detect
  - Respond

## image

```sh
# list vulnerabilities in an image
trivy image "node:14.9.0"

# only vulnerabilities that have been fixed in other versions
trivy image --ignore-unfixed "node:14.9.0"

```

## repo

```sh
# list vulnearbilities in a repository
trivy repo "https://github.com/user/repo"
```

## config

```sh
# spot misconfiguration in kubernetes manifests
trivy config "deployment.yaml"

# spot misconfiguration in terraform files
trivy config "main.tf"
```

## fs

```sh
# vulnearbilities in a filesystem
trivy fs "/"
```
