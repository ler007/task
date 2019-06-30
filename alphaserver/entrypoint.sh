#!/bin/bash
set -e

service rsyslog start
service ssh start
#service ssh status
 
exec "$@"
