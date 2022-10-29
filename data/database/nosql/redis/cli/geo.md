# geo

- <https://redis.io/commands#geo>

```sh
# Create some string data
GEOADD demo.cities -118.243685  34.052234 "Los Angeles"
GEOADD demo.cities 28.047305 -26.204103 "Johannesburg"
GEOADD demo.cities 18.424055  -33.924869 "Cape Town"

# We can add more than one at a time. Doesn't add duplicate
GEOADD demo.cities -0.127758 51.507351 London 139.650311 35.676192 Tokyo 172.636225 -43.532054 Christchurch
GEOADD demo.cities -74.005941 40.712784 "New York" -46.633309 -23.550520 "Sao paolo" 3.379206 6.524379 Lagos
GEOADD demo.cities 13.404954 52.520007 Berlin 55.270783 25.204849 Dubai 3.379206 6.524379 Lagos

# Let's use a sorted set command to see the list of cities in our geo structure
ZRANGE demo.cities 0 -1 WITHSCORES

# Let's using GEODIST to see the distance between any two members in kilometers
GEODIST demo.cities Dubai Berlin km

# Return the position of a member
GEOPOS demo.cities Christchurch

# Introspecting our geo data structure. It is just a sorted set
TYPE demo.cities
OBJECT ENCODING demo.cities

GEOHASH demo.cities "Los Angeles"

# Show cities in the radius n
GEORADIUSBYMEMBER demo.cities Berlin 2000 km
```
