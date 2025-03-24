# metap.py
# Description: connects to the device's metasploit implementation and searches for exploit modules related to a given CVE.
# Created: 3/24/25
# Updated: 3/24/25

from pymetasploit3.msfrpc import MsfRpcClient

client = MsfRpcClient('NfF9sTEo', port=55553, ssl=True)

def search_exploit(cve):
    print(client)
    return

search_exploit('test')
