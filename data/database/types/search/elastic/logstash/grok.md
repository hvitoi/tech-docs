# Parsing unstructured data with GROK

- Grok uses regex behind the scenes
- A predefined list of regex rules and its name can be found at <https://www.elastic.co/guide/en/logstash/current/plugins-filters-grok.html>
- Grok debugger tool: <http://grokdebug.herokuapp.com/>
- Generic grok sintax

```conf
%{PATTERN:identifier}
```

- Example: `2020-07-16T19:20:30.45+01:00 DEBUG This is sample log`

```log
2020-10-11T09:49:35Z INFO variable server value is tomcat
2020-03-14T22:50:34Z ERROR cannot find the requested resource
2020-01-02T14:58:40Z INFO initializing the bootup
2020-06-04T06:56:04Z DEBUG initializing checksum
2020-05-07T03:07:11Z INFO variable server value is tomcat
```

```conf
input {
  file {
    path => "/tmp/txt/log-data.txt"
    start_position => "beginning"
    sincedb_path => "/dev/null"
  }
}
filter {
  grok {
    match => { "message" => ['%{TIMESTAMP_ISO8601:time} %{LOGLEVEL:logLevel} %{GREEDYDATA:logMessage}'] }
  }
}
output {
   elasticsearch {
     hosts => "http://elasticsearch:9200"
     index => "grok-demo"
  }
  stdout {}
}
```

## Pattern failure

- If a pattern doesn't match, a tag `_grokparsefailure` will be added to the document

```shell
curl -s "localhost:9200/nginx-logs/_search" \
  --request GET \
  --header "Content-Type: application/json" \
  --data @search.json \
| jq .
```

- Exclude glok parse failure from the search

```json
{
  "size": 1,
  "track_total_hits": true,
  "query": {
    "bool": {
      "must_not": [
        {
          "term": {
            "tags.keyword": "_grokparsefailure"
          }
        }
      ]
    }
  }
}
```

- Get only multiline logs

```json
{
  "size": 1,
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "tags": "multiline"
          }
        }
      ]
    }
  }
}
```
