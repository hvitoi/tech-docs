# Command Query Responsibility Segregation (CQRS)

- Responsabilities for the data aggregation (`command` and `query`) are "segregated"
- `queries` (select) are performed in a database and `commands` (update, create, delete) are performed in another database

![CQRS](../images/cqrs.png)

![CQRS Databases](../images/cqrs-databases.png)

## Sync strategies

- The process of replication the database from the command database to the query database is called `event`
- Ways to sync the data
  - `Automatic`: synchronously sync the databases on every state state. Slow!
  - `Eventual`: asynchronously sync the databases on every state state
  - `Controlled`: sync operation is scheduled
  - `On Demand`: sync is performed when the data is requested

## Consistency

- `Eventual consistency`: updates from time to time, not immediately
- `Strong consistency`: updates on every change immediately
