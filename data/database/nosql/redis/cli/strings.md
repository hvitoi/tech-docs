# strings

- <https://redis.io/commands#string>

```sh
# Create some string data
# EX - Expiration / NX - If not exists / XX - If already exists

SET demo.webapp.visitor_count 2
SET demo.ml.movie.2  "2::Jumanji (1995)::Adventure|Children's|Fantasy"
SET demo.app.usertoken:abc@yahoo.co.za RBPouKfAKzSUJdPihrJJAMkRCGcn5P5MICuzLZ2rPAldqeQa4U EX 21600 XX
SET demo.app.usertoken:abc@yahoo.co.za RBPouKfAKzSUJdPihrJJAMkRCGcn5P5MICuzLZ2rPAldqeQa4U EX 21600 NX

# Get the results

GET demo.webapp.visitor_count
GET demo.ml.movie.2
GET demo.app.usertoken:abc@yahoo.co.za
GET demo.app.usertoken:doesnotexist@yahoo.co.za

# MSET and MGET are used for multiple value pairs
MGET demo.webapp.visitor_count demo.ml.movie.2 demo.app.usertoken:abc@yahoo.co.za demo.app.usertoken:doesnotexist@yahoo.co.za


# The type of the key is
TYPE demo.webapp.visitor_count
TYPE demo.ml.movie.2
TYPE demo.app.usertoken:abc@yahoo.co.za

# But the encoding will differ
OBJECT ENCODING demo.webapp.visitor_count
OBJECT ENCODING demo.ml.movie.2
OBJECT ENCODING demo.app.usertoken:abc@yahoo.co.za

# The object encoding determines the permissible operation that can be performed
INCR demo.webapp.visitor_count
DECR demo.webapp.visitor_count

# INCR and DECR cannot be performed on raw object encoding
INCR demo.app.usertoken:abc@yahoo.co.za

# INCR performs values different from 1
INCRBY demo.webapp.visitor_count 10
INCRBY demo.ml.movie.2 2.1
DECRBY demo.webapp.visitor_count 2

# Get the length of the user token
STRLEN demo.app.usertoken:abc@yahoo.co.za
STRLEN demo.webapp.visitor_count
```
