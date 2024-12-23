# ACID

## Atomicity

- Each transaction is `all or nothing`
- If a part of a transaction fails, the entire transaction fails and the db is left unchanged
- The outcome of a transaction can either be completely successful or completely unsuccessful. The whole transaction must be rolled back if one part of it fails.

## Consistency

- Transactions maintain integrity restrictions by moving the database from one valid state to another valid state. The transaction cannot violate predefined rules or else it will fail.

## Isolation

- Concurrent transactions are isolated from one another, assuring the accuracy of the data. On modern rdbms it has lock-by-row mechanisms

## Durability

- Once a transaction is committed, its modifications remain in effect even in the event of a system failure.
