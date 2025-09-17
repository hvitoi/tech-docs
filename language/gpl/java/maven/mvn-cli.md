# mvn

## Built-in Goals (Tasks)

```shell
# Deletes the target/ directory (where compiled classes and built JARs go)
mvn clean

# Compiles the code, runs tests, and builds the artifact (JAR/WAR) in target
mvn package

mvn install # install the current project into the ~/.m2 folder
mvn test # test reports are stored at "target/surefire-reports" folder
mvn -B -DskipTests clean package
```
