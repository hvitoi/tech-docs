# spring-boot-starter-data-jpa

- `org.springframework.boot.spring-boot-starter-data-jpa`

- JPA (Java Persistence API) and hibernate
- JPA is an standard API for ORM (a set of interfaces)
- Hibernate implements the JPA interfaces
- Hibernate is the default implementation of JPA on Spring Boot
- `EntityManager` is a wrapper on the hibernate session (wraps the SessionFactory)

- Generate `DAO API` from an `Entity` and `Primary Key`
- Expose methods to manipulate database information automatically

```java
package com.hvitoi.demo.dao;

import org.springframework.data.jpa.repository.JpaRepository;
import com.hvitoi.demo.entity.Employee;

public interface EmployeeRepository extends JpaRepository<Employee, Integer> {
}
```

- Expose many methods such as
  - findAll
  - findById
  - save
  - deleteById
