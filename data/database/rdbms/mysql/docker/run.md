# Docker Run

```sh
# Run
docker build -t "mysql-custom" "." # Only if creating a new image from Dockerfile
docker run \
  --name "meusql" \
  -d \
  -v "$HOME/data/mysql:/var/lib/mysql" \
  -p "3305:3306" \
  -e "MYSQL_ROOT_PASSWORD=123" \
  "mysql-custom"

# Exec
docker exec -it "meusql" /bin/bash
docker exec -it "meusql" mysql -uroot -p123
```
