# Automated testing

from net_scan import *
from vuln_scan import *

# Precondition: none
# Postcondition: runs sample scans and ouputs the results to nmap_results.txt
def run_scans():
    test_range = '127.0.0.1'
    test_ports = '1-1000'

    port_scan(test_range, test_ports, '-sV')

def run_vulns():
    test_range = '10.25.1.8'
    test_ports = '1-1000'

    vuln_scanner(test_range, test_ports)

run_vulns()