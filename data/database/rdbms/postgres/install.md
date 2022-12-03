# Install PostgreSQL 12

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
  --name "meu-postgres" \
  -p "5432:5432" \
  -e "POSTGRES_PASSWORD=123" \
  -d \
  "postgres:13.1"

docker container exec -it meu-postgres bash
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
