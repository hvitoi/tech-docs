# Database Cursor

- A database cursor is essentially a `pointer` or handle that the database gives you to iterate over the results of a query.
- It doesn't load all the results into your program at once, instead it lets you read piece by piece.

- When you execute a query, the database doesn’t have to send all rows to your program immediately.
- Instead, it creates a cursor that keeps track of where you are in the result set.
- Your application can then fetch rows one at a time, or in chunks, from that cursor.

## Why?

- `Efficient memory use`: you can work with very large result sets without loading everything into RAM.
- `Streaming`: you can start processing rows as they arrive, instead of waiting for the entire query to finish.
- `Control`: you can fetch, skip, or close the cursor as needed.

## Active connection

- The cursor keeps the connection "alive" until you finish fetching all rows or explicitly close it.
- For very large result sets, the database may maintain locks or resources for that query, which can impact performance.

## Best practices

- Fetch in batches if possible (e.g., 100–1000 rows at a time) instead of row by row. Many DB drivers support fetchmany(batch_size).
- Close cursors and connections as soon as you're done.
- For read-heavy applications, consider `pagination` or `materialized views` to reduce the size of queries that keep cursors open for a long time.
