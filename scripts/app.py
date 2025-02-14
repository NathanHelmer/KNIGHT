from flask import Flask, render_template, jsonify, request
from net_scan import port_scan 

app = Flask(__name__, template_folder='../User Interface')

@app.route('/run-nmap/')
def run_nmap_page():
    return render_template('nmap-scans.html') 

@app.route('/run-nmap-scan/', methods=['GET'])
def run_nmap():
    ipaddr = request.args.get('ip', '192.168.2.241')
    ports = request.args.get('ports', '1-6000')
    return jsonify(port_scan(ipaddr, ports, 'sN'))

if __name__ == '__main__':
    app.run(debug=True)