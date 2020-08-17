#!/usr/bin/env python
import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast/arp_request
    print(arp_request.show())
    print(broadcast.show())
    print(arp_request_broadcast.show())


if __name__ == '__main__':
    scan('10.0.2.1/24')
