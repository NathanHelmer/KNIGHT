import sys
import os

def nmap_results_path():
    windowspath = os.path.abspath('scripts\\results\\latest_nmap_results.txt')
    #linuxpath = './results/latest_nmap_results.txt'
    linuxpath = os.path.abspath('scripts/results/latest_nmap_results.txt')
    if (sys.platform == 'linux'):
        return linuxpath
    else:
        return windowspath