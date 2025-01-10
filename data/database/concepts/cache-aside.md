# Cache Aside

> When an application needs to access data, it first checks the cache. If the data is not present (a cache miss), it fetches the data from the data store, stores it in the cache, and then returns the data to the user. This pattern is particularly useful for scenarios where data is read frequently but updated less often.

- <https://learn.microsoft.com/en-us/azure/architecture/patterns/cache-aside>
- Improve performance of frequently-accessed data
- Check the cache first for the data (`lookup`) and it's it's not there, `fetch` and cache the data from db (`miss`)
  - Lookup of miss
