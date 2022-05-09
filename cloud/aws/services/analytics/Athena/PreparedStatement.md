# AWS::Athena::PreparedStatement

- Specifies a prepared statement for use with SQL queries in Athena.

```yaml
Type: AWS::Athena::PreparedStatement
Properties:
  Description: String
  QueryStatement: String
  StatementName: String
  WorkGroup: String
```

## QueryStatement

```sql
-- Select ALL
SELECT * FROM "s3_access_logs_db"."mybucket_logs" limit 10;

-- Group BY
SELECT
  requesturi_operation,
  httpstatus,
  count(*)
FROM
  "s3_access_logs_db"."mybucket_logs"
GROUP BY
  requesturi_operation,
  httpstatus;

-- Where
SELECT
  *
FROM
  "s3_access_logs_db"."mybucket_logs"
where
  httpstatus = '403';
```
