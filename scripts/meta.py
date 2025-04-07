'''
metap.py
Description: connects to the device's metasploit implementation and searches for exploit modules related to a given CVE.
Created: 3/24/25
Updated: 4/6/25
'''

from pymetasploit3.msfrpc import MsfRpcClient

'''
Instructions for MsfRpcClient:
Load msfrpc in msf console (started with command `msfconsole`) using the `load msgprc` command.
Run `load msgrpc Pass=knight` to load the msgrpc module.

The RPC server can be started using the command `msfrpcd -P knight`. This command will start the
server on port 55553. The default password used is 'knight'. The MsfRpcClient function
will connect to the server on port 55553 and return a metasploit object ot client.
'''

__password__ = 'knight'

#Precondition: The MsfRpcClient service is running on the device.
#Postcondition: Returns an object for the MsfRpcClient connection or null if the connection fails. 
def connect_meta():
    print('Connecting to MsfRpcClient...')

    try:
        print('Trying connection...')
        client = MsfRpcClient(__password__, port=55553, ssl=True)
        print('Connected to MsfRpcClient')

        return client
    except:
        print("Failed to connect to MsfRpcClient")
        return null

# Precondition: cve is a string for the cve name to be searched.
# Postcondition: returns a list of exploit objects for matching exploits.
def search_exploit(cve):

    client = connect_meta()
    
    found = []
    
    if client == null:
        return found

    print('Searching for exploits...')

    

    for m in client.modules.exploits:
        exploit = client.modules.use('exploit', m)

        if cve in exploit.cve:
            found.append(exploit.name)
    
    print('Search finished')

    return found
