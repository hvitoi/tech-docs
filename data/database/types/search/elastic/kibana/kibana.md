# Kibana

- Access: `localhost:5601`
- First create a `index pattern` must be created under `Stack Management`

## Tools

- `Discover`: Search term
- `Visualize`: Plot graphs
- `DevTools`: Make search manually
- `Dashboard`: Combine multiple graphs for visualization
- `Lens`: A grab & drop approach to generate graphs

## Kibana Management

### Spaces

- `Spaces` for segregating users
- One `default` space by default

```shell
curl localhost:5601/api/spaces/space/devops
```

### Saved Objects

- Objects allow `importing json dashboards`
- Saved objects are `per space`!
- Objects can be `copied` to other spaces or `exported` as json

### Avanced settings

- The settings mostly apply to the active space (not global)
- `Default route`: default landing page
- `Dark mode`: ativate dark mode
- `Time filters`: How dates are displayed in kibana
