# CI/CD (Continuous Integration / Continuous Delivery)

- `CI` is the process in which developers regularly merge their code into main branches of repositories
  - Either through short-lived branches or directly to main
  - Regular merging into mainline requires `automated testing`
  - The final stage of CI is an artifact (a jar, a docker image, etc) that is deliverable
- `CD` is the process of regularly delivering code changes to production

## Steps

1. Merge code changes
2. Tests
3. Build
4. Scans
5. Artifact repository
6. Deploy
