# Prometheus Server

## Configuration

- `prometheus.yml`: defines which targets at which interval
- Usually you won't go create the prometheus configuration, but use the prometheus CRDs created by the `prometheus operator` to deploy the configuration
- The prometheus operator is a manager of all prometheus components

```yaml
global:
  scrape_interval: 15s
  evaluation_interval: 15s # how often to evaluate the rules
rule_files: # aggregating metrics and create alerts
  - "first.rules"
  - "second.rules"
scrape_configs: # what resources prometheus monitors
  - job_name: prometheus # scrape prometheus own metrics
    static_configs:
      - targets: ["localhost:9090"]
  - job_name: node_exporter
    scrape_interval: 1m
    scrape_timeout: 1m
    static_configs:
      - targets: ["localhost:9100"]
```

## Endpoints

- Status page: <http://localhost:9090>
- Prometheus own metrics: <http://localhost:9090/metrics>
- Expression browser: <http://localhost:9090/graph>
