# Flattened datatype

- ES auto-generate the field types for subfields. And sometimes subfield can grow too much!
- Documents which contain many fields can cause the cluster to go down! `field mapping explosion`
- `flattened` datatype is designed to handle unknown or large number of inner fields
  - Map the parent field with a single type named flattened, the inner fields don't appear in the mappings at all

## Auto-generated inner data types

```shell
# Create index with auto-generated data types
curl -X PUT "http://localhost:9200/demo-default/_doc/1" \
  -H "Content-Type: application/json" \
  -d  '{
        "message": "[5592:1:0309/123054.737712:ERROR:child_process_sandbox_support_impl_linux.cc(79)] FontService unique font name matching request did not receive a response.",
        "fileset": {
          "name": "syslog"
        },
        "process": {
          "name": "org.gnome.Shell.desktop",
          "pid": 3383
        },
        "@timestamp": "2020-03-09T18:00:54.000+05:30",
        "host": {
          "hostname": "bionic",
          "name": "bionic"
        }
      }'

# Check index configuration auto-generated
curl -X GET "http://localhost:9200/demo-default/_mapping?pretty=true"

# Get cluster state
curl -X GET "http://localhost:9200/_cluster/state?pretty=true" > es-cluster-state.json
```

## Flattened data type specified

```shell
# Create index
curl -X PUT "http://localhost:9200/demo-flattened"

# Create mapping
curl -X PUT "http://localhost:9200/demo-flattened/_mapping" \
  -H "Content-Type: application/json" \
  -d  '{
        "properties": {
          "host": {
            "type": "flattened"
          }
        }
      }'
curl -X GET "http://localhost:9200/demo-flattened/_mapping?pretty=true"

# Index log document
curl -X PUT "http://localhost:9200/demo-flattened/_doc/1" \
  -H "Content-Type: application/json" \
  -d  '{
        "message": "[5592:1:0309/123054.737712:ERROR:child_process_sandbox_support_impl_linux.cc(79)] FontService unique font name matching request did not receive a response.",
        "fileset": {
          "name": "syslog"
        },
        "process": {
          "name": "org.gnome.Shell.desktop",
          "pid": 3383
        },
        "@timestamp": "2020-03-09T18:00:54.000+05:30",
        "host": {
          "hostname": "bionic",
          "name": "bionic"
        }
      }'

# Update flattened field with new inner fields.
# Inner fields will not be added to mappings
curl -X POST "http://localhost:9200/demo-flattened/_update/1" \
  -H "Content-Type: application/json" \
  -d  '{
        "doc" : {
          "host" : {
            "osVersion": "Bionic Beaver",
            "osArchitecture":"x86_64"
          }
        }
      }'
```

## Search fields with type flattened

- Supported queries

  - `term`
  - `prefix`
  - `range`
  - `match`
  - `query_string`
  - `exists`

```shell
# Search term "host" check all inner fields
curl -X GET "http://localhost:9200/demo-flattened/_search?pretty=true" \
  -H "Content-Type: application/json" \
  -d  '{
        "query": {
          "term": {
            "host": "Bionic Beaver"
          }
        }
      }'

# Search term "host.osVersion" check all inner fields
curl -X GET "http://localhost:9200/demo-flattened/_search?pretty=true" \
  -H "Content-Type: application/json" \
  -d  '{
        "query": {
          "term": {
            "host.osVersion": "Bionic Beaver"
          }
        }
      }'

# Partial match to inner fields wil not work! Because the fields are not analyzed
curl -X GET "http://localhost:9200/demo-flattened/_search?pretty=true" \
  -H "Content-Type: application/json" \
   -d '{
        "query": {
          "term": {
            "host.osVersion": "Beaver"
          }
        }
      }'
```
