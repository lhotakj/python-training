import socket
from datetime import datetime

def recvall(sock):
    BUFF_SIZE = 4096  # 4 KiB
    data = b''
    while True:
        part = sock.recv(BUFF_SIZE)
        data += part
        if len(part) < BUFF_SIZE:
            # either 0 or end of data
            break
    return data.decode()

class Storage(object):

    def __init__(self):
        self.__data = {}

    def Set(self, name, value):
        self.__data[name] = [value, datetime.utcnow().timestamp()]

    def Get(self, name):
        if name in self.__data:
            return self.__data[name][0]
        return "None"

    def Dump(self):
        return self.__data


def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # get instance
    server_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(5)

    conn, address = server_socket.accept()  # accept new connection

    storage = Storage()

    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = recvall(conn)
        #print(storage.Dump())
        #if not data:
        #    break

        if data.startswith("D"):
            conn.send(str(storage.Dump()).encode())  # send data to the client
        elif data.startswith("S"):
            data = data[1:]
            lines = data.split("\n")
            storage.Set(lines[0], lines[1])
            conn.send(("SET: " + data).encode())  # send data to the client
        elif data.startswith("G"):
            data = data[1:-1]
            #print("getting '" + data + "'")
            r = storage.Get(data)
            conn.send(("GET: " + r).encode())  # send data to the client
        elif data.startswith("Q"):
            break

    print("exiting")
    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()
