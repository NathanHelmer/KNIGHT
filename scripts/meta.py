'''
metap.py
Description: connects to the device's metasploit implementation and searches for exploit modules related to a given CVE.
Created: 3/24/25
Updated: 3/24/25
'''

from pymetasploit3.msfrpc import MsfRpcClient
from pymetasploit3.msfconsole import MsfRpcConsole

'''
Instructions for MsfRpcClient:
The RPC server can be started using the command `msfrpcd -P <password>`. This command will start the
server on port 55553. The current password to being the service is NfF9sTEo. The MsfRpcClient function
will connect to the server on port 55553 and return a metasploit object ot client.
'''

try:
    client = MsfRpcClient('NfF9sTEo', port=55553, ssl=True)
except:
    print("Failed to connect to MsfRpcClient")
    exit(0)

try:
    console = MsfRpcConsole(client, cb=read_console)
except:
    print("Failed to initialize console")
    exit(0)

# Precondition: cve is a string for the cve name to be searched.
# Postcondition: returns a the name/path of the exploit module if found.
def search_exploit(cve):
    for m in dir(client):
        if not m.startswith('_'):
            print(m)
            if m == 'modules':
                print('\nmodule:\n')
                for i in dir(m):
                    print(i)

    return

search_exploit('test')
