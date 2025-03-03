from flask import Flask, render_template, jsonify, request
from net_scan import port_scan, get_flags
from vuln_scan import vuln_scanner
from osdetection import nmap_results_path

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
    ipaddr = request.args.get('ip', '192.168.2.241')
    ports = request.args.get('ports', '1-6000')
    cmd_line = request.args.get('cmd', 'nmap 127.0.0.1')

    scan_flags = get_flags(cmd_line, ipaddr, ports)

    return jsonify(port_scan(ipaddr, ports, scan_flags))

@app.route('/run-vuln-scan/', methods=['GET'])
def run_vuln_scan():
    ipaddr = request.args.get('ip', '192.168.2.241')

    return jsonify(vuln_scanner(ipaddr))

latestnmappath = nmap_results_path()

@app.route('/get-nmap-results/', methods=['GET'])
def get_nmap_results():
    path = nmap_results_path()
    try:
        with open(path, "r") as file:
            content = file.read()
        return content, 200, {'Content-Type': 'text/plain'}
    except FileNotFoundError:
        return "No scan results available yet.", 200, {'Content-Type': 'text/plain'}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)