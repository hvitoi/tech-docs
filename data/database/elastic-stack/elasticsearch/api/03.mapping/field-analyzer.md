# Mapping Field Analyzer

- `Character filtering`
  - E.g., remove html encoding, convert & to and
- `Tokenizer`
  - Split strings with a pattern
- `Token filter`

  - Lowercasing, stemming, synonyms, stopwords

- Analyzer options
  - `standard`: split on words boundaries, remove punctuation, lowercase everything
  - `simple`: split on anything that isn't a letter, lowercase everything
  - `whitespace`: split on whitespaces
  - `english`: account for language-specific stop-words and stemming

```json
{
  "mappings": {
    "properties": {
      "description": {
        "type": "text",
        "analyzer": "english" // field analyzer
      }
    }
  }
}
```
