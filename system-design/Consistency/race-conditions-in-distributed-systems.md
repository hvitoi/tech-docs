# Handling race condition

- If two instances try to acquire and change a resource at the same time, it may lead to consistent states
- Example: two people try to book a seat at the same time

## Locks

- Whenever an instance tries to start a transaction (e.g., select + update) than it acquires a lock to avoid other instances to access it

## Conditional Updates

- Performs a check before updating an item
- This way, the race condition (caused by the select + update) is handled by the database iself
