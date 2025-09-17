# spring-boot-starter-data-rest

- `org.springframework.boot.spring-boot-starter-data-rest`
- Generate REST API automatically from an Entity

- Generate a `REST API` from a `Repository`
- Expose REST endpoints for entities automatically
- Simply add the dependency

```xml
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-data-rest</artifactId>
</dependency>
```

![Spring Data JPA & Spring Data REST](./images/data-jpa-data-rest.png)

- Spring Data REST endpoints are `HATEOAS` compliant

  - `Hypermedia as the Engine of Application State` (HATEOS)
  - Hypermedia-driven sites provide information to access REST interfaces (Metadata of REST data)
  - HATEOS uses `Hypertext Application Language` (HAL) data format (format of the json)
  - Offer `pagination`, `sorting`, `searching`, etc
  - Offer `Query Domain Specific Language` (Query DSL)

- @RepositoryRestResource(path = "employees"): modifies the path (case the word has a complex plural)

```java
@RepositoryRestResource(path = "employees") // if not specified "employee + s" will be used
public interface EmployeeRepository extends JpaRepository<Employee, Integer> {
  // Give "Entity Type" and "Primary Key" and receive a funcional DAO
  // There is no implementation, just the interface
}

```

- Example: `GET /employees`
  - For collections, medata includes page size, total elements, pages, etc

```json
{
  "_embedded": {
    "employees": [
      {
        "firstName": "Leslie",
        "lastName": "Andrews",
        "email": "leslie@luv2code.com",
        "_links": {
          "self": {
            "href": "http://localhost:8080/magic-api/employees/1"
          },
          "employee": {
            "href": "http://localhost:8080/magic-api/employees/1"
          }
        }
      },
      {
        "firstName": "Emma",
        "lastName": "Baumgarten",
        "email": "emma@luv2code.com",
        "_links": {
          "self": {
            "href": "http://localhost:8080/magic-api/employees/2"
          },
          "employee": {
            "href": "http://localhost:8080/magic-api/employees/2"
          }
        }
      }
    ]
  },
  "_links": {
    "self": {
      "href": "http://localhost:8080/magic-api/employees"
    },
    "profile": {
      "href": "http://localhost:8080/magic-api/profile/employees"
    }
  },
  "page": {
    "size": 20,
    "totalElements": 2,
    "totalPages": 1,
    "number": 0
  }
}
```

- Example: `GET /employees/1`

```json
{
  "firstName": "Leslie",
  "lastName": "Andrews",
  "email": "leslie@luv2code.com",
  "_links": {
    "self": {
      "href": "http://localhost:8080/magic-api/employees/1"
    },
    "employee": {
      "href": "http://localhost:8080/magic-api/employees/1"
    }
  }
}
```

- Other queries
  - `/employees?page=1`
  - `/employees?page=1`
  - `/employees?sort=lastName`
  - `/employees?sort=lastName,desc`
  - `/employees?sort=lastName,firstName,asc`
