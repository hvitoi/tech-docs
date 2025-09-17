# Repositories

- To install a maven dependency in maven, go to the [MVN Repository](https://mvnrepository.com/) and search for the dependency

## Private repositories

- Maven server tools
  - `Archiva` (Apache)
  - `Artifactory` (JFrog)
  - `Nexus` (Sonatype)

```xml
<repositories>
  <repository>
    <id>confluent</id>
    <url>https://packages.confluent.io/maven/</url>
  </repository>
</repositories>
```
