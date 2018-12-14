#!/usr/bin/python3
#https://pymotw.com/2/socket/tcp.html

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address given on the command line
server_address = ('0.0.0.0', 10000)
sock.bind(server_address)
sys.stdout.write('starting up on ' + str(sock.getsockname()))
# print >> sys.stderr, 'starting up on %s port %s' % sock.getsockname()
sock.listen(1)

while True:
    sys.stderr.write('waiting for a connection ...')
    sys.stdout.flush()
    # print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    try:
        sys.stdout.write('client connected:' + str(client_address))
        sys.stdout.flush()
        #print >>sys.stderr, 'client connected:', client_address
        while True:
            data = connection.recv(1000)
            sys.stdout.write('OUT~  received "%s"' % data)
            sys.stdout.flush()
            #print >>sys.stderr, 'received "%s"' % data
            if data:
                connection.sendall(data)
            else:
                break
    except KeyboardInterrupt:
        sys.stdout.write("[CTRL+C detected]")
        sys.stdout.flush()
        exit()

    finally:
        connection.close()
