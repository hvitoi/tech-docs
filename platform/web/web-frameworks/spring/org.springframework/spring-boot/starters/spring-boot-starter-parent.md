# spring-boot-starter-parent

- Spring boot starters are dependencies! Like features you can add to your application
- `spring-boot-starter-parent` is a special starter that provides Maven defaults

```xml
<parent>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-parent</artifactId>
  <version>3.5.5</version>
  <relativePath /> <!-- lookup parent from repository -->
</parent>
```

- There's no need to specify versions spring boot dependencies (e.g., spring-boot-starter, spring-boot-starter-test, spring-boot-maven-plugin)
- They are all inherited by the `spring-boot-starter-parent` parent
- Ensures that all versions are compatible
