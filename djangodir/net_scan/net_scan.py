# net_scan.py
# Runs an nmap scan after taking an IP address and port range as input. Must be run with administrator privileges.
# Created: 1/20/25
# Updated: 1/26/25

import nmap

def port_scan(ipaddr, port_nums):
    nm = nmap.PortScanner()

    scan_output = nm.scan(ipaddr, port_nums)

    map_out = open('nmap_results.txt', 'w')

    for host in nm.all_hosts():
        map_out.write('---------------------------------\n')
        map_out.write("Host: {} ({})\n".format(host, nm[host].hostname()))
        map_out.write("State: {}\n".format(nm[host].state()))

        for protocol in nm[host].all_protocols():
            map_out.write("Protocol: {}\n".format(protocol))

            list_port = nm[host][protocol].keys()

            for port in list_port:
                map_out.write("Port: {}\tState: {}\n".format(port, nm[host][protocol][port]['state']))

    map_out.close()