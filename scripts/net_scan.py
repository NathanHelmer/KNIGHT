import nmap

nm = nmap.PortScanner()

ipaddr = input("Enter the IP address: ")
port_nums = input("Enter the port range (e.g. 25-50): ")

scan_output = nm.scan(ipaddr, port_nums)

print(scan_output)