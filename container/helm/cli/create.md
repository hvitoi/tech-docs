# create

```sh
# Create new chart
helm create "chart"
```

## Chart file structure

`foo/`
├── `.helmignore` # Contains patterns to ignore when packaging Helm charts.
├── `Chart.yaml` # Information about your chart
├── `values.yaml` # The default values for your templates
├── `charts/` # Charts that this chart depends on
└── `templates/` # The template files
└── `tests/` # The test files

- `mychart/`: Top level folder

  - **Chart.yaml**: metadata about the chart (name, version, dependencies, etc)
  - **LICENSE** (optional): a plain text file containing the license for the chart
  - **README.md** (optional): a human-readable README file
  - **values.yaml**: default configuration values for this chart
  - **(values.schema.json)** (optional): schema for imposing a structure on the values.yaml file
  - **charts/** # A directory containing any charts upon which this chart depends.
  - **crds/**: custom Resource Definitions
  - **templates/**: templates to generate the kubernetes manifest files
  - **templates/NOTES.txt** (optional): plain text file containing short usage notes
