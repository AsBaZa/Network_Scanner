#!/usr/bin/env python
import scapy.all as scapy


def scan(ip):
    scapy.arping(ip)


if __name__ == '__main__':
    scan("10.0.2.1/24")
