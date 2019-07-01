FROM ubuntu:latest
 
ARG SSH_SERVER_USER
ARG SSH_SERVER_PASS
 
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

RUN mkdir /root/static
RUN touch /root/static/data.json
RUN mkdir /root/templates
COPY index.html /root/templates/index.html

COPY ssh_config /etc/ssh/ssh_config
COPY sshd_config /etc/ssh/sshd_config
 
COPY user.sh /usr/local/bin/user.sh
RUN chmod +x /usr/local/bin/user.sh
RUN /usr/local/bin/user.sh

COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

COPY server.py /root/server.py

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

CMD tail -f /dev/null
