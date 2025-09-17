# Properties

- <https://docs.spring.io/spring-boot/docs/current/reference/html/application-properties.html#application-properties>
  - Core
  - Web
  - Security: login form and user management
  - Data: data source, entity manager
  - Actuator
  - Integration
  - DevTools
  - Testing

```conf
spring.application.name=demo


server.port=8585
coach.name=Mickey Mouse
team.name=The Mouse Crew
```

```java
@RestController
public class FunRestController {
  @Value("${coach.name}")
  private String coachName

  @Value("${team.name}")
  private String teamName
}
```
