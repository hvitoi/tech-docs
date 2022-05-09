# list

- <https://redis.io/commands#list>

```shell
# Create some string data

# Insert on the left - Head
LPUSH demo.ml.ratings "1::1193::5::978300760" "1::661::3::978302109"
# Insert on the right - Tail
RPUSH demo.ml.ratings "1::914::3::978301968" "1::3408::4::978300275"

# Gives everything in a list, beginning from the head(0) until the total (-1)
LRANGE demo.ml.ratings 0 -1

# Add more data from the tail end of the list
RPUSH demo.ml.ratings "1::2355::5::978824291" "1::1197::3::978302268"

# Return the element at the index of the list. This happens from the head

# Returns element n
LINDEX demo.ml.ratings 0
LINDEX demo.ml.ratings 1
LINDEX demo.ml.ratings -1

# Return and remove an item from the head and tail respectively.
LPOP demo.ml.ratings
RPOP demo.ml.ratings

# Reduce the list to (0,3) - 4 itens
LTRIM demo.ml.ratings 0 3

# Reduce the list to just one item
LTRIM demo.ml.ratings 0 0

# Use blocking pop to remove an item from the list with 0 timeout
# The first command should work while the second will block indefinitely
BLPOP demo.ml.ratings 0
BLPOP demo.ml.ratings 0
```
