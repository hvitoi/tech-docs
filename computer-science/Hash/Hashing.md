# Hashing

- Take any-length input and convert it to a fixed length hash output (128bit, 160bit, etc)
- Hash function always generate `same hash` for `same input` (**idempotent**)
- The hash function is ONE WAY
- Different input generate completely different hashes
- It's a `one-way function`. You cannot take the input value from the hash
- The input can be anything from a short string to a gigabyte file
- The hash verifies if the data was not changed! (Integrity)
- Keys in hashing are optional
