import nmap

nm = nmap.PortScanner()

ipaddr = input("Enter the IP address: ")
port_nums = input("Enter the port range (e.g. 25-50): ")

scan_output = nm.scan(ipaddr, port_nums)

for host in nm.all_hosts():
    print('---------------------------------')
    print("Host: {} ({})".format(host, nm[host].hostname()))
    print("State: {}".format(nm[host].state()))

    for protocol in nm[host].all_protocols():
        print("Protocol: {}".format(protocol))

        list_port = nm[host][protocol].keys()
        list_port.sort()
        for port in list_port:
            print("Port: {}\tState: {}".format(port, nm[host][proto][port][state]))