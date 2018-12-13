#https://pymotw.com/2/socket/tcp.html

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port on the server given by the caller
server_address = ('localhost', 10000)
sys.stdout.write('connecting to ' + str(server_address))
# print >> sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:

    message = '\nThis is the message. It will be repeated.'
    sys.stdout.write('\nsending `%s`' % message)
    # print >> sys.stderr, 'sending "%s"' % message
    sock.sendall(message.encode())
    sys.stdout.write('sent')

    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(1000)
        amount_received += len(data)
        sys.stdout.write('\nreceived `%s`' % data)
        # print >> sys.stderr, 'received "%s"' % data

finally:
    sock.close()
