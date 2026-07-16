# Consistency

- A transaction moves the database from one **valid state** to another — it cannot violate constraints (primary keys, foreign keys, check constraints, triggers)
- If a transaction would leave the database in an invalid state, it is aborted
- This is the **application-level** ACID property: the database enforces the rules, but the application defines what "valid" means via schema and constraints
