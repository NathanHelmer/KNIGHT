'''
vuln_scan.py
Description: Runs an nmap vulnerability scan using a script and returns the results.
Created 2/20/25
Updated: 2/23/25
'''

import nmap
from osdetection import vuln_results_path


# Precondition: ipaddr is a string of an IP address or IP address range.
# Postcondition: returns an nmap scan object of scan results on ipaddr.
def vuln_scanner(ipaddr, ports='1-1000'):
    __script_flag__ = '--script vuln'
    
    vs = nmap.PortScanner()
    vuln_output = vs.scan(ipaddr, ports, __script_flag__)

<<<<<<< HEAD
    path = vuln_results_path()

    vuln_out = open(path)
    vuln_out.write
=======
    vuln_out = open('latest_vuln_results.txt', 'w')
    vuln_out.close()
>>>>>>> cb8bc963200f48182fd2a763cded08dccfaa2ebf

    return vuln_output