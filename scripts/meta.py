'''
metap.py
Description: connects to the device's metasploit implementation and searches for exploit modules related to a given CVE.
Created: 3/24/25
Updated: 4/5/25
'''

from pymetasploit3.msfrpc import MsfRpcClient

'''
Instructions for MsfRpcClient:
Load msfrpc in msf console using the `load msgprc` command. Run `load msgrpc Pass=knight`.

The RPC server can be started using the command `msfrpcd -P knight`. This command will start the
server on port 55553. The current password to being the service is NfF9sTEo. The MsfRpcClient function
will connect to the server on port 55553 and return a metasploit object ot client.
'''

__password__ = 'knight'

print('Connecting to MsfRpcClient...')

try:
    print('Trying connection...')
    client = MsfRpcClient(__password__, port=55553, ssl=True)
    print('Connected to MsfRpcClient')
except:
    print("Failed to connect to MsfRpcClient")
    exit(0)

# Precondition: cve is a string for the cve name to be searched.
# Postcondition: returns a list of matching exploits.
def search_exploit(cve):

    print('Searching for exploits...')

    found = []

    for m in client.modules.exploits:
        exploit = client.modules.use('exploit', m)

        if cve in exploit.description:
            found.append(exploit)
    
    print('Search finished')

    return found
