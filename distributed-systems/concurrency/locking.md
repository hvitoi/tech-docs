# Locking

## Optimistic Locking

- Each `write operation` includes a `version` or `timestamp`.
- Before updating the data, check whether the version or timestamp has changed since the data was retrieved
- If it has changed, it indicates that another operation has modified the data, and appropriate actions can be taken, such as retrying the operation or notifying the user.
- The write operation has to be done using `conditional write` to ensure that the version/timestamp is the same as previously fetched

## Pessimistic Locking

- This involves `locking the data resource exclusively` when it is being worked on by a service or thread
- While effective in preventing race conditions, it can also lead to `scalability and performance issues`, as it may introduce contention among multiple services or threads.
