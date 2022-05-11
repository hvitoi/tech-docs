# Kafka Setup

## System preparation

```shell
# Install Java JDK
sudo apt install "openjdk-8-jdk"

# Download Kafka (2.6.0)
curl -O "https://dlcdn.apache.org/kafka/3.1.0/kafka_2.13-3.1.0.tgz"

# Extract kafka .tgz to home folder
tar -xzvf "kafka_2.13-3.1.0.tgz"

# Test the binary
cd "kafka_2.13-3.1.0/"
./bin/kafka-topics.sh

# Add link
ln -s "kafka_2.13-2.6.0" "~/kafka"

# Add Kafka to path
echo 'export PATH=$PATH:$HOME/kafka/bin' >> "~/.zshrc"
```

## Start Zookeeper

```shell
# Setup config file
vim "~/kafka/bin/config/zookeeper.properties" # edit dataDir=/home/hvitoi/kafka/data/zookeeper

# Start zookeeper
~/kafka/bin/zookeeper-server-start.sh "~/kafka/config/zookeeper.properties" # Bind to port 2181. A version-2 folder inside of data/zookeeper is created
~/kafka/bin/zookeeper-server-start.sh -daemon "~/kafka/config/zookeeper.properties" # Run as a daemon
```

## Start Kafka

- You can start multiple brokers, but the broker id and the advertised listeners of each broker must be different!

```shell
# Setup config file
vim "~/kafka/bin/config/server.properties" # edit log.dirs=/home/hvitoi/kafka/data/kafka

# Start kafka
~/kafka/bin/kafka-server-start.sh "~/kafka/bin/config/server.properties"
~/kafka/bin/kafka-server-start.sh -daemon "~/kafka/bin/config/server.properties" # Run as a daemon
```

## Service scripts

```shell
# Stop Kafka & Zookeeper
sudo ~/kafka/bin/kafka-server-stop.sh
sudo ~/kafka/bin/zookeeper-server-stop.sh
```

### zookeeper.service

- Create `/etc/systemd/system/zookeeper.service` and copy the content below

```shell
sudo vim "/etc/systemd/system/zookeeper.service"
```

```conf
[Unit]
Description=Apache Zookeeper server
Documentation=http://zookeeper.apache.org
Requires=network.target remote-fs.target
After=network.target remote-fs.target

[Service]
Type=simple
ExecStart=/home/hvitoi/kafka/bin/zookeeper-server-start.sh /home/hvitoi/kafka/config/zookeeper.properties
ExecStop=/home/hvitoi/kafka/bin/zookeeper-server-stop.sh

[Install]
WantedBy=multi-user.target
```

### kafka.service

- Create `/etc/systemd/system/kafka.service` and copy the content below

```shell
sudo vim "/etc/systemd/system/kafka.service"
```

```conf
[Unit]
Description=Apache Kafka server (broker)
Documentation=http://kafka.apache.org/documentation.html
Requires=zookeeper.service

[Service]
Type=simple
ExecStart=/home/hvitoi/kafka/bin/kafka-server-start.sh /home/hvitoi/kafka/config/server.properties
ExecStop=/home/hvitoi/kafka/bin/kafka-server-stop.sh

[Install]
WantedBy=multi-user.target
```

### Enable systemd scripts

```shell
sudo systemctl enable "zookeeper.service"
sudo systemctl enable "kafka.service"
```

### Service management via systemd

```shell
sudo systemctl status "zookeeper"
sudo systemctl status "kafka"

sudo systemctl start "zookeeper"
sudo systemctl start "kafka" # Starts the zookeeper automatically

sudo systemctl stop "zookeeper"
sudo systemctl stop "kafka"
```

### Logs

```shell
sudo journalctl -u "kafka"
```
