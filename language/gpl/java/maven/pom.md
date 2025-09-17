# pom (Project Object Model)

- Metadata: name, version, output (jar, war)
- Dependencies: list of dependencies to download
- Plugins: additional tasks to run (e.g., generate test reports)

```xml
<!-- pom.xml -->
<project ...>
  <modelVersion>4.0.0</modelVersion>

  <groupId>com.hvitoi</groupId>
  <artifactId>awesome-app</artifactId>
  <version>1.0-SNAPSHOT</version>
  <name>aop-demo</name>

  <properties>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <maven.compiler.source>11</maven.compiler.source>
    <maven.compiler.target>11</maven.compiler.target>
  </properties>

  <dependencies>
    <dependency> <!-- GAV: GroupID, ArtifactID, Version -->
      <groupId>org.springframework</groupId>
      <artifactId>spring-context</artifactId>
      <version>5.3.9</version> <!-- version is optional but highly recommended -->
    </dependency>
  </dependencies>

  <build>
    <pluginManagement>
      <plugins>
        ...
      </plugins>
    </pluginManagement>
  </build>

</project>
```
