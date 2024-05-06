# Handling race condition

- If two instances try to acquire and change a resource at the same time, it may lead to consistent states
- Example: two people try to book a seat at the same time

## Transactions

- In databases, `transactions` provide `ACID properties` (atomicity, consistency, isolation, and durability)
- This way, it's guaranteed that two instances won't update a value simultaneously

## Optimistic Locking

- Each `write operation` includes a `version` or `timestamp`.
- Before updating the data, check whether the version or timestamp has changed since the data was retrieved
- If it has changed, it indicates that another operation has modified the data, and appropriate actions can be taken, such as retrying the operation or notifying the user.
- The write operation has to be done using `conditional write` to ensure that the version/timestamp is the same as previously fetched

## Pessimistic Locking

- This involves `locking the data resource exclusively` when it is being worked on by a service or thread
- While effective in preventing race conditions, it can also lead to `scalability and performance issues`, as it may introduce contention among multiple services or threads.

## Idempotent Operations

- Design operations to be idempotent, meaning that performing the operation multiple times has the same effect as performing it once.
- This allows retries of failed operations without causing unintended side effects or data inconsistencies

## Eventual Consistency

- Accepts `Availability` & `Partition Tolerance` in favor of Consistency
- Embrace the concept of eventual consistency, where data replicas may temporarily diverge but eventually converge to a consistent state.
- Design services to handle eventual consistency gracefully by implementing conflict resolution mechanisms and reconciliation processes.

## Circuit Breaker Pattern

- Implement circuit breaker patterns to prevent cascading failures caused by race conditions.
- When a service detects that a downstream service is experiencing issues, it can temporarily halt requests to that service, preventing further degradation of the system.
