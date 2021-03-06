# sortedset

- <https://redis.io/commands#sorted_set>

```shell
# Create some string data

ZADD demo.ml.genre_hist 20 Action 34 Adventure 10 Animation 16 Children 55 Comedy 19 Crime 39 Drama 11 Fantasy
# NX - If not exists
ZADD demo.ml.genre_hist NX 22 War 8 Western
# CH - Change if exists
ZADD demo.ml.genre_hist CH 8.9 Horror 8 Sci-Fi 3 Mystery 24 Romance 10 Thriller 3.11 Documentary 1 Film-Noir

# Get cardinality
ZCARD demo.ml.genre_hist

# List out the items of this sorted set. Then do it in a reverse order
ZRANGE demo.ml.genre_hist 0 -1
ZRANGE demo.ml.genre_hist 0 -1 WITHSCORES

# Reverse range
ZREVRANGE demo.ml.genre_hist 0 2
ZREVRANGE demo.ml.genre_hist 0 2 WITHSCORES

ZRANGE demo.ml.genre_hist 0 2000


# Inspecting our data structure
TYPE demo.ml.genre_hist
OBJECT ENCODING demo.ml.genre_hist

# Getting the ranks of member or non-members of this sorted set
ZRANK demo.ml.genre_hist Action
ZREVRANK demo.ml.genre_hist Action
ZREVRANK demo.ml.genre_hist Comedy

ZRANK demo.ml.genre_hist Actions

# Return the score for this member
ZSCORE demo.ml.genre_hist Action

# Increasing and decreasing an item score and seeing the effect on ranking
ZRANK demo.ml.genre_hist Action
ZINCRBY demo.ml.genre_hist 3 Action
ZRANK demo.ml.genre_hist Action
ZINCRBY demo.ml.genre_hist -3 Action
ZRANK demo.ml.genre_hist Action


# Removing items from a sorted set
ZPOPMIN demo.ml.genre_hist
ZRANGE demo.ml.genre_hist 0 -1

ZPOPMAX demo.ml.genre_hist
ZRANGE demo.ml.genre_hist 0 -1

# Removing items
ZREM demo.ml.genre_hist XXXXXX
ZRANGE demo.ml.genre_hist 0 -1
```
