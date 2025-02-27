# Automated testing

from net_scan import *

# Precondition: none
# Postcondition: runs sample scans and ouputs the results to nmap_results.txt
def run_scans():
    test_range = '127.0.0.1'
    test_ports = '1-1000'

    port_scan(test_range, test_ports, '-sV')

run_scans()