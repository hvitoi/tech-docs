# list-credentials-as-xml

- Export credentials as XML
- `store-id` is identified by `Provider::Resolver::ContextPath`
  - E.g., _system::system::jenkins_, _folder::item::/full/name/of/folder_

```sh
jenkinscli list-credentials-as-xml "store-id"
jenkinscli list-credentials-as-xml "system::system::jenkins"
```
