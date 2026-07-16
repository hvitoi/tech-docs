# MongoDB Local Installation

## Debian package

```shell
sudo apt install mongodb-server
mongo
```

## Tarball

- `Version`: 4.2.6 Debian Linux x64 Package TGZ

```shell
# Move the mongodb folder to a permanent place
mv mongodb ~/mongodb

# Create a database folder @ ~/
mkdir data

#Setup the data folder in mongodb and RUN on port 27017 (default)
/home/hvitoi/mongodb/bin/mongod --dbpath=/home/hvitoi/data/mongo
```

## Mongo custom repository

```shell
wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -
echo "deb http://repo.mongodb.org/apt/debian buster/mongodb-org/4.2 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list
sudo apt-get update
sudo apt-get install -y mongodb-org

sudo systemctl start mongod
sudo systemctl status mongod
sudo systemctl stop mongod

mongo
```

## Install GUI viewer (robo 3t)

- Website: <https://robomongo.org/>
- Install Robo 3T (not studio). .tar.gz file

```shell
mv robo3t /usr/local/bin/robo3t
cd /usr/local/bin/robo3t/bin
sudo chmod +x robo3t
```

- Create desktop icon
  - `/usr/share/applications/robo3t.desktop`

```conf
[Desktop Entry]
Encoding=UTF-8
Type=Application
Name=Robo3t
Icon=/usr/local/bin/robo3t/bin/icon.png
Exec="/usr/local/bin/robo3t/bin/robo3t"
Comment=Robo3t
Categories=Development;
Terminal=false
StartupNotify=true
```
