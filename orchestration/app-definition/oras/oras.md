# ORAS

- `ORAS` stands for **OCI Registry As Storage**
- Distribute arbitrary artifacts (not just container images) through any OCI-compliant registry
- Reuses the same registries, auth, and tooling already in place for Docker images
- Common use cases: Helm charts, Kubernetes manifests, WASM modules, configs, SBOMs, signatures

## Why ORAS

- A single registry becomes the source of truth for all deployable artifacts
- No need for separate storage backends (S3, artifact servers) for non-image content
- Works with Docker Hub, GHCR, ECR, GAR, Harbor, Artifactory, etc.

## Installation

```shell
# macOS
brew install oras

# Verify
oras version
```

## Basic usage

```shell
# Login to a registry
oras login ghcr.io -u <user> -p <token>

# Push a file as an OCI artifact
oras push ghcr.io/org/my-artifact:v1 ./config.yaml

# Push with a custom media type
oras push ghcr.io/org/my-artifact:v1 \
  ./config.yaml:application/vnd.acme.config.v1+yaml

# Pull the artifact back
oras pull ghcr.io/org/my-artifact:v1

# Inspect manifest
oras manifest fetch ghcr.io/org/my-artifact:v1
```

## How it works

- An artifact is packaged as an OCI manifest with one or more layers
- Each layer has a `mediaType` describing its content (image, chart, config, etc.)
- The registry stores blobs and manifests the same way it does for container images
- Clients (Helm, Flux, ArgoCD) use the `mediaType` to know how to consume the artifact

## OCI references

```text
<registry>/<repository>:<tag>
ghcr.io/org/my-chart:1.2.3
```

## Related tools

- `Helm` v3.8+ supports pushing/pulling charts via OCI (built on ORAS)
- `Flux` and `ArgoCD` can source manifests directly from OCI registries
- `Cosign` stores signatures and attestations as OCI artifacts
