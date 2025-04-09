'''
test.py
Description: Automated testing for the KNIGHT UI backend
Created: 2/26/25
Updated: 3/18/25
'''

from net_scan import *
from vuln_scan import *
from meta import *

# Precondition: none
# Postcondition: runs sample nmap scans
def run_scans():
    test_range = 'scanme.nmap.org'
    test_ports = '1-1000'

    port_scan(test_range, test_ports, '-sV')

# Precondition: none
# Postcondition: runs sample vulnerability scans
def run_vulns():
    test_range = 'scanme.nmap.org'
    test_ports = '1-1000'

    vuln_scanner(test_range, test_ports)

# Precondition: none
# Postocndition: runs a sample search of CVEs from 2017 and outputs their names to the terminal
def test_meta():
    search_term = 'CVE-2017'

    findings = search_exploit(search_term)

    for i in findings:
        print("Found exploit: ", i.name, "\n")