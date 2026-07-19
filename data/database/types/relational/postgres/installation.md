# Install PostgreSQL

## Debian package manager

```shell
sudo apt install postgresql # Currently version 13
```

## PostgreSQL native package

```shell
# Create the file repository configuration:
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

# Import the repository signing key:
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

# Update the package lists:
sudo apt update

# Install the latest version of PostgreSQL.
# If you want a specific version, use 'postgresql-12' or similar instead of 'postgresql':
sudo apt -y install postgresql

# Install pgadmin
sudo apt install pgadmin4

# Change user password
sudo -u postgres psql -c "ALTER USER postgres PASSWORD 'postgres';"
```

## Docker

```shell
docker container run \
  --name mypostgres \
  -e POSTGRES_USER=myuser \
  -e POSTGRES_PASSWORD=mypass \
  -e POSTGRES_DB=mydb \
  -p 5432:5432 \
  -v my_postgres_data:/var/lib/postgresql \
  -v "$(pwd)/db/init:/docker-entrypoint-initdb.d:ro" \
  "docker.io/postgres:18"

docker container exec -it mypostgres bash
```

## Docker Compose

```yaml
services:
  db:
    image: docker.io/postgres:18
    environment:
      POSTGRES_USER: myuser
      POSTGRES_PASSWORD: mypass
      POSTGRES_DB: mydb
    ports:
      - "5432:5432"
    volumes:
      - my_postgres_data:/var/lib/postgresql
      - ./db/init:/docker-entrypoint-initdb.d:ro
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U myuser -d mydb"]
      interval: 5s
      timeout: 5s
      retries: 5
  app:
    build: .
    environment:
      DATABASE_URL: postgresql+psycopg://myuser:mypass@db:5432/mydb # db = the host of the database, could be localhost
    ports:
      - "8000:8000"
    depends_on:
      db:
        condition: service_healthy
volumes:
  postgres_data:
```

## Restore the DB dvdrental.tar

- Right click on "PostgreSQL 12" > Create DB
- Set name "dvdrental" > Create
- Right click on "dvdrental" > Restore
- Select dvdrental.tar
- Restore options select: Pre-date, Data, Post-data
- Right click on "dvdrental" > Refresh
- Right click on "dvdrental" > Query tool

## DB creation

```sql
CREATE DATABASE dvdtest;
```

## Populate DB

- cd C:\Program Files\PostgreSQL\12\bin
- pg_restore -U postgres -d dvdtest "C:\dvdrental.tar"
