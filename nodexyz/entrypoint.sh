#!/bin/bash
set -e

service rsyslog start
service ssh start
 
exec "$@"
