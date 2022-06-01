# hashes

- <https://redis.io/commands#hash>

```shell
# Create some string data
HSET demo.ml.movie#1 title "Toy Story (1995)"
HSET demo.ml.movie#1 year 1995
HSET demo.ml.movie#1 genres "Animation|Children's|Comedy"
HSET demo.ml.movie#1 id 1

# Return all pairs in the hash
HGETALL demo.ml.movie#1

# Return the value for a field in the hash
HGET demo.ml.movie#1 id

# Load all key value pair in one command. See string MSET and MGET
HMSET demo.ml.movie#2 title "Jumanji (1995)" year 1995  genres "Adventure|Children's|Fantasy" id 2 id 1
HMSET demo.ml.movie#3952 title "Contender, The (2000)" year 2000  genres "Thriller" id 3952
HMSET demo.ml.movie#3947 title "Get Carter (1971)" year 1971  genres "Thriller" id 3947
HMSET demo.ml.movie#3945 title "The Movie (2000)" year 2000  genres "Adventure|Animation|Children's" id 3945
HMSET demo.ml.movie#3941 title "Sorority House Massacre (1986)" year 1986  genres "Horror" id 3941
HMSET demo.ml.movie#3942 title "Sorority House Massacre II (1990)" year 1990  genres "Horror" id 3942
HMSET demo.ml.movie#3927 title "Fantastic Voyage (1966)" year 1966  genres "Adventure|Sci-Fi" id 3927

# List all the keys in the hash for this key
HKEYS demo.ml.movie#3927

# List all the values in the hash for this key
HVALS demo.ml.movie#2

# Returns the size of the hash for this key. Number of keys
HLEN demo.ml.movie#3941

# Confirm the existence of this key in the hash for this key
HEXISTS demo.ml.movie#3927 id
HEXISTS demo.ml.movie#3927 ids

# Inspecting the type of this key
TYPE demo.ml.movie#3952
OBJECT ENCODING demo.ml.movie#3952

# Return the listed fields from the hash identified by this key. Non-existing field return nill
HMGET demo.ml.movie#1 id title year genres field5

# Increase and decrease the value of this field in the hash for this key by the value x
HINCRBY demo.ml.movie#1 year 1
HINCRBY demo.ml.movie#1 year -1
```
