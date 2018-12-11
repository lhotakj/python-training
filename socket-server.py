#https://pymotw.com/2/socket/tcp.html

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address given on the command line
server_address = ('', 10000)
sock.bind(server_address)
sys.stderr.write('starting up on %s port %s' % sock.getsockname())
# print >> sys.stderr, 'starting up on %s port %s' % sock.getsockname()
sock.listen(1)

while True:
    sys.stderr.write('waiting for a connection')
    # print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    try:
        sys.stderr.write('client connected:', client_address)
        #print >>sys.stderr, 'client connected:', client_address
        while True:
            data = connection.recv(16)
            sys.stderr.write('received "%s"' % data)
            #print >>sys.stderr, 'received "%s"' % data
            if data:
                connection.sendall(data)
            else:
                break
    finally:
        connection.close()