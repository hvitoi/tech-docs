# Hash Table

- Uses a `hash function` to calculate the index (hash code) based on the `key` name
- The values are stored within a large array, known as `array of buckets` or `slots`
- Ideally, the hash function assigns each `key` to a unique `bucket` (within the array of buckets). This is where the `key-value` pair is stored
- During lookup, the key is hashed and the resulting hash indicates where the corresponding value is stored (within the array of buckets)
- Hash tables are `unordered`

## Tradeoffs

- Hash tables have a `great time complexity` ($O(1)$) for all operation (insert, remove, lookup)
- At the cost of a `bad space complexity` given that a large array of buckets is needed to accomodate all possible key-value pairs

## Load factor

The proportion between `filled slots` in the array of buckets and the `total available slots`

$$load\ factor\ (\alpha) = \frac{n}{m}$$

where

- $n$ is the number of entries occupied in the hash table.
- $m$ is the number of buckets

When the load factor is reaching 1, it's necessary to resize the array of buckets and rehash everything

## Collisions

- Since hash functions are `surjective functions` (sobrejetora), different keys can output the same hash, leading to the so called `collision`
- **Separate chaining**
  - It's a collision resolution method
  - Whenever a collision happens, the data in saved on top of the previous data, not overwriting it, but referencing the new data like a `linked list`
  - When there is a collision, the access to the element is then $O(n/k)$ instead of $O(1)$

## Other applications

- Associative arrays
- Database indexing
- Caches
- Sets
