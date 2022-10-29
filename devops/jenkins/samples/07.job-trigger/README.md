# Job triggering in Jenkins

## Crontab

- New Item -> `Build Triggers` -> Build periodically
- <https://crontab.guru/>

```crontab
H 1 * * *
```

- With `H` (Instead of `0`), jenkins decides which job to run first (instead of running all of them at same time)
  - In order to control resources

## Trigger a job externally

- Give user permission to trigger any job
- Invoke the URL of the job `http://localhost:8080/job/simple-job/build?delay=0sec` with a crumb!
- CSRF protection must be enabled in Global security in order to get a crumb

```sh
# Get a Jenkins-crumb token!
curl -u "admin:123" -s 'http://localhost:8080/crumbIssuer/api/xml?xpath=concat(//crumbRequestField,":",//crumb)'

# Invoke job with a crumb (No parameters)
curl -u "admin:123" -H "$crumb" -X POST "http://localhost:8080/job/simple-job/build?delay=0sec"

# Invoke job with a crumb (With parameters)
curl -u "admin:123" -H "$crumb" -X POST "http://localhost:8080/job/simple-job/buildWithParameters?DB_HOST=db&DB_NAME=testdbql"
```

```sh
# Invoke job with a token (No parameters)
curl -u "admin:123" "http://localhost:8080/job/simple-job/build?token=mytoken" # Token is configured in the item configuration

# Invoke job with a token (With parameters)
curl -u "admin:123" "http://localhost:8080/job/simple-job/buildWithParameters?token=mytoken&DB_HOST=db&DB_NAME=testdbql"
```
