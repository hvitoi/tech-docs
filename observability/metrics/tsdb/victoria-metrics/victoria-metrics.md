# Victoria Metrics

- It's a drop-in, more scalable replacement for Prometheus's storage and querying layer
- It's only the time series `storage` and `query` layers
- It doesn't scrape metrics. For that it relies on prometheus (via remote write) or vmagent
- Supports high cardinality metrics
- No concept of `metric types`, only raw samples and labels.

## Components

- Separate components so it scales horizontally to billions of series and years of retention

- `vmstorage`
- `vminsert`
- `vmselect`
