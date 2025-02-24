'''
vuln_scan.py
Description: Runs an nmap vulnerability scan using a script and returns the results.
Created 2/20/25
Updated: 2/23/25
'''

import nmap


# Precondition: ipaddr is a string of an IP address or IP address range.
# Postcondition: returns an nmap scan object of scan results on ipaddr.
def vuln_scanner(ipaddr):
    __script_flag__ = '--script vuln'
    
    vs = nmap.PortScanner()
    vuln_output = vs.scan(ipaddr, '-p-', __script_flag__)

    return vuln_output