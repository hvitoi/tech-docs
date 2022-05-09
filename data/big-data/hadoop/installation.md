# Hadoop installation

## Debian

```sh
# Setup environment and user
sudo apt install default jdk
sudo adduser hadoop
sudo usermod -aG sudo hadoop
su - hadoop

# Download and install binaries
wget https://downloads.apache.org/hadoop/common/hadoop-3.2.1/hadoop-3.2.1.tar.gz
tar -zxvf hadoop-3.2.1.tar.gz
mv hadoop-3.2.1 /usr/local/hadoop
sudo chown -R hadoop:hadoop /usr/local/hadoop

# set environment variables
echo 'export HADOOP_HOME=/usr/local/hadoop' >> ~/.bashrc
echo 'export HADOOP_INSTALL=$HADOOP_HOME' >> ~/.bashrc
echo 'export HADOOP_MAPRED_HOME=$HADOOP_HOME' >> ~/.bashrc
echo 'export HADOOP_COMMON_HOME=$HADOOP_HOME' >> ~/.bashrc
echo 'export HADOOP_HDFS_HOME=$HADOOP_HOME' >> ~/.bashrc
echo 'export YARN_HOME=$HADOOP_HOME' >> ~/.bashrc
echo 'export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native' >> ~/.bashrc
echo 'export PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin' >> ~/.bashrc
echo 'export HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib/native"' >> ~/.bashrc
source ~/.bashrc

# Hadoop configuration
echo 'export JAVA_HOME=/usr/lib/jvm/java-15-openjdk-amd64' >> /usr/local/hadoop/etc/hadoop/hadoop-env.sh

# Test hadoop
hadoop version
```
