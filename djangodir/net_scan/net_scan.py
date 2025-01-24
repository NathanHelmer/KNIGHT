# net_scan.py
# Runs an nmap scan after taking an IP address and port range as input. Must be run with administrator privileges.
# Created: 1/20/25
# Updated: 1/23/25

import nmap

def port_scan(ipaddr, port_nums):
    nm = nmap.PortScanner()

    scan_output = nm.scan(ipaddr, port_nums)

    for host in nm.all_hosts():
        print('---------------------------------')
        print("Host: {} ({})".format(host, nm[host].hostname()))
        print("State: {}".format(nm[host].state()))

        for protocol in nm[host].all_protocols():
            print("Protocol: {}".format(protocol))

            list_port = nm[host][protocol].keys()

            for port in list_port:
                print("Port: {}\tState: {}".format(port, nm[host][protocol][port]['state']))