'''
osdetection.py
Description: returns file paths given the host's OS. Note: when running the program in linux, run it
from ~/PATHTOFLASK --app ~/PATHTOAPP.PY run
Created: 2/25/25
Updated: 3/19/25
'''

import sys, os, datetime

# Precondition: none
# Postcondition: returns the file path for Nmap scan results based on the host OS (Windows or Linux)
def nmap_results_path():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # Avoids colons so windows doesn't error

    windowspath = os.path.abspath(f'results\\nmap\\{timestamp}.txt')
    linuxpath = os.path.abspath(f'./results/nmap/{timestamp}.txt')
    
    linuxdir = os.path.abspath("./results/nmap/")
    windowsdir = os.path.abspath("results\\nmap\\")

    if (sys.platform == 'linux'):
        if not os.path.exists(linuxdir):
            os.makedirs(linuxdir)
        return linuxpath
    else:
        if not os.path.exists(windowsdir):
            os.makedirs(windowsdir)
        return windowspath

# Precondition: none
# Postcondition: returns the file path for Nmap logs directory based on the host OS (Windows or Linux)
def nmap_logs_path():
    linuxdir = os.path.abspath("./results/nmap/")
    windowsdir = os.path.abspath("results\\nmap\\")
    if (sys.platform == 'linux'):
        if not os.path.exists(linuxdir):
            os.makedirs(linuxdir)
        return linuxdir
    else:
        if not os.path.exists(windowsdir):
            os.makedirs(windowsdir)
        return windowsdir

# Precondition: none
# Postcondition: returns the file path for vulnerability scan results based on the host OS (Windows or Linux)
def vuln_results_path():
    windowspath = os.path.abspath('scripts\\results\\latest_vuln_results.txt')
    linuxpath = os.path.abspath('./scripts/results/latest_vuln_results.txt')
    if (sys.platform == 'linux'):
        return linuxpath
    else:
        return windowspath
