# Helm dependencies

- A chart can depend on other charts (subcharts). E.g., an app chart that needs a Redis
- Dependencies are declared in `Chart.yaml` under `dependencies` (requires `apiVersion: v2`)

```yaml
# Chart.yaml
apiVersion: v2
name: devops-toolkit
version: "0.1.0"
dependencies:
  - name: redis # chart name in the repository
    version: "20.x.x" # semver range
    repository: oci://registry-1.docker.io/bitnamicharts # or https://... or file://../local-chart
    condition: redis.enabled # only installed if this value is true
    # alias: cache # rename the subchart (values key and resource names change accordingly)
    # tags: [backend] # enable/disable groups of dependencies via .Values.tags.backend
```

- `repository` formats
  - `https://charts.example.com`: HTTP repo URL
  - `oci://registry/path`: OCI registry
  - `file://../local-chart`: local path, relative to the chart
  - `@foo` (or `alias:foo`): name of a repo previously added with `helm repo add foo <url>`
    - Resolved from the local repo config (`helm repo list`), so every machine/CI must add it with the same name first
    - Otherwise fails with `no repository definition for @foo`
    - HTTP repos only: OCI registries can't be added with `helm repo add`

## Workflow

```shell
helm dependency update ./sample-chart # resolve versions, download tgz into charts/ and write Chart.lock
helm dependency build ./sample-chart # download exactly what Chart.lock says (reproducible, use in CI)
helm dependency list ./sample-chart # show dependencies and their status (ok, missing, wrong version)

helm install "release" ./sample-chart # installs the app AND the redis subchart as a single release
```

## Configuring the subchart

- The parent's `values.yaml` can override subchart values under a key named after the dependency (or its `alias`)
- The subchart only sees its own section (`.Values.auth.enabled` inside redis = `.Values.redis.auth.enabled` in the parent)

```yaml
# values.yaml (parent)
redis:
  enabled: true # used by "condition"
  architecture: standalone
  auth:
    enabled: false

global:
  storageClass: gp3 # "global" values are visible to the parent and ALL subcharts as .Values.global.*
```

- The subchart resource names follow its own naming helpers, usually `<release>-<chart>` (e.g., service `myapp-redis-master`), so the parent can reference it

```yaml
env:
  - name: REDIS_HOST
    value: "{{ .Release.Name }}-redis-master"
```

## Under the hood

1. **Resolution** (`helm dependency update`)
   - For each entry, Helm fetches the repo index (or queries the OCI registry) and picks the highest version matching the semver range
   - The chart `.tgz` is downloaded into `charts/` and the exact resolved versions + a digest are written to `Chart.lock`

```
sample-chart/
├── Chart.yaml
├── Chart.lock          # pinned versions (commit it)
├── charts/
│   └── redis-20.6.2.tgz # vendored subchart (usually gitignored, rebuilt with `helm dependency build`)
├── templates/
└── values.yaml
```

```yaml
# Chart.lock
dependencies:
  - name: redis
    repository: oci://registry-1.docker.io/bitnamicharts
    version: 20.6.2
digest: sha256:...
generated: "2026-11-27T10:00:00Z"
```

1. **Loading** (`helm install/upgrade/template`)
   - Helm loads the parent chart and every chart found in `charts/` (archives or unpacked directories) into a tree
   - Anything inside `charts/` is a subchart, declared in `dependencies` or not. `dependencies` just manages what gets downloaded there
   - If `Chart.yaml` declares a dependency missing from `charts/`, install fails (`found in Chart.yaml, but missing in charts/ directory`)

2. **Enabling**
   - `condition` and `tags` are evaluated against the merged values. Disabled subcharts are pruned from the tree before rendering

3. **Values coalescing**
   - Values are merged with priority: `--set` > `-f` files > parent `values.yaml` > subchart `values.yaml`
   - Each subchart receives `parentValues.<name>` merged on top of its own defaults, plus `global`
   - A subchart can never read the parent's values (only `global`)

4. **Rendering**
   - Templates of parent and all subcharts are rendered together. Named templates (`define`) are global, so subchart helpers can collide with the parent's if names are not prefixed (e.g., `"redis.fullname"`)

5. **Release**
   - All rendered manifests are sorted by kind (Namespace, ConfigMap, Secret, Service, Deployment, ...) and applied as **one release**
   - There is no ordering "subchart first": the subchart is not a separate release, `helm list` shows only the parent, and `helm uninstall` removes everything
   - If the app must wait for Redis, use readiness probes / init containers, or hooks (`helm.sh/hook-weight`)

```shell
# See it flattened
helm template "release" ./sample-chart | grep -E '^(kind|  name):'
```
