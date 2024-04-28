# Materialized View

- A read-only database that is populated based on the events coming from multiple other databases
- This way, all the information that the service needs to operate is contained in itself and there is no need to perform multiple integrations
- A materialized view is never updated directly by an application, and so it's a `specialized cache`
- Materialized View is usually applied in conjunction with CQRS

![Materialized View](.images/materialized-view.png)
![CQRS + Materialized View](.images/cqrs+materialized-view.png)
