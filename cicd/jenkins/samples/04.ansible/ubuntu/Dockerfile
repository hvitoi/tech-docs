# Tag: "ubuntu-ssh-mysql-awscli"
FROM ubuntu:20.04
RUN apt update && apt install -y openssh-server sudo curl unzip
RUN useradd -rm -d /home/ubuntu -s /bin/bash -g root -G sudo -u 1000 ubuntu 
RUN echo 'ubuntu:123' | chpasswd
RUN mkdir -p /home/ubuntu/.ssh && chmod 700 /home/ubuntu/.ssh
COPY remote-key.pub /home/ubuntu/.ssh/authorized_keys
RUN chown ubuntu:root -R /home/ubuntu/.ssh && chmod 600 /home/ubuntu/.ssh/authorized_keys
RUN service ssh start
RUN apt install -y mysql-client
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && unzip awscliv2.zip && sudo ./aws/install
CMD /usr/sbin/sshd -D
EXPOSE 22
