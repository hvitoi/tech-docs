# disable-plugin

- Disable one or more installed plugins
- Disable strategy
  - `none`: if it has a mandatory dependent plugin, it cannot be disabled
  - `mandatory`: all mandatory dependent plugins are also disabled, optional dependent plugins are kept
  - `all`: all mandatory and optional dependent plugins are disabled

```sh
jenkinscli disable-plugin "plugin-name"
jenkinscli disable-plugin "plugin-name" -quiet # print only error messages
jenkinscli disable-plugin "plugin-name" -restart # restart after disabling

# disable strategy
jenkinscli disable-plugin "plugin-name" -strategy "none"
jenkinscli disable-plugin "plugin-name" -strategy "mandatory"
jenkinscli disable-plugin "plugin-name" -strategy "all"
```
