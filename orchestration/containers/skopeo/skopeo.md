# Skopeo

Skopeo is an open-source CLI for working with container images and registries without a container runtime or daemon

It operates on images stored in registries, local OCI layouts, container storage, tarballs, etc. — purely as data. No dockerd, no root, no pulling-then-pushing through a local store.

```shell
# Inspect a remote image without pulling
skopeo inspect docker://docker.io/library/nginx:latest
skopeo inspect --config docker://alpine:3.19   # the image config JSON

# List tags
skopeo list-tags docker://ghcr.io/owner/image

# Copy between registries (no local pull/push round-trip)
skopeo copy \
  docker://docker.io/library/alpine:3.19 \
  docker://registry.example.com/mirror/alpine:3.19

# Copy ALL tags / a multi-arch manifest list
skopeo copy --all docker://nginx:latest docker://registry.example.com/nginx:latest

# Export to a local OCI layout or tarball
skopeo copy docker://alpine:3.19 oci:./alpine-oci:3.19
skopeo copy docker://alpine:3.19 docker-archive:alpine.tar

# Compare two images by digest
skopeo inspect --format '{{.Digest}}' docker://nginx:1.25
skopeo inspect --format '{{.Digest}}' docker://nginx:1.26

# Delete a tag from a registry
skopeo delete docker://registry.example.com/org/image:old-tag

# Sign / verify images (sigstore, GPG)
skopeo copy --sign-by <key@example.com> ...
```
