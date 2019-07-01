#!/bin/bash
set -e
 
printf "\n\033[0;44m---> Creating SSH xyz user.\033[0m\n"
 
useradd -m -d /home/${SSH_XYZ_USER} -G ssh ${SSH_XYZ_USER} -s /bin/bash
echo "${SSH_XYZ_USER}:${SSH_XYZ_PASS}" | chpasswd
echo 'PATH="/usr/local/bin:/usr/bin:/bin:/usr/sbin"' >> /home/${SSH_XYZ_USER}/.profile
 
usermod -aG sudo ${SSH_SERVER_USER}

exec "$@"
