# Key-Value Databases

Key: value
→ The access mechanism is the key
→ High performance!

## Redis

→ Key-value NoSQL DB
→ Open source
→ Can be scaled horizontally in a distributed mode
→ Automatically partition data to other nodes

## The Big-O notation

- O (1): time for the operation always constant
- O (n): time for the operation linearly proportional to the data it contains
- O (LogN): ...
- O (NlogN): ...
- O (Log N+M): …

## Data Structures

- String: Most generic data type, can store anything. Until 512MB

→ Key
→ String
→ Hash: Allows multiple keys
→ List: Order preserved and acessed by LPOP and RPOP
→ Set: Order not preserved. Do not allow duplicates
→ Sorted set
→ Hyperloglog
→ Geo: Coordinates. GIS. Extension of the sorted list.
→ Pub sub
→ Transaction

## Modelling in Key-Value Databases

→ Redis as primary database
→ Redis are cache (fast memory access)
