# Splunk Query Language

```conf
index=<index>
source=<source>
data.log=in-response*
data.path=/api/quote
| stats avg(data.timing-ms)
```
