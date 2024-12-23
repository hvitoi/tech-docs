# Optimistic Concurrency Control

- A `_seq_no_` number stores the sequence number to represent the chronological number of the event
- `seq_no` does not increase one by one

## Parameters

- `if_seq_no` checks if you are picking the correct sequence number
- `if_primary_term`
- `retry_on_conflict`: number of times to retry automatically

```shell
# Deal with concurrency issues
curl -X PUT "localhost:9200/movies/_doc/109487?if_seq_no=7&if_primary_term=1&retry_on_conflict=5" \
  -H "Content-Type: application/json" \
  -d  '
        {
          "genre": ["IMAX", "Sci-Fi"],
          "title": "Interstellar",
          "year": 2014
        }
      '
```
