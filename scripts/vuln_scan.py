'''
vuln_scan.py
Description: Runs an nmap vulnerability scan using a script and returns the results.
Created 2/20/25
Updated: 2/20/25
'''

import nmap

def vuln_scanner(ipaddr):
    __script_flag__ = '--script vuln'
    
    vs = nmap.PortScanner()
    vuln_output = vs.scan(ipaddr, '-p-', __script_flag__)

    return vuln_output