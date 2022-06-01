# Redis local installation

```sh
# Download redis
wget http://download.redis.io/releases/redis-5.0.5.tar.gz .

# Extract the archive file
tar xfzv redis-5.0.5.tar.gz

# Change directory into the redis folder
cd redis-5.0.5

# Build the redis binary using make
make

# Go up one step
cd ..

# Copy your folder into the desired location
sudo mv redis-5.0.5/ /opt/

# Optionally put the src folder in path
add /opt/redis-5.0.5/src to $PATH variable

# Redis
redis-server (redis start server)
redis-benchmark
redis-cli
```
