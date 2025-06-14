'''
net_scan.py
Description: Runs a nmap scan after taking an IP address and port range as input. Must be run with
administrator privileges.
Created: 1/20/25
Updated: 3/19/25
'''

import nmap, textwrap
from osdetection import nmap_results_path

# Precondition: ipaddr is a string for the IP address of the form '255.255.255.255' and port_nums is a string for
# the port range of the form 'x-y'
# Postcondition: writes nmap scan results to nmap_results.txt
def port_scan(ipaddr, port_nums='1-1000', scan_flags='', path=""):    
    nm = nmap.PortScanner()
    
    map_out = open(path, 'w')
    
    # Handle a ping scan
    if '-sP' in scan_flags:
        nm.scan(hosts=ipaddr, arguments=scan_flags)

        map_out.write('nmap {} {}\n'.format(scan_flags, ipaddr))

        for host in nm.all_hosts():
            map_out.write('---------------------------------\n')
            map_out.write("Host: {} ({})\n".format(host, nm[host].hostname()))
            map_out.write("State: {}\n".format(nm[host].state()))
            return

    scan_output = nm.scan(ipaddr, port_nums, scan_flags)

    map_out.write('nmap {} -p {} {}\n'.format(scan_flags, port_nums, ipaddr))

    for host in nm.all_hosts():
        map_out.write('---------------------------------\n')
        map_out.write("Host: {} ({})\n".format(host, nm[host].hostname()))
        map_out.write("State: {}\n".format(nm[host].state()))

        for protocol in nm[host].all_protocols():
            map_out.write("Protocol: {}\n".format(protocol))

            list_port = nm[host][protocol].keys()

            if '-sV' in scan_flags:
                map_out.write("{: <5} {: <10} {: <20} {: <20}\n".format('Port', 'State', 'Service', 'Version'))
            else:
                map_out.write("{: <5} {: <10} {: <20}\n".format('Port', 'State', 'Service'))

            # Loop through found ports and print out port information
            for port in list_port:
                # Check for the -sV flag and output the service version if it is used
                if '-sV' in scan_flags:
                    map_out.write("{: <5} {: <10} {: <20} {: <20} {}\n".format(port, nm[host][protocol][port]['state'], nm[host][protocol][port]['name'], nm[host][protocol][port]['product'], nm[host][protocol][port]['version']))
                else:
                    map_out.write("{: <5} {: <10} {: <20}\n".format(port, nm[host][protocol][port]['state'], nm[host][protocol][port]['name']))
        
        if '-O' in scan_flags:
            map_out.write("{: <30} {}\n".format('\nHost OS Guess', ' Accuracy')) 

            for os_match in nm[host]['osmatch']:
                os_name = textwrap.fill(os_match['name'], width=30)  # Wrap long names to fit within 30 characters
                accuracy = os_match['accuracy']

                lines = os_name.split('\n')

                map_out.write("{: <30} {}%\n".format(lines[0], accuracy))

                for line in lines[1:]:
                    map_out.write("{}\n".format(line)) 
        
        
    map_out.write('\n')

    map_out.close()

    return scan_output

# Precondition: line is a string for the command line command, ipaddr is a string of the target IP range, and
#               ports is a string of the port range
# Postcondition: returns a string of the optional scan flags from the command
def get_flags(line, ipaddr, ports):
    line = line.replace(ipaddr, '')
    line = line.replace(ports, '')
    line = line.replace('-p', '')
    line = line[5:]

    return line