# Helm template

## Built-in objects

- Built-in objects always begin with capital letter (Go naming convention)

### Release

- `Release`: describes the release itself
  - _Release.Name_: release name
  - _Release.Namespace_: namespace to be released into
  - _Release.IsUpgrade_: set to true if the current operation is an upgrade or rollback
  - _Release.IsInstall_: set to true if the current operation is an install
  - _Release.Revision_: revision number for this release. On install, this is 1, and it is incremented with each upgrade and rollback.
  - _Release.Service_: The service that is rendering the present template. On Helm, this is always Helm.

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: {{ .Release.Name }}-configmap
data:
  myvalue: "Hello World"
```

### Values

- `Values`: object structure defined in values.yaml

### Chart

- `Chart`: contents of the Chart.yaml file

### Files

- `Files`: access to non-special files in a chart
  - _Files.Get_: function for getting a file by name (.Files.Get config.ini)
  - _Files.GetBytes_ function for getting the contents of a file as an array of bytes instead of as a string. This is useful for things like images.
  - _Files.Glob_: function that returns a list of files whose names match the given shell glob pattern.
  - _Files.Lines_: function that reads a file line-by-line. This is useful for iterating over each line in a file.
  - _Files.AsSecrets_: function that returns the file bodies as Base 64 encoded strings.
  - _Files.AsConfig_: function that returns file bodies as a YAML map.

### Capabilities

- `Capabilities`: provides information about what capabilities the Kubernetes cluster supports
  - _Capabilities.APIVersions_: is a set of versions.
  - _Capabilities.APIVersions.Has_: $version indicates whether a version (e.g., batch/v1) or resource (e.g., apps/v1/Deployment) is available on the cluster.
  - _Capabilities.KubeVersion_ and _Capabilities.KubeVersion.Version_ is the Kubernetes version.
  - _Capabilities.KubeVersion.Major_: is the Kubernetes major version.
  - _Capabilities.KubeVersion.Minor_: is the Kubernetes minor version.
  - _Capabilities.HelmVersion_: is the object containing the Helm Version details, it is the same output of helm version
  - _Capabilities.HelmVersion.Version_: is the current Helm version in semver format.
  - _Capabilities.HelmVersion.GitCommit_: is the Helm git sha1.
  - _Capabilities.HelmVersion.GitTreeState_: is the state of the Helm git tree.
  - _Capabilities.HelmVersion.GoVersion_: is the version of the Go compiler used.

### Template

- `Template`: contains information about the current template that is being executed
  - _Template.Name_: A namespaced file path to the current template (e.g. mychart/templates/mytemplate.yaml)
  - _Template.BasePath_: The namespaced path to the templates directory of the current chart (e.g. mychart/templates)

## Functions

- `quote`: add quotes to the value {{ quote .Values.favorite.food }} or {{ .Values.favorite.food | quote }}
- `lookup`: return a resource in the template {{ lookup "v1" "Pod" "mynamespace" "mypod" }}
- `range`
  {{ range $index, $service := (lookup "v1" "Service" "mynamespace" "").items }}
  {{/* do something with each service */}}
  {{ end }}

### Logic and Control Flow

- `and`: returns a boolean of two arguments {{ and .Arg1 .Arg2 }}
- `or`: {{ or .Arg1 .Arg2 }}
- `not`: {{ not .Arg }}
- `eq`: {{ eq .Arg1 .Arg2 }}
- `ne`: {{ ne .Arg1 .Arg2 }}
- `lt`: {{ lt .Arg1 .Arg2 }}
- `gt`: {{ gt .Arg1 .Arg2 }}
- `ge`: {{ ge .Arg1 .Arg2 }}
- `empty`: true is the value is empty {{ empty .Foo }}
- `default`: set a default value {{ .Values.favorite.drink | default (printf "%s-tea" (include "fullname" .)) }}
- `fail`: unconditionally returns error {{ fail "Please accept the end user license agreement"}}
- `coalesce`: takes a list and returns the first non-empty {{ coalesce 0 1 2 }} returns 1 {{ coalesce .name .parent.name "Matt" }} returns matt if the others are empty
- `ternary`: {{ true | ternary "foo" "bar"}} returns foo {{ false | ternary "foo" "bar"}} retruns bar

### String Functions

- `print`: {{ print "Matt has " .Dogs " dogs"}}
- `println`: adds a newline
- `printf`: {{ printf "%s has %d dogs." .Name .NumberDogs }}
- `trim`: {{ trim "   hello    " }}
- `trimAll`: {{ trimAll "$" "$5.00" }} returns 5.00
- `trimPrefix`: {{ trimPrefix "-" "-hello" }} returns hello
- `trimSuffix`: {{ trimSuffix "-" "hello-" }} returns hello
- `lower`: {{ lower "HELLO" }}
- `upper`: {{ upper "hello" }}
- `title`: {{ title "hello world" }} returns Hello World
- `untitle`: {{ untitle "Hello World" }} returns hello world
- `repeat`: {{ repeat 2 "hello" }} returns hellohello
- `substr`: {{ substr 0 5 "hello world" }} returns hello
- `nospace`: {{ nospace "hello w o r l d" }} returns helloworld
- `trunc`: {{ trunc 5 "hello world" }} returns hello {{ trunc -5 "hello world" }} returns world
- `abbrev`: truncate with ellipses (...) {{ abbrev 5 "hello world" }} returns he...
- `abbrevboth`: truncate both sides {{ abbrevboth 5 10 "1234 5678 9123" }} returns ...5678...
- `initials`: {{ initials "First Try" }} returns FT
- `randAlphaNum`: uses 0-9a-zA-Z {{ randNumeric 3 }}
- `randAlpha` uses a-zA-Z
- `randNumeric` uses 0-9
- `randAscii` uses all printable ASCII characters
- `wrap`: {{ wrap 80 $someText }} wrap the string in 80 columns (creates a list)
- `wrapWith`: {{ wrapWith 5 "\t" "Hello World" }}
- `contains`: {{ contains "cat" "catch" }} returns true

## Flow Control

## If/Else

- a `false` is a boolean false, numeric 0, empty string, nil, empty collection (map, slice, tuple, dict, array)

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: {{ .Release.Name }}-configmap
data:
  myvalue: "Hello World"
  drink: {{ .Values.favorite.drink | default "tea" | quote }}
  food: {{ .Values.favorite.food | upper | quote }}
  {{- if eq .Values.favorite.drink "coffee" }} # {{- consumes new lines on the left
  mug: "true"
  {{- end }}
```

