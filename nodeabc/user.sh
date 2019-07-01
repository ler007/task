#!/bin/bash
set -e
 
printf "\n\033[0;44m---> Creating SSH abc user.\033[0m\n"
 
useradd -m -d /home/${SSH_ABC_USER} -G ssh ${SSH_ABC_USER} -s /bin/bash
echo "${SSH_ABC_USER}:${SSH_ABC_PASS}" | chpasswd
echo 'PATH="/usr/local/bin:/usr/bin:/bin:/usr/sbin"' >> /home/${SSH_ABC_USER}/.profile
 
usermod -aG sudo ${SSH_SERVER_USER}

exec "$@"
