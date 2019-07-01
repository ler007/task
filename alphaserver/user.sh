#!/bin/bash
set -e
 
printf "\n\033[0;44m---> Creating SSH server user.\033[0m\n"
 
useradd -m -d /home/${SSH_SERVER_USER} -G ssh ${SSH_SERVER_USER} -s /bin/bash
echo "${SSH_SERVER_USER}:${SSH_SERVER_PASS}" | chpasswd
echo 'PATH="/usr/local/bin:/usr/bin:/bin:/usr/sbin"' >> /home/${SSH_SERVER_USER}/.profile

usermod -aG sudo ${SSH_SERVER_USER}
 
exec "$@"
