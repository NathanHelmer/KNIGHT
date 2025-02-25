import sys

def nmap_results_path():
    windowspath = '\results\latest_nmap_results.txt'
    linuxpath = './results/latest_nmap_results.txt'
    if (sys.platform == 'linux'):
        return linuxpath
    else:
        return windowspath