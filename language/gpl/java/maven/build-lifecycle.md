# Lifecycle phases

- <https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html>

- `validate` → `compile` → `test` → `package` → `verify` → `install` → `deploy`

## test

- By default, uses the surefire plugin
- Test reports are stored at "target/surefire-reports" folder

```shell
mvn test # Equivalent to mvn surefire:test
```

## package

```shell
# Compiles the code, runs tests, and builds the artifact (JAR/WAR) in target
mvn package

mvn -B -DskipTests clean package
```
