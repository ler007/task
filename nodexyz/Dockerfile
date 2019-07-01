FROM ubuntu:latest
 
ARG SSH_XYZ_USER
ARG SSH_XYZ_PASS
 
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    vim \
    sudo \
    net-tools \
    apt-utils \
    iputils-ping \
    rsyslog \
    python3 \
    python3-pip \
    openssh-server
COPY requirements.txt /root/requirements.txt
RUN pip3 install --no-cache-dir -r /root/requirements.txt
 
COPY ssh_config /etc/ssh/ssh_config
COPY sshd_config /etc/ssh/sshd_config
 
COPY user.sh /usr/local/bin/user.sh
RUN chmod +x /usr/local/bin/user.sh
RUN /usr/local/bin/user.sh
 
COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

COPY client.py /root/client.py
 
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
 
CMD tail -f /dev/null
