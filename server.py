#!/usr/bin/python
import socket, sys, os, subprocess
#
##########################################################
#Please edit these to your particular environment
##########################################################
PATH_TO_CONFS='/root/programs/ezipsec/strongswan/conf_files/'  #ensure this path points to the directory of ipsec.conf and ipsec.secrets resides.
SERVER_ADDRESS='10.2.63.86'
##########################################################


counter=0

def main(argv):
	verify_variable_environment()
	stop_instances_of_ipsec()
	while True:
		check_args(argv)
        	received_ip_array = setup_a_socket_to_listen_to()
		create_config_files(argv, received_ip_array)
		start_ipsec()

def verify_variable_environment():
	if raw_input("Ensure you have properly edited the variables within this script.  Proceed?[y | n]").lower().startswith('n'):
		print("Leaaving...")
		sys.exit(1)

#    	Vexcept KeyboardInterrupt:
#        print("Ok ok, quitting")
#        sys.exit(1)
#

def stop_instances_of_ipsec():
	os.system("ipsec stop")
	os.system("rm -f " + PATH_TO_CONFS + "ipsec.*")

def check_args(argv):
	if len(argv) != 1: 
		print("ERROR: You need to specify whether this server is to run as the left or right server.  You can do this by providing a \"left\" or \"right\" argument")
		exit(2)
		
def start_ipsec():
	os.system("ipsec start")

def create_config_files(argv, received_ip_array):
	if argv[0] == 'right':
		create_config_files_right(received_ip_array)
	elif argv[0] == 'left':
		create_config_files_left(received_ip_array)
	else: 
		print("You have not correctly specified \"right\" or \"left\"")
		sys.exit(1)

def create_config_files_left(received_ip_array):
	global counter 
	config_file = open(PATH_TO_CONFS + 'ipsec.conf','a')
	config_file.write('conn test' + str(counter) + '\n')	
	config_file.write('\tleft=' + received_ip_array[1] + '\n')	
	config_file.write('\tright=' + received_ip_array[2] + '\n')	
	config_file.write('\tleftsubnet=' + received_ip_array[0] + '\n')	
	config_file.write('\trightsubnet=' + received_ip_array[3] + '\n')	
	config_file.write('\tleftfirewall=no\n')	
	config_file.write('\trightfirewall=no\n')	
	config_file.write('\tauto=start\n')	
	config_file.write('\tauthby=secret\n')	
	config_file.write('\ttype=tunnel')	
	config_file.write('\n\n')

	secret_file = open(PATH_TO_CONFS + 'ipsec.secrets','a')
	secret_file.write(received_ip_array[1] + ' ' + received_ip_array[2] + ' : PSK \"shared key\"\n')	
	counter = counter+1

def create_config_files_right(received_ip_array):
	global counter 
	config_file = open(PATH_TO_CONFS + 'ipsec.conf','a')
	config_file.write('conn test' + str(counter) + '\n')	
	config_file.write('\tleft=' + received_ip_array[2] + '\n')	
	config_file.write('\tright=' + received_ip_array[1] + '\n')	
	config_file.write('\tleftsubnet=' + received_ip_array[3] + '\n')	
	config_file.write('\trightsubnet=' + received_ip_array[0] + '\n')	
	config_file.write('\tleftfirewall=no\n')	
	config_file.write('\trightfirewall=no\n')	
	config_file.write('\tauto=start\n')	
	config_file.write('\tauthby=secret\n')	
	config_file.write('\ttype=tunnel')	
	config_file.write('\n\n')

	secret_file = open(PATH_TO_CONFS + 'ipsec.secrets','a')
	secret_file.write(received_ip_array[2] + ' ' + received_ip_array[1] + ' : PSK \"shared key\"\n')	
	counter = counter+1

def setup_a_socket_to_listen_to():
	try:
		sys.tracebacklimit = 0 #used to mask any issues with creating the socket. 
        	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        	server_address = (SERVER_ADDRESS, 10000)
        	sock.bind(server_address)
        	sock.listen(1)
        	ip_array = listen_to_socket_and_receive_info(sock)
		return ip_array
	except:
		print("ERROR: Check your IP of SERVER_ADDRESS")
	
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
        main(sys.argv[1:])
                                 
