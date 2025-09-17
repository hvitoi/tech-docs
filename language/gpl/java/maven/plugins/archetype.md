# maven-archetype-plugin

- <https://maven.apache.org/archetype/maven-archetype-plugin/>
- <https://maven.apache.org/plugins/>

- Create a Maven project from an existing template

## Templates (Archetypes)

- `org.apachage.maven.archetypes.maven-archetype-quickstart`
- `org.apachage.maven.archetypes.maven-archetype-webapp`

## Goals

### generate

```shell
mvn archetype:generate \
  -DgroupId=com.hvitoi \
  -DartifactId=demo \
  -DarchetypeArtifactId=maven-archetype-quickstart \
  -DarchetypeVersion=1.5 \
  -DinteractiveMode=false
```
