'''
metap.py
Description: connects to the device's metasploit implementation and searches for exploit modules related to a given CVE.
Created: 3/24/25
Updated: 3/28/25
'''

from pymetasploit3.msfrpc import MsfRpcClient

'''
Instructions for MsfRpcClient:
The RPC server can be started using the command `msfrpcd -P <password>`. This command will start the
server on port 55553. The current password to being the service is NfF9sTEo. The MsfRpcClient function
will connect to the server on port 55553 and return a metasploit object ot client.
'''

__password__ = 'NfF9sTEo' # The current password for msfrpcd; this will need to be changed for every system

try:
    client = MsfRpcClient(__password__, port=55553, ssl=True)
except:
    print("Failed to connect to MsfRpcClient")
    exit(0)

# Precondition: cve is a string for the cve name to be searched.
# Postcondition: returns a the name/path of the exploit module if found.
def search_exploit(cve):
    for m in client.modules.exploits:
        exploit = client.modules.use('exploit', m)

        if cve in exploit.description:
            return exploit.description

    return

search_exploit('test')
