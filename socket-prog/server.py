#!/usr/bin/python

import socket
#import time

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 10002

serversocket.bind((host, port))
serversocket.listen(5)

while True:
    clientsocket, addr = serversocket.accept()
    print("Got a connection from %s" % str(addr))
    #currentTime = time.ctime(time.time()) + "\r\n"
    mesg = "Hello Client"
    clientsocket.send(mesg.encode('ascii'))
    clientsocket.close()
