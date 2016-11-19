#!/bin/bash

iptables -F
ufw disable

echo 1 >/proc/sys/net/ipv4/ip_forward

ip route add 10.10.1.1/32 via 10.10.5.2 dev eth3
ip route add 10.10.4.2/32 via 10.10.4.1 dev eth2

arp -i eth2 -s 10.10.4.2 02:21:ff:7f:01:e8
arp -i eth3 -s 10.10.5.1 02:84:32:9c:ff:31
