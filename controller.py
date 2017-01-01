#!/usr/bin/python

import socket, sys, getopt

GW1_ADDRESS='10.10.5.1'
GW2_ADDRESS='10.10.5.2'


def main(argv):
	AddressA = argv[0]
	AddressB = argv[1]
	gateway1 = argv[2]
	gateway2 = argv[3]
	
	message= AddressA+" "+AddressB+" "+gateway1+" "+gateway2
	
	sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	gateway1_address = (GW1_ADDRESS, 10000)
	sock1.connect(gateway1_address)
	
	
	sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	gateway2_address = (GW2_ADDRESS, 10000)
	sock2.connect(gateway2_address)
	
	try:
	
		sock1.send(message)
		sock2.send(message)
	
	
	finally:
		sock1.close()
		sock2.close()
	

if __name__ == "__main__":
    main(sys.argv[1:])
