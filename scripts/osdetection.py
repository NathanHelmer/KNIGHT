'''
osdetection.py
Description: returns file paths given the host's OS
Created: 2/25/25
Updated: 3/18/25
'''

import sys
import os
import datetime


#NOTE: When running the program on linux, run it from ~/PATHTOFLASK --app ~/PATHTOAPP.PY run

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
    
def vuln_results_path():
    windowspath = os.path.abspath('scripts\\results\\latest_vuln_results.txt')
    linuxpath = os.path.abspath('./scripts/results/latest_vuln_results.txt')
    if (sys.platform == 'linux'):
        return linuxpath
    else:
        return windowspath
