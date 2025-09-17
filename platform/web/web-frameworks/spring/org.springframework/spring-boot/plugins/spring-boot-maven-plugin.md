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

```shell
# Build (generate jar)
mvn package

# Run app
java -jar "demo-0.0.1-SNAPSHOT.jar"
mvn spring-boot:run

# Build container image for the app
mvn spring-boot:build-image
```
