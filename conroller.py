#!/usr/bin/python

import socket, sys, getopt


def main(argv):
    AddressA = argv[0]
    print(AddressA)
    AddressB = argv[1]
    print(AddressB)
    gateway1 = argv[2]
    gateway2 = argv[3]
    message= AddressA+" "+AddressB+" "+gateway1+" "+gateway2
    sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    gateway1_address = (gateway1, 10000)
    print gateway1
    sock1.connect(gateway1_address)


    sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    gateway2_address = (gateway2, 10000)
    sock2.connect(gateway2_address)

    try:

        sock1.send(message)
        sock2.send(message)

        amount_received = 0
        amount_expected = len(message)

        while amount_received < amount_expected:
                data = sock1.recv(64)
                amount_received += len(data)
                print(data)

    finally:
       sock1.close()
       sock2.close()

if __name__ == "__main__":
    main(sys.argv[1:])
