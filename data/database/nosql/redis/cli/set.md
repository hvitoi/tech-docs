# set

- <https://redis.io/commands#set>

```sh
# Set data
SET "key" "value"
SET "count" "10"

# Create some string data
SADD demo.ml.genres Action Adventure Animation Children Comedy Crime Drama Fantasy
SADD demo.ml.genres War Western Horror Sci-Fi Mystery Romance Thriller Fantasy Documentary Film-Noir

# Return the cardinality of the set
SCARD demo.ml.genres

# Inspect the type and object encoding
TYPE demo.ml.genres
OBJECT ENCODING demo.ml.genres

# Return all members of the set. Be careful as this could contain a lot of records
SMEMBERS demo.ml.genres

# Check if an item is a member of the set
SISMEMBER demo.ml.genres Action
SISMEMBER demo.ml.genres Actions

# Randomly return x members of the set
SRANDMEMBER demo.ml.genres 2

# Create a new set
SADD demo.ml.genres.viewed Documentary Adventure Thriller Comedy Drama Fantasy

# Find all items common to both sets. use SINTERSTORE to do the same but store the value in a new set
SINTER demo.ml.genres demo.ml.genres.viewed

# Find the difference between the first set and the rest. use SDIFFSTORE to do the same but store the value in a new set
SDIFF demo.ml.genres demo.ml.genres.viewed

# Remove and return a random value from this set
SPOP demo.ml.genres.viewed

# Remove the item named from this set
SREM demo.ml.genres.viewed Drama
```
