#!/usr/bin/python

import socket

host = socket.gethostname()
port = 12000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s_udp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.sendall("My Socket Opened")
data = s.recv(1024)
print(repr(data))
s.close()
