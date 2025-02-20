# net_scan.py
# Runs an nmap scan after taking an IP address and port range as input. Must be run with administrator privileges.
# Created: 1/20/25
# Updated: 2/19/25

import nmap

# Precondition: ipaddr is a string for the IP address of the form '255.255.255.255' and port_nums is a string for
# the port range of the form 'x-y'
# Postcondition: writes nmap scan results to nmap_results.txt
def port_scan(ipaddr, port_nums='1-100', scan_flags=''):    
    nm = nmap.PortScanner()

    scan_output = nm.scan(ipaddr, port_nums, scan_flags)

    map_out = open('nmap_results.txt', 'a')

    map_out.write('nmap {} -p {} {}\n'.format(scan_flags, port_nums, ipaddr))

    for host in nm.all_hosts():
        map_out.write('---------------------------------\n')
        map_out.write("Host: {} ({})\n".format(host, nm[host].hostname()))
        map_out.write("State: {}\n".format(nm[host].state()))

        for protocol in nm[host].all_protocols():
            map_out.write("Protocol: {}\n".format(protocol))

            list_port = nm[host][protocol].keys()

            for port in list_port:
                map_out.write("Port: {}\tState: {}\n".format(port, nm[host][protocol][port]['state']))
    
    map_out.write('\n')

    map_out.close()

    return scan_output

# Precondition: none
# Postcondition: runs sample scans and ouputs the results to nmap_results.txt
def run_scans():
    test_range = '127.0.0.1'
    test_ports = '1-6000'

    port_scan(test_range, test_ports, 'ping')
    port_scan(test_range, test_ports, 'quick')
    port_scan(test_range, test_ports, 'intense')

# Precondition: line is a string for the command line command, ipaddr is a string of the target IP range, and
#               ports is a string of the port range
# Postcondition: returns a string of the optional scan flags from the command
def get_flags(line, ipaddr, ports):
    line = line.replace(ipaddr, '')
    line = line.replace(ports, '')
    line = line.replace('-p', '')
    line = line[5:]

    return line