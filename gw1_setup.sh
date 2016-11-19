#!/bin/bash

iptables -F
ufw disable

echo 1 >/proc/sys/net/ipv4/ip_forward

ip route add 10.10.4.2/32 via 10.10.5.1 dev eth3
ip route add 10.10.1.1/32 via 10.10.1.2 dev eth1

arp -i eth1 -s 10.10.1.1 02:bc:14:94:03:12
arp -i eth3 -s 10.10.5.2 02:58:91:db:74:19
