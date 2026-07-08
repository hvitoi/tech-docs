# Victoria Metrics

- It's only the time series `storage` and `query`
- It doesn't scrape metrics. For that it relies on prometheus (via remote write) or vmagent
- Supports high cardinality metrics
- No concept of `metric types`, only raw samples and labels.
