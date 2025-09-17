# Spring Boot

- Make it easy to start a Spring project
- Minimize the amount of manual configuration
- Provides an `embedded HTTP server` (tomcat, jetty, undertow, ...)
  - But you can also deploy the `war file` to an external server

## Spring Initializr

- `Spring Initializr` creates a spring project boilerplate
  - <https://start.spring.io/>
  - `jar`: do not use src/main/webapp folder
  - `war`: use src/main/webapp

## Project Structure

```txt
.
├── HELP.md
├── pom.xml
├── mvnw         # embedded maven cmdline, run maven commands with no need to have maven installed (safe to remove) ./mvnw clean compile test
├── mvnw.cmd     # same as mvnw, but for windows
├── .mvn
│   └── wrapper
│       └── maven-wrapper.properties # maven properties
├── src/
│   ├── main/
│   │   ├── java/                        # source code
│   │   │   └── com/
│   │   └── resources/
│   │       ├── static/                 # html, css, js, images, etc
│   │       ├── templates/              #
│   │       └── application.properties  # properties and config file
│   └── test/
│       └── java/                        # unit tests
│           └── com/
└── target/
    ├── classes/
    │   ├── application.properties
    │   └── com/
    └── test-classes/
        └── com/
```

## Application

- `@SpringBootApplication`
  - @EnableAutoConfiguration: auto-configuration support
  - @ComponentScan: scan components to register beans
  - @Configuration: register extra beans

- `SpringApplication.run(DemoApplication.class, args)`
  - Creates the application context and register all beans
  - Starts the embedded server

- Place your `Application.java` in the root package
  - Implicitly defines the base search package (component scanning)
  - You can also explicitly base package with `scanBasePackages` parameter

```java
package com.hvitoi.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication // @SpringBootApplication(scanBasePackages={"com.hvitoi.demo", "org.acme.iot.utils"})
public class DemoApplication {

  public static void main(String[] args) {
    SpringApplication.run(DemoApplication.class, args);
  }
}
```
