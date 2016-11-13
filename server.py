#!/usr/bin/python
import socket, sys





def main():
        setup_a_socket_to_listen_to()

def setup_a_socket_to_listen_to():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('localhost', 10000)
        sock.bind(server_address)
        sock.listen(1)
        listen_to_socket_and_receive_info(sock)

def listen_to_socket_and_receive_info(sock):
        while True:
                connection, client_address = sock.accept()
                try:
                        while True:
                                data = connection.recv(16)
                                if data:
                                        connection.sendall(data)
                                        print(data)
                                else:   
                                        print >>sys.stderr, 'Connection with the following IP/Port pair has sent information', client_address
                                        break

                finally:
                        connection.close()




if __name__ == "__main__":
        main()
~                                 
