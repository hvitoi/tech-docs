# Scalability

- It's the measure of a system's ability to `handle a growing amount of work` by adding resources to the system
- The resources need to be well managed in order to be used effectively and avoid overheads
- Solutions
  - LB
  - DB Sharding
  - API gateway (organization scalability/flexibility - decouple the frontend from the internal structure)

## Vertical Scalability (scale up)

- Add or upgrade existing resources on a single computer
- E.g., more memory, cpu
- Any application can benefit from it (node code changes required)

## Horizontal Scalability (scale out)

- Add more resources in form of new instances/machines
- No limit on scalability
- The system should be designed to scale horizontally (sometimes not easily refactored, e.g., concurrency issues)
- Increased complexity, coordination overhead

## Team/Org Scalability

- More engineers
- Better to have smaller groups of engineers each working on a module/service of the system
