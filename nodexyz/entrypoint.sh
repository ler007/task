#!/bin/bash
set -e

service rsyslog start
service ssh start
/usr/bin/python3 /root/client.py &
 
exec "$@"
