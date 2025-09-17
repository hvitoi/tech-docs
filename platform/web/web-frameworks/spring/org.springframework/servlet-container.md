# Servlet containers

- Servlet containers implement the `Jakarta Servlet`, `Jakarta Pages (JSP)`, and `WebSocket specifications`. That means it can run Java web applications built on these technologies.

## Tomcat

- Process `java servlet` applications
- Provides a pure java http web server
- Manage requests and responses (no EJB)
- Currently version 10

- Production: <https://www.digitalocean.com/community/tutorials/how-to-install-apache-tomcat-9-on-debian-10>
- Development: <https://askubuntu.com/questions/968089/how-to-add-tomcat-8-into-intellij-idea>

```shell
# Download tomcat binary
curl -O "https://ftp.unicamp.br/pub/apache/tomcat/tomcat-10/v10.0.7/bin/apache-tomcat-10.0.7.tar.gz"

# Install to anywhere
sudo mkdir "/opt/tomcat"
sudo tar -zxvf "apache-tomcat-9.0.41.tar.gz"
sudo mv "apache-tomcat-9.0.41/*" "/opt/tomcat"

# Export catalina home to .zshrc
export CATALINA_HOME=/opt/tomcat

# Tomcat permissions (development)
sudo chgrp -R hvitoi "/opt/tomcat"
sudo chown -R hvitoi /opt/tomcat/webapps/ /opt/tomcat/work/ /opt/tomcat/temp/ /opt/tomcat/logs/

# Tomcat permissions (production)
sudo chgrp -R tomcat /opt/tomcat
sudo chown -R tomcat /opt/tomcat/webapps/ /opt/tomcat/work/ /opt/tomcat/temp/ /opt/tomcat/logs/
sudo chmod -R g+r conf
sudo chmod g+x conf
```

- Systemd service file ($JAVA_HOME must be set)
- `/etc/systemd/system/tomcat.service`

```conf
[Unit]
Description=Apache Tomcat Web Application Container
After=network.target

[Service]
Type=forking

Environment=JAVA_HOME=/usr/lib/jvm/java-1.11.0-openjdk-amd64
Environment=CATALINA_PID=/opt/tomcat/temp/tomcat.pid
Environment=CATALINA_HOME=/opt/tomcat
Environment=CATALINA_BASE=/opt/tomcat
Environment='CATALINA_OPTS=-Xms512M -Xmx1024M -server -XX:+UseParallelGC'
Environment='JAVA_OPTS=-Djava.awt.headless=true -Djava.security.egd=file:/dev/./urandom'

ExecStart=/opt/tomcat/bin/startup.sh
ExecStop=/opt/tomcat/bin/shutdown.sh

User=tomcat
Group=tomcat
UMask=0007
RestartSec=10
Restart=always

[Install]
WantedBy=multi-user.target
```

```shell
sudo vim /etc/systemd/system/tomcat.service
sudo systemctl daemon-reload
sudo systemctl start tomcat
sudo systemctl status tomcat
sudo systemctl enable tomcat # OPTIONAL!
```

```shell
# Allow firewall rule for accepting connections from anywhere
sudo ufw allow 8080
```

- Add a login to tomcat in order to manage the web app
  - `/opt/tomcat/conf/tomcat-users.xml`

```xml
<tomcat-users>
    <user username="admin" password="123" roles="manager-gui,admin-gui"/>
</tomcat-users>
```

- Allow access to `Manager` and `Host Manager` apps
  - `/opt/tomcat/webapps/manager/META-INF/context.xml`
  - `/opt/tomcat/webapps/host-manager/META-INF/context.xml`
- Comment out the IP address restriction to allow connections from anywhere

```shell
# Restart tomcat service
sudo systemctl restart tomcat

# Access default splash page
open "http://localhost:8080"
```

## Jetty
