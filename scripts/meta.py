# metap.py
# Description: connects to the device's metasploit implementation and searches for exploit modules related to a given CVE.
# Created: 3/24/25
# Updated: 3/24/25

from pymetasploit3.msfrpc import MsfRpcClient

client = MsfRpcClient('NfF9sTEo', port=55553, ssl=True)

# Precondition: cve is a string for the cve name to be searched.
# Postcondition: returns a the name/path of the exploit module if found.
def search_exploit(cve):
    for m in dir(client):
        if not m.startswith('_'):
            print(m)
    return

search_exploit('test')
