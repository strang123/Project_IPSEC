#!/usr/bin/python
import socket, sys, os, subprocess
#




def main():
        received_ip_array = setup_a_socket_to_listen_to()
	create_config_files(received_ip_array)

def create_config_files(received_ip_array)
	

def setup_a_socket_to_listen_to():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('10.10.5.1', 10000)
        sock.bind(server_address)
        sock.listen(1)
        listen_to_socket_and_receive_info(sock)

def listen_to_socket_and_receive_info(sock):
	ip_array = []
        while True:
                connection, client_address = sock.accept()
                try:
                        while True:
                                data = connection.recv(48)
                                if data:
					ip_array = data.split()
					if len(ip_array) == 4:
						return ip_array
                                else:   
                                        print >>sys.stderr, 'Connection with the following IP/Port pair has sent information', client_address
                                        break

                finally:
                        connection.close()




if __name__ == "__main__":
        main()
                                 
