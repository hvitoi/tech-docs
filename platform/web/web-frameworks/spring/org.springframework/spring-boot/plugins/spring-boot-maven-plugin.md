# spring-boot-maven-plugin

```xml
<build>
  <plugins>
   <plugin>

    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-maven-plugin</artifactId>

    <!-- Container image build configuration -->
    <configuration>
      <image>
        <name>hvitoi/ms-${project.artifactId}:${project.version}</name>
      </image>
      <pullPolicy>IF_NOT_PRESENT</pullPolicy>
    </configuration>

   </plugin>
  </plugins>
 </build>
```

## Goals

### run

```shell
mvn spring-boot:run

# Or compile & run manually
mvn package
java -jar "demo-0.0.1-SNAPSHOT.jar"
```

### build-image

```shell
# Build container image for the app
mvn spring-boot:build-image
```
