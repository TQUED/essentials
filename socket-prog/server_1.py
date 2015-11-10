#!/usr/bin/python

import socket

host = ''
port = 12000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.listen(2)

conn, addr = s.accept()
print('Connected by', addr)

while True:
    data = conn.recv(1024)
    if not data: break
    conn.sendall(data)
conn.close()
