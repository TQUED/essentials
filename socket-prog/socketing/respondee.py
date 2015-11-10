__author__ = 'nirajK'

import argparse
import socket

#ACTION_RUN = "ctrl_req_action=run;"
#ACTION_OK = "ctrl_resp_message=Ok;"
#ACTION_ERR = "ctrl_resp_message=Error;"


def parse_commands():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--host",
                        help="The hostname or IP address of the server to connect",
                        required=True)
    parser.add_argument("-p", "--port",
                        help="The remote server port",
                        required=True,
                        type=int)
    parser.add_argument("-c", "--command",
                        help="The command to run on remote server",
                        required=True)
    
    return parser.parse_args()


def run_process(sock, command):
    try:
        sock.send(ACTION_RUN + "command=" + command + "\n")
        resp_msg = sock.recv(64)
        buf = []
        if resp_msg == ACTION_OK:
            while True:
                data = sock.recv(64)
                if not data:
                    break
                buf.append(data)
        elif resp_msg == ACTION_ERR:
            print "Ctrl response error"
        else:
            print "No response received from server"

        sock.close()
        return "".join(buf)
    except socket.error:
        print "Socket error in running command"
        sock.close()


def connect(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        return sock
    except socket.error:
        return None


def main():
    opts = parse_commands()
    host = opts.host
    port = opts.port
    command = opts.command

    command_flag = False
    
    if command and not host and not port:
        print "[USAGE ERROR] Provide host and port info"
    elif host and port and not command:
        print "[USAGE ERROR] Provide command to run any operation with the server"
    elif host and port and command:
        command_flag = True
    else:
        print "[USAGE ERROR] Unhandaled type; will be handaled in future upgraded codes"
    
    if command_flag:
        sock = connect(host, port)    
        output = run_process(sock, command)

if __name__ == '__main__':
    main()
