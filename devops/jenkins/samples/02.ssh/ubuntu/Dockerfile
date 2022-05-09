# Tag: "ubuntu-ssh"
FROM ubuntu:latest
RUN apt update && apt install -y "openssh-server" "sudo"
RUN useradd -rm -d "/home/ubuntu" -s "/bin/bash" -g "root" -G "sudo" -u "1000" "ubuntu"
RUN echo "ubuntu:123" | chpasswd
RUN mkdir -p "/home/ubuntu/.ssh" && chmod "700" "/home/ubuntu/.ssh"
COPY "ubuntu-key.pub" "/home/ubuntu/.ssh/authorized_keys"
RUN chown "ubuntu:root" -R "/home/ubuntu/.ssh" && chmod "600" "/home/ubuntu/.ssh/authorized_keys"
RUN service ssh start
CMD /usr/sbin/sshd -D
EXPOSE 22