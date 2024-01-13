# Hugo

- Static website generator
- Similar tools
  - Jekyll
  - 11ty
- Website is configured with `hugo.toml`

## Go templates

- `go templates` is used control how to content is presented
- Interpolate and transform dynamic data

```html
{{ define "main" }}
  <h1>List</h1>
  {{ range .Pages }}

  <article>
    <h2>{{ .Title }}</h2>
    {{ .Content }}
  </article>

{{ end }}
```

```go
// variables
{{ $hello := value }}

// loops
{{ ranger .Pages }}
{{ end }}

// fetch
{{ $myData := getJSON "url" }}
```

## Directories

- **content/**
  - The markdown files
  - Can be divided in subdirectories that represent subsections
