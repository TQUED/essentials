#!/usr/bin/python

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 10002

s.connect((host, port))

mesg = s.recv(1024)

s.close()

print("Server said)  %s" %mesg.decode('ascii'))
