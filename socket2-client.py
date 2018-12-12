
# https://www.journaldev.com/15906/python-socket-programming-server-client

import socket

def recvall(sock):
    BUFF_SIZE = 4096 # 4 KiB
    data = b''
    while True:
        part = sock.recv(BUFF_SIZE)
        data += part
        if len(part) < BUFF_SIZE:
            # either 0 or end of data
            break
    return data.decode()

def send(client_socket, message):
    client_socket.send(message.encode())  # send message
    data = recvall(client_socket)
    print('Received from server: ' + data)  # show in terminal

def MessageSet(name, value):
    return "S"+name+"\n"+value

def MessageGet(name):
    return "G"+name+"\n"

def MessageDebug():
    return "D"

def MessageQuit():
    return "Q"

def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    send(client_socket, MessageSet("ahoj", "1"))
    send(client_socket, MessageSet("ahoj", "2"))
    send(client_socket, MessageSet("hi", "2545646"))
    send(client_socket, MessageGet("hi"))
    send(client_socket, MessageDebug())
    send(client_socket, MessageQuit())

    client_socket.close()  # close the connection

if __name__ == '__main__':
    client_program()
