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
    timestamp = datetime.datetime.now()
    windowspath = os.path.abspath(f'results\\nmap\\{timestamp}.txt')
    linuxpath = os.path.abspath(f'./results/nmap/{timestamp}.txt')
    if (sys.platform == 'linux'):
        return linuxpath
    else:
        return windowspath
    
def vuln_results_path():
    windowspath = os.path.abspath('scripts\\results\\latest_vuln_results.txt')
    linuxpath = os.path.abspath('./scripts/results/latest_vuln_results.txt')
    if (sys.platform == 'linux'):
        return linuxpath
    else:
        return windowspath
