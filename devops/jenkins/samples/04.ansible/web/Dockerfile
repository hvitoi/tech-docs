# Tag: "web"
FROM centos:7

RUN yum -y install openssh-server

RUN useradd remote-user && \
  echo "1234" | passwd remote-user  --stdin && \
  mkdir /home/remote-user/.ssh && \
  chmod 700 /home/remote-user/.ssh

COPY remote-key.pub /home/remote-user/.ssh/authorized_keys

RUN chown remote-user:remote-user   -R /home/remote-user && \
  chmod 400 /home/remote-user/.ssh/authorized_keys

RUN ssh-keygen -A

RUN yum -y install mysql

RUN yum -y install epel-release && \
  yum -y install python3-pip && \
  pip3 install --upgrade pip && \
  pip3 install awscli

# CMD /usr/sbin/sshd -D # will be started in start.sh

COPY ./nginx.repo /etc/yum.repos.d/nginx.repo

RUN                                                                          \
  yum -y install nginx-1.12.2 openssl --enablerepo=nginx                  && \
  yum -y install https://repo.ius.io/ius-release-el7.rpm                  && \
  yum -y install                                                             \
  php71u-fpm                                                               \
  php71u-cli                                                               \
  php71u-mysqlnd                                                           \
  php71u-soap                                                              \
  php71u-xml                                                               \
  php71u-zip                                                               \
  php71u-json                                                              \
  php71u-mcrypt                                                            \
  php71u-mbstring                                                          \
  php71u-zip                                                               \
  php71u-gd                                                                \
  --enablerepo=ius-archive && yum clean all

EXPOSE 80 443

VOLUME /var/www/html /var/log/nginx /var/log/php-fpm /var/lib/php-fpm

COPY ./nginx.conf /etc/nginx/conf.d/default.conf

COPY ./start.sh /start.sh

RUN chmod +x /start.sh

CMD /start.sh



# Check a simple index.php in /var/www/html