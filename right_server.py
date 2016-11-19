#!/usr/bin/python
import socket, sys, os, subprocess
#

PATH_TO_CONFS='/users/faezehka/strong_swan_install/conf'
SERVER_ADDRESS='10.10.5.1'

def main():
        received_ip_array = setup_a_socket_to_listen_to()
	create_config_files_right(received_ip_array)

def create_config_files_left(received_ip_array):
	config_file = open('ipsec.conf','w')
	config_file.write('conn test\n')	
	config_file.write('\tleft=' + received_ip_array[1] + '\n')	
	config_file.write('\tright=' + received_ip_array[2] + '\n')	
	config_file.write('\tleftsubnet=' + received_ip_array[0] + '\n')	
	config_file.write('\trightsubnet=' + received_ip_array[3] + '\n')	
	config_file.write('\tleftfirewall=no\n')	
	config_file.write('\trightfirewall=no\n')	
	config_file.write('\tauto=start\n')	
	config_file.write('\tauthby=secret\n')	
	config_file.write('\ttype=tunnel')	

	secret_file = open('ipsec.secrets','w')
	secret_file.write(received_ip_array[1] + ' ' + received_ip_array[2] + ' : PSK \"shared key\"\n')	
	os.system('mv ipsec.conf ipsec.secrets ' + PATH_TO_CONFS)	


def create_config_files_right(received_ip_array):
	config_file = open('ipsec.conf','w')
	config_file.write('conn test\n')	
	config_file.write('\tleft=' + received_ip_array[2] + '\n')	
	config_file.write('\tright=' + received_ip_array[1] + '\n')	
	config_file.write('\tleftsubnet=' + received_ip_array[3] + '\n')	
	config_file.write('\trightsubnet=' + received_ip_array[0] + '\n')	
	config_file.write('\tleftfirewall=no\n')	
	config_file.write('\trightfirewall=no\n')	
	config_file.write('\tauto=start\n')	
	config_file.write('\tauthby=secret\n')	
	config_file.write('\ttype=tunnel')	

	secret_file = open('ipsec.secrets','w')
	secret_file.write(received_ip_array[2] + ' ' + received_ip_array[1] + ' : PSK \"shared key\"\n')	
	os.system('mv ipsec.conf ipsec.secrets ' + PATH_TO_CONFS)	

def setup_a_socket_to_listen_to():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (SERVER_ADDRESS, 10000)
        sock.bind(server_address)
        sock.listen(1)
        ip_array = listen_to_socket_and_receive_info(sock)
	return ip_array
	
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
                                 
