# list-credentials

- Lists the Credentials in a specific Store
- `store-id` is identified by `Provider::Resolver::ContextPath`
  - E.g., _system::system::jenkins_, _folder::item::/full/name/of/folder_

```sh
jenkinscli list-credentials "store-id"
jenkinscli list-credentials "system::system::jenkins"
```
