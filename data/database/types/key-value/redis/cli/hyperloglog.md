# hyperloglog

- <https://redis.io/commands#hyperloglog>

```shell
# Create some string data
PFADD demo.ml.rating.users 1 1 3 4 12 3 4 6 3 5 7 65 5 33 2 213 3 7 4

# Introspecting our structure
TYPE demo.ml.rating.users
OBJECT ENCODING demo.ml.rating.users

# Count the number of items in our hyperloglog. Hyperloglog stores only unique values"
PFCOUNT demo.ml.rating.users
```
