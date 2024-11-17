# Scout

- Displays a the `summary of vulnerabilities` of an image
- Following artifacts are supported:
  - `Images` (default): image://curlimages/curl:7.87.0
  - `OCI layout directories`: oci-dir://
  - `Tarball archives` (as created by docker save): archive://
  - `Local directory or file`: local://welcome-to-docker:latest
  - `Registry`: registry://
  - `Filesystem`: fs://
- The tool analyzes the provided software artifact, and generates a vulnerability report

```shell
# If not specified, the most recently built image is used
docker scout quickview
docker scout qv
docker scout qv "image://curlimages/curl:7.87.0"
```
