'''
app.py
Description: runs Flask applications at the routes specified in '@app.route()'
Created: 2/7/25
Updated: 3/18/25
'''
import os
from flask import Flask, render_template, jsonify, request
from net_scan import port_scan, get_flags
from vuln_scan import vuln_scanner
from osdetection import nmap_results_path, vuln_results_path, nmap_logs_path

app = Flask(__name__, template_folder='../UserInterface', static_folder='../UserInterface/images')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/nmap-scans/')
def run_nmap_page():
    return render_template('nmap-scans.html')

@app.route('/nmap-logs/')
def run_nmap_logs_page():
    return render_template('nmap-logs.html')

@app.route('/vuln-scans/')
def run_vuln_scans_page():
    return render_template('vuln-scans.html')

@app.route('/help/')
def run_help_page():
    return render_template('help.html')

@app.route('/run-nmap-scan/', methods=['GET'])
def run_nmap_scan():
    ipaddr = request.args.get('ip','')
    ports = request.args.get('ports','')
    cmd_line = request.args.get('cmd','')
    
    if ports == '':
        ports = '1-1000'
    
    if ipaddr == '':
        ipaddr = '127.0.0.1'

    scan_flags = get_flags(cmd_line, ipaddr, ports)
    path = nmap_results_path() 

    port_scan(ipaddr, ports, scan_flags, path)
    return jsonify({"message": "Scan completed", "path": path})

@app.route('/run-vuln-scan/', methods=['GET'])
def run_vuln_scan():
    ipaddr = request.args.get('ip', '127.0.0.1')
    ports = request.args.get('ports', '1-1000')

    return jsonify(vuln_scanner(ipaddr, ports))

@app.route('/get-nmap-results/', methods=['GET'])
def get_nmap_results():
    path = request.args.get('path')
    print("Received path:", path)

    try:
        print("Opening file")
        with open(path, "r") as file:
            content = file.read()
        return content, 200, {'Content-Type': 'text/plain'}
    except FileNotFoundError:
        return "No scan results available yet.", 200, {'Content-Type': 'text/plain'}
    
@app.route('/get-vuln-results/', methods=['GET'])
def get_vuln_results():
    path = vuln_results_path()
    try:
        with open(path, "r") as file:
            content = file.read()
        return content, 200, {'Content-Type': 'text/plain'}
    except FileNotFoundError:
        return "No scan results available yet.", 200, {'Content-Type': 'text/plain'}

@app.route('/get-all-nmap-logs/', methods=['GET'])
def get_all_nmap_logs():
    print('getnmap')
    LOGS_DIR = os.path.abspath("./results/nmap/")
    print(LOGS_DIR)
    try:
        files = os.listdir(LOGS_DIR)
        logs = [{"Name": file} for file in files]
        return jsonify(logs)
    except Exception as e:
        print("error")
        return jsonify({"error": str(e)}), 500
    
@app.route('/get-nmap-dir/', methods=['GET'])
def get_nmap_dir():
    path = nmap_logs_path()
    return jsonify({"nmap_logs_dir": path})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)