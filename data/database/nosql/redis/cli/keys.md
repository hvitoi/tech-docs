# keys

- <https://redis.io/commands#generic>

```sh
ECHO "List keys in your redis server"
KEYS *


# There is no command to create a key. Keys are created when key-value pairs are set.

# Create some key-value pairs
SET foo bar
SET demo.redis.cli.hello world
SET demo.redis.cli.keys 12999030039

SADD demo.redis.cli.set0001 apple
HSET demo.redis.cli.hash001 movieId 3 title "Shawshank Redemption" genres "Comedy|Adventure" year 1998
ZADD demo.redis.cli.10202-scoreboard 6 James 2 Shane 9 Ezekiel 1 Darwin
PFADD demo.redis.cli.hll001

# List keys with conditions
KEYS *
KEYS demo.*

# Confirm the existence of a key
EXISTS demo.redis.cli.hll001
EXISTS demo.redis.cli.hll002s

# Confirm the TTL (time to live) of a key. PTTL the same, but in ms.
TTL demo.redis.cli.set0001
PTTL demo.redis.cli.10202-scoreboard

# Set the TTL of a key. PEXPIRE in ms.
EXPIRE foos 5
GET foos
PEXPIRE mylist 3600000

# Delete a key
DEL demo.redis.cli.keys

# Check the type of the value held by a key
TYPE demo.redis.cli.set0001
TYPE demo.redis.cli.hash001
TYPE demo.redis.cli.10202-scoreboard
TYPE demo.redis.cli.hll001
```
