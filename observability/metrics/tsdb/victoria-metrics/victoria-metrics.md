# Victoria Metrics

- It's a drop-in, more scalable replacement for Prometheus's storage and querying layer
- It's only the time series `storage` and `query` layers
- It doesn't scrape metrics. For that it relies on prometheus (via remote write) or vmagent
- Supports high cardinality metrics
- No concept of `metric types`, only raw samples and labels.

## Components

- Scraping components
  - **vmagent** (scrapes)
- Core components
  - **vminsert** (ingests)
  - **vmstorage** (persists)
  - **vmselect** (queries)
- Auxiliary components
  - **vmauth**
  - **vmalert**

- This separates components so it scales horizontally to billions of series and years of retention
- There's also a single-node VictoriaMetrics (victoria-metrics binary). That is one process that does ingestion, storage, and querying. It scales vertically very far with no vminsert/vmstorage/vmselect splits.

## Tenant concept

- In the cluster version everything is tenant-aware. A tenant is `accountID`, and it appears in the URL path:

- Insert: <http://vminsert:8480/insert/0/prometheus/api/v1/write> (0 is the account-id)
- Select: <http://vmselect:8481/select/0/prometheus/api/v1/query>

## Flows

### Write Path

  **your service** `/metrics`
        │  (scrape)
        ▼
     **vmagent** ──remote_write (HTTP)──► **vmauth** ──► **vminsert** ──binary 8400──► **vmstorage**(s)
   (disk buffer)                                           (shards + replicates)        (persist)

### Read Path

  **Grafana** / **user** / **vmalert**
        │  PromQL (HTTP)
        ▼
     **vmauth** ──► **vmselect** ──binary 8401──► **vmstorage**(1..N)  (fan-out to ALL)
                    │  ◄──── raw data ────────┘
                    └── merge + dedup + evaluate MetricsQL ──► result

## Deployment modes

### Single vmstorage cluster

┌─────────────────────────────┐        ┌─────────────────────────────┐
│ Workload account A (EKS)    │        │ Workload account B (EKS)    │
│                             │        │                             │
│  pods /metrics              │        │  pods /metrics              │
│      │ scrape (in-cluster)  │        │      │ scrape               │
│      ▼                      │        │      ▼                      │
│   vmagent  ──┐              │        │   vmagent ──┐               │
│  (disk buf)  │ remote_write │        │  (disk buf) │ remote_write  │
└──────────────┼──────────────┘        └─────────────┼───────────────┘
               │  HTTPS                              │  HTTPS
               └──────────────┬──────────────────────┘
                              ▼
        ┌──────────────────────────────────────────────┐
        │ Observability account (EKS)                  │
        │                                              │
        │   vmauth / ALB  (single ingress, TLS + auth) │
        │        │                                     │
        │        ▼                                     │
        │     vminsert  ──► vmstorage (persist)        │
        │                        ▲                     │
        │     vmselect  ─────────┘  (fan-out reads)    │
        │        ▲                                     │
        │     Grafana / vmalert                        │
        └──────────────────────────────────────────────┘

### Multiple vmstorage clusters

- VictoriaMetrics supports a `global query across multiple vmselects` because vmselect can treat another vmselect as if it were a vmstorage node.
- This is the `multi-level` / `hierarchical` vmselect pattern:

                         ┌─────────────────────────┐
                         │   Top-level (global)    │
   Grafana ──PromQL──►   │   vmselect              │
                         │   -storageNode=         │
                         │     vmselect-A:8401,    │
                         │     vmselect-B:8401,    │
                         │     vmselect-C:8401     │
                         └───────┬─────────┬───────┘
              clusternative      │         │     │  (looks like storage)
                     ┌───────────┘         │     └───────────────┐
                     ▼                     ▼                     ▼
         ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
         │ Customer A      │    │ Customer B      │    │ Customer C      │
         │ vmselect        │    │ vmselect        │    │ vmselect        │
         │ (-clusternative │    │ (-clusternative │    │ (-clusternative │
         │  ListenAddr)    │    │  ListenAddr)    │    │  ListenAddr)    │
         │   │  fan-out    │    │   │             │    │   │             │
         │   ▼             │    │   ▼             │    │   ▼             │
         │ vmstorage x N   │    │ vmstorage x N   │    │ vmstorage x N   │
         └─────────────────┘    └─────────────────┘    └─────────────────┘

## Endpoints

- UI <https://myhost/select/0/vmui/>
- API <https://myhost/select/0/prometheus/api/v1/query>
