#!/usr/bin/python

import socket, sys, getopt


def main(argv):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_address = ('10.10.5.2',10000)
	sock.connect(server_address)
	try:
		message = argv[0]
		sock.sendall(message)
		amount_received = 0
		amount_expected = len(message)
		
		while amount_received < amount_expected:
			data = sock.recv(16)
			amount_received += len(data)
			print(data)
			
	finally:
		sock.close()


if __name__ == "__main__":
	main(sys.argv[1:])
