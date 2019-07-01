#!/bin/bash
set -e

service rsyslog start
service ssh start
/usr/bin/python3 /root/server.py &
 
exec "$@"
