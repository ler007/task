import time
import re
import requests

filePath = '/var/log/auth.log'
server = 'nodexyz'

def coba(text):
    if 'Starting session:' in text:
        result = {"status" : "connect", "server" : server}
        r = requests.post('http://172.16.238.10:5000/retrieve', json=result)
    if 'session closed ' in text:
        result = {"status" : "disconnect", "server" : server}
        r = requests.post('http://172.16.238.10:5000/retrieve', json=result)

    return True

lastLine = None
with open(filePath,'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            coba(line)
            lastLine = line

while True:
    with open(filePath,'r') as f:
        lines = f.readlines()
    if lines[-1] != lastLine:
        lastLine = lines[-1]
        coba(lastLine)
    time.sleep(1)
