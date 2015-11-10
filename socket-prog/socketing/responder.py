__author__ = 'nirajK'

import subprocess
import socket
import sys
from threading import Thread

#ACTION_RUN = "ctrl_req_action=run;"
#ACTION_OK = "ctrl_resp_message=Ok;"
#ACTION_ERR = "ctrl_resp_message=Error;"


def get_output_message(command):
    p = subprocess.Popen(command.strip(),
			 stdout=subprocess.PIPE,
			 stderr=subprocess.STDOUT,
			 shell=True)

    return iter(p.stdout.readline, b'')


class Responder(object):
    RCV_PCT_BUFF = 1024


    def __init__(self, host="localhost", port=7808):
        self.host = host
        self.port = port
        self.server_socket = None

    
    def start(self):
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(Responder.RCV_PCT_BUFF)
            self.serve_forever()
        except socket.error:
            print "Error in starting server."
            sys.exit(1)

        
    def serve_forever(self):
        try:
            while True:
                connection, address = self.server_socket.accept()
                print "Client with %s:%s connected" % address
                client_message = connection.recv(64)
                if client_message.startswith(ACTION_RUN):
                    thread = Thread(target=self.run_command, args=(connection, client_message))
                    thread.start()
                else:
                    connection.send(ACTION_ERR + "\n")
                    connection.close()

        except KeyboardInterrupt, socket.error:
            self.stop()


    def run_command(self, connection, client_message):
        run_message = client_message[len(ACTION_RUN):].strip()
        keyword_command = run_message.split("=")
        try:
            command_to_run = keyword_command[1]
            print "Running command: %s" % command_to_run
            connection.send(ACTION_OK)
            for output in get_output_message(command_to_run):
                connection.send(output)

            connection.close()
        except IndexError:
            print "Invalid command received."
            connection.send(ACTION_ERR + "desc=Command not provided" + "\n")
            connection.close()
        except socket.error:
            print "Connection closed by client"
            connection.close()


rs = Responder()
rs.start()
