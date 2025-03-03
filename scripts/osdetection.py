import sys
import os

#NOTE: When running the program on linux, run it from ~/PATHTOFLASK --app ~/PATHTOAPP.PY run

def nmap_results_path():
    windowspath = os.path.abspath('scripts\\results\\latest_nmap_results.txt')
    linuxpath = os.path.abspath('./scripts/results/latest_nmap_results.txt')
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