# Apache Pig

- Alternative way to write mapreduce/tez code
- Uses `Pig Latin` as scripting language with a `SQL-like syntax`
- Extensible with `user-defined functions` (UDF)
- Running pig
  - From grunt CLI
  - Script filename
  - Ambari/Hue UI
- Using pig with Tez is faster because it uses `directed acyclic graph`

## Commands

- `FILTER`: filter data
- `DISTINCT`: select unique values
- `FOREACH/GENERATE`: allows mapping data
- `MAPREDUCE`: explicit mappers and reducers
- `STREAM`: use stdin/stdout
- `SAMPLE`: sample from relation

- `JOIN BY`: join tables
- `COGROUP`: separate tuple for each key
- `GROUP BY`: groub by. Aggregate different keys
- `CROSS`: cross join
- `CUBE`: cross join for multiple tables

- `ORDER`: order by
- `RANK`: assigns a number for each row
- `LIMIT`: max number of results

- `UNION`: merge relations
- `SPLIT`: split relations

- `DESCRIBE`: describes the columns of a relation
- `EXPLAIN`: explains how the query will be executed
- `ILLUSTRATE`: explain but more detailed with examples

- Input/Output

  - `LOAD`: read data from a file
  - `STORE`: write data to a file (STORE ratings INTO 'outRatings' USING PigStorage(':');)
  - `DUMP`: print result

- User Defined Functions

  - `REGISTER`: UDF from jar files
  - `DEFINE`: assign names to UDFs
  - `IMPORT`: import macros from other pig scripts

- Aggregation functions

  - `AVG`
  - `CONCAT`
  - `COUNT`
  - `MAX`
  - `MIN`
  - `SIZE`
  - `SUM`

- Pig Storage Classes

  - `PigStorage`: set the delimiter (; , |) of the input/output data
  - `TextLoader`: loads one line at time
  - `JsonLoader`: loads from json
  - `AvroStorage`: loads from avro
  - `ParquetLoader`: loads from parquet (this is a column-oriented data structure)
  - `OrcStorage`: loads from orc (compressed format)
  - `HBaseStorage`: integrate pig with hbase
