FROM ubuntu:18.04

RUN apt-get update

RUN apt-get install -y openssh-server
RUN mkdir /var/run/sshd

RUN mkdir /root/.ssh

RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY authorized_keys /root/.ssh/

EXPOSE 22

CMD    ["/usr/sbin/sshd", "-D"]
