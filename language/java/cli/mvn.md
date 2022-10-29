# Maven

- Build management and dependencies
- Avoid having to manually add jar files to `classpath` (build path)
- Local cache is stored at `~/.m2/repository/`

## Standard Directory Structure

- `src/main/java`: source code
- `src/main/resources`: properties and config files
- `src/main/webapp`: JSP files and web config files. Other web assets (images, css, js)
- `src/test`: unit tests
- `target`: compiled code

## pom.xml

- `Project Object Model` (POM file)
  - Metadata: name, version, output (jar,war)
  - Dependencies: list of dependencies to download
  - Plugins: additional tasks to run (e.g., generate test reports)

```xml
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

- To install a maven dependency in maven, go to the [MVN Repository](https://mvnrepository.com/) and search for the dependency

## Archetypes

- Boilerplate for new projects
  - `org.apachage.maven.archetypes.maven-archetype-quickstart`
  - `org.apachage.maven.archetypes.maven-archetype-webapp`

## Private Repositories

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

## Command Line Interface

```sh
mvn clean
mvn package
mvn install # install the current project into the ~/.m2 folder
mvn test # test reports are stored at "target/surefire-reports" folder
mvn -B -DskipTests clean package
```
