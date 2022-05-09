# Fuzzy queries

- A way to account for typos and misspellings
- The `levenshtein edit distance` accounts for:
  1. `substitution`: interstellar -> intersteller
  1. `insertions`: interstellar -> insterstellar
  1. `deletion`: interstellar -> interstelar
- The edit distance can be parametrized with `fuzziness`

```shell
curl -s "localhost:9200/movies/_search" \
  --request GET \
  --header "Content-Type: application/json" \
  --data @search.json \
| jq .
```

## Fuzziness

- Fuzziness defines the levenshtein edit distance
- The auto option defines the edit distance dynamically
- `"fuzziness": "auto"`
  - `0` to 1-2 character strings
  - `1` to 3-5 character strings
  - `2` for anything else

```json
{
  "query": {
    "fuzzy": {
      "title": {
        "value": "intrsteller",
        "fuzziness": 2
      }
    }
  }
}
```
