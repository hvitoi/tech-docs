# maven-clean-plugin

- <https://maven.apache.org/plugins/>
- <https://maven.apache.org/plugins/maven-clean-plugin/>
- <https://maven.apache.org/ref/current/maven-core/lifecycles.html#clean_Lifecycle>

```xml
<plugin>
  <artifactId>maven-clean-plugin</artifactId>
  <version>3.4.0</version>
</plugin>
```

- Deletes the `target/` directory (where compiled classes and built JARs go)

## Goals

### clean (default)

```shell
mvn clean
mvn clean:clean # same
```
