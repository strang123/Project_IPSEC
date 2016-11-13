#!/usr/bin/python

import socket, sys, getopt


def main(argv):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_address = ('10.10.5.1',10000)
	sock.connect(server_address)
	try:
		message1 = argv[0]
	#	message2 = argv[1]
	#	message3 = argv[2]
	#	message4 = argv[3]
		sock.sendall(message1)
		#sock.sendall(message2)
		#sock.sendall(message3)
		#sock.sendall(message4)
		
		#amount_received = 0
		#amount_expected = len(message)
		#
		#while amount_received < amount_expected:
		#	data = sock.recv(16)
		#	amount_received += len(data)
		#	print(data)
			
	finally:
		sock.close()


if __name__ == "__main__":
	main(sys.argv[1:])