## With

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: {{ .Release.Name }}-configmap
data:
  myvalue: "Hello World"
  {{- with .Values.favorite }} # uses scope .Values.favorite (inside this block .drink and .food may be mentioned directly)
  drink: {{ .drink | default "tea" | quote }}
  food: {{ .food | upper | quote }}
  release: {{ $.Release.Name }} # $ is a reference to the root scope
  {{- end }}
```

## Range

- range can be used over `list`, `tuple`, `map` or `dict`

```yaml
pizzaToppings:
  - mushrooms
  - cheese
  - peppers
  - onions
favorite:
  a: b
  c: d
```

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: {{ .Release.Name }}-configmap
data:
  myvalue: "Hello World"

  # predefined list
  toppings: |-
    {{- range .Values.pizzaToppings }}
    - {{ . | title | quote }}
    {{- end }}

  # dinamic list
  sizes: |-
    {{- range tuple "small" "medium" "large" }}
    - {{ . }}
    {{- end }}

  # iterate list
  toppings: |-
    {{- range $index, $topping := .Values.pizzaToppings }}
      {{ $index }}: {{ $topping }}
    {{- end }}

  # iterate object
  {{- range $key, $val := .Values.favorite }}
  {{ $key }}: {{ $val | quote }}
  {{- end }}

```

## Variables

- Variables can be created using `:=` operator

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: {{ .Release.Name }}-configmap
data:
  myvalue: "Hello World"
  {{- $relname := .Release.Name -}}
  release: {{ $relname }}
```
