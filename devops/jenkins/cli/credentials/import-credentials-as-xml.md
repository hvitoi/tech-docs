# import-credentials-as-xml

- Import credentials as XML
- The output of `list-credentials-as-xml` can be used as input here (just set the actual Secrets which are redacted in the output)
- `store-id` is to store to where import the credentials. E.g., "system::system::jenkins"

```sh
jenkinscli import-credentials-as-xml "store-id" < "credentials.xml"
```
