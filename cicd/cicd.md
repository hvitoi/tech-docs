# CI/CD (Continuous Integration / Continuous Delivery)

- `CI` is the process in which developers regularly merge their code into main branches of repositories
  - Either through short-lived branches or directly to main
  - Regular merging into mainline requires `automated testing`
  - The final stage of CI is an artifact (a jar, a docker image, etc) that is deliverable
- `CD` is the process of regularly delivering code changes to production

## Steps

- **Continuous Integration**
  1. `Code`: Commit and merge code changes to a git repository.
  1. `Build`: build the code into a binary (jar, docker image)
  1. `Test`
  1. `Release`: Push to Artifact repository

- **Continuos Delivery**
  1. `Deploy`
  1. `Operate`
  1. `Observe`
  1. `Plan`: plan the next code changes
