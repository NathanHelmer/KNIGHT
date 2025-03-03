'''
vuln_scan.py
Description: Runs an nmap vulnerability scan using a script and returns the results.
Created 2/20/25
Updated: 3/3/25
'''

import nmap
from osdetection import vuln_results_path


# Precondition: ipaddr is a string of an IP address or IP address range.
# Postcondition: returns an nmap scan object of scan results on ipaddr.
def vuln_scanner(ipaddr, ports='1-1000'):
    __script_flag__ = '--script vuln'
    
    vs = nmap.PortScanner()
    vuln_output = vs.scan(ipaddr, ports, __script_flag__)

    path = vuln_results_path()

    vuln_out = open(path, 'w')
    vuln_out.close()

    return vuln_output