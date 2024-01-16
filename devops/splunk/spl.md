# Splunk Query Language

```conf
index=<index>
source=<source>
log=<log>
```

## stats

```sql
| stats avg(<field>)
```

```sql
| stats count by <field>
```

```sql
-- distinct count
| stats dc(<field>)
```

## dedup

- Get only one entry for each unique field

```sql
| dedup <field>
```

## table

- Generate a table and specify the fields to be the columns

```sql
| table <field>
```

## timechart

- Count occurences by a time interval

```sql
| timechart count span=60s
```
