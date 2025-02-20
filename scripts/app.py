from flask import Flask, render_template, jsonify, request
from net_scan import port_scan, get_flags

app = Flask(__name__, template_folder='../User Interface', static_folder='../User Interface/images')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/nmap-scans/')
def run_nmap_page():
    return render_template('nmap-scans.html')

@app.route('/nmap-logs/')
def run_nmap_logs_page():
    return render_template('nmap-logs.html') 

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

if __name__ == '__main__':
    app.run(debug=True)