# npm config

## List

```shell
npm config list
npm config list -l # additional info
```

## Set

```shell
# Set the registry globally
npm config set registry "registry-url"

# Set the registry for the package scope
npm config set "@your-scope":registry "registry-url"
npm config set "@microservicos-api":registry "http://my-registry:8082/repository/microservicos-api-npm"
```

```json
{
  "publishConfig": {
    "registry": "http://my-registry:8082/repository/microservicos-api-npm"
  }
}
```
