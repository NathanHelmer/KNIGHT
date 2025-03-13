'''
vuln_scan.py
Description: Runs an nmap vulnerability scan using a script and returns the results.
Created 2/20/25
Updated: 3/13/25
'''

import nmap
from osdetection import vuln_results_path


# Precondition: ipaddr is a string of an IP address or IP address range.
# Postcondition: returns an nmap scan object of scan results on ipaddr.
def vuln_scanner(ipaddr, ports='1-1000'):
    __script_flag__ = '--script vuln'
    
    vs = nmap.PortScanner()
    #vuln_output = vs.scan(ipaddr, ports, __script_flag__)
    vuln_output = "test"

    path = vuln_results_path()

    vuln_out = open(path, 'w')

    for host in vs.all_hosts():
        vuln_out.write('---------------------------------\n')
        vuln_out.write("Host: {} ({})\n".format(host, vs[host].hostname()))
        vuln_out.write("State: {}\n".format(vs[host].state()))

        for protocol in vs.all_hosts():
            list_port = vs[host][protocol].keys()

            for port in list_port:
                vuln_out.write("Port: {}\n".format(vs[host][protocol][port]))

                list_scans = vs[host][protocol][port]['script'].keys()
                for scan in list_scans:
                    if 'CVE' in vs[host][protocol][port]['script'][scan]:
                        vuln_out.write("Vulnerability: {}\n".format(vs[host][protocol][port]['script'][scan]))

    vuln_out.close()

    return vuln_output