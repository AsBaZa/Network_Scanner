#!/usr/bin/env python
import scapy.all as scapy
import argparse


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--target', dest='target', help='Target IP / IP range.')
    options = parser.parse_args()
    return options


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast/arp_request
    answered_list, unanswered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)

    clients_list = []
    for element in answered_list:
        clients_list += [{'ip': element[1].psrc, 'mac': element[1].hwsrc}]
    return clients_list


def print_result():
    print('IP\t\t\tMAC Adress')
    print('--------------------------------------')
    for element in results_list:
        print(f"{element['ip']}\t\t{element['mac']}")


if __name__ == '__main__':
    # Example: `python network_scanner.py -t "10.0.2.1/24"`
    opts = get_arguments()
    results_list = scan(opts.target)
    print_result()
